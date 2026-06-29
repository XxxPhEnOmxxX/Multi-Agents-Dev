# Claude Code Context Audit

Issue: #1
Related updates: #3, #5

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
7. Preload only the primary skill per subagent.
8. Invoke architecture/practice skills only on demand.
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

## Skill preload policy

Each subagent should preload only its primary operational skill through frontmatter `skills:`.

```txt
software-architect -> architecting-systems
frontend-specialist -> designing-frontend
backend-specialist -> building-backend-apis
security-engineer -> securing-apps
qa-engineer -> qa-github-actions
devops-engineer -> managing-docker-n8n-infra
```

Architecture/practice skills stay available on demand through the `Skill` tool:

```txt
ddd-modeling
clean-architecture
hexagonal-architecture
cqrs
code-quality
security-by-design
testing-strategy
capability-driven-integration
```

This avoids loading multiple long practice guides into every subagent context while preserving specialist access when the task requires it.

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

Issue #5 optimizes those skills so they are available on demand instead of being preloaded into every subagent context.

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
- Keep subagent preloaded skills minimal; use on-demand skills for specialized practice guidance.
```
