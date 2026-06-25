#!/usr/bin/env python3
"""
Claude Code PreToolUse hook for Bash.

Blocks or asks confirmation for risky shell commands in project workflows.
Input: JSON from Claude Code on stdin.
Output: JSON decision for PreToolUse, or no output to continue normal permission flow.
"""

import json
import os
import re
import subprocess
import sys


def emit_decision(decision: str, reason: str) -> None:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": decision,
            "permissionDecisionReason": reason,
        }
    }))


def current_branch(cwd: str) -> str:
    try:
        return subprocess.check_output(
            ["git", "branch", "--show-current"],
            cwd=cwd or None,
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=2,
        ).strip()
    except Exception:
        return ""


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    if payload.get("tool_name") != "Bash":
        return 0

    tool_input = payload.get("tool_input") or {}
    command = tool_input.get("command") or ""
    cwd = payload.get("cwd") or os.getcwd()
    normalized = " ".join(command.lower().split())

    # Block direct push to protected branches.
    if re.search(r"\bgit\s+push\b", normalized):
        if re.search(r"(\bmain\b|\bmaster\b|:main\b|:master\b)", normalized):
            emit_decision(
                "deny",
                "Bloqueado: não faça push direto para main/master. Crie uma branch de trabalho e abra Pull Request.",
            )
            return 0

    # Block commits while currently on protected branches.
    if re.search(r"\bgit\s+commit\b", normalized):
        branch = current_branch(cwd)
        if branch in {"main", "master"}:
            emit_decision(
                "deny",
                f"Bloqueado: commit direto na branch protegida '{branch}'. Crie uma branch de trabalho antes de commitar.",
            )
            return 0

    # Block clearly destructive filesystem commands.
    destructive_patterns = [
        r"\brm\s+-[^\n;]*r[^\n;]*f\s+(/|~|\$home\b|\.\s*$|\.\.\s*$)",
        r"\bchmod\s+-r\s+777\s+(/|~|\$home\b|\.\s*$)",
        r"\bchown\s+-r\b.*\s+(/|~|\$home\b)",
    ]
    if any(re.search(pattern, normalized) for pattern in destructive_patterns):
        emit_decision("deny", "Bloqueado: comando destrutivo de alto risco detectado.")
        return 0

    # Ask confirmation for commands that can discard work or mutate infra/state.
    ask_patterns = [
        r"\bgit\s+reset\s+--hard\b",
        r"\bgit\s+clean\s+-",
        r"\bdocker\s+compose\s+down\b.*\s-v\b",
        r"\bdocker\s+volume\s+rm\b",
        r"\bnpm\s+publish\b",
        r"\bterraform\s+(apply|destroy)\b",
        r"\bkubectl\s+(apply|delete|replace)\b",
    ]
    if any(re.search(pattern, normalized) for pattern in ask_patterns):
        emit_decision(
            "ask",
            "Confirme manualmente: este comando pode descartar trabalho, publicar artefatos ou alterar infraestrutura/estado.",
        )
        return 0

    # Prevent accidental exposure of env files through shell commands.
    if ".env" in normalized and ".env.example" not in normalized:
        if re.search(r"\b(cat|less|more|head|tail|grep|sed|awk|printenv)\b", normalized):
            emit_decision("deny", "Bloqueado: tentativa de ler ou imprimir arquivo/valor sensível de ambiente.")
            return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
