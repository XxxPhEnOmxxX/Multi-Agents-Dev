---
description: Auditar dependências, versões, CVEs, lockfiles, licenças e risco de supply chain.
argument-hint: [projeto ou lockfile]
allowed-tools: Read, Glob, Grep, Bash, Edit, MultiEdit, Write
---

# Dependency Audit

Tarefa solicitada:

$ARGUMENTS

Procedimento:
1. Identifique gerenciador de pacotes, lockfile e dependências diretas.
2. Revise versões obsoletas, pacotes abandonados, licenças e scripts perigosos.
3. Recomende atualização com menor quebra possível.
4. Entregue riscos, correções e validação pós-upgrade.
