---
description: Analisar Docker, Docker Compose, networks, volumes, healthchecks, proxy e logs.
argument-hint: [serviço, erro ou docker-compose]
allowed-tools: Read, Glob, Grep, Bash, Edit, MultiEdit, Write
---

# Docker Infrastructure

Tarefa solicitada:

$ARGUMENTS

Procedimento:
1. Leia docker-compose, Dockerfile, .env.example e nginx/proxy.
2. Verifique portas, networks, volumes, DNS interno, healthchecks e logs.
3. Procure conflitos entre porta interna, porta publicada e proxy.
4. Entregue causa provável, correção mínima, ideal e validação.
