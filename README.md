# Multi-Agents-Dev

Estrutura reutilizável de **subagents** e **skills** para Claude Code.

Este repositório contém apenas arquivos operacionais do Claude Code:

```txt
.claude/
├── agents/
└── skills/
```

## Instalação

Copie a pasta `.claude` para a raiz do projeto onde deseja usar os agents e skills.

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

O agent `development-orchestrator` existe para padronizar essa decisão:

- classificar a tarefa;
- escolher o agent especializado;
- controlar execução local no WSL;
- decidir se Codex deve ser usado;
- revisar diff e validações;
- aprovar branch, commit, push e Pull Request.

A skill `delegate-to-codex` deve ser usada somente pelo orquestrador, com apoio da skill `orchestrator-codex-gate`.

## Regra de arquitetura

```txt
Claude principal = orquestrador soberano
Agents = especialistas executores/revisores
Skills = procedimentos reutilizáveis
CLAUDE.md = contexto fixo do projeto
```
