# Mapeamento de agents e skills

## Regra central de orquestração

O Claude principal é o orquestrador soberano do fluxo de desenvolvimento.

Os agents especializados executam, analisam ou revisam dentro de seus papéis, mas não decidem sozinhos quando usar o Codex.

A skill `delegate-to-codex` deve ser pré-carregada somente no agent `development-orchestrator`.

## Regra para `delegate-to-codex`

Somente o `development-orchestrator` pode decidir usar `delegate-to-codex`.

Agents especializados podem recomendar uma consulta ao Codex, mas devem justificar:

- qual risco existe;
- qual pergunta seria feita;
- quais arquivos ou diffs precisam ser analisados;
- qual resultado esperado;
- por que uma segunda opinião independente é útil.

Não usar Codex para documentação simples, testes comuns, pequenas alterações de código, ajustes de texto, renomeações simples, refatorações triviais ou tarefas que um agent resolve com segurança.

Usar Codex apenas quando houver ganho real de segunda opinião independente, como diff arriscado, mudança crítica, bug difícil, falha de teste não óbvia, refatoração grande ou decisão técnica de alto impacto.

## development-orchestrator
- orchestrator-codex-gate
- delegate-to-codex

## backend-specialist
- api-design
- database-design
- backend-architecture
- security-audit
- test-strategy

## frontend-specialist
- frontend-ui-review
- react-optimization
- responsive-design
- accessibility-review
- test-strategy

## devops-engineer
- devops-ci-cd
- docker-infrastructure
- cloud-architecture
- observability-review

Uso de Codex: não pré-carregar. Pode sugerir ao orquestrador quando houver risco técnico real.

## security-engineer
- security-audit
- threat-modeling
- compliance-review
- secure-code-review
- dependency-audit

Uso de Codex: não pré-carregar. Pode sugerir ao orquestrador quando uma revisão independente reduzir risco.

## corporate-cto
- architecture-review
- technical-roadmap
- risk-analysis
- build-vs-buy
- engineering-strategy

Uso de Codex: não pré-carregar.

## engineering-manager
- engineering-planning
- performance-review
- delivery-risk-review
- team-process-review

Uso de Codex: não pré-carregar.

## software-architect
- system-design
- architecture-review
- design-pattern-review
- integration-design
- scalability-review

Uso de Codex: não pré-carregar. Pode sugerir ao orquestrador para decisões arquiteturais complexas.

## qa-engineer
- test-strategy
- test-automation
- regression-plan
- acceptance-criteria-review

Uso de Codex: não pré-carregar. Pode sugerir ao orquestrador para falhas de teste difíceis ou regressões não óbvias.

## product-owner
- requirements-analysis
- user-story-writing
- acceptance-criteria-review
- stakeholder-communication

Uso de Codex: não pré-carregar.

## project-manager
- project-planning
- timeline-risk-review
- resource-planning
- status-reporting

Uso de Codex: não pré-carregar.

## senior-fullstack-developer
- fullstack-feature-delivery
- api-design
- frontend-ui-review
- database-design
- test-automation

Uso de Codex: não pré-carregar. Pode sugerir ao orquestrador para feature fullstack complexa, refatoração grande ou bug difícil.

## technical-writer
- technical-documentation
- api-documentation
- knowledge-base
- release-notes

Uso de Codex: não pré-carregar. Pode sugerir ao orquestrador apenas para validar documentação técnica complexa contra o código real.
