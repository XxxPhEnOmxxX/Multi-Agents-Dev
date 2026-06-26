# Skill: Karpathy Code Discipline

## Objetivo

Aplicar uma disciplina de engenharia antes de alterar código: pensar antes de codar, escolher a solução mais simples, limitar o diff e trabalhar com critérios verificáveis.

Use esta skill em toda feature, bugfix, refatoração ou alteração técnica planejada.

## Quando usar

Use obrigatoriamente quando a tarefa envolver:

- código;
- arquitetura;
- banco de dados;
- frontend;
- backend;
- infraestrutura;
- autenticação;
- integração;
- testes;
- refatoração.

Pode ser dispensada apenas para conversa casual, explicação conceitual ou documentação simples sem alteração técnica.

## Procedimento

### 1. Entender antes de editar

Antes de alterar arquivos, declare:

```txt
O que a issue pede:
O que não está sendo pedido:
Arquivos prováveis:
Risco:
Critério de sucesso:
```

### 2. Declarar suposições

Liste suposições importantes, como:

- estrutura esperada do projeto;
- comportamento esperado de APIs;
- formato de dados;
- permissões;
- dependências;
- estado de banco;
- premissas de UI/UX.

Se uma suposição puder mudar a solução, confirme antes de implementar.

### 3. Identificar ambiguidade

Se houver ambiguidade, classifique:

- baixa: pode seguir com decisão conservadora;
- média: registrar suposição e seguir com cuidado;
- alta: pedir decisão antes de mexer.

Ambiguidade alta inclui:

- regra de negócio não definida;
- mudança de contrato público;
- alteração de autenticação/autorização;
- alteração de schema/banco;
- comportamento de produção;
- exposição de dados sensíveis.

### 4. Escolher a solução mais simples

Antes de implementar, compare mentalmente:

```txt
Solução mínima:
Solução mais robusta:
Solução exagerada:
```

Escolha a mínima que atende aos critérios de aceite.

### 5. Evitar overengineering

Não crie:

- abstrações genéricas para um caso único;
- factories/adapters/services sem necessidade clara;
- arquitetura para requisito futuro ainda não pedido;
- refatoração estrutural junto com feature pequena;
- múltiplas camadas para lógica simples.

### 6. Implementar diff cirúrgico

Durante a implementação:

- altere somente arquivos necessários;
- mantenha estilo do projeto;
- não formate arquivos inteiros sem necessidade;
- não renomeie símbolos fora do escopo;
- não misture limpeza com feature.

### 7. Verificar sucesso

Antes de finalizar, confirme:

- critérios de aceite atendidos;
- testes/lint/build executados quando existirem;
- sistema local iniciado quando necessário;
- smoke test executado quando aplicável;
- limitações registradas;
- riscos restantes claros.

## Saída esperada no plano

```txt
Disciplina de código:
- Suposições:
- Ambiguidades:
- Solução mais simples:
- Fora do escopo:
- Critérios verificáveis:
```

## Saída esperada no fechamento

```txt
Disciplina de implementação:
- A solução foi mínima?
- O diff foi cirúrgico?
- Houve refatoração fora do escopo?
- Critérios de aceite verificados?
- Limitações/riscos:
```
