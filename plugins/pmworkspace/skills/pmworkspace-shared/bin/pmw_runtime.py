#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import pathlib
import re
import subprocess
from datetime import datetime, timezone
from typing import Any


SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
STATE_DIR = pathlib.Path(os.environ.get("PMW_HOME", str(pathlib.Path.home() / ".pmworkspace"))).expanduser()

TERMINAL_STATUS_TOKENS = [
    "已完成",
    "可交付",
    "可进入原型复审",
    "已结束",
    "DONE",
    "complete",
]

BRIEF_STATUS_LABELS = [
    "确认状态",
    "对齐状态",
    "状态",
]

BRIEF_STATUS_NEGATIVE_TOKENS = [
    "待确认",
    "草稿",
    "缺失门槛",
    "有漂移",
    "实质漂移",
    "未对齐",
    "需要补充",
    "待补充",
]


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def now_fragment() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def current_slug() -> str:
    env_slug = os.environ.get("PMW_PROJECT_SLUG", "").strip()
    if env_slug:
        return env_slug
    try:
        return subprocess.check_output([str(SCRIPT_DIR / "pmw-slug")], text=True).strip()
    except Exception:
        return "local-project"


def projects_root() -> pathlib.Path:
    return STATE_DIR / "projects"


def project_dir(slug: str | None = None) -> pathlib.Path:
    path = projects_root() / (slug or current_slug())
    path.mkdir(parents=True, exist_ok=True)
    (path / "runs").mkdir(parents=True, exist_ok=True)
    return path


def project_path(slug: str | None = None) -> pathlib.Path:
    return project_dir(slug) / "project.json"


def read_json(path: pathlib.Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except Exception:
        return {}


def write_json(path: pathlib.Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_jsonl(path: pathlib.Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        try:
            value = json.loads(line)
        except Exception:
            continue
        if isinstance(value, dict):
            rows.append(value)
    return rows


def append_jsonl(path: pathlib.Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def read_project(slug: str | None = None) -> dict[str, Any]:
    data = read_json(project_path(slug))
    data.setdefault("slug", slug or current_slug())
    return data


def write_project(data: dict[str, Any], slug: str | None = None) -> None:
    resolved_slug = slug or str(data.get("slug") or current_slug())
    data["slug"] = resolved_slug
    data["updated_at"] = now()
    write_json(project_path(resolved_slug), data)
    try:
        (STATE_DIR / "current-project").write_text(resolved_slug + "\n", encoding="utf-8")
    except Exception:
        pass


def project_for_run(run_id: str) -> str:
    if not run_id:
        return ""
    for path in sorted(projects_root().glob(f"*/runs/{run_id}.jsonl")):
        return path.parent.parent.name
    return ""


def run_path(run_id: str, slug: str | None = None) -> pathlib.Path:
    resolved_slug = slug or project_for_run(run_id) or current_slug()
    return project_dir(resolved_slug) / "runs" / f"{run_id}.jsonl"


def is_terminal_status(value: str) -> bool:
    return any(token in (value or "") for token in TERMINAL_STATUS_TOKENS)


def project_context(project: dict[str, Any]) -> dict[str, str]:
    return {
        "run_id": str(project.get("current_run_id") or ""),
        "task_digest": str(project.get("current_task_digest") or ""),
        "input_revision": str(project.get("current_input_revision") or ""),
        "controller_verdict": str(project.get("last_controller_verdict") or ""),
        "context_source": "project_current",
        "legacy_context_status": "current",
    }


def run_snapshot(run_id: str, slug: str | None = None) -> dict[str, str]:
    rows = read_jsonl(run_path(run_id, slug))
    for row in reversed(rows):
        if row.get("event") != "task_intake":
            continue
        digest = str(row.get("task_digest") or "")
        revision = str(row.get("input_revision") or "")
        if digest or revision:
            return {
                "run_id": run_id,
                "task_digest": digest,
                "input_revision": revision,
                "controller_verdict": str(row.get("controller_verdict") or row.get("status") or ""),
                "context_source": "run_snapshot",
                "legacy_context_status": "current",
            }
    return {
        "run_id": run_id,
        "task_digest": "",
        "input_revision": "",
        "controller_verdict": "",
        "context_source": "run_snapshot",
        "legacy_context_status": "legacy_no_snapshot",
    }


def resolve_context(project: dict[str, Any], run_id: str | None = None) -> dict[str, str]:
    if run_id:
        return run_snapshot(run_id, str(project.get("slug") or "") or None)
    return project_context(project)


def stamp_row(row: dict[str, Any], context: dict[str, str]) -> dict[str, Any]:
    row["run_id"] = context.get("run_id", "")
    row["task_digest"] = context.get("task_digest", "")
    row["input_revision"] = context.get("input_revision", "")
    row["controller_verdict"] = context.get("controller_verdict", "")
    row["context_source"] = context.get("context_source", "")
    row["legacy_context_status"] = context.get("legacy_context_status", "current")
    return row


def row_matches_context(row: dict[str, Any], context: dict[str, str]) -> bool:
    if context.get("legacy_context_status") == "legacy_no_snapshot":
        return False
    run_id = str(context.get("run_id") or "")
    digest = str(context.get("task_digest") or "")
    revision = str(context.get("input_revision") or "")
    if run_id and str(row.get("run_id") or "") != run_id:
        return False
    if digest and str(row.get("task_digest") or "") != digest:
        return False
    if revision and str(row.get("input_revision") or "") != revision:
        return False
    return True


def row_context_status(row: dict[str, Any], context: dict[str, str]) -> str:
    if row_matches_context(row, context):
        return "current_artifact"
    if not row.get("task_digest") and not row.get("input_revision"):
        return "legacy_no_snapshot"
    if row.get("run_id") == context.get("run_id"):
        return "legacy_mixed_context"
    return "candidate_context"


def confirmation_state(status: str, summary: str = "", explicit: str = "") -> str:
    if explicit in {"confirmed", "pending", "rejected"}:
        return explicit
    text = f"{status} {summary}"
    if any(token in text for token in ["拒绝", "不同意", "驳回", "rejected"]):
        return "rejected"
    if any(token in text for token in ["已确认", "已对齐", "批准", "用户确认", "用户同意", "confirmed"]):
        return "confirmed"
    return "pending"


def event_is_confirmed(row: dict[str, Any]) -> bool:
    state = str(row.get("confirm_state") or "")
    if state:
        return state == "confirmed"
    return confirmation_state(str(row.get("status") or ""), str(row.get("summary") or "")) == "confirmed"


def event_is_rejected(row: dict[str, Any]) -> bool:
    state = str(row.get("confirm_state") or "")
    if state:
        return state == "rejected"
    return confirmation_state(str(row.get("status") or ""), str(row.get("summary") or "")) == "rejected"


def clean_brief_status_line(line: str) -> str:
    return re.sub(r"^[\s#>*\-•]+", "", line or "").strip()


def extract_brief_status_line(text: str) -> str:
    for line in (text or "").splitlines()[:160]:
        stripped = clean_brief_status_line(line)
        for label in BRIEF_STATUS_LABELS:
            if re.match(rf"^{re.escape(label)}\s*[：:]", stripped):
                return stripped
    return ""


def brief_is_aligned(text: str) -> bool:
    status_line = extract_brief_status_line(text)
    if not status_line:
        return False
    return "已对齐" in status_line and not any(token in status_line for token in BRIEF_STATUS_NEGATIVE_TOKENS)


def brief_fingerprint(text: str) -> str:
    normalized = "\n".join(line.rstrip() for line in (text or "").splitlines()).strip()
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:16]


def latest_brief_lock(project: dict[str, Any]) -> dict[str, Any]:
    context = resolve_context(project)
    run_id = str(context.get("run_id") or "")
    if not run_id:
        return {}
    latest_brief = str(project.get("latest_brief") or "")
    latest_version = str(project.get("latest_brief_version") or "")
    rows = read_jsonl(run_path(run_id, str(project.get("slug") or "") or None))
    for row in reversed(rows):
        if not row_matches_context(row, context):
            continue
        event = str(row.get("event") or "")
        if event == "brief_change" and str(row.get("lock_status") or "") == "needs_relock":
            return row
        if event != "brief_lock":
            continue
        if latest_brief and str(row.get("brief_path") or "") != latest_brief:
            continue
        if latest_version and str(row.get("brief_version") or "") != latest_version:
            continue
        return row
    return {}


def brief_lock_is_locked(row: dict[str, Any]) -> bool:
    return str(row.get("lock_status") or row.get("status") or "") == "locked"


IMAGE_OUTPUT_MODES = {"three_page_exploration", "three_page_experiment", "single_page_confirmed"}


def normalize_image_output_mode(value: str = "", summary: str = "", locked: bool = True) -> str:
    raw = str(value or "").strip()
    if raw in IMAGE_OUTPUT_MODES:
        return raw
    text = f"{raw} {summary or ''}"
    compact = re.sub(r"\s+", "", text)
    single_tokens = [
        "只要1个",
        "只要一个",
        "只出1个",
        "只出一个",
        "只生成1个",
        "只生成一个",
        "单页主方案",
        "单方案",
        "1个方案",
        "一个方案",
    ]
    if any(token in compact for token in single_tokens):
        return "single_page_confirmed"
    if not locked:
        return "three_page_exploration"
    return "three_page_experiment"


def image_output_mode_from_lock(lock: dict[str, Any], locked: bool = True) -> str:
    return normalize_image_output_mode(
        str(lock.get("image_output_mode") or ""),
        str(lock.get("summary") or ""),
        locked=locked,
    )


def expected_output_units(mode: str) -> int:
    return 1 if normalize_image_output_mode(mode) == "single_page_confirmed" else 3


def image_output_mode_label(mode: str) -> str:
    normalized = normalize_image_output_mode(mode)
    labels = {
        "three_page_exploration": "三页探索模式",
        "three_page_experiment": "三页实验模式",
        "single_page_confirmed": "单页主方案模式",
    }
    return labels.get(normalized, labels["three_page_experiment"])


def gate_id(subject: str, context: dict[str, str]) -> str:
    revision = context.get("input_revision") or "no-revision"
    return f"{revision}:{subject}"


def fingerprint(parts: list[Any]) -> str:
    raw = json.dumps(parts, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def operation_id(operation_type: str, context: dict[str, str], summary: str = "") -> str:
    seed = "|".join(
        [
            now_fragment(),
            operation_type or "operation",
            context.get("run_id", ""),
            context.get("task_digest", ""),
            context.get("input_revision", ""),
            summary or "",
        ]
    )
    return f"op_{hashlib.sha256(seed.encode('utf-8')).hexdigest()[:20]}"


def resolve_parent_context(project: dict[str, Any], run_id: str | None = None) -> dict[str, str]:
    context = resolve_context(project, run_id)
    return {
        "parent_run_id": context.get("run_id", ""),
        "parent_task_digest": context.get("task_digest", ""),
        "parent_input_revision": context.get("input_revision", ""),
        "context_source": context.get("context_source", ""),
        "legacy_context_status": context.get("legacy_context_status", "current"),
    }


def latest_operation(project: dict[str, Any], operation_type: str = "") -> dict[str, Any]:
    run_id = str(project.get("current_run_id") or "")
    if not run_id:
        return {}
    context = resolve_context(project)
    rows = read_jsonl(run_path(run_id, str(project.get("slug") or "") or None))
    for row in reversed(rows):
        if row.get("event") != "operation":
            continue
        if operation_type and row.get("operation_type") != operation_type:
            continue
        if not operation_matches_context(row, context):
            continue
        return row
    return {}


def operation_matches_context(row: dict[str, Any], context: dict[str, str]) -> bool:
    if context.get("legacy_context_status") == "legacy_no_snapshot":
        return False
    mappings = {
        "parent_run_id": context.get("run_id", ""),
        "parent_task_digest": context.get("task_digest", ""),
        "parent_input_revision": context.get("input_revision", ""),
    }
    for key, value in mappings.items():
        if value and str(row.get(key) or "") != str(value):
            return False
    return True


def operation_expected_units(operation: dict[str, Any], default: int = 1) -> int:
    try:
        value = int(operation.get("expected_output_units") or default)
    except (TypeError, ValueError):
        value = default
    return max(1, min(value, 12))


def operation_variant_roles(operation: dict[str, Any]) -> list[str]:
    raw = operation.get("variant_roles") or operation.get("variant_role") or []
    if isinstance(raw, str):
        roles = [item.strip() for item in re.split(r"[,，/、\s]+", raw) if item.strip()]
    elif isinstance(raw, list):
        roles = [str(item).strip() for item in raw if str(item).strip()]
    else:
        roles = []
    expected = operation_expected_units(operation, len(roles) or 1)
    while len(roles) < expected:
        roles.append(f"variant_{len(roles) + 1}")
    return roles[:expected]
