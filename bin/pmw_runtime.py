#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import pathlib
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


def gate_id(subject: str, context: dict[str, str]) -> str:
    revision = context.get("input_revision") or "no-revision"
    return f"{revision}:{subject}"


def fingerprint(parts: list[Any]) -> str:
    raw = json.dumps(parts, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]
