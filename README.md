# Multi-Agents-Dev

Estrutura reutilizável de **subagents**, **skills** e instruções de projeto para Claude Code.

Este repositório contém apenas arquivos operacionais do Claude Code:

```txt
.claude/
├── CLAUDE.md
├── agents/
└── skills/
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

## Regra de arquitetura

```txt
Claude principal = orquestrador soberano
CLAUDE.md = instruções persistentes do projeto
Agents = especialistas executores/revisores
Skills = procedimentos reutilizáveis
```
