# Codex Delegation Rules

## Regra central

O Codex é uma segunda opinião técnica controlada pelo Claude principal.

Subagents não devem decidir sozinhos quando usar Codex.

## Quando não usar

Não use Codex para:

- documentação simples;
- testes comuns;
- pequenas alterações;
- ajustes de texto;
- renomeações simples;
- formatação;
- tarefas sem risco relevante.

## Quando considerar

Considere Codex quando houver:

- diff arriscado;
- bug difícil;
- falha de teste não óbvia;
- refatoração grande;
- decisão técnica de alto impacto;
- alteração sensível em autenticação, autorização, dados ou infraestrutura.

## Procedimento

Antes de chamar `delegate-to-codex`, use `orchestrator-codex-gate`.

O prompt enviado ao Codex deve ser autocontido e incluir:

- objetivo;
- contexto;
- arquivos ou diff relevante;
- pergunta específica;
- formato esperado da resposta.

Use `read-only` por padrão. Use `workspace-write` somente quando a tarefa exigir alteração real em arquivos.
