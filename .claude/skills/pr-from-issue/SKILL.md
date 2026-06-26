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

### 2. Revisar diff

Revise o diff e confirme:

- arquivos alterados;
- comportamento novo;
- comportamento preservado;
- impacto em banco, API, UI, auth, Docker ou Telegram;
- necessidade de revisores adicionais.

### 3. Validar

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

### 4. Smoke test local

Quando aplicável, registre:

- se o sistema foi iniciado;
- comando usado;
- rotas/fluxos testados;
- resultado;
- limitações, como ausência de sessão real ou credenciais locais.

Nunca leia `.env` ou credenciais para forçar smoke test.

### 5. Montar PR

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

- `skill-name`
- `rule-name`

## Arquivos alterados

- `path/to/file`: motivo

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

## Saída esperada

Ao finalizar, responda com:

```txt
PR preparado:
Issue vinculada:
Branch:
Agent principal:
Revisores:
Validações:
Sistema local:
Riscos:
Status:
```
