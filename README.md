# Multi-Agents-Dev

Estrutura reutilizável de **subagents**, **skills**, **rules**, **settings**, **hooks** e **templates GitHub** para Claude Code.

Este repositório contém arquivos operacionais para transformar um projeto em um fluxo de engenharia assistido por agentes:

```txt
.claude/
├── CLAUDE.md
├── settings.json
├── agents/
├── skills/
├── rules/
├── hooks/
└── templates/
```

## Instalação

Copie a pasta `.claude` para a raiz do projeto onde deseja usar os agents, skills e instruções do Claude.

```bash
cp -r .claude /caminho/do/seu/projeto/
cd /caminho/do/seu/projeto
claude
```

Valide dentro do Claude Code:

```txt
/agents
/skills
/hooks
/memory
```

## Orquestração

O Claude principal deve atuar como orquestrador soberano do fluxo.

A regra de orquestração fica em:

```txt
.claude/CLAUDE.md
```

Esse arquivo orienta o Claude principal a:

- consultar GitHub Issues como backlog;
- aplicar disciplina de código antes de editar;
- classificar a tarefa;
- escolher o subagent especializado;
- definir skills/procedimentos;
- decidir revisores;
- controlar execução local no WSL;
- decidir se Codex deve ser usado;
- revisar diff e validações;
- aprovar branch, commit, push e Pull Request.

## Gestão por Issues e PRs

Fonte de verdade recomendada:

```txt
GitHub Issues = trabalho pendente
Pull Requests = trabalho implementado
Commits       = histórico técnico real
Código atual  = estado real da aplicação
```

Fluxo padrão:

```txt
issue -> branch -> commit -> push -> Pull Request -> merge -> issue fechada
```

O PR deve usar `Closes #ID` quando resolver a issue.

## Disciplina de código

Antes de alterar código o agente deve declarar:

- o que a issue pede;
- suposições;
- ambiguidades;
- solução mais simples aceitável;
- fora do escopo;
- critérios verificáveis de sucesso;
- validações planejadas.

Antes de PR, o agente deve executar:

- `minimal-diff-review`;
- `success-criteria-check`.

## Frontend Design e UX Engineering

A camada frontend cobre UI visual, design system, UX engineering e implementação em stack moderna.

Skills principais:

- `frontend-design`: direção visual, identidade, copy e revisão estética.
- `frontend-design-system`: tokens, Tailwind, shadcn/ui, radius, tipografia, grid, spacing, imagens e aspect ratio.
- `frontend-ux-engineering`: filtros, busca, formulários, skeletons, empty states, erros, validação, mobile e feedback assíncrono.
- `next-react-tailwind-shadcn-motion`: implementação com Next.js, React, TypeScript, Tailwind CSS, shadcn/ui e Motion.

## Rules

As regras modulares ficam em:

```txt
.claude/rules/
```

Arquivos incluídos:

- `git-workflow.md`
- `github-issues-workflow.md`
- `coding-discipline.md`
- `wsl-development.md`
- `security.md`
- `testing.md`
- `backend.md`
- `frontend.md`
- `documentation.md`
- `codex-delegation.md`
- `feature-team-flow.md`

## Skills

As skills ficam em:

```txt
.claude/skills/
```

Skills importantes:

- `issue-to-feature-flow`
- `karpathy-code-discipline`
- `minimal-diff-review`
- `success-criteria-check`
- `frontend-design`
- `frontend-design-system`
- `frontend-ux-engineering`
- `next-react-tailwind-shadcn-motion`
- `pr-from-issue`
- `orchestrator-codex-gate`
- `delegate-to-codex`

## Templates GitHub

Templates reutilizáveis ficam em:

```txt
.claude/templates/github/
```

Incluídos:

```txt
.claude/templates/github/ISSUE_TEMPLATE/feature.md
.claude/templates/github/ISSUE_TEMPLATE/bug.md
.claude/templates/github/PULL_REQUEST_TEMPLATE.md
```

Ao aplicar em um projeto real, você pode copiar esses templates para:

```txt
.github/ISSUE_TEMPLATE/feature.md
.github/ISSUE_TEMPLATE/bug.md
.github/PULL_REQUEST_TEMPLATE.md
```

## Settings e hooks

Configuração compartilhada:

```txt
.claude/settings.json
```

Hooks incluídos:

```txt
.claude/hooks/bash-guard.py
.claude/hooks/file-guard.py
.claude/hooks/post-edit-reminder.py
```

Eles protegem contra:

- leitura/alteração de arquivos sensíveis;
- commit direto em branch protegida;
- push direto para `main` ou `master`;
- comandos destrutivos de alto risco;
- alterações sem lembrete de validação.

## Regra de arquitetura

```txt
Claude principal = orquestrador soberano
CLAUDE.md = instruções persistentes do projeto
GitHub Issues = backlog e pendências
Pull Requests = entregas implementadas
Commits = histórico técnico real
Rules = instruções modulares por tópico
Settings = permissões e hooks compartilhados
Agents = especialistas executores/revisores
Skills = procedimentos reutilizáveis
Templates = padrões de issue e PR
Coding Discipline = simplicidade, diff cirúrgico e critérios verificáveis
Frontend Design = identidade visual, UX writing e qualidade estética de interface
Frontend Design System = tokens, grids, tipografia, spacing, radius e componentes reutilizáveis
Frontend UX Engineering = estados, feedback, filtros, formulários, mobile e acessibilidade operacional
Frontend Stack = Next.js, React, TypeScript, Tailwind CSS, shadcn/ui e Motion
```
