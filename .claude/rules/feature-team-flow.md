# Feature Team Flow

## Regra central

Toda feature deve ser tratada como entrega de time, não como alteração isolada.

O Claude principal continua sendo o orquestrador, mas deve conduzir a feature com papéis claros:

- agent principal implementador;
- agents revisores quando necessário;
- validações automatizadas;
- validação local com o sistema rodando quando possível ou necessário;
- Pull Request com evidências.

## Antes de implementar

Antes de editar arquivos, o Claude principal deve declarar:

1. feature ou task;
2. branch pretendida;
3. agent principal;
4. skills/procedimentos aplicáveis;
5. agents revisores prováveis;
6. validações mínimas;
7. se será necessário subir o sistema localmente;
8. risco técnico da alteração.

## Critério para subir o sistema localmente

Suba o sistema localmente quando a feature envolver:

- fluxo de usuário;
- frontend ou painel admin;
- API consumida pelo frontend;
- integração com Telegram/gateway;
- autenticação ou autorização;
- Docker ou infraestrutura local;
- alteração de banco ou migration;
- comportamento que não pode ser validado apenas por teste estático.

Se não for possível subir o sistema, registre o motivo e use a melhor validação disponível.

## Revisão por agents

Após implementar, o Claude principal deve decidir se o código precisa de revisão por outros agents.

Use revisão obrigatória quando houver:

- backend com regra de negócio relevante: `backend-specialist`;
- UI, React ou painel admin: `frontend-specialist`;
- autenticação, autorização, dados sensíveis ou tokens: `security-engineer`;
- refatoração estrutural ou arquitetura: `software-architect`;
- testes, regressão ou cobertura: `qa-engineer`;
- documentação, README, API docs ou instruções: `technical-writer`;
- Docker, CI/CD, proxy, deploy ou observabilidade: `devops-engineer`.

Uma feature fullstack normalmente deve ter pelo menos:

- `senior-fullstack-developer` como implementador;
- `backend-specialist` para backend;
- `frontend-specialist` para frontend;
- `qa-engineer` para validação;
- `security-engineer` quando tocar dados sensíveis, autenticação ou permissões.

## Validação mínima da feature

Antes de PR, execute o que existir no projeto:

- testes;
- lint;
- build;
- typecheck;
- validação Docker;
- smoke test local;
- teste manual do fluxo quando o sistema subir.

Exemplos:

```bash
npm test
npm run lint
npm run build
docker compose config
docker compose up -d
```

Não invente sucesso. Se algo não existir ou falhar, registre claramente.

## Evidências para PR

A PR deve conter:

- agent principal usado;
- agents revisores usados ou justificativa para não usar;
- skills/procedimentos aplicáveis;
- comandos executados;
- resultado das validações;
- se o sistema foi iniciado localmente;
- evidências de smoke test, quando aplicável;
- riscos conhecidos;
- plano de rollback quando aplicável.
