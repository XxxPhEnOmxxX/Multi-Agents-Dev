# Git Workflow

## Regra central

Nunca trabalhar diretamente em `main` ou `master` para tarefas de desenvolvimento.

Toda alteração aprovada deve seguir este fluxo:

```txt
branch de trabalho -> commit -> push -> Pull Request
```

## Antes de alterar arquivos

1. Verifique o diretório do projeto.
2. Rode `git status`.
3. Identifique a branch atual.
4. Atualize a base quando aplicável.
5. Crie uma branch específica para a tarefa.

## Padrão de branch

Use nomes objetivos:

```txt
feature/<descricao-curta>
fix/<descricao-curta>
docs/<descricao-curta>
chore/<descricao-curta>
refactor/<descricao-curta>
```

## Commit

Commits devem ser claros e pequenos.

Exemplos:

```txt
feat: add password reset flow
fix: handle login validation error
docs: update authentication API guide
chore: add Claude Code project rules
```

## Pull Request

Toda PR deve conter:

- resumo do que mudou;
- motivo da alteração;
- testes/validações executadas;
- riscos conhecidos;
- plano de rollback quando aplicável.
