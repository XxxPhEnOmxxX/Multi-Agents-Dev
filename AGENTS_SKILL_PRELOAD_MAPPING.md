# Mapeamento de agents e skills

## Regra para `delegate-to-codex`

A skill `delegate-to-codex` deve ser pré-carregada nos agents que se beneficiam de uma segunda análise independente do Codex em tarefas de código, diff, bug, teste, arquitetura ou segurança.

Ela não deve ser pré-carregada em agents de gestão/produto, porque esses papéis trabalham mais com escopo, prioridade, comunicação e coordenação. Neles, a skill pode ser chamada manualmente apenas quando houver uma necessidade técnica concreta.

## backend-specialist
- api-design
- database-design
- backend-architecture
- security-audit
- test-strategy
- delegate-to-codex

## frontend-specialist
- frontend-ui-review
- react-optimization
- responsive-design
- accessibility-review
- test-strategy
- delegate-to-codex

## devops-engineer
- devops-ci-cd
- docker-infrastructure
- cloud-architecture
- observability-review

Uso recomendado de `delegate-to-codex`: sob demanda, para revisão cruzada de pipeline, Dockerfile, compose, infraestrutura como código ou mudança de deploy com risco real.

## security-engineer
- security-audit
- threat-modeling
- compliance-review
- secure-code-review
- dependency-audit
- delegate-to-codex

## corporate-cto
- architecture-review
- technical-roadmap
- risk-analysis
- build-vs-buy
- engineering-strategy

Uso recomendado de `delegate-to-codex`: não pré-carregar. Chamar manualmente apenas quando uma decisão estratégica depender de validação técnica em código ou arquitetura concreta.

## engineering-manager
- engineering-planning
- performance-review
- delivery-risk-review
- team-process-review

Uso recomendado de `delegate-to-codex`: não pré-carregar. Chamar manualmente apenas para avaliar risco técnico de uma entrega específica.

## software-architect
- system-design
- architecture-review
- design-pattern-review
- integration-design
- scalability-review
- delegate-to-codex

## qa-engineer
- test-strategy
- test-automation
- regression-plan
- acceptance-criteria-review
- delegate-to-codex

## product-owner
- requirements-analysis
- user-story-writing
- acceptance-criteria-review
- stakeholder-communication

Uso recomendado de `delegate-to-codex`: não pré-carregar. Chamar manualmente apenas quando o requisito depender de investigação técnica no código.

## project-manager
- project-planning
- timeline-risk-review
- resource-planning
- status-reporting

Uso recomendado de `delegate-to-codex`: não pré-carregar. Chamar manualmente apenas quando houver bloqueio técnico que precise de análise independente.

## senior-fullstack-developer
- fullstack-feature-delivery
- api-design
- frontend-ui-review
- database-design
- test-automation
- delegate-to-codex

## technical-writer
- technical-documentation
- api-documentation
- knowledge-base
- release-notes

Uso recomendado de `delegate-to-codex`: sob demanda, para revisar documentação técnica contra o código real ou validar exemplos de API.
