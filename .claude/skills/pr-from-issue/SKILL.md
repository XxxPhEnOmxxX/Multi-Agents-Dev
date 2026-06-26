# Skill: PR from Issue

## Objetivo

Criar uma Pull Request clara, auditável e vinculada à GitHub Issue que originou a entrega.

Use esta skill ao finalizar uma issue implementada, uma correção ou uma refatoração rastreada.

## Entradas esperadas

- Número da issue.
- Título da issue.
- Branch da implementação.
- Resumo do que foi alterado.
- Agent principal usado.
- Agents revisores usados ou justificativa para não usar.
- Skills/procedimentos aplicáveis.
- Suposições relevantes.
- Resultado de `minimal-diff-review`.
- Resultado de `success-criteria-check`.
- Validações executadas.
- Resultado do smoke test local, quando aplicável.
- Riscos conhecidos.
- Plano de rollback.

## Procedimento

### 1. Confirmar escopo

Antes de abrir PR, confirme:

- a alteração resolve a issue;
- o escopo não extrapolou a issue;
- não houve alteração sensível fora do combinado;
- o diff não contém segredos, `.env`, tokens, chaves ou dados reais;
- a branch não é `main` nem `master`.

### 2. Confirmar disciplina de implementação

Antes de montar o PR, confirme:

- suposições importantes foram declaradas;
- ambiguidades relevantes foram resolvidas ou registradas;
- a solução escolhida é a mais simples que atende à issue;
- não houve overengineering;
- não houve drive-by refactor;
- o diff é cirúrgico;
- cada arquivo alterado tem relação direta com a issue.

Use `minimal-diff-review` antes de abrir PR.

### 3. Revisar diff

Revise o diff e confirme:

- arquivos alterados;
- comportamento novo;
- comportamento preservado;
- impacto em banco, API, UI, auth, Docker ou Telegram;
- necessidade de revisores adicionais.

### 4. Validar critérios de sucesso

Use `success-criteria-check` e registre:

- critérios que passaram;
- critérios que falharam;
- critérios não validados;
- evidências;
- limitações.

Não marque como concluído o que não foi validado.

### 5. Validar comandos

Registre comandos executados e resultados.

Exemplos:

```bash
npm run lint
npm test
npm run build
git diff --check
docker compose config
```

Se algum comando não existir ou falhar, registre claramente.

### 6. Smoke test local

Quando aplicável, registre:

- se o sistema foi iniciado;
- comando usado;
- rotas/fluxos testados;
- resultado;
- limitações, como ausência de sessão real ou credenciais locais.

Nunca leia `.env` ou credenciais para forçar smoke test.

### 7. Montar PR

Use este formato:

```md
## Issue relacionada

Closes #<id>

## Resumo

- ...
- ...

## Motivo

Explique por que esta alteração foi feita.

## Agent principal

- `<agent-name>`

## Agents revisores

- `<agent-name>`: motivo
- Não usado: justificativa

## Skills/procedimentos

- `karpathy-code-discipline`
- `minimal-diff-review`
- `success-criteria-check`
- `skill-name`

## Disciplina de implementação

- Suposições relevantes:
- Ambiguidades resolvidas:
- Solução mínima escolhida:
- Fora do escopo preservado:
- Confirmação de diff cirúrgico:

## Arquivos alterados

- `path/to/file`: motivo

## Critérios de sucesso

- [ ] Critério — evidência

## Validações executadas

- `comando` — resultado

## Sistema local

- Iniciado localmente: sim/não
- Comando:
- Smoke test:
- Limitações:

## Fora do escopo

- ...

## Riscos conhecidos

- ...

## Rollback

Explique como reverter com segurança.
```

## Regras

- Use `Closes #<id>` somente se a issue realmente foi resolvida.
- Use `Refs #<id>` quando o PR apenas avança parcialmente a issue.
- Não declare validação que não foi executada.
- Não declare smoke test local se o sistema não foi iniciado.
- Não oculte falhas; registre falhas e impacto.
- Não misture múltiplas issues grandes em um único PR sem justificativa.
- Não oculte mudanças fora do escopo; remova ou documente.

## Saída esperada

Ao finalizar, responda com:

```txt
PR preparado:
Issue vinculada:
Branch:
Agent principal:
Revisores:
Disciplina de implementação:
Minimal Diff Review:
Critérios de sucesso:
Validações:
Sistema local:
Riscos:
Status:
```
