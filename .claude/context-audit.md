# Claude Code Context Audit

Issue: #1  
Related updates: #3, #5, #12, #14, #16

## Goal

Reduce always-loaded context while preserving detailed behavior through agents, skills, prompts, guides, templates, and reference documents.

The repository must support Claude Code, Codex-compatible workflows, and other coding-agent sessions without forcing every model to load every instruction.

---

## Methodology Applied

```txt
1. Keep CLAUDE.md as a compact Claude Code kernel.
2. Keep AGENTS.md as a thin Codex adapter, not a full duplicate.
3. Move detailed procedures to skills, prompts, guides, templates, or reference docs.
4. Avoid duplicated instructions across always-loaded files.
5. Use smart dispatch for model/agent routing.
6. Keep issue/PR workflow for continuity.
7. Preload only the primary skill per subagent.
8. Invoke architecture/practice/delivery skills only on demand.
9. Keep project-specific domains out of the base template.
10. Keep review/planning agents read-oriented by default.
11. Keep project/feature planning guides on demand.
12. Keep fill-in documents as templates so models load only what they need.
13. Keep full template documentation in reference files, not CLAUDE.md.
```

---

## Current Repository State

```txt
Always-loaded or likely entrypoint files:
- .claude/CLAUDE.md         -> Claude Code orchestration kernel
- AGENTS.md                 -> thin Codex-compatible adapter
- README.md                 -> human entrypoint

Detailed behavior loaded on demand:
- .claude/skills/orchestrating-agents/
- .claude/skills/smart-dispatch/
- .claude/skills/designing-frontend/
- .claude/skills/building-backend-apis/
- .claude/skills/securing-apps/
- .claude/skills/qa-github-actions/
- .claude/skills/managing-infrastructure/
- .claude/skills/architecting-systems/
- .claude/skills/ddd-modeling/
- .claude/skills/clean-architecture/
- .claude/skills/hexagonal-architecture/
- .claude/skills/cqrs/
- .claude/skills/code-quality/
- .claude/skills/security-by-design/
- .claude/skills/testing-strategy/
- .claude/skills/tlc-spec-driven/

Specialists:
- .claude/agents/software-architect.md
- .claude/agents/frontend-specialist.md
- .claude/agents/backend-specialist.md
- .claude/agents/security-engineer.md
- .claude/agents/qa-engineer.md
- .claude/agents/devops-engineer.md

Session prompts loaded on demand:
- .claude/prompts/bootstrap.md

Project and feature planning guides loaded on demand:
- .claude/guides/README.md
- .claude/guides/project-from-zero.md
- .claude/guides/feature-planning.md

Fill-in templates loaded only when needed:
- .claude/templates/project/
- .claude/templates/feature/

Reference documents not auto-loaded unless read:
- .claude/template-usage.md
- .claude/agent-skill-governance.md
- .claude/architecture-skill-matrix.md
- .claude/context-audit.md
```

---

## Important Decision

Do not duplicate detailed agent, skill, guide, or template behavior in `.claude/CLAUDE.md` or `AGENTS.md`.

`CLAUDE.md` should only contain:

```txt
- core flow;
- non-negotiable safety/workflow rules;
- short agent routing map;
- short on-demand skill routing hints;
- sensitive access gate;
- completion report format;
- pointers to skills and governance references.
```

`AGENTS.md` should only contain:

```txt
- compact Codex-compatible workflow;
- minimal read order;
- security and context-economy rules;
- pointer to .claude/ files when needed.
```

---

## Skill Preload Policy

Each subagent should preload only its primary operational skill through frontmatter `skills:`.

```txt
software-architect -> architecting-systems
frontend-specialist -> designing-frontend
backend-specialist -> building-backend-apis
security-engineer -> securing-apps
qa-engineer -> qa-github-actions
devops-engineer -> managing-infrastructure
```

Architecture/practice/delivery skills stay available on demand through the `Skill` tool:

```txt
ddd-modeling
clean-architecture
hexagonal-architecture
cqrs
code-quality
security-by-design
testing-strategy
tlc-spec-driven
```

`tlc-spec-driven` is intentionally on demand because it contains a full feature-delivery method with `.specs/`, references, validation, and lessons. Loading it globally would violate context economy.

Project-specific skills should be added only when the repository has a concrete domain, vendor, platform, integration style, or team convention that needs repeatable guidance.

---

## Guide and Template Policy

Guides should be short workflow spines.

Templates should contain fill-in Markdown structures.

Use this split:

```txt
.claude/guides/project-from-zero.md   -> what to do and in what order
.claude/templates/project/            -> detailed project files to create
.claude/guides/feature-planning.md    -> what to do and in what order
.claude/templates/feature/            -> detailed feature files to create
```

This prevents a model from loading a large guide when it only needs one template.

---

## Tool Permission Policy

Review/planning agents are read-oriented by default:

```txt
software-architect -> Read, Glob, Grep, Bash, Skill
security-engineer -> Read, Glob, Grep, Bash, Skill
qa-engineer -> Read, Glob, Grep, Bash, Skill
```

Implementation agents keep edit/write tools because their role is to apply scoped changes after planning and delegation:

```txt
backend-specialist
frontend-specialist
devops-engineer
```

---

## Documentation Policy

Full documentation belongs in reference files, not in `.claude/CLAUDE.md`.

```txt
README.md -> human entrypoint and quick-start guide
AGENTS.md -> thin Codex adapter
.claude/CLAUDE.md -> Claude Code orchestration kernel
.claude/prompts/bootstrap.md -> session bootstrap policy
.claude/guides/ -> project/feature planning spines
.claude/templates/ -> fill-in documents for project and feature specs
.claude/template-usage.md -> complete usage and adaptation guide
.claude/agent-skill-governance.md -> maintenance and extension rules
.claude/architecture-skill-matrix.md -> agent, skill, and permission matrix
.claude/context-audit.md -> context economy record
.claude/skills/tlc-spec-driven/references/ -> spec-driven delivery details
```

---

## Ongoing Rules

```txt
- Do not create AGENTS.md as a full duplicate of CLAUDE.md.
- Keep AGENTS.md thin for Codex compatibility.
- Do not add @ references from root CLAUDE.md unless absolutely necessary.
- Do not put long checklists in CLAUDE.md.
- Prefer skills/references/prompts/guides/templates for detailed behavior.
- Keep project and feature guides short; move fill-in structures to templates.
- Avoid prompt hooks unless the benefit clearly beats the extra API call cost.
- Keep context audit updated when adding always-loaded files or changing the skill/agent topology.
- Keep subagent preloaded skills minimal; use on-demand skills for specialized practice guidance.
- Keep tlc-spec-driven on demand; do not preload it globally.
- Keep the base template generic; add domain-specific skills only inside project adaptations.
- Keep review/planning agents read-oriented unless a project adaptation explicitly changes their role.
- Keep DevOps/infrastructure guidance generic; add Docker, Kubernetes, n8n, cloud, or vendor-specific detail only in project clones.
```
