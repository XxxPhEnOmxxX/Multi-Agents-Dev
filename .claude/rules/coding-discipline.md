# Coding Discipline

## Regra central

Antes de escrever ou alterar código, pense no menor caminho seguro para resolver a issue.

O objetivo não é produzir mais código. O objetivo é resolver a tarefa com clareza, simplicidade, baixo risco e validação objetiva.

## Princípios obrigatórios

### 1. Think Before Coding

Antes de editar arquivos, declare:

- o que a issue pede;
- quais suposições estão sendo feitas;
- quais ambiguidades existem;
- quais arquivos provavelmente precisam mudar;
- qual é o critério verificável de sucesso;
- o que está fora do escopo.

Se houver ambiguidade que muda arquitetura, regra de negócio, segurança ou contrato público, pare e peça decisão ao usuário.

### 2. Simplicity First

Prefira a solução mais simples que resolva a issue.

Evite:

- abstrações antes da necessidade real;
- services genéricos para uso único;
- refatoração ampla sem solicitação;
- alteração de arquitetura sem issue própria;
- troca de biblioteca ou framework sem justificativa;
- complexidade para cenários futuros não pedidos.

Se duas soluções resolvem a issue, escolha a menor e mais fácil de validar.

### 3. Surgical Changes

Faça mudanças cirúrgicas.

Cada arquivo alterado deve ter relação direta com a issue.
Cada linha alterada deve ser justificável pelo escopo.

Evite:

- drive-by refactor;
- renomeações não relacionadas;
- formatação massiva sem necessidade;
- mexer em comentários ou arquivos fora da issue;
- misturar feature, refactor e limpeza no mesmo PR.

Se encontrar melhoria fora do escopo, registre como nova issue em vez de implementar junto.

### 4. Goal-Driven Execution

A task só está pronta quando os critérios de aceite forem verificados.

Antes de finalizar, confirme:

- a issue foi resolvida;
- os critérios de aceite foram checados;
- as validações foram executadas ou limitações foram registradas;
- o sistema foi iniciado localmente quando necessário;
- o diff foi revisado;
- riscos restantes foram documentados.

## Checklist antes de implementar

Antes de editar, responda internamente ou no plano:

```txt
Issue:
Objetivo exato:
Suposições:
Ambiguidades:
Solução mais simples:
Arquivos esperados:
Fora do escopo:
Critérios de sucesso:
Validações:
```

## Checklist antes de PR

Antes de abrir PR:

```txt
A solução é mínima?
O diff é cirúrgico?
Há refatoração fora do escopo?
Cada arquivo alterado está ligado à issue?
Os critérios de aceite foram verificados?
As validações foram executadas?
Os riscos foram documentados?
```

## Regra para reviewers

Agents revisores devem bloquear ou pedir separação quando encontrarem:

- alteração grande demais para a issue;
- abstração prematura;
- mudança de arquitetura não solicitada;
- alteração de contrato sem critério de aceite;
- modificação em arquivos não relacionados;
- testes ausentes para mudança crítica;
- validação declarada mas não executada.

## Regra final

Se a solução parece elegante, mas aumenta escopo, risco ou complexidade sem necessidade, escolha a solução mais simples.
