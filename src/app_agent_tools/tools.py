# src/app_agent_tools/tools.py
from __future__ import annotations

import datetime
import re
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
    # "internal_notes.txt",     # add only if you truly want it readable
    # "confidential.txt",       # keep blocked for Week 7
}

# Very strict filename policy: only letters/numbers/_/-. and must end in .txt
FILENAME_RE = re.compile(r"^[A-Za-z0-9_.-]+\.txt$")

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
    raw = filename
    filename = filename.strip()

    # Reject suspicious filenames early (defense-in-depth)
    if not FILENAME_RE.match(filename):
        _log("tool_read_sandbox_file_rejected_bad_name", {"raw": raw, "normalized": filename})
        return "DENIED: invalid filename format."

    if filename not in ALLOWED_FILES:
        _log("tool_read_sandbox_file_denied", {"filename": filename})
        return f"DENIED: filename '{filename}' is not allowlisted."

    path = SANDBOX_DIR / filename
    if not path.exists():
        _log("tool_read_sandbox_file_missing", {"filename": filename, "path": str(path)})
        return f"ERROR: file '{filename}' not found in sandbox."

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

    """
    files = sorted(ALLOWED_FILES)
    _log("tool_list_allowed_files", {"allowed": files})
    return "\n".join(files) if files else "(no files allowlisted)"

