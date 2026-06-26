# Feature Team Flow

## Regra central

Toda feature deve ser tratada como entrega de time, não como alteração isolada.

O Claude principal continua sendo o orquestrador, mas deve conduzir a feature com papéis claros:

- agent principal implementador;
- agents revisores quando necessário;
- disciplina de código antes de editar;
- validações automatizadas;
- validação local com o sistema rodando quando possível ou necessário;
- Pull Request com evidências.

## Antes de implementar

Antes de editar arquivos, o Claude principal deve declarar:

1. feature ou task;
2. issue relacionada, quando aplicável;
3. branch pretendida;
4. agent principal;
5. skills/procedimentos aplicáveis;
6. agents revisores prováveis;
7. suposições e ambiguidades relevantes;
8. solução mais simples aceitável;
9. validações mínimas;
10. se será necessário subir o sistema localmente;
11. risco técnico da alteração.

A skill `karpathy-code-discipline` deve ser aplicada antes de qualquer alteração técnica relevante.

## Disciplina de implementação

Durante a execução:

- resolva somente a issue;
- prefira a solução mais simples;
- evite abstrações prematuras;
- não faça drive-by refactor;
- não misture feature com limpeza ampla;
- preserve contratos e comportamento fora do escopo;
- mantenha o diff pequeno e revisável.

Se encontrar melhoria fora do escopo, registre como nova issue em vez de implementar junto.

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

## Minimal Diff Review

Antes de considerar a feature pronta, execute revisão de diff mínimo.

Use a skill `minimal-diff-review` para confirmar:

- cada arquivo alterado tem relação direta com a issue;
- não houve refatoração fora do escopo;
- não houve formatação massiva sem necessidade;
- não foram criadas abstrações especulativas;
- contratos públicos foram preservados, salvo quando a issue exigir mudança;
- o PR continua pequeno o suficiente para revisão segura.

Se o diff estiver grande demais, recomende dividir em nova issue/PR.

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

Use a skill `success-criteria-check` para confirmar que os critérios de aceite foram verificados.

## Evidências para PR

A PR deve conter:

- agent principal usado;
- agents revisores usados ou justificativa para não usar;
- skills/procedimentos aplicáveis;
- suposições relevantes;
- confirmação de solução mínima;
- confirmação de diff cirúrgico;
- comandos executados;
- resultado das validações;
- se o sistema foi iniciado localmente;
- evidências de smoke test, quando aplicável;
- riscos conhecidos;
- plano de rollback quando aplicável.
