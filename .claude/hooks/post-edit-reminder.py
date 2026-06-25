#!/usr/bin/env python3
"""
Claude Code PostToolUse hook for Write/Edit.

Adds a lightweight reminder after file changes so the main Claude thread validates before commit/PR.
"""

import json
import os
import sys


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    tool_name = payload.get("tool_name")
    if tool_name not in {"Write", "Edit"}:
        return 0

    tool_input = payload.get("tool_input") or {}
    path = tool_input.get("file_path") or "arquivo alterado"
    filename = os.path.basename(path)

    print(json.dumps({
        "systemMessage": (
            f"Arquivo alterado: {filename}. Antes de commit/PR, revise o diff, rode validações compatíveis e verifique se não há secrets ou mudanças fora de escopo."
        )
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
