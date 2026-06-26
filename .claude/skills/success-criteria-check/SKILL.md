# Skill: Success Criteria Check

## Objetivo

Garantir que uma issue, feature, bugfix ou refatoração tenha critérios de sucesso claros e verificáveis antes da implementação e antes do PR.

Use esta skill para transformar tarefas vagas em entregas objetivas.

## Quando usar

Use obrigatoriamente quando:

- a issue tiver critérios de aceite vagos;
- a task envolver regra de negócio;
- a mudança afetar usuário final;
- a mudança envolver backend, frontend, banco, auth, Telegram/gateway ou infraestrutura;
- a entrega precisar de validação local ou teste.

## Procedimento antes de implementar

### 1. Extrair critérios da issue

Leia a issue e extraia critérios no formato checklist:

```txt
- [ ] Critério 1 verificável
- [ ] Critério 2 verificável
- [ ] Critério 3 verificável
```

Critério bom é algo que pode ser testado, observado ou validado.

### 2. Reescrever critérios vagos

Critérios vagos:

```txt
Melhorar tela.
Arrumar login.
Deixar mais seguro.
Otimizar código.
```

Critérios verificáveis:

```txt
A página `/admin/login` não deve ter overflow horizontal em 390px.
Após 5 senhas incorretas, o usuário admin deve ficar bloqueado por 15 minutos.
`npm run build` deve passar sem erro TypeScript.
A rota deve continuar retornando o mesmo contrato JSON.
```

### 3. Definir validações

Associe cada critério a uma validação:

```txt
Critério:
Validação:
Comando ou smoke test:
Evidência esperada:
```

### 4. Identificar critérios não verificáveis

Se um critério não puder ser validado agora, registre:

- motivo;
- limitação;
- risco;
- validação alternativa.

## Procedimento antes de PR

Antes de abrir PR, confirme cada critério:

```txt
Critério:
Status: passou / falhou / não validado
Evidência:
Limitação:
```

Não marque como concluído o que não foi validado.

## Validações comuns

Use conforme a stack:

```bash
npm run lint
npm test
npm run build
git diff --check
docker compose config
pytest
ruff check .
mypy .
```

Smoke tests comuns:

- rota responde com status esperado;
- página abre sem erro;
- fluxo principal funciona;
- formulário preserva validações;
- API mantém contrato;
- sem overflow horizontal em viewport móvel;
- redirecionamento/autorização preservado.

## Saída esperada antes de implementar

```txt
Critérios de sucesso:
- [ ] ...
- [ ] ...
Validações planejadas:
- ...
Critérios não verificáveis agora:
- ...
```

## Saída esperada antes de PR

```txt
Success Criteria Check:
- Critério 1: passou/falhou/não validado — evidência
- Critério 2: passou/falhou/não validado — evidência
- Limitações:
- Riscos:
```
