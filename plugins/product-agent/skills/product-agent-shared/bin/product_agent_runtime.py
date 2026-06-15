#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import shutil
import sys
from datetime import datetime, timezone


ROOT = pathlib.Path(__file__).resolve().parents[1]
STATE_DIR = pathlib.Path(os.environ.get("PRODUCT_AGENT_HOME", pathlib.Path.home() / ".product_agent"))
ASSETS_PATH = STATE_DIR / "assets.json"
ROUTES = {
    "workspace": "product-agent-workspace",
    "problem": "product-agent-problem",
    "autoplan": "product-agent-autoplan",
    "strategy": "product-agent-strategy-review",
    "brief": "product-agent-brief",
    "prototype": "product-agent-prototype",
    "prototype_review": "product-agent-prototype-review",
    "handoff": "product-agent-handoff",
}
SKILLS = list(ROUTES.values())
ASSET_KINDS = {"product_brief", "visual_baseline", "prototype_manifest", "prototype_review", "handoff"}


def ensure_state() -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_json(path: pathlib.Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def write_json(path: pathlib.Path, data) -> None:
    ensure_state()
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def has_any(text: str, words: list[str]) -> bool:
    return any(word in text for word in words)


def classify_text(text: str) -> dict:
    lower = text.lower()
    signals: list[str] = []

    selection_answer = bool(re.search(r"(我选|选择|确认|按)\s*[ABCabcＡＢＣａｂｃ]", text)) and has_any(text, ["继续", "确认", "按"])
    local_edit = has_any(text, ["文案", "改一下", "只改", "局部", "小改"]) and not has_any(text, ["完整评审", "一路推进", "三条", "三个方案", "原型", "PRD", "交付", "简报", "brief"])
    online_change_without_baseline = (
        has_any(text, ["线上", "已上线功能", "已上线"])
        and has_any(text, ["改", "迭代"])
        and has_any(text, ["没有", "缺", "未提供"])
        and has_any(text, ["截图", "URL", "url", "设计稿"])
    )
    brief_unaligned = has_any(text, ["还没有确认产品简报", "没有确认产品简报", "brief 未对齐", "简报未对齐", "未对齐"])
    image2_no_html = ("image-2" in lower or "出图" in text or "原型" in text) and has_any(text, ["不要退回 HTML", "不退回 HTML", "不要退回HTML", "不退回HTML", "HTML"])
    handoff_missing_facts = has_any(text, ["接口", "埋点", "数据来源", "数据口径"]) and has_any(text, ["不知道", "不能瞎编", "不可虚构", "别瞎编", "不能虚构"])
    prototype_request_intent = has_any(text, ["原型", "出图", "image-2", "截图修改"])

    if selection_answer:
        op, route = "answer_pending_gate", ROUTES["workspace"]
        signals.append("answer_pending_gate_only")
    elif online_change_without_baseline:
        op, route = "attach_evidence", ROUTES["workspace"]
        signals.append("needs_visual_baseline")
    elif local_edit:
        op, route = "local_edit", ROUTES["workspace"]
        signals.append("local_edit_only")
    elif any(word in text for word in ["PRD", "交付", "研发", "产品设计文档", "handoff"]):
        op, route = "handoff_continue", ROUTES["handoff"]
        signals.append("no_fake_interfaces")
    elif (not prototype_request_intent) and any(word in text for word in ["截图", "url", "URL", "figma", "Figma", "数据"]):
        op, route = "attach_evidence", ROUTES["workspace"]
    elif any(word in text for word in ["改成", "改为", "修改", "变更"]) and any(word in text for word in ["目标", "范围", "承诺", "用户", "场景", "反指标"]):
        op, route = "modify_brief", ROUTES["brief"]
    elif any(word in text for word in ["复审", "能不能用", "需不需要重出", "评审原型"]):
        op, route = "prototype_review", ROUTES["prototype_review"]
    elif any(word in text for word in ["原型", "出图", "image-2", "截图修改"]):
        op, route = "prototype_request", ROUTES["prototype"]
    elif any(word in text for word in ["简报", "brief", "产品说明"]):
        op, route = "brief_request", ROUTES["brief"]
    elif any(word in text for word in ["策略", "范围", "风险", "价值交换", "收缩", "转向"]):
        op, route = "strategy_review", ROUTES["strategy"]
    elif any(word in text for word in ["自动", "完整评审", "按推荐", "一路推进"]):
        op, route = "new_product_workflow", ROUTES["autoplan"]
    elif any(word in text for word in ["问题", "值不值得", "痛点", "想法"]):
        op, route = "new_product_workflow", ROUTES["problem"]
    else:
        op, route = "new_product_workflow", ROUTES["workspace"]

    if brief_unaligned:
        signals.append("needs_brief_alignment")
    if image2_no_html or "image-2" in lower:
        signals.append("no_html_fallback")
    if handoff_missing_facts and "no_fake_interfaces" not in signals:
        signals.append("no_fake_interfaces")

    return {
        "product": "product_agent",
        "operation_type": op,
        "route": route,
        "signals": sorted(set(signals)),
        "state_dir": str(STATE_DIR),
        "reason": "基于用户请求中的产品意图关键词进行最小路由。",
    }


def cmd_classify(args: argparse.Namespace) -> int:
    print(json.dumps(classify_text(args.text or ""), ensure_ascii=False, indent=2 if args.json else None))
    return 0


def current_assets() -> list[dict]:
    data = read_json(ASSETS_PATH, {"assets": []})
    return list(data.get("assets", []))


def cmd_artifact(args: argparse.Namespace) -> int:
    ensure_state()
    if args.action == "add":
        if args.kind not in ASSET_KINDS:
            print(f"unknown asset kind: {args.kind}", file=sys.stderr)
            return 2
        data = read_json(ASSETS_PATH, {"assets": []})
        data.setdefault("assets", []).append({
            "kind": args.kind,
            "title": args.title,
            "summary": args.summary,
            "created_at": now(),
        })
        write_json(ASSETS_PATH, data)
        print(json.dumps({"status": "recorded", "kind": args.kind, "state_dir": str(STATE_DIR)}, ensure_ascii=False))
        return 0
    print(json.dumps({"assets": current_assets(), "state_dir": str(STATE_DIR)}, ensure_ascii=False, indent=2))
    return 0


def readiness_from_assets() -> dict:
    assets = current_assets()
    kinds = {item.get("kind") for item in assets}
    brief_ready = "product_brief" in kinds
    review_ready = "prototype_review" in kinds
    return {
        "product": "product_agent",
        "state_dir": str(STATE_DIR),
        "assets": sorted(kinds),
        "prototype": "可出原型" if brief_ready else "阻断：缺少已对齐 product_brief",
        "handoff": "可交付" if brief_ready and review_ready else "阻断：缺少 product_brief 或 prototype_review",
    }


def cmd_dashboard(args: argparse.Namespace) -> int:
    data = readiness_from_assets()
    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print("product_agent status")
        print(f"state_dir: {data['state_dir']}")
        print(f"assets: {', '.join(data['assets']) if data['assets'] else 'none'}")
        print(f"prototype: {data['prototype']}")
        print(f"handoff: {data['handoff']}")
    return 0


def cmd_controller(args: argparse.Namespace) -> int:
    data = readiness_from_assets()
    result = {
        "product": "product_agent",
        "next": "product-agent-brief" if "product_brief" not in data["assets"] else "product-agent-prototype",
        "prototype_readiness": data["prototype"],
        "handoff_readiness": data["handoff"],
        "state_dir": str(STATE_DIR),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2 if args.json else None))
    return 0


def fixture_paths() -> pathlib.Path:
    return ROOT / "evals"


def load_fixture(fid: str) -> dict:
    path = fixture_paths() / "fixtures" / f"{fid}.json"
    if not path.exists():
        raise SystemExit(f"missing fixture: {fid}")
    return json.loads(path.read_text(encoding="utf-8"))


def suite_ids(name: str) -> list[str]:
    if name == "full":
        return sorted(path.stem for path in (fixture_paths() / "fixtures").glob("*.json"))
    path = fixture_paths() / "suites" / f"{name}.txt"
    if not path.exists():
        raise SystemExit(f"missing suite: {name}")
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip() and not line.startswith("#")]


def evaluate_fixture(fixture: dict) -> tuple[bool, list[str]]:
    expected = fixture.get("expected", {})
    actual = classify_text(fixture.get("prompt", ""))
    failures = []
    if expected.get("route") and actual["route"] != expected["route"]:
        failures.append(f"route expected {expected['route']} got {actual['route']}")
    if expected.get("operation_type") and actual["operation_type"] != expected["operation_type"]:
        failures.append(f"operation_type expected {expected['operation_type']} got {actual['operation_type']}")
    for forbidden_route in expected.get("must_not_route", []):
        if actual["route"] == forbidden_route:
            failures.append(f"forbidden route selected: {forbidden_route}")
    actual_signals = set(actual.get("signals", []))
    for signal in expected.get("must_include_signals", []):
        if signal not in actual_signals:
            failures.append(f"missing signal: {signal}")
    for signal in expected.get("must_exclude_signals", []):
        if signal in actual_signals:
            failures.append(f"excluded signal present: {signal}")
    for forbidden in expected.get("must_not", []):
        if forbidden in json.dumps(actual, ensure_ascii=False):
            failures.append(f"forbidden token present: {forbidden}")
    return not failures, failures


def cmd_eval(args: argparse.Namespace) -> int:
    if args.action == "sync":
        sync_packaged_trees()
        print("synced evals and examples into product-agent-shared")
        return 0
    ids = [args.fixture] if args.fixture else suite_ids(args.suite)
    results = []
    failed = 0
    for fid in ids:
        fixture = load_fixture(fid)
        ok, failures = evaluate_fixture(fixture)
        failed += 0 if ok else 1
        results.append({"id": fid, "passed": ok, "failures": failures})
    output = {"suite": args.suite if not args.fixture else None, "total": len(results), "failed": failed, "results": results}
    print(json.dumps(output, ensure_ascii=False, indent=2 if args.json else None))
    return 1 if failed else 0


def cmd_gen_docs(args: argparse.Namespace) -> int:
    manifest = json.loads((ROOT / "product-agent-shared" / "skill-docs" / "skill-docs.manifest.json").read_text(encoding="utf-8"))
    failures = []
    for skill in manifest["skills"]:
        path = ROOT / skill / "SKILL.md"
        text = path.read_text(encoding="utf-8") if path.exists() else ""
        if f"name: {skill}" not in text:
            failures.append(f"{skill}: missing matching frontmatter name")
        if "description:" not in text:
            failures.append(f"{skill}: missing description")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    if args.command == "list":
        print("\n".join(manifest["skills"].keys()))
    else:
        print("product_agent skill docs check passed")
    return 0


def copytree(src: pathlib.Path, dst: pathlib.Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".DS_Store", "__pycache__"))


def sync_packaged_trees() -> None:
    copytree(ROOT / "evals", ROOT / "product-agent-shared" / "evals")
    copytree(ROOT / "examples", ROOT / "product-agent-shared" / "examples")


def cmd_build_plugin(args: argparse.Namespace) -> int:
    sync_packaged_trees()
    plugin_dir = pathlib.Path(args.dest) if args.dest else ROOT / "plugins" / "product-agent"
    if plugin_dir.exists():
        shutil.rmtree(plugin_dir)
    (plugin_dir / ".codex-plugin").mkdir(parents=True)
    (plugin_dir / "skills").mkdir()
    (plugin_dir / "assets").mkdir()
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    plugin = {
        "name": "product-agent",
        "version": version,
        "description": "product_agent turns product ideas, screenshots, PRDs, and feedback into aligned briefs, prototype directions, reviews, and handoff assets.",
        "author": {"name": "Stephen Fan", "url": "https://github.com/stephenfan80"},
        "homepage": "https://github.com/stephenfan80/product-agent",
        "repository": "https://github.com/stephenfan80/product-agent",
        "license": "MIT",
        "keywords": ["product-agent", "product_agent", "product management", "prd", "prototype", "产品 Agent", "产品简报", "原型复审"],
        "skills": "./skills/",
        "interface": {
            "displayName": "产品 Agent",
            "shortDescription": "Product briefs, prototypes, reviews, and handoff assets",
            "longDescription": "product_agent is a product capability skill suite that routes product ideas, screenshots, PRDs, and feedback through alignment, prototype, review, and delivery.",
            "developerName": "Stephen Fan",
            "category": "Productivity",
            "capabilities": ["Interactive", "Read", "Write"],
            "websiteURL": "https://github.com/stephenfan80/product-agent",
            "privacyPolicyURL": "https://github.com/stephenfan80/product-agent#privacy",
            "termsOfServiceURL": "https://github.com/stephenfan80/product-agent#license",
            "defaultPrompt": [
                "使用 product-agent-workspace 帮我判断这个产品想法应该怎么推进。",
                "使用 product-agent-brief 把这次产品对齐整理成产品简报。",
                "使用 product-agent-prototype 基于已对齐 brief 规划三个移动端原型方向。"
            ],
            "brandColor": "#2563EB",
            "composerIcon": "./assets/icon.png",
            "logo": "./assets/logo.png",
            "screenshots": ["./assets/screenshot-onboarding.png", "./assets/screenshot-brief.png", "./assets/screenshot-prototype.png"]
        }
    }
    (plugin_dir / ".codex-plugin" / "plugin.json").write_text(json.dumps(plugin, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for skill in SKILLS:
        copytree(ROOT / skill, plugin_dir / "skills" / skill)
    copytree(ROOT / "product-agent-shared", plugin_dir / "skills" / "product-agent-shared")
    shared_bin = plugin_dir / "skills" / "product-agent-shared" / "bin"
    shared_bin.mkdir(parents=True, exist_ok=True)
    for script in (ROOT / "bin").glob("product-agent*"):
        shutil.copy2(script, shared_bin / script.name)
    shutil.copy2(ROOT / "bin" / "product_agent_runtime.py", shared_bin / "product_agent_runtime.py")
    for src_name, dst_name in [
        ("assets/plugin-listing/icon.png", "icon.png"),
        ("assets/plugin-listing/logo.png", "logo.png"),
        ("assets/plugin-listing/screenshot-onboarding.png", "screenshot-onboarding.png"),
        ("assets/plugin-listing/screenshot-brief.png", "screenshot-brief.png"),
        ("assets/plugin-listing/screenshot-prototype.png", "screenshot-prototype.png"),
    ]:
        src = ROOT / src_name
        if src.exists():
            shutil.copy2(src, plugin_dir / "assets" / dst_name)
    print(f"built {plugin_dir}")
    return 0


def cmd_upgrade(args: argparse.Namespace) -> int:
    host = args.host
    if host != "codex":
        print(f"unsupported host: {host}", file=sys.stderr)
        return 2
    sync_packaged_trees()
    dest = pathlib.Path(os.environ.get("CODEX_SKILLS_DIR", pathlib.Path.home() / ".codex" / "skills"))
    dest.mkdir(parents=True, exist_ok=True)
    for skill in SKILLS:
        copytree(ROOT / skill, dest / skill)
    copytree(ROOT / "product-agent-shared", dest / "product-agent-shared")
    shared_bin = dest / "product-agent-shared" / "bin"
    shared_bin.mkdir(parents=True, exist_ok=True)
    for script in (ROOT / "bin").glob("product-agent*"):
        shutil.copy2(script, shared_bin / script.name)
    shutil.copy2(ROOT / "bin" / "product_agent_runtime.py", shared_bin / "product_agent_runtime.py")
    print(f"product_agent installed to {dest}")
    return 0


def cmd_version(args: argparse.Namespace) -> int:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if args.json:
        print(json.dumps({"product": "product_agent", "version": version}, ensure_ascii=False))
    else:
        print(version)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("classify")
    p.add_argument("--text", default="")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_classify)
    p = sub.add_parser("artifact")
    p.add_argument("action", choices=["add", "list"])
    p.add_argument("--kind", default="product_brief")
    p.add_argument("--title", default="Untitled")
    p.add_argument("--summary", default="")
    p.set_defaults(func=cmd_artifact)
    p = sub.add_parser("dashboard")
    p.add_argument("action", nargs="?", default="status", choices=["status"])
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_dashboard)
    p = sub.add_parser("controller")
    p.add_argument("action", choices=["next"])
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_controller)
    p = sub.add_parser("eval")
    p.add_argument("action", choices=["run", "sync"])
    p.add_argument("--suite", default="smoke")
    p.add_argument("--fixture")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_eval)
    p = sub.add_parser("gen-docs")
    p.add_argument("command", choices=["list", "check", "write", "render"], default="check")
    p.set_defaults(func=cmd_gen_docs)
    p = sub.add_parser("build-plugin")
    p.add_argument("--dest")
    p.set_defaults(func=cmd_build_plugin)
    p = sub.add_parser("upgrade")
    p.add_argument("--host", default="codex")
    p.set_defaults(func=cmd_upgrade)
    p = sub.add_parser("version")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_version)
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
