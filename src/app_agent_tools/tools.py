# src/app_agent_tools/tools.py
from __future__ import annotations

import datetime
from pathlib import Path
from typing import Any, Dict

# Repo root = parents[2] because: src/app_agent_tools/tools.py
REPO_ROOT = Path(__file__).resolve().parents[2]
SANDBOX_DIR = REPO_ROOT / "data" / "agent_files"
LOG_DIR = REPO_ROOT / "logs"
LOG_FILE = LOG_DIR / "week7_agent_log.txt"

LOG_DIR.mkdir(exist_ok=True)
SANDBOX_DIR.mkdir(parents=True, exist_ok=True)

# Only allow reading THESE exact filenames (least privilege)
ALLOWED_FILES = {
    "public_info.txt",
    # Intentionally NOT allowing confidential.txt
}

def _log(event: str, payload: Dict[str, Any]) -> None:
    ts = datetime.datetime.now().isoformat()
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"Time: {ts}\n")
        f.write(f"Event: {event}\n")
        for k, v in payload.items():
            f.write(f"{k}: {v}\n")

def read_sandbox_file(filename: str) -> str:
    """
    Safe tool: read only allowlisted files from data/agent_files/.
    """
    filename = filename.strip()

    if filename not in ALLOWED_FILES:
        msg = f"DENIED: filename '{filename}' is not allowlisted."
        _log("tool_read_sandbox_file_denied", {"filename": filename})
        return msg

    path = SANDBOX_DIR / filename
    if not path.exists():
        msg = f"ERROR: file '{filename}' not found in sandbox."
        _log("tool_read_sandbox_file_missing", {"filename": filename})
        return msg

    text = path.read_text(encoding="utf-8", errors="replace")
    _log("tool_read_sandbox_file_ok", {"filename": filename, "bytes": len(text)})
    return text

def list_allowed_files() -> str:
    """
    Safe tool: show the allowlist to the agent (prevents guessing).
    """
    files = sorted(ALLOWED_FILES)
    _log("tool_list_allowed_files", {"allowed": files})
    return "\n".join(files) if files else "(no files allowlisted)"
