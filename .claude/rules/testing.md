# Testing Rules

## Regra central

Toda alteração deve ter validação proporcional ao risco.

## Escolha de validação

Use comandos existentes no projeto.

Node/React:

```bash
npm test
npm run lint
npm run build
```

Python:

```bash
pytest
ruff check .
mypy .
```

Docker:

```bash
docker compose config
```

## Quando comandos não existirem

Se um comando não existir, não invente sucesso.

Informe:

```txt
O comando não existe neste projeto. Usei a validação mais próxima: ...
```

## Antes da PR

A PR deve informar:

- quais validações foram executadas;
- quais falharam;
- quais não existem no projeto;
- qual risco permanece.
