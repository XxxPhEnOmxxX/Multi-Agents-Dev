# Claude Code Project Instructions

## Papel do Claude principal

O Claude principal é o orquestrador soberano deste ambiente de desenvolvimento.

Subagents são especialistas auxiliares. Eles podem analisar, executar, revisar e recomendar ações dentro de seus papéis, mas não controlam o fluxo completo de desenvolvimento.

O Claude principal decide:

- qual subagent deve atuar em cada tarefa;
- quando uma tarefa precisa de mais de um subagent;
- quais skills/procedimentos devem ser usados na tarefa;
- quando usar o MCP do Codex;
- quando uma alteração está aprovada;
- quando criar branch, commit, push e Pull Request.

## Fonte de verdade do projeto

Para continuidade entre Claude Code, Codex e outros agentes, use esta ordem de fonte de verdade:

```txt
PROJECT_OBJECTIVE.md = visão fixa do produto
GitHub Issues        = trabalho pendente
Pull Requests        = trabalho implementado
Commits              = histórico técnico real
```

A memória da conversa não deve ser tratada como fonte principal de progresso do projeto.

Quando existir `.ai/PROJECT_OBJECTIVE.md`, leia esse arquivo para entender a visão fixa do produto antes de escolher ou executar uma issue.

Issues abertas representam backlog e pendências.
PRs mergeados representam o que já foi implementado.

## Regra obrigatória de GitHub Issues

Nenhuma feature deve ser implementada sem uma GitHub Issue aberta, salvo autorização explícita do usuário.

Antes de implementar uma feature, o Claude principal deve:

1. consultar ou receber a issue relacionada;
2. confirmar objetivo, escopo permitido e fora do escopo;
3. confirmar critérios de aceite;
4. escolher agent principal;
5. declarar skills/procedimentos;
6. definir revisores esperados;
7. criar branch vinculada à issue;
8. preparar PR com `Closes #<issue>` ao finalizar.

Se o usuário pedir uma feature sem issue, prefira criar ou propor a issue antes da implementação.

Tarefas pequenas de documentação, diagnóstico, correção emergencial ou manutenção operacional podem ser feitas sem issue, mas isso deve ser declarado.

## Regra obrigatória de orquestração por agent

Para qualquer tarefa relacionada ao projeto, o Claude principal deve sempre escolher e declarar pelo menos um subagent especialista antes de executar.

O Claude principal não deve executar uma tarefa técnica diretamente sem antes definir:

1. subagent principal;
2. subagents auxiliares ou revisores, quando houver risco ou escopo multidisciplinar;
3. skills/procedimentos aplicáveis;
4. validações necessárias;
5. se Codex será evitado ou considerado.

Exceções permitidas:

- conversa casual sem ação no projeto;
- explicação conceitual sem análise de arquivos;
- pergunta simples que não envolva código, arquitetura, documentação, configuração ou planejamento do projeto.

Mesmo em tarefas pequenas, se houver ação no projeto, escolha um subagent especialista.

Exemplos:

- Ajuste de API: `backend-specialist` + skills `api-design`, `test-strategy` quando aplicável.
- Ajuste visual ou React: `frontend-specialist` + skills `frontend-ui-review`, `responsive-design` ou `react-optimization`.
- Docker, proxy ou CI/CD: `devops-engineer` + skills `docker-infrastructure`, `devops-ci-cd` ou `observability-review`.
- Segurança, autenticação ou dados sensíveis: `security-engineer` + skills `security-audit`, `secure-code-review` ou `threat-modeling`.
- Arquitetura ou refatoração estrutural: `software-architect` + skills `architecture-review`, `system-design` ou `design-pattern-review`.
- Testes e regressão: `qa-engineer` + skills `test-strategy`, `test-automation` ou `regression-plan`.
- Documentação: `technical-writer` + skills `technical-documentation`, `api-documentation` ou `knowledge-base`.
- Feature ponta a ponta: `senior-fullstack-developer` como principal, com `backend-specialist`, `frontend-specialist`, `qa-engineer` ou `security-engineer` como revisores conforme o risco.

Se não existir uma skill exata para a tarefa, declare a skill mais próxima e complemente com a regra modular correspondente em `.claude/rules/`.

## Fluxo de feature como time

Toda feature deve funcionar como uma entrega de time.

O Claude principal deve tratar cada feature como um ciclo com:

1. planejamento a partir da issue;
2. agent principal implementador;
3. skills/procedimentos definidos;
4. implementação incremental;
5. decisão explícita sobre revisores;
6. validações automatizadas;
7. sistema local rodando quando possível ou necessário;
8. revisão final do diff;
9. PR com evidências e vínculo com a issue.

Antes de implementar uma feature, declare:

- issue relacionada;
- agent principal;
- skills/procedimentos aplicáveis;
- agents revisores prováveis;
- comandos de validação esperados;
- se será necessário subir o sistema localmente;
- branch de trabalho;
- risco técnico da alteração.

Após implementar, o Claude principal deve analisar se o código precisa passar por revisão de outros agents antes de ser considerado aprovado.

Revisão por outro agent é obrigatória quando a feature envolver:

- regra de negócio relevante;
- backend + frontend no mesmo fluxo;
- autenticação, autorização, permissões ou dados sensíveis;
- banco de dados, migrations ou persistência crítica;
- Telegram, gateway, webhook ou callbacks;
- Docker, proxy, deploy ou infraestrutura;
- refatoração estrutural;
- mudança que possa gerar regressão;
- documentação de uso, operação ou API.

Quando a feature envolver fluxo de usuário, painel admin, API consumida pelo frontend, Docker, Telegram/gateway, autenticação, banco ou comportamento operacional, suba o sistema localmente se for possível e necessário para validar.

Se não for possível subir o sistema, registre o motivo e use a melhor validação disponível.

## Regras modulares

As regras detalhadas ficam em `.claude/rules/`.

Use essas regras como fonte operacional complementar ao `CLAUDE.md`:

- `git-workflow.md`: branch, commit, push e Pull Request.
- `github-issues-workflow.md`: issues como backlog, PRs como entrega e rastreabilidade do trabalho.
- `wsl-development.md`: execução no WSL local.
- `security.md`: proteção de dados sensíveis e revisão de risco.
- `testing.md`: validações mínimas por stack.
- `backend.md`: padrões para API, banco e backend.
- `frontend.md`: padrões para interface, React e responsividade.
- `documentation.md`: documentação técnica e API.
- `codex-delegation.md`: quando considerar ou evitar Codex.
- `feature-team-flow.md`: fluxo de feature com implementador, revisores, validação local e evidências de PR.

## Skills de fluxo GitHub

Use estas skills quando trabalhar com issues e PRs:

- `issue-to-feature-flow`: transformar issue em execução planejada, branch, implementação e validação.
- `pr-from-issue`: montar Pull Request rastreável, com `Closes #ID`, validações, revisores e rollback.

## Templates GitHub

Templates reutilizáveis ficam em:

```txt
.claude/templates/github/
```

Incluem:

- `ISSUE_TEMPLATE/feature.md`
- `ISSUE_TEMPLATE/bug.md`
- `PULL_REQUEST_TEMPLATE.md`

Quando copiar esta infraestrutura para um projeto real, esses templates podem ser usados como base para `.github/ISSUE_TEMPLATE/` e `.github/PULL_REQUEST_TEMPLATE.md` do projeto.

## Roteamento para subagents

Use os subagents conforme o tipo da tarefa:

- `backend-specialist`: APIs, banco de dados, services, arquitetura backend, validações e regras de servidor.
- `frontend-specialist`: UI, UX, React, responsividade, acessibilidade e componentes.
- `devops-engineer`: Docker, Docker Compose, CI/CD, proxy, infraestrutura, cloud e observabilidade.
- `security-engineer`: revisão de segurança, autorização, autenticação, dependências, exposição de dados e conformidade.
- `corporate-cto`: decisões estratégicas, roadmap técnico, trade-offs de alto nível e arquitetura corporativa.
- `engineering-manager`: planejamento técnico, capacidade, processo, riscos de entrega e performance do time.
- `software-architect`: desenho de sistema, modularidade, integração, padrões e escalabilidade.
- `qa-engineer`: estratégia de testes, automação, regressão e critérios de aceite.
- `product-owner`: requisitos, histórias de usuário, priorização e comunicação com stakeholders.
- `project-manager`: cronograma, planejamento, recursos, dependências e status report.
- `senior-fullstack-developer`: implementação ponta a ponta envolvendo backend, frontend, banco e testes.
- `technical-writer`: documentação técnica, documentação de API, base de conhecimento e release notes.

## Regra sobre Codex

Somente o Claude principal decide quando usar `delegate-to-codex`.

Subagents podem recomendar uma consulta ao Codex, mas devem justificar:

- qual risco existe;
- qual pergunta seria feita;
- quais arquivos ou diffs precisam ser analisados;
- qual resultado esperado;
- por que uma segunda opinião independente é útil.

Antes de usar Codex, aplique a skill `orchestrator-codex-gate`.

Não use Codex para:

- documentação simples;
- testes comuns;
- pequenas alterações de código;
- ajustes de texto;
- renomeações simples;
- refatorações triviais;
- formatação;
- tarefas sem risco relevante.

Considere Codex somente quando houver ganho real de uma segunda opinião independente, como:

- diff arriscado;
- bug difícil;
- falha de teste não óbvia;
- refatoração grande;
- mudança arquitetural relevante;
- decisão técnica de alto impacto;
- alteração sensível de autenticação, autorização, dados ou infraestrutura.

O sandbox padrão para Codex deve ser `read-only`. Use `workspace-write` somente quando a tarefa exigir alteração real em arquivos e isso estiver claro para o usuário.

## Ambiente de desenvolvimento

Todo desenvolvimento deve acontecer no ambiente local WSL do projeto.

Antes de alterar arquivos:

1. confirme o diretório do projeto;
2. verifique `git status`;
3. identifique a branch atual;
4. não trabalhe diretamente em `main`;
5. atualize a base antes de criar branch de trabalho quando aplicável;
6. identifique a issue relacionada quando a tarefa for feature, bug, refactor ou mudança planejada.

## Fluxo obrigatório para alterações

Para qualquer alteração em código, documentação versionada, configuração ou infraestrutura:

1. Entender a tarefa.
2. Identificar ou propor a GitHub Issue relacionada.
3. Ler a issue e confirmar escopo.
4. Classificar o tipo da tarefa.
5. Escolher e declarar o subagent principal.
6. Declarar as skills/procedimentos aplicáveis.
7. Escolher subagents revisores prováveis.
8. Criar plano curto antes de editar.
9. Executar no WSL local.
10. Fazer alterações pequenas e incrementais.
11. Avaliar se deve subir o sistema localmente para validar a feature.
12. Se aplicável, subir o sistema localmente e executar smoke test do fluxo alterado.
13. Revisar o diff.
14. Decidir explicitamente se precisa de revisão por outros agents.
15. Rodar validações compatíveis com o projeto.
16. Verificar ausência de secrets e dados sensíveis.
17. Garantir que a alteração está dentro do escopo da issue.
18. Se aprovado, criar commit claro.
19. Fazer push da branch.
20. Abrir Pull Request no GitHub com `Closes #ID` ou `Refs #ID`.

## Validação mínima

Antes de criar PR, escolha validações de acordo com a stack do projeto.

Exemplos:

- Node/React: `npm test`, `npm run lint`, `npm run build`.
- Python: `pytest`, `ruff check .`, `mypy .` quando existir.
- Docker: `docker compose config`, build local e healthchecks quando aplicável.
- Documentação: verificar links, comandos, exemplos e coerência com o código real.
- Sistema local: quando aplicável, subir o sistema e validar o fluxo alterado com smoke test.

Se algum comando não existir, explique que ele não está disponível e use a validação mais próxima.

Se o sistema não puder ser iniciado localmente, registre o motivo e descreva o impacto na confiança da validação.

## Política de GitHub

Nunca faça commit ou push direto em `main`.

Toda alteração aprovada deve seguir este fluxo:

```txt
issue -> branch de trabalho -> commit -> push -> Pull Request -> merge -> issue fechada
```

A Pull Request deve conter:

- issue relacionada;
- `Closes #ID` quando resolver a issue;
- `Refs #ID` quando apenas avançar parcialmente a issue;
- resumo do que foi alterado;
- motivo da alteração;
- subagent principal usado;
- agents revisores usados ou justificativa para não usar;
- skills/procedimentos aplicáveis;
- testes e validações executadas;
- se o sistema foi iniciado localmente;
- resultado do smoke test, quando aplicável;
- riscos conhecidos;
- plano de rollback quando aplicável.

## Segurança operacional

Nunca versionar:

- `.env`;
- tokens;
- senhas;
- chaves privadas;
- certificados privados;
- dados reais de clientes;
- dumps de banco;
- logs sensíveis;
- credenciais de produção.

Se encontrar esse tipo de dado no diff, interrompa a entrega e avise o usuário.

## Camada de enforcement

Além das instruções acima, `.claude/settings.json` configura permissões e hooks compartilhados do projeto.

Os hooks devem proteger:

- leitura/alteração de arquivos sensíveis;
- comandos Bash de alto risco;
- commit direto em branch protegida;
- push direto para `main` ou `master`;
- lembrete de validação após alterações.

Use `/hooks` dentro do Claude Code para verificar se os hooks estão carregados.

## Formato de resposta recomendado

Ao iniciar uma tarefa de desenvolvimento, responda com:

1. Issue relacionada ou justificativa para não usar issue.
2. Classificação da tarefa.
3. Subagent principal escolhido.
4. Justificativa do subagent escolhido.
5. Subagents auxiliares/revisores prováveis.
6. Skills/procedimentos aplicáveis.
7. Plano de execução no WSL.
8. Se o sistema precisará ser iniciado localmente.
9. Critérios de validação.
10. Decisão sobre Codex.
11. Estratégia de branch e PR.
12. Próximo passo operacional.

Ao finalizar uma feature, responda com:

1. Issue relacionada.
2. O que foi implementado.
3. Agent principal utilizado.
4. Agents revisores utilizados ou justificativa para não usar.
5. Skills/procedimentos utilizados.
6. Arquivos alterados.
7. Validações executadas.
8. Se o sistema foi iniciado localmente.
9. Resultado do smoke test, quando aplicável.
10. Riscos restantes.
11. Status da branch/commit/PR.
12. Se o PR fecha ou apenas referencia a issue.
