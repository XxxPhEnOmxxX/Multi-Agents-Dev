# Multi-Agents-Dev

Estrutura reutilizável de **subagents**, **skills**, **rules**, **settings** e **hooks** para Claude Code.

Este repositório contém apenas arquivos operacionais do Claude Code:

```txt
.claude/
├── CLAUDE.md
├── settings.json
├── agents/
├── skills/
├── rules/
└── hooks/
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

- classificar a tarefa;
- escolher o subagent especializado;
- controlar execução local no WSL;
- decidir se Codex deve ser usado;
- revisar diff e validações;
- aprovar branch, commit, push e Pull Request.

A skill `delegate-to-codex` deve ser usada somente por decisão do Claude principal, com apoio da skill `orchestrator-codex-gate`.

## Rules

As regras modulares ficam em:

```txt
.claude/rules/
```

Arquivos incluídos:

- `git-workflow.md`
- `wsl-development.md`
- `security.md`
- `testing.md`
- `backend.md`
- `frontend.md`
- `documentation.md`
- `codex-delegation.md`

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
Rules = instruções modulares por tópico
Settings = permissões e hooks compartilhados
Agents = especialistas executores/revisores
Skills = procedimentos reutilizáveis
```
