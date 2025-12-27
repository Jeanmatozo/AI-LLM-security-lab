# src/app_agent_tools/tools.py
from __future__ import annotations

import datetime
from pathlib import Path
from typing import List

# -----------------------------
# Paths + logging
# -----------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]
SANDBOX_DIR = REPO_ROOT / "data" / "agent_files"
LOG_DIR = REPO_ROOT / "logs"
LOG_FILE = LOG_DIR / "week7_agent_log.txt"

LOG_DIR.mkdir(exist_ok=True)
SANDBOX_DIR.mkdir(exist_ok=True)

# -----------------------------
# Allowlist
# -----------------------------

ALLOWED_FILES: List[str] = [
    "public_info.txt",
]

# -----------------------------
# Logging helper (tool-level)
# -----------------------------

def _log_tool_event(event: str, payload: dict) -> None:
    ts = datetime.datetime.now().isoformat()
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"Time: {ts}\n")
        f.write(f"Event: {event}\n")
        for k, v in payload.items():
            f.write(f"{k}: {v}\n")


# -----------------------------
# Tools
# -----------------------------

def list_allowed_files() -> str:
    """
    List filenames that are explicitly allowlisted for reading.
    """
    _log_tool_event(
        "tool_list_allowed_files",
        {"allowed_files": ", ".join(ALLOWED_FILES)},
    )
    return "\n".join(ALLOWED_FILES)


def read_sandbox_file(filename: str) -> str:
    """
    Read an allowlisted file from the sandbox directory.

    SECURITY PROPERTIES:
    - filename must be exactly allowlisted
    - no path traversal
    - all outcomes are logged
    """

    # Enforce exact allowlist
    if filename not in ALLOWED_FILES:
        _log_tool_event(
            "tool_read_sandbox_file_denied",
            {"filename": filename},
        )
        return f"DENIED: filename '{filename}' is not allowlisted."

    file_path = SANDBOX_DIR / filename

    if not file_path.exists():
        _log_tool_event(
            "tool_read_sandbox_file_missing",
            {"filename": filename},
        )
        return f"MISSING: filename '{filename}' does not exist."

    content = file_path.read_text(encoding="utf-8")

    _log_tool_event(
        "tool_read_sandbox_file_ok",
        {"filename": filename, "bytes": len(content)},
    )

    return content

