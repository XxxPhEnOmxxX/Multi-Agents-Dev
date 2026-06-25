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

## Regra de arquitetura

```txt
Agents = quem pensa
Skills = como executa
CLAUDE.md = contexto fixo do projeto
```
