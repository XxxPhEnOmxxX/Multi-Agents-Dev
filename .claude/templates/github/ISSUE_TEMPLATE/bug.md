# Bug Issue

## Problema

Descreva o bug observado.

## Comportamento atual

Explique o que está acontecendo hoje.

## Comportamento esperado

Explique o resultado correto esperado.

## Como reproduzir

1. ...
2. ...
3. ...

## Evidências

- Logs:
- Prints:
- Erros:
- PRs/commits relacionados:

## Escopo permitido

- [ ] Corrigir o bug descrito.
- [ ] Adicionar teste de regressão, quando aplicável.
- [ ] Preservar comportamento existente fora do bug.

## Fora do escopo

- Não implementar feature nova.
- Não refatorar módulos não relacionados.
- Não alterar contrato público sem autorização.

## Suposições conhecidas

- 
- 

## Ambiguidades ou decisões pendentes

- [ ] Não há ambiguidade relevante.
- [ ] Existem decisões pendentes:

Detalhes:

```txt
Liste qualquer dúvida que possa mudar regra de negócio, arquitetura, segurança, contrato público ou banco.
```

## Correção esperada

Descreva a menor correção aceitável para resolver o bug.

Evite incluir melhoria futura, redesign ou refatoração ampla junto com a correção.

## Agent principal sugerido

`<agent-name>`

Sugestões:

- `backend-specialist` para API, banco, services e regras de negócio.
- `frontend-specialist` para UI, React, painel e responsividade.
- `security-engineer` para auth, permissão, dados sensíveis ou vulnerabilidade.
- `devops-engineer` para Docker, proxy, deploy ou CI/CD.
- `qa-engineer` para falha de teste, regressão ou cobertura.

## Revisores esperados

- [ ] `qa-engineer`
- [ ] `security-engineer`, se tocar auth, permissões, dados sensíveis ou vulnerabilidade
- [ ] `software-architect`, se a correção exigir mudança estrutural

## Skills/procedimentos sugeridos

- `karpathy-code-discipline`
- `minimal-diff-review`
- `success-criteria-check`
- `test-strategy`
- `regression-plan`
- `secure-code-review`, se aplicável
- `issue-to-feature-flow`
- `pr-from-issue`

## Critérios de aceite verificáveis

- [ ] Bug corrigido.
- [ ] Cenário de reprodução validado.
- [ ] Teste de regressão criado ou justificativa registrada.
- [ ] Comportamento fora do bug foi preservado.
- [ ] O diff é pequeno e diretamente relacionado à issue.
- [ ] Validações obrigatórias executadas.
- [ ] PR vincula esta issue com `Closes #<id>`.

## Validações obrigatórias

Marque o que se aplica:

- [ ] `npm run lint`
- [ ] `npm test`
- [ ] `npm run build`
- [ ] `git diff --check`
- [ ] smoke test local

## Riscos

- Risco técnico:
- Risco de regressão:
- Risco operacional:

## Observações

Adicione qualquer detalhe importante para o agente que executará a correção.
