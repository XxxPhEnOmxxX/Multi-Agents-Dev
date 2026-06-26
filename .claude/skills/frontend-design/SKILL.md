# Skill: Frontend Design

## Objetivo

Criar ou revisar interfaces com identidade visual intencional, específica ao produto e menos genérica.

Use esta skill quando a tarefa envolver criação de telas, redesign, landing pages, painel admin, dashboard, componentes visuais, design system, UX writing, experiência visual, responsividade ou revisão estética.

Esta skill foi adaptada para a estrutura multi-agent a partir da skill pública `frontend-design` do plugin `frontend-design` do repositório `anthropics/claude-code`.

## Quando usar

Use obrigatoriamente quando a issue envolver:

- nova página ou tela;
- redesenho de página existente;
- migração visual para componentes compartilhados;
- dashboard;
- painel admin;
- landing page;
- componente visual importante;
- design system;
- copy de interface;
- empty states, erros, alerts, toasts e mensagens de formulário;
- validação visual antes de PR.

## Princípios

### 1. Design específico ao produto

Não use aparência genérica de template.

Antes de desenhar, identifique:

```txt
Produto:
Usuário principal:
Tarefa principal da tela:
Contexto emocional/operacional:
O que esta interface precisa comunicar:
```

O visual deve nascer do assunto real do produto, não de padrões genéricos.

### 2. Hero ou tela inicial como tese

Se houver uma tela inicial, dashboard ou página de entrada, ela deve comunicar rapidamente o valor principal da experiência.

Evite usar sempre o mesmo padrão de:

```txt
headline genérico + subtítulo + cards com números + gradiente
```

Use esse padrão apenas se ele realmente for o mais adequado para a tela.

### 3. Tipografia com intenção

A tipografia deve ajudar a personalidade da interface.

Defina papéis claros:

- display/título;
- corpo;
- labels, dados ou captions.

Evite usar pesos, tamanhos e espaçamentos aleatórios.

### 4. Estrutura deve carregar informação

Elementos como números, divisores, etiquetas, cards, agrupamentos e ícones devem representar algo verdadeiro sobre o conteúdo.

Não use decoração apenas para parecer sofisticado.

Exemplo:

- numeração faz sentido em uma sequência ou processo;
- badges fazem sentido para status;
- cards fazem sentido para agrupamentos comparáveis;
- tabelas fazem sentido para dados densos.

### 5. Movimento com propósito

Animações, transições e microinterações devem servir à usabilidade ou à identidade da tela.

Evite efeitos espalhados que passam sensação de IA genérica.

Prefira poucos momentos bem escolhidos.

### 6. Uma assinatura visual memorável

Para cada tela importante, tente definir um elemento visual ou interação que a torne reconhecível.

A assinatura pode ser:

- layout incomum mas útil;
- tratamento tipográfico;
- padrão visual conectado ao produto;
- microinteração relevante;
- componente com linguagem própria;
- modo claro de organizar informação.

Use ousadia em um ponto e mantenha o resto disciplinado.

## Processo obrigatório antes de codar

Antes de escrever código visual, faça um plano curto:

```txt
Tela ou componente:
Usuário:
Tarefa principal:
Tom visual:
Paleta sugerida:
Tipografia/escala:
Layout:
Assinatura visual:
Riscos de parecer genérico:
```

Se a issue já tiver design system, tokens ou componentes definidos, respeite-os.

Se não houver direção visual, proponha uma direção simples e justificável antes de implementar.

## Planejamento visual

Ao planejar uma tela, defina:

### Paleta

Use 4 a 6 cores com função clara:

```txt
background:
surface:
text:
muted:
accent:
danger/success, se necessário:
```

Não adicione cores sem função.

### Tipografia

Defina uma escala simples:

```txt
page title:
section title:
body:
label:
data/caption:
```

### Layout

Descreva a composição antes de codar:

```txt
Topo:
Conteúdo principal:
Ações:
Estados vazios:
Erros:
Mobile:
```

### Copy de interface

Escreva do ponto de vista do usuário.

Prefira:

```txt
Salvar alterações
Criar colaborador
Ativar notificação
Ver detalhes
```

Evite:

```txt
Submit
Enviar dados
Processar ação
Webhook config
```

A ação deve manter o mesmo nome no botão, loading, toast e mensagem final.

## Restrições para painel admin e produto operacional

Em sistemas administrativos, a interface deve priorizar clareza.

Evite excesso de criatividade que prejudique:

- leitura rápida;
- operação em campo;
- auditoria;
- acessibilidade;
- consistência entre módulos;
- manutenção.

O design pode ser distintivo, mas nunca deve atrapalhar a operação.

## Checklist de implementação

Antes do PR, confirme:

- [ ] A tela tem objetivo claro.
- [ ] O visual foi definido a partir do produto real.
- [ ] A solução não parece template genérico.
- [ ] Existe consistência com o design system do projeto.
- [ ] A hierarquia visual está clara.
- [ ] A copy usa linguagem simples e orientada à ação.
- [ ] Estados vazios orientam o próximo passo.
- [ ] Erros explicam o que aconteceu e como corrigir.
- [ ] Focus states são visíveis.
- [ ] Mobile foi considerado.
- [ ] Reduced motion foi respeitado quando houver animação.
- [ ] O design não cria complexidade desnecessária.

## Integração com outras skills

Use junto com:

- `frontend-ui-review` para revisão geral de interface;
- `responsive-design` para viewport e mobile;
- `accessibility-review` para acessibilidade;
- `react-optimization` quando envolver React;
- `minimal-diff-review` para evitar redesign fora do escopo;
- `success-criteria-check` para validar critérios visuais.

## Saída esperada no plano

```txt
Frontend Design:
- Produto/tela:
- Usuário:
- Tarefa principal:
- Direção visual:
- Paleta/tokens:
- Tipografia:
- Layout:
- Assinatura visual:
- Risco de parecer genérico:
- Validações visuais:
```

## Saída esperada no fechamento

```txt
Frontend Design Review:
- Identidade visual aplicada:
- Componentes/tokens usados:
- Copy revisada:
- Mobile/responsividade:
- Acessibilidade:
- Estados vazios/erros:
- Riscos restantes:
```
