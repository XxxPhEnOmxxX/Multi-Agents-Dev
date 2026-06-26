# GitHub Issues Workflow

## Fonte de verdade

Use estas fontes na seguinte ordem:

```txt
GitHub Issues = trabalho pendente
Pull Requests = trabalho implementado
Commits       = histórico técnico real
Código atual  = estado real da aplicação
```

A memória do chat não deve ser tratada como fonte de verdade para progresso do projeto.

## Regra central

Nenhuma feature deve ser implementada sem uma issue aberta ou uma justificativa explícita do usuário.

A issue representa o escopo pendente.
O Pull Request representa a entrega implementada.
O código atual representa o estado real da aplicação.

## Antes de implementar

Antes de iniciar qualquer alteração, o Claude principal deve:

1. Consultar ou pedir a issue da tarefa.
2. Confirmar se a issue está pronta para execução.
3. Verificar se a issue tem objetivo, escopo e critérios de aceite claros.
4. Identificar labels de tipo, área, status e risco, quando existirem.
5. Declarar agent principal, skills e revisores com base na issue.
6. Criar ou sugerir branch vinculada à issue.

## Quando não existir issue

Se o usuário pedir uma feature sem issue, o Claude principal deve preferir:

1. propor criar a issue primeiro;
2. gerar o conteúdo da issue;
3. aguardar autorização para implementar;
4. só implementar direto se o usuário pedir explicitamente para pular a issue.

Tarefas pequenas de documentação, correção emergencial ou diagnóstico podem ser executadas sem issue, mas isso deve ser declarado.

## Padrão de branch

Use nomes de branch vinculados à issue:

```txt
feat/issue-123-descricao-curta
fix/issue-123-descricao-curta
refactor/issue-123-descricao-curta
docs/issue-123-descricao-curta
```

## Durante a implementação

Durante a execução:

- altere somente o escopo descrito na issue;
- não implemente itens fora do escopo;
- registre bloqueios encontrados;
- mantenha alterações pequenas e revisáveis;
- rode validações compatíveis com a stack;
- suba o sistema localmente quando possível ou necessário;
- use agents revisores quando a issue envolver risco, múltiplas áreas ou regra crítica.

## Pull Request

Todo PR de feature deve vincular a issue usando:

```txt
Closes #<id-da-issue>
```

O PR deve conter:

- issue relacionada;
- resumo da entrega;
- agent principal;
- agents revisores usados ou justificativa para não usar;
- skills/procedimentos aplicáveis;
- arquivos alterados;
- validações executadas;
- se o sistema foi iniciado localmente;
- resultado de smoke test, quando aplicável;
- riscos conhecidos;
- plano de rollback.

## Fechamento da issue

Uma issue só deve ser considerada concluída quando:

- o PR vinculado foi criado;
- as validações foram registradas;
- os riscos restantes foram documentados;
- o escopo foi atendido;
- o PR contém `Closes #<id>` ou explicação equivalente.

## Labels recomendadas

Tipo:

```txt
type:feature
type:bug
type:refactor
type:docs
type:test
type:security
type:infra
```

Área:

```txt
area:admin
area:telegram
area:backend
area:frontend
area:database
area:auth
area:locations
area:schedules
area:hour-bank
area:notifications
area:audit
area:devops
```

Status:

```txt
status:ready
status:in-progress
status:blocked
status:review
```

Risco:

```txt
risk:low
risk:medium
risk:high
```

## Regra final

Se houver conflito entre memória de conversa, issue, PR e código atual, confie nesta ordem:

```txt
código atual + PRs mergeados
issues abertas
documentação do projeto
memória do chat
```
