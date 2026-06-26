# Skill: Issue to Feature Flow

## Objetivo

Transformar uma GitHub Issue em uma entrega de feature pequena, validável e rastreável.

Use esta skill quando o usuário pedir para implementar uma issue, continuar uma task pendente ou escolher a próxima feature do backlog.

## Entradas esperadas

- Número da issue, URL da issue ou descrição da task.
- Repositório alvo.
- Objetivo fixo do projeto, quando existir.
- Stack do projeto.

## Procedimento

### 1. Ler contexto fixo

Antes de implementar, leia:

- `CLAUDE.md`, quando existir;
- `AGENTS.md`, quando existir;
- `.ai/PROJECT_OBJECTIVE.md`, quando existir;
- documentação equivalente indicada pelo usuário.

### 2. Resolver a issue

Identifique:

- número da issue;
- título;
- objetivo;
- escopo permitido;
- fora do escopo;
- critérios de aceite;
- labels de tipo, área, status e risco;
- dependências e bloqueios.

Se a issue estiver vaga, gere uma proposta de refinamento antes de implementar.

### 3. Aplicar disciplina antes de codar

Use a skill `karpathy-code-discipline` antes de alterar arquivos.

Declare:

- o que a issue realmente pede;
- o que não está sendo pedido;
- suposições importantes;
- ambiguidades;
- solução mais simples aceitável;
- arquivos prováveis;
- critérios verificáveis de sucesso.

Se a ambiguidade afetar regra de negócio, segurança, contrato público, banco ou produção, peça decisão antes de seguir.

### 4. Definir critérios de sucesso

Use a skill `success-criteria-check` para transformar os critérios de aceite em checklist verificável.

Cada critério deve ter:

```txt
Critério:
Validação:
Evidência esperada:
```

Não implemente tarefa vaga sem critério verificável mínimo.

### 5. Classificar a task

Classifique a issue como uma ou mais categorias:

- backend;
- frontend;
- fullstack;
- devops;
- segurança;
- teste;
- documentação;
- arquitetura;
- produto/projeto.

### 6. Escolher agent principal

Escolha um agent principal conforme a task:

- `backend-specialist` para API, banco, services e regras de negócio;
- `frontend-specialist` para UI, React, painel e responsividade;
- `senior-fullstack-developer` para feature ponta a ponta;
- `devops-engineer` para Docker, CI/CD, proxy e infraestrutura;
- `security-engineer` para auth, permissões, dados sensíveis e risco;
- `qa-engineer` para testes, regressão e validações;
- `software-architect` para arquitetura e refatoração estrutural;
- `technical-writer` para documentação.

### 7. Declarar skills/procedimentos

Declare as skills/procedimentos aplicáveis, por exemplo:

- `karpathy-code-discipline`;
- `success-criteria-check`;
- `minimal-diff-review`;
- `api-design`;
- `database-design`;
- `frontend-ui-review`;
- `responsive-design`;
- `security-audit`;
- `test-strategy`;
- `docker-infrastructure`;
- `feature-team-flow`;
- `pr-from-issue`.

### 8. Escolher revisores

Escolha revisores simulados quando houver risco ou escopo multidisciplinar:

- backend relevante: `backend-specialist`;
- frontend/UI: `frontend-specialist`;
- segurança/auth/dados sensíveis: `security-engineer`;
- testes/regressão: `qa-engineer`;
- arquitetura/refatoração grande: `software-architect`;
- infraestrutura: `devops-engineer`;
- documentação de uso/API/operação: `technical-writer`.

### 9. Criar branch

Use branch vinculada à issue:

```txt
feat/issue-123-descricao-curta
fix/issue-123-descricao-curta
refactor/issue-123-descricao-curta
docs/issue-123-descricao-curta
```

Nunca trabalhe direto em `main` ou `master`.

### 10. Implementar escopo mínimo

Durante a implementação:

- altere somente o escopo da issue;
- não antecipe features futuras;
- não misture refatoração ampla com feature;
- preserve comportamento existente fora do escopo;
- mantenha commits pequenos e claros;
- prefira solução direta quando não houver necessidade real de abstração;
- registre melhorias fora do escopo como novas issues.

### 11. Revisar diff mínimo

Antes de validar, use `minimal-diff-review` para confirmar:

- arquivos alterados têm relação direta com a issue;
- não há drive-by refactor;
- não há formatação massiva sem necessidade;
- não há abstração prematura;
- o PR está pequeno o suficiente para revisão segura.

### 12. Validar

Rode validações compatíveis com o projeto:

- testes;
- lint;
- build;
- typecheck;
- validação Docker;
- smoke test local quando aplicável.

Se o sistema envolver fluxo de usuário, API, frontend, Telegram/gateway, banco, autenticação ou Docker, tente subir localmente e validar.

Use `success-criteria-check` novamente para confirmar quais critérios passaram, falharam ou não puderam ser validados.

### 13. Preparar PR

Ao finalizar, use a skill `pr-from-issue` para montar a descrição do PR.

O PR deve conter `Closes #<issue>` quando a issue for resolvida.

## Saída esperada

Ao iniciar:

```txt
Issue:
Classificação:
Agent principal:
Revisores:
Skills:
Suposições:
Ambiguidades:
Solução mais simples:
Fora do escopo:
Critérios de sucesso:
Branch:
Validações planejadas:
Sistema local será iniciado:
Riscos:
```

Ao finalizar:

```txt
Issue:
Implementado:
Arquivos alterados:
Agent principal:
Revisores usados:
Skills:
Minimal Diff Review:
Critérios verificados:
Validações executadas:
Sistema local:
Smoke test:
Riscos restantes:
PR:
```
