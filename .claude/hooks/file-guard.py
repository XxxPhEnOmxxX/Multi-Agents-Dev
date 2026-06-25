#!/usr/bin/env python3
"""
Claude Code PreToolUse hook for Read, Write and Edit.

Blocks access to files that should not be read or modified by an automated agent.
"""

import json
import os
import re
import sys


SENSITIVE_PATTERNS = [
    r"(^|/)\.env($|\.)",
    r"(^|/)secrets(/|$)",
    r"(^|/)credentials(/|$)",
    r"(^|/)config/credentials\.json$",
    r"(^|/)id_rsa$",
    r"(^|/)id_ed25519$",
    r"\.pem$",
    r"\.key$",
    r"\.p12$",
    r"\.pfx$",
    r"service-account.*\.json$",
]


def emit_deny(reason: str) -> None:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))


def normalize(path: str) -> str:
    return path.replace("\\", "/").lower()


def is_sensitive(path: str) -> bool:
    value = normalize(path)
    return any(re.search(pattern, value) for pattern in SENSITIVE_PATTERNS)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    tool_name = payload.get("tool_name")
    if tool_name not in {"Read", "Write", "Edit"}:
        return 0

    tool_input = payload.get("tool_input") or {}
    path = tool_input.get("file_path") or ""

    if not path:
        return 0

    if is_sensitive(path):
        emit_deny(
            f"Bloqueado: o arquivo '{os.path.basename(path)}' parece conter segredo, credencial ou dado sensível. Não leia nem modifique esse arquivo via Claude Code."
        )
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
