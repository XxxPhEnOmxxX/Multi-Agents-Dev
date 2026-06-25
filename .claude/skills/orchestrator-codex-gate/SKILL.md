---
name: orchestrator-codex-gate
description: Decide se uma tarefa justifica delegação ao Codex via MCP. Esta skill deve ser usada somente pelo orquestrador principal para controlar quando usar ou não `delegate-to-codex`.
argument-hint: [descrição da tarefa, diff, risco ou dúvida técnica]
allowed-tools: Read, Glob, Grep, Bash
---

# Orchestrator Codex Gate

Tarefa a avaliar:

$ARGUMENTS

## Objetivo

Decidir se a tarefa deve ser delegada ao Codex ou se deve ser resolvida diretamente pelo Claude/orquestrador e agents especializados.

O Codex é uma segunda perspectiva técnica, não um executor padrão para qualquer tarefa.

## Regra central

Somente o orquestrador principal pode decidir usar `delegate-to-codex`.

Agents especializados podem recomendar a consulta, mas a decisão final é do orquestrador.

## Não delegar ao Codex

Não use Codex para:

- documentação simples;
- criação ou ajuste comum de README;
- testes comuns de unidade ou integração simples;
- pequenas alterações de código;
- mudança de texto, label, botão ou estilo simples;
- renomeação trivial;
- correção óbvia de lint;
- formatação;
- tarefas já bem compreendidas;
- tarefas sem risco relevante;
- qualquer chamada apenas por curiosidade.

Motivo: usar Codex sem necessidade aumenta custo, latência e ruído operacional.

## Considerar delegar ao Codex

Considere usar Codex quando houver ganho real de uma segunda leitura independente:

- diff arriscado antes de PR;
- autenticação, autorização ou sessão;
- segurança, criptografia, permissões ou exposição de dados;
- bug difícil ou intermitente;
- falha de teste não óbvia;
- refatoração grande;
- mudança arquitetural com impacto alto;
- migração de banco sensível;
- integração crítica entre serviços;
- suspeita de regressão difícil de avaliar;
- decisão técnica onde errar custa caro.

## Checklist de decisão

Antes de aprovar uso do Codex, responda:

1. Qual é o risco real da tarefa?
2. O Claude ou um agent especializado consegue resolver com segurança?
3. O Codex terá contexto suficiente para responder bem?
4. O prompt enviado será autocontido?
5. O sandbox deve ser `read-only` ou `workspace-write`?
6. A tarefa exige apenas opinião ou alteração real em arquivos?
7. O usuário foi informado antes da delegação?

## Política de sandbox

Use por padrão:

```txt
read-only
```

Use `workspace-write` somente quando a tarefa exigir que o Codex edite arquivos e isso tiver sido informado ao usuário.

Não use `danger-full-access` sem pedido explícito e justificativa forte.

## Resultado esperado

Responda com uma decisão clara:

```txt
Decisão: NÃO DELEGAR AO CODEX
Motivo: ...
Agent recomendado: ...
Validação necessária: ...
```

ou:

```txt
Decisão: DELEGAR AO CODEX
Motivo: ...
Prompt autocontido a enviar: ...
Sandbox recomendado: read-only | workspace-write
Timeout recomendado: ...
Como interpretar o resultado: ...
```
