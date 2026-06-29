# Claude Code Context Audit

Issue: #1
Related update: #3

## Goal

Reduce always-loaded context while preserving detailed behavior through skills and agents.

## Methodology applied

Based on the token-saving approach:

```txt
1. Audit always-loaded context.
2. Keep CLAUDE.md as a compact kernel.
3. Move detailed procedures to skills.
4. Avoid duplicated instructions.
5. Use smart dispatch for model/agent routing.
6. Keep issue/PR workflow for continuity.
```

## Current repository state

```txt
Always-loaded project orchestrator:
- .claude/CLAUDE.md

Detailed behavior loaded on demand:
- .claude/skills/orchestrating-agents/
- .claude/skills/smart-dispatch/
- .claude/skills/designing-frontend/
- .claude/skills/building-backend-apis/
- .claude/skills/securing-apps/
- .claude/skills/qa-github-actions/
- .claude/skills/managing-docker-n8n-infra/
- .claude/skills/architecting-systems/
- .claude/skills/ddd-modeling/
- .claude/skills/clean-architecture/
- .claude/skills/hexagonal-architecture/
- .claude/skills/cqrs/
- .claude/skills/code-quality/
- .claude/skills/security-by-design/
- .claude/skills/testing-strategy/
- .claude/skills/capability-driven-integration/

Specialists:
- .claude/agents/software-architect.md
- .claude/agents/frontend-specialist.md
- .claude/agents/backend-specialist.md
- .claude/agents/security-engineer.md
- .claude/agents/qa-engineer.md
- .claude/agents/devops-engineer.md

Reference documents not auto-loaded unless read:
- .claude/architecture-skill-matrix.md
- .claude/context-audit.md
```

## Important decision

Do not duplicate detailed agent behavior in `.claude/CLAUDE.md`.

The orchestrator kernel should only contain:

```txt
- core flow;
- non-negotiable safety/workflow rules;
- short agent routing map;
- sensitive access gate;
- completion report format;
- pointers to skills.
```

## Reduction applied

`.claude/CLAUDE.md` remains a compact kernel.

Detailed rules remain in project skills and supporting reference files, including:

```txt
.claude/skills/orchestrating-agents/SKILL.md
.claude/skills/orchestrating-agents/references/
.claude/skills/smart-dispatch/SKILL.md
.claude/skills/*/SKILL.md
```

## Architecture skill update

Issue #3 adds practice-based architecture skills without increasing the number of agents.

These skills are project skills under `.claude/skills/`, so Claude Code can load them on demand instead of keeping their full content in `.claude/CLAUDE.md`.

The distribution is documented in:

```txt
.claude/architecture-skill-matrix.md
```

## Ongoing rules

```txt
- Do not create AGENTS.md as an always-loaded duplicate.
- Do not add @ references from root CLAUDE.md unless absolutely necessary.
- Do not put long checklists in CLAUDE.md.
- Prefer skills/references/examples for detailed behavior.
- Avoid prompt hooks unless the benefit clearly beats the extra API call cost.
- Keep context audit updated when adding always-loaded files or changing the skill/agent topology.
```
