#!/usr/bin/env python3
"""Project-local lessons helper for the tlc-spec-driven skill.

The agent supplies judgment. This script handles deterministic bookkeeping:
IDs, recurrence, confirmed/candidate/quarantined status, and rendering.

Canonical state: .specs/lessons.json
Rendered view:   .specs/LESSONS.md
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
from typing import Any

STORE_REL = os.path.join(".specs", "lessons.json")
RENDER_REL = os.path.join(".specs", "LESSONS.md")

SIGNALS = {
    "ac_gap": "Acceptance criterion gap",
    "surviving_mutant": "Discrimination sensor mutant survived",
    "spec_precision_gap": "Spec precision gap",
    "spec_deviation": "Implementation deviated from spec/design",
    "gate_fail": "Gate check failed",
}

DEFAULTS = {
    "promote_threshold": 2,
    "quarantine_threshold": 2,
}


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def norm(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def key(signal: str, text: str) -> str:
    return f"{signal}::{norm(text)}"


def store_path(root: str) -> str:
    return os.path.join(root, STORE_REL)


def render_path(root: str) -> str:
    return os.path.join(root, RENDER_REL)


def load(root: str) -> dict[str, Any]:
    path = store_path(root)
    if not os.path.exists(path):
        return {
            "schema": 1,
            "next_id": 1,
            "promote_threshold": DEFAULTS["promote_threshold"],
            "quarantine_threshold": DEFAULTS["quarantine_threshold"],
            "lessons": [],
        }
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    data.setdefault("schema", 1)
    data.setdefault("next_id", 1)
    data.setdefault("promote_threshold", DEFAULTS["promote_threshold"])
    data.setdefault("quarantine_threshold", DEFAULTS["quarantine_threshold"])
    data.setdefault("lessons", [])
    return data


def save(root: str, data: dict[str, Any]) -> None:
    os.makedirs(os.path.join(root, ".specs"), exist_ok=True)
    with open(store_path(root), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    render(root, data)


def render(root: str, data: dict[str, Any]) -> None:
    grouped = {"confirmed": [], "candidate": [], "quarantined": []}
    for lesson in data["lessons"]:
        grouped.setdefault(lesson.get("status", "candidate"), []).append(lesson)

    lines = [
        "# LESSONS — auto-maintained by tlc-spec-driven/scripts/lessons.py",
        "",
        "> Do not hand-edit. Canonical state lives in `.specs/lessons.json`.",
        "",
    ]

    sections = [
        ("Confirmed", "confirmed", "Load these at Specify/Design."),
        ("Candidates", "candidate", "Tracked, not trusted yet."),
        ("Quarantined", "quarantined", "Ignore until reviewed."),
    ]

    for title, status, note in sections:
        lines.extend([f"## {title}", "", note, ""])
        items = sorted(grouped.get(status, []), key=lambda x: x["id"])
        if not items:
            lines.extend(["_none_", ""])
            continue
        for item in items:
            scope = f" · scope: `{item['scope']}`" if item.get("scope") else ""
            lines.append(f"### {item['id']} — {item['text']}")
            lines.append(f"- signal: `{item['signal']}` · recurrence: {item['recurrence']}{scope}")
            lines.append(f"- features: {', '.join(item.get('features', [])) or '—'}")
            if item.get("evidence"):
                lines.append(f"- evidence: {item['evidence'][0]}")
            lines.append(f"- last seen: {item.get('last_seen', '—')}")
            lines.append("")

    with open(render_path(root), "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")


def cmd_init(args: argparse.Namespace) -> int:
    data = load(args.root)
    save(args.root, data)
    print(f"Initialized {STORE_REL} and {RENDER_REL}")
    return 0


def cmd_add(args: argparse.Namespace) -> int:
    if args.signal not in SIGNALS:
        print(f"ERROR: --signal must be one of {sorted(SIGNALS)}", file=sys.stderr)
        return 2
    if not args.source.strip():
        print("ERROR: --source is required; lessons must be grounded.", file=sys.stderr)
        return 2
    if not args.feature.strip():
        print("ERROR: --feature is required.", file=sys.stderr)
        return 2
    if len(args.text.strip()) < 12:
        print("ERROR: --text is too short.", file=sys.stderr)
        return 2

    data = load(args.root)
    existing = None
    lesson_key = key(args.signal, args.text)
    for lesson in data["lessons"]:
        if lesson.get("key") == lesson_key:
            existing = lesson
            break

    timestamp = now()
    evidence = args.source if not args.scope else f"{args.source} ({args.scope})"

    if existing:
        if args.feature not in existing["features"]:
            existing["features"].append(args.feature)
        if evidence not in existing["evidence"]:
            existing["evidence"].append(evidence)
        existing["recurrence"] = len(existing["features"])
        existing["last_seen"] = timestamp
        if existing["status"] == "candidate" and existing["recurrence"] >= data["promote_threshold"]:
            existing["status"] = "confirmed"
        save(args.root, data)
        print(f"UPDATED {existing['id']} status={existing['status']} recurrence={existing['recurrence']}")
        return 0

    lesson_id = f"L-{data['next_id']:03d}"
    data["next_id"] += 1
    data["lessons"].append({
        "id": lesson_id,
        "key": lesson_key,
        "text": args.text.strip(),
        "signal": args.signal,
        "scope": args.scope.strip(),
        "status": "candidate",
        "features": [args.feature.strip()],
        "recurrence": 1,
        "harmful": 0,
        "evidence": [evidence],
        "created": timestamp,
        "last_seen": timestamp,
    })
    save(args.root, data)
    print(f"ADDED {lesson_id} status=candidate recurrence=1")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    data = load(args.root)
    rows = []
    for lesson in data["lessons"]:
        if args.status != "all" and lesson.get("status") != args.status:
            continue
        if args.query and args.query.lower() not in lesson["text"].lower():
            continue
        if args.scope and args.scope.lower() not in lesson.get("scope", "").lower():
            continue
        rows.append(lesson)

    if not rows:
        print(f"(no {args.status} lessons)")
        return 0

    for lesson in sorted(rows, key=lambda x: x["id"]):
        scope = f" [scope:{lesson['scope']}]" if lesson.get("scope") else ""
        print(f"{lesson['id']} ({lesson['status']}, x{lesson['recurrence']}){scope}: {lesson['text']}")
    return 0


def cmd_penalize(args: argparse.Namespace) -> int:
    data = load(args.root)
    for lesson in data["lessons"]:
        if lesson["id"].lower() == args.id.lower():
            lesson["harmful"] = lesson.get("harmful", 0) + 1
            lesson["last_seen"] = now()
            if lesson["harmful"] >= data["quarantine_threshold"]:
                lesson["status"] = "quarantined"
            save(args.root, data)
            print(f"PENALIZED {lesson['id']} harmful={lesson['harmful']} status={lesson['status']}")
            return 0
    print(f"ERROR: no lesson with id {args.id}", file=sys.stderr)
    return 2


def cmd_status(args: argparse.Namespace) -> int:
    data = load(args.root)
    counts = {"confirmed": 0, "candidate": 0, "quarantined": 0}
    for lesson in data["lessons"]:
        counts[lesson.get("status", "candidate")] = counts.get(lesson.get("status", "candidate"), 0) + 1
    print(f"lessons: {len(data['lessons'])} total | confirmed={counts['confirmed']} candidate={counts['candidate']} quarantined={counts['quarantined']}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="lessons.py")
    parser.add_argument("--root", default=".", help="Project root containing .specs/.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    init = sub.add_parser("init")
    init.set_defaults(fn=cmd_init)

    add = sub.add_parser("add")
    add.add_argument("--feature", required=True)
    add.add_argument("--signal", required=True, choices=sorted(SIGNALS))
    add.add_argument("--source", required=True)
    add.add_argument("--text", required=True)
    add.add_argument("--scope", default="")
    add.set_defaults(fn=cmd_add)

    list_cmd = sub.add_parser("list")
    list_cmd.add_argument("--status", default="confirmed", choices=["confirmed", "candidate", "quarantined", "all"])
    list_cmd.add_argument("--query", default="")
    list_cmd.add_argument("--scope", default="")
    list_cmd.set_defaults(fn=cmd_list)

    penalize = sub.add_parser("penalize")
    penalize.add_argument("--id", required=True)
    penalize.set_defaults(fn=cmd_penalize)

    status = sub.add_parser("status")
    status.set_defaults(fn=cmd_status)

    args = parser.parse_args(argv)
    args.root = os.path.abspath(args.root)
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
