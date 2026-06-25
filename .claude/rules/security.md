# Security Rules

## Regra central

Segurança tem prioridade sobre velocidade.

Nunca versionar ou expor:

- `.env`;
- tokens;
- senhas;
- chaves privadas;
- certificados privados;
- dados reais de clientes;
- dumps de banco;
- logs sensíveis;
- credenciais de produção.

## Antes de commit ou PR

Verifique:

```bash
git diff --stat
git diff --cached --stat
git status
```

Procure alterações fora de escopo e arquivos sensíveis.

## Autenticação e autorização

Mudanças em autenticação, sessão, autorização, permissões, dados sensíveis ou infraestrutura devem receber revisão de segurança.

Use `security-engineer` como revisor quando a tarefa tocar nessas áreas.

## Codex

Codex só deve ser usado por decisão do Claude principal, depois da skill `orchestrator-codex-gate`.

Não usar Codex para tarefa simples. Usar apenas quando uma segunda opinião técnica reduzir risco real.
