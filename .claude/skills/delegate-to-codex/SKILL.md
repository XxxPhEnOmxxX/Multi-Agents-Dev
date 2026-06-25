---
name: delegate-to-codex
description: Delega uma tarefa a uma instância independente da Codex CLI (OpenAI) através da ferramenta MCP `delegate_to_codex` (servidor `codex-delegation`), e repassa a resposta final do Codex. Use sempre que o usuário mencionar "codex", "delegar ao codex", "perguntar pro codex", "rodar com o codex" ou pedir uma "segunda opinião" / "revisão cruzada" de um código, diff ou decisão. Considere também sugerir proativamente esta skill, mesmo sem pedido explícito, quando uma tarefa se beneficiaria claramente de um agente independente: revisar um plano ou diff arriscado antes de aplicá-lo, validar uma decisão arquitetural, investigar um bug em paralelo enquanto você segue com outra parte do trabalho, ou obter uma leitura de um repositório diferente do atual. Não sugira para tarefas triviais que você já resolve sozinho sem ganho real de uma segunda perspectiva — sugestões demais cansam o usuário.
---

# Delegar ao Codex

## O que é

`delegate_to_codex` é uma ferramenta MCP (servidor `codex-delegation`, registrado em escopo
user) que chama `codex exec` e devolve a mensagem final do Codex junto com stdout/stderr e
metadados da execução. Ela roda o Codex como um processo isolado — ele não vê nada desta
conversa além do que for colocado no campo `prompt`.

## Quando usar

**Gatilho explícito** — o usuário pede diretamente ("delega isso ao codex", "veja o que o
codex pensa disso", "roda em paralelo com o codex").

**Sugestão proativa** — ofereça delegar quando o ganho de uma segunda perspectiva for real:
- revisão cruzada de um diff/plano arriscado antes de aplicá-lo;
- validar uma decisão arquitetural onde estar errado é caro;
- investigar algo em paralelo (ex: um bug numa parte do código) enquanto você continua outra
  frente de trabalho;
- analisar um repositório/diretório diferente do que está em foco na conversa atual.

Antes de invocar proativamente, diga ao usuário o que você está prestes a perguntar ao Codex
e por quê — não execute silenciosamente em nome dele.

## Como chamar a ferramenta

O prompt enviado ao Codex precisa ser **autocontido**: o Codex não tem memória desta
conversa, então trate-o como um colega que acabou de chegar — inclua caminhos de arquivo,
o que já foi tentado, e o que exatamente você quer de volta. Prompts vagos ("revise isso")
produzem respostas vagas.

Parâmetros e como escolhê-los:

- **`prompt`** (obrigatório): a tarefa completa e autocontida.
- **`cwd`**: o diretório do projeto relevante para a tarefa. Padrão se omitido: diretório de
  trabalho do servidor MCP — prefira sempre passar explicitamente o cwd do projeto em questão.
- **`sandbox`**: padrão desta skill é **`read-only`**, mesmo que o padrão da ferramenta seja
  `workspace-write`. Só use `workspace-write` quando a tarefa exigir que o Codex crie/edite
  arquivos de fato — e avise o usuário disso antes de chamar, já que isso tem efeito real no
  filesystem dele. Nunca use `danger-full-access` a menos que o usuário peça isso
  explicitamente e entenda que desativa o sandbox (inclusive de rede).
- **`model`**: omita por padrão (deixa o Codex usar o modelo dele). Só passe se o usuário
  pedir um modelo específico.
- **`timeoutMs`**: padrão de 10 minutos é suficiente para a maioria das tarefas. Aumente para
  tarefas grandes (limite da ferramenta é 60 minutos) em vez de deixar truncar.
- **`extraArgs`**: avançado, raramente necessário.

## Interpretando o resultado

A resposta vem em `structuredContent` com estes campos — leia-os, não só o texto bruto:

- **`finalMessage`** — a resposta autoritativa do Codex. É isso que você repassa ao usuário.
- **`stdout`** — geralmente duplica `finalMessage`.
- **`stderr`** — banner do Codex (modelo, sandbox, session id, tokens usados). Útil para
  transparência/debug, não é a resposta.
- **`exitCode`** / **`timedOut`** — se `exitCode !== 0` ou `timedOut === true`, trate como
  falha: mostre o `stderr` e o que aconteceu, não finja que deu certo nem invente uma resposta
  no lugar da do Codex.

## Problemas comuns

- **Servidor não conectado**: confirme com `claude mcp list` que `codex-delegation` aparece
  como Connected. Ele está registrado em escopo user apontando para
  `C:\Users\isaqu\Desktop\Dev Agent Template\work\codex-mcp-server\server.mjs`.
- **Timeout em tarefa grande**: suba `timeoutMs` em vez de quebrar a tarefa sem avisar.
- **Sandbox insuficiente**: se o Codex precisar escrever arquivos e você só pediu
  `read-only`, ele vai falhar ou recusar a ação — escale para `workspace-write`
  explicitamente, avisando o usuário.

## Exemplo

```json
{
  "name": "delegate_to_codex",
  "arguments": {
    "prompt": "Revise o diff em src/auth/session.ts (cole o diff aqui) e aponte riscos de regressão de segurança. Não aplique nenhuma mudança.",
    "cwd": "C:\\Users\\isaqu\\Desktop\\g7-ponto",
    "sandbox": "read-only",
    "timeoutMs": 300000
  }
}
```
