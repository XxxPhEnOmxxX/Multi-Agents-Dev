# WSL Development

## Regra central

Todo desenvolvimento deve acontecer no ambiente local WSL do projeto.

## Antes de executar comandos

Confirme:

```bash
pwd
git status
git branch --show-current
```

## Boas práticas

- Prefira caminhos Linux dentro do WSL.
- Evite misturar execução Windows e WSL na mesma tarefa.
- Use o gerenciador de pacotes detectado no projeto.
- Não instale dependências globais sem necessidade.
- Não altere arquivos sensíveis ou locais sem autorização.

## Docker

Quando houver Docker Compose:

```bash
docker compose config
```

Use esse comando para validar sintaxe antes de sugerir execução de containers.

## Node/Python

Escolha comandos conforme arquivos existentes:

- Node: `package.json`, lockfile e scripts disponíveis.
- Python: `pyproject.toml`, `requirements.txt`, `pytest.ini` ou estrutura equivalente.

Se um comando recomendado não existir, explique e use a validação mais próxima.
