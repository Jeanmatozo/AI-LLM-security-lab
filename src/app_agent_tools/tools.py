# src/app_agent_tools/tools.py
from __future__ import annotations

import datetime
from pathlib import Path


# Repo root = <repo>/src/app_agent_tools/tools.py -> parents[2]
REPO_ROOT = Path(__file__).resolve().parents[2]
SANDBOX_DIR = REPO_ROOT / "data" / "agent_files"
SANDBOX_DIR.mkdir(parents=True, exist_ok=True)

LOG_DIR = REPO_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "week7_agent_log.txt"


def _log(line: str) -> None:
    ts = datetime.datetime.now().isoformat()
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"[{ts}] {line}\n")


def _safe_resolve_path(user_path: str) -> Path:
    """
    Only allow access inside data/agent_files/.
    This prevents path traversal like: ..\\..\\secrets.txt
    """
    p = (SANDBOX_DIR / user_path).resolve()
    if SANDBOX_DIR.resolve() not in p.parents and p != SANDBOX_DIR.resolve():
        raise ValueError("Access denied: path is outside the sandbox directory.")
    return p


def read_file(path: str) -> str:
    """
    Tool: Read a file from the sandbox (data/agent_files/).
    """
    _log(f"TOOL_CALL read_file path={path!r}")
    p = _safe_resolve_path(path)
    if not p.exists():
        msg = f"File not found: {p.name}"
        _log(f"TOOL_RESULT read_file error={msg!r}")
        return msg

    text = p.read_text(encoding="utf-8", errors="replace")
    _log(f"TOOL_RESULT read_file bytes={len(text)}")
    return text


def write_report(filename: str, content: str) -> str:
    """
    Tool: Write a report file inside the sandbox.
    This simulates an agent producing an artifact (incident report, summary, ticket draft, etc.).
    """
    _log(f"TOOL_CALL write_report filename={filename!r} content_len={len(content)}")

    # Force .txt or .md only (simple restriction)
    if not (filename.endswith(".txt") or filename.endswith(".md")):
        msg = "Only .txt or .md reports are allowed."
        _log(f"TOOL_RESULT write_report error={msg!r}")
        return msg

    p = _safe_resolve_path(filename)
    p.write_text(content, encoding="utf-8")
    _log(f"TOOL_RESULT write_report wrote={p.name!r}")
    return f"Wrote report: {p.name}"

