# Skill: Minimal Diff Review

## Objetivo

Revisar se uma alteração ficou pequena, focada e diretamente ligada à issue.

Use esta skill após implementar uma feature, bugfix ou refatoração e antes de abrir PR.

## Quando usar

Use quando houver qualquer diff em:

- código;
- configuração;
- infraestrutura;
- schema/banco;
- documentação operacional;
- templates;
- testes.

## Procedimento

### 1. Mapear arquivos alterados

Liste cada arquivo alterado e responda:

```txt
Arquivo:
Por que mudou:
Relação com a issue:
Risco:
```

Se um arquivo não tiver relação direta com a issue, remova do PR ou justifique explicitamente.

### 2. Procurar drive-by changes

Verifique se o diff contém:

- refatoração não solicitada;
- renomeação sem necessidade;
- formatação ampla;
- limpeza de código não relacionada;
- comentários alterados sem relação;
- dependência nova sem necessidade;
- mudança de comportamento fora do escopo.

Se encontrar, separe em outra issue/PR.

### 3. Avaliar abstrações

Pergunte:

```txt
Essa abstração é usada em mais de um lugar?
Ela reduz complexidade real agora?
Ela foi pedida pela issue?
Ela facilita teste ou segurança?
```

Se a resposta for não, prefira código direto e simples.

### 4. Avaliar tamanho do PR

Sinais de PR grande demais:

- toca muitas áreas não relacionadas;
- mistura frontend, backend, banco e infra sem ser feature fullstack planejada;
- altera contratos públicos sem critério claro;
- adiciona refatoração junto com feature;
- dificulta rollback.

Se ficar grande, recomende dividir em issues menores.

### 5. Confirmar preservação de comportamento

Verifique:

- rotas públicas preservadas;
- contratos de API preservados;
- schema não alterado sem necessidade;
- autenticação/autorização não alterada por acidente;
- layout não modificado fora da área da issue;
- testes existentes continuam válidos.

## Checklist de bloqueio

Bloqueie ou peça ajuste se houver:

- arquivo sem relação com issue;
- alteração sensível sem reviewer de segurança;
- schema/migration fora do escopo;
- refatoração estrutural escondida;
- mudança sem teste ou validação compatível;
- PR difícil de reverter.

## Saída esperada

```txt
Minimal Diff Review:
- Arquivos alterados e justificativa:
- Mudanças fora do escopo encontradas:
- Abstrações justificadas:
- Risco do diff:
- Recomendação: aprovar / ajustar / dividir PR
```
