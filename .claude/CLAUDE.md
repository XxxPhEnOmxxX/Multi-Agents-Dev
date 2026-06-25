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

## Regras modulares

As regras detalhadas ficam em `.claude/rules/`.

Use essas regras como fonte operacional complementar ao `CLAUDE.md`:

- `git-workflow.md`: branch, commit, push e Pull Request.
- `wsl-development.md`: execução no WSL local.
- `security.md`: proteção de dados sensíveis e revisão de risco.
- `testing.md`: validações mínimas por stack.
- `backend.md`: padrões para API, banco e backend.
- `frontend.md`: padrões para interface, React e responsividade.
- `documentation.md`: documentação técnica e API.
- `codex-delegation.md`: quando considerar ou evitar Codex.

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
5. atualize a base antes de criar branch de trabalho quando aplicável.

## Fluxo obrigatório para alterações

Para qualquer alteração em código, documentação versionada, configuração ou infraestrutura:

1. Entender a tarefa.
2. Classificar o tipo da tarefa.
3. Escolher e declarar o subagent principal.
4. Declarar as skills/procedimentos aplicáveis.
5. Escolher subagents revisores quando houver risco.
6. Criar plano curto antes de editar.
7. Executar no WSL local.
8. Fazer alterações pequenas e incrementais.
9. Revisar o diff.
10. Rodar validações compatíveis com o projeto.
11. Verificar ausência de secrets e dados sensíveis.
12. Garantir que a alteração está dentro do escopo.
13. Se aprovado, criar commit claro.
14. Fazer push da branch.
15. Abrir Pull Request no GitHub.

## Validação mínima

Antes de criar PR, escolha validações de acordo com a stack do projeto.

Exemplos:

- Node/React: `npm test`, `npm run lint`, `npm run build`.
- Python: `pytest`, `ruff check .`, `mypy .` quando existir.
- Docker: `docker compose config`, build local e healthchecks quando aplicável.
- Documentação: verificar links, comandos, exemplos e coerência com o código real.

Se algum comando não existir, explique que ele não está disponível e use a validação mais próxima.

## Política de GitHub

Nunca faça commit ou push direto em `main`.

Toda alteração aprovada deve seguir este fluxo:

```txt
branch de trabalho -> commit -> push -> Pull Request
```

A Pull Request deve conter:

- resumo do que foi alterado;
- motivo da alteração;
- subagent principal usado;
- skills/procedimentos aplicáveis;
- testes e validações executadas;
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

1. Classificação da tarefa.
2. Subagent principal escolhido.
3. Justificativa do subagent escolhido.
4. Subagents auxiliares, se houver.
5. Skills/procedimentos aplicáveis.
6. Plano de execução no WSL.
7. Critérios de validação.
8. Decisão sobre Codex.
9. Estratégia de branch e PR.
10. Próximo passo operacional.
