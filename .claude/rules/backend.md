# Backend Rules

## Responsabilidade

Use `backend-specialist` para tarefas de API, banco de dados, services, autenticação, validação e arquitetura de servidor.

## Padrões esperados

- Separar controller, service, repository/model quando o projeto usar esse padrão.
- Validar entrada antes de regra de negócio.
- Retornar erros consistentes.
- Evitar vazamento de detalhes internos em resposta HTTP.
- Usar transações quando houver múltiplas escritas dependentes.
- Não criar migration destrutiva sem plano e rollback.

## Antes de finalizar

Verifique:

- contrato da API;
- status HTTP;
- autenticação/autorização;
- logs;
- testes;
- impacto em banco.
