# Skill: Frontend UX Engineering

## Objetivo

Projetar e implementar experiência de usuário com interações rápidas, estados claros, feedback assíncrono, formulários resilientes, navegação simples e HTML semântico.

Use esta skill quando a tarefa envolver UX, filtros, busca, formulários, estado, loading, skeletons, empty states, erros, validação, navegação mobile, microinterações ou acessibilidade.

## Quando usar

Use obrigatoriamente quando a issue envolver:

- filtros, busca, ordenação ou listagem;
- formulários;
- requisições assíncronas;
- loading, skeletons, erros ou estados vazios;
- navegação mobile;
- menu, sidebar, tabs, dialog, drawer ou dropdown;
- feedback de clique, hover, submit ou sucesso;
- acessibilidade de fluxo;
- arquitetura de informação da tela.

## Princípios centrais

### 1. Arquitetura de informação rasa

O usuário não deve cavar fundo para encontrar o que precisa.

Antes de implementar navegação, defina:

```txt
Ação principal da tela:
Informações primárias:
Informações secundárias:
Filtros necessários:
Ações frequentes:
Ações perigosas:
```

Categorias e ações principais devem estar visíveis ou a poucos cliques.

### 2. Mobile-first real

Mobile-first não é apenas fazer caber na tela.

Verifique:

- touch targets com tamanho seguro;
- ações principais acessíveis com o polegar;
- filtros e ações críticas não escondidos demais;
- modais/drawers utilizáveis em tela pequena;
- tabelas com alternativa responsiva quando necessário.

Regra prática:

```txt
Ação primária frequente no mobile deve estar fácil de alcançar.
Ação destrutiva deve estar protegida contra toque acidental.
```

### 3. Filtragem de alta performance

Filtros e busca devem parecer instantâneos quando os dados forem locais ou pequenos.

Estruture dados em objetos claros:

```txt
id
name
category
status
price
color
createdAt
updatedAt
```

Use filtros previsíveis, memoização apenas quando necessário e evite recarregar a página inteira sem motivo.

Se os dados forem grandes, considere paginação, debounce, busca server-side ou virtualização conforme a stack.

### 4. Estados assíncronos

Toda ação assíncrona deve ter feedback.

Estados mínimos:

```txt
idle
loading
success
error
empty
```

Nunca deixe a tela em branco enquanto dados carregam.

Use skeletons quando o layout esperado é conhecido.

Use spinner apenas quando o conteúdo não tiver estrutura previsível ou a espera for curta.

### 5. Skeletons úteis

Skeleton deve imitar a estrutura real do conteúdo.

Bom:

```txt
Card skeleton com bloco de imagem + linhas de texto + ação
Tabela skeleton com linhas e colunas
Form skeleton com labels e campos
```

Ruim:

```txt
Um spinner central para toda tela sem contexto
Blocos cinzas aleatórios que não representam o layout final
```

### 6. Empty states acionáveis

Se uma busca, filtro ou categoria retornar vazio, a interface deve explicar e sugerir ação.

Um empty state bom contém:

```txt
Título claro
Descrição curta
Ação sugerida
Opção de limpar filtros, criar item ou voltar
```

Exemplo:

```txt
Nenhum local encontrado.
Tente limpar os filtros ou cadastre um novo local autorizado.
[Limpar filtros] [Novo local]
```

### 7. Erros contextuais

Erros devem dizer o que aconteceu e como corrigir.

Evite:

```txt
Erro inesperado.
Falha.
Invalid input.
```

Prefira:

```txt
Não foi possível salvar o local.
Verifique latitude, longitude e raio antes de tentar novamente.
```

### 8. Validação antecipada

Formulários devem orientar o usuário antes do submit final.

Use validação em:

- `onBlur` para campos textuais;
- `onChange` para máscaras, seletores e campos curtos;
- submit para validação final;
- server action/API para validação de autoridade.

A mensagem deve ficar perto do campo e explicar a correção.

### 9. Microinterações

Microinterações confirmam que o sistema recebeu a ação.

Use para:

- hover de botão/card;
- foco de campo;
- submit em andamento;
- sucesso ao salvar;
- item adicionado/removido;
- expansão/recolhimento;
- troca de aba/filtro.

Não exagere. Movimento deve ajudar, não distrair.

### 10. HTML semântico

A estrutura deve fazer sentido sem CSS.

Use corretamente:

```txt
<header>
<nav>
<main>
<section>
<article>
<aside>
<footer>
<form>
<label>
<button>
```

Evite transformar tudo em `div` clicável.

Botão que executa ação deve ser `<button>`.

Link que navega deve ser `<a>` ou `Link`.

### 11. Acessibilidade operacional

Verifique:

- labels de formulário;
- foco visível;
- ordem de tab coerente;
- contraste suficiente;
- `aria-*` apenas quando necessário;
- mensagens de erro associadas ao campo;
- navegação por teclado;
- reduced motion em animações relevantes.

## Checklist antes de implementar

```txt
UX Engineering Check:
- Ação principal clara?
- Navegação rasa?
- Estados idle/loading/success/error/empty definidos?
- Skeleton necessário?
- Empty state necessário?
- Validação antecipada necessária?
- Mobile touch targets e zona do polegar considerados?
- HTML semântico preservado?
- Microinterações com propósito?
```

## Checklist antes do PR

- [ ] Tela não fica em branco durante loading.
- [ ] Empty states orientam próxima ação.
- [ ] Erros são contextuais.
- [ ] Formulários validam cedo e no servidor/API.
- [ ] Ação principal está clara.
- [ ] Mobile foi validado.
- [ ] Elementos clicáveis têm tamanho seguro.
- [ ] HTML semântico foi usado.
- [ ] Foco visível e navegação por teclado foram considerados.
- [ ] Microinterações não atrapalham a operação.

## Integração com outras skills

Use junto com:

- `frontend-design-system` para tokens, layout e componentes;
- `frontend-design` para direção visual;
- `next-react-tailwind-shadcn-motion` para implementação;
- `accessibility-review` para validação assistiva;
- `test-strategy` para cenários de UX;
- `success-criteria-check` para evidências.

## Saída esperada no plano

```txt
Frontend UX Engineering:
- Ação principal:
- Fluxo do usuário:
- Estados necessários:
- Loading/skeleton:
- Empty state:
- Erros e validações:
- Mobile/touch:
- Semântica/acessibilidade:
- Microinterações:
```

## Saída esperada no fechamento

```txt
UX Engineering Review:
- Fluxo validado:
- Estados implementados:
- Empty/loading/error:
- Formulários/validação:
- Mobile:
- Semântica/acessibilidade:
- Riscos restantes:
```
