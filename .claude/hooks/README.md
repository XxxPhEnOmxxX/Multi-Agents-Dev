# Claude Code Hooks

Hooks aplicam uma camada de segurança e validação que não depende apenas de instrução em linguagem natural.

## Hooks incluídos

- `bash-guard.py`: protege comandos Bash de alto risco, como commit/push direto em branch protegida e comandos destrutivos.
- `file-guard.py`: bloqueia leitura ou alteração de arquivos sensíveis como `.env`, chaves e credenciais.
- `post-edit-reminder.py`: lembra o Claude principal de revisar diff, rodar validações e verificar escopo antes de commit/PR.

## Validação

Dentro do Claude Code, use:

```txt
/hooks
```

Esse comando mostra os hooks carregados e de qual arquivo vieram.

## Observação

Os scripts são chamados por `.claude/settings.json` usando `python3`, então não dependem de permissão executável no Git.
