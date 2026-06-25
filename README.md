# Claude Code Operational Stack

Estrutura reutilizável de **subagents** e **skills** para Claude Code.

Este repositório contém apenas arquivos operacionais do Claude Code:

```txt
.claude/
├── agents/
└── skills/
```

Não coloque neste repositório:

- senhas
- tokens
- `.env`
- IPs sensíveis
- dados de clientes
- credenciais de produção
- scripts destrutivos de deploy

## Instalação por projeto

Copie a pasta `.claude` para a raiz do projeto onde você quer usar os agents e skills:

```bash
cp -r .claude /caminho/do/seu/projeto/
```

Depois abra o Claude Code dentro da raiz do projeto:

```bash
cd /caminho/do/seu/projeto
claude
```

Valide:

```txt
/agents
/skills
```

## Agents incluídos

- `backend-specialist`
- `frontend-specialist`
- `devops-engineer`
- `security-engineer`
- `corporate-cto`
- `engineering-manager`
- `software-architect`
- `qa-engineer`
- `product-owner`
- `project-manager`
- `senior-fullstack-developer`
- `technical-writer`

## Uso prático

```txt
Use o backend-specialist para revisar minha API de autenticação.
```

```txt
Use o devops-engineer para analisar meu docker-compose e proxy nginx.
```

```txt
/security-audit revisar autenticação, autorização e exposição de secrets
```

```txt
/api-design criar endpoint de cadastro de cliente
```

## Regra de arquitetura

```txt
Agents = quem pensa
Skills = como executa
CLAUDE.md = contexto fixo do projeto
```
