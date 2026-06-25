---
description: Planejar deploy seguro com validações, rollback, janela, riscos e checklist manual.
argument-hint: [ambiente ou release]
disable-model-invocation: true
allowed-tools: Read, Glob, Grep, Bash, Edit, MultiEdit, Write
---

# Deployment Plan

Tarefa solicitada:

$ARGUMENTS

Procedimento:
1. Verifique branch, diff, testes, build, migrations e dependências.
2. Liste riscos, janela, rollback, backup e validações pós-deploy.
3. Nunca execute ação destrutiva sem confirmação explícita.
4. Entregue checklist manual, plano de rollback e critérios de sucesso.
