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

- ler a visão fixa do produto;
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

A skill `delegate-to-codex` deve ser usada somente por decisão do Claude principal, com apoio da skill `orchestrator-codex-gate`.

## Gestão por Issues e PRs

Fonte de verdade recomendada:

```txt
PROJECT_OBJECTIVE.md = visão fixa do produto
GitHub Issues        = trabalho pendente
Pull Requests        = trabalho implementado
Commits              = histórico técnico real
```

Regra operacional:

```txt
Nenhuma feature deve ser implementada sem issue aberta,
salvo autorização explícita do usuário.
```

Fluxo padrão:

```txt
issue -> branch -> commit -> push -> Pull Request -> merge -> issue fechada
```

O PR deve usar:

```txt
Closes #ID
```

quando resolver a issue.

## Disciplina de código

Inspirado nos princípios de simplicidade e execução orientada por objetivo, a estrutura agora exige:

```txt
Think Before Coding
Simplicity First
Surgical Changes
Goal-Driven Execution
```

Na prática, antes de alterar código o agente deve declarar:

- o que a issue pede;
- suposições;
- ambiguidades;
- solução mais simples aceitável;
- fora do escopo;
- critérios verificáveis de sucesso;
- validações planejadas.

Antes de PR, o agente deve executar:

- `minimal-diff-review`: confirma que o diff é pequeno, focado e diretamente ligado à issue;
- `success-criteria-check`: confirma que os critérios de aceite foram verificados com evidências.

## Frontend Design

A skill `frontend-design` adiciona uma camada de direção visual para evitar interfaces genéricas.

Ela deve ser usada quando a tarefa envolver:

- nova tela;
- redesign;
- painel admin;
- dashboard;
- landing page;
- componente visual importante;
- design system;
- UX writing;
- empty states, erros, alerts, toasts ou mensagens de formulário.

Agentes que recebem essa skill:

- `frontend-specialist`;
- `senior-fullstack-developer`;
- `product-owner`;
- `qa-engineer`;
- `software-architect`.

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

Skills importantes para o fluxo GitHub, disciplina de código e frontend:

- `issue-to-feature-flow`: transforma uma issue em execução planejada com agent, skills, branch e validações.
- `karpathy-code-discipline`: força pensar antes de codar, declarar suposições, evitar overengineering e escolher a solução mínima.
- `minimal-diff-review`: revisa se o diff é cirúrgico, focado e diretamente ligado à issue.
- `success-criteria-check`: transforma critérios de aceite em validações verificáveis e registra evidências.
- `frontend-design`: define direção visual específica ao produto, copy de interface, identidade visual e revisão estética.
- `pr-from-issue`: cria PR rastreável com `Closes #ID`, validações, revisores, smoke test e rollback.
- `orchestrator-codex-gate`: decide se Codex deve ser usado.
- `delegate-to-codex`: delega análise/execução ao Codex quando aprovado pelo orquestrador.

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
PROJECT_OBJECTIVE.md = visão fixa do produto
GitHub Issues = backlog e pendências
Pull Requests = entregas implementadas
Rules = instruções modulares por tópico
Settings = permissões e hooks compartilhados
Agents = especialistas executores/revisores
Skills = procedimentos reutilizáveis
Templates = padrões de issue e PR
Coding Discipline = simplicidade, diff cirúrgico e critérios verificáveis
Frontend Design = identidade visual, UX writing e qualidade estética de interface
```
