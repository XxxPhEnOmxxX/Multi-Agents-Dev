# Skill: Next React Tailwind shadcn Motion

## Objetivo

Implementar frontend moderno com Next.js, React, TypeScript, Tailwind CSS, shadcn/ui e Framer Motion de forma organizada, performática, acessível e manutenível.

Use esta skill quando a issue envolver páginas, componentes, animações, formulários, tabelas, imagens, rotas, Server Components, Client Components, Tailwind, shadcn/ui ou Motion.

## Quando usar

Use obrigatoriamente quando a stack do projeto incluir uma ou mais destas tecnologias:

- Next.js;
- React;
- TypeScript;
- Tailwind CSS;
- shadcn/ui;
- Framer Motion ou Motion;
- App Router;
- Server Actions;
- componentes visuais interativos.

## Separação de responsabilidades

### Next.js

Use Next.js para:

- rotas;
- layouts;
- Server Components;
- data fetching no servidor quando aplicável;
- metadata;
- redirects;
- cache/revalidate quando aplicável;
- imagens otimizadas quando houver suporte.

### React

Use React para:

- componentes;
- props;
- composição de UI;
- estado local;
- eventos;
- listas;
- formulários interativos;
- componentes client quando necessário.

### TypeScript

Use TypeScript para:

- tipar props;
- tipar dados de entrada;
- tipar estados;
- tipar retornos de função;
- evitar `any` sem justificativa;
- deixar contratos claros entre componentes.

### Tailwind CSS

Use Tailwind para:

- spacing;
- layout;
- grid/flex;
- responsividade;
- cor baseada em tokens;
- estados visuais;
- utilitários previsíveis.

Evite classes arbitrárias quando tokens existentes resolvem.

### shadcn/ui

Use shadcn/ui para:

- botões;
- cards;
- inputs;
- forms;
- dialogs;
- tables;
- badges;
- dropdowns;
- skeletons;
- toasts;
- componentes acessíveis reutilizáveis.

Não duplique componente base se já existe equivalente no projeto.

### Framer Motion / Motion

Use Motion para:

- transições de entrada;
- hover/tap feedback;
- expansão/recolhimento;
- troca de lista/aba;
- animações de layout;
- microinterações.

Não transforme toda a tela em animação. Movimento deve ter propósito.

## Server Component vs Client Component

Por padrão, prefira Server Components.

Use `"use client"` somente quando o componente precisar de:

- `useState`;
- `useEffect`;
- eventos complexos do navegador;
- Framer Motion;
- acesso a `window`, `document` ou APIs do browser;
- hooks de bibliotecas client;
- estado visual interativo.

Regra:

```txt
Componente que só renderiza dados -> Server Component
Componente que interage/anima -> Client Component
```

Evite transformar páginas inteiras em client sem necessidade.

## Arquitetura de componentes

Organize componentes por responsabilidade.

Exemplo:

```txt
src/app/
  layout.tsx
  page.tsx
  admin/
    layout.tsx
    locations/page.tsx

src/components/
  ui/
    button.tsx
    card.tsx
    table.tsx
  admin/
    page-header.tsx
    data-table.tsx
    empty-state.tsx
  marketing/
    hero-section.tsx
    features-section.tsx
```

Regras:

- `app/` guarda rotas e layouts;
- `components/ui/` guarda shadcn/base components;
- `components/admin/` guarda componentes do painel;
- `components/marketing/` guarda landing pages;
- componentes grandes devem ser quebrados por responsabilidade;
- não misturar regra de negócio pesada em componente visual.

## Imagens

Para Next.js, prefira `next/image` quando aplicável.

Boas práticas:

- definir `alt` útil;
- usar aspect ratio fixo;
- evitar layout shift;
- usar `sizes` correto;
- usar `priority` só acima da dobra;
- usar `object-cover` quando a imagem deve preencher card;
- garantir fallback visual para imagem ausente.

Para catálogos ou grids:

```txt
Moda / vestuário: aspect-[3/4]
Produto geral: aspect-square
Hero/banner: aspect-[16/9] ou aspect-[21/9]
```

## Formulários

Para formulários:

- labels visíveis;
- mensagens de erro perto do campo;
- validação antecipada quando fizer sentido;
- estado de submit;
- botão disabled/loading durante envio;
- feedback de sucesso/erro;
- validação no servidor/API além da validação client.

Com shadcn/ui, prefira `Form`, `Input`, `Label`, `Textarea`, `Select`, `Checkbox`, `Button` e mensagens consistentes do projeto.

## Estados de UI

Toda tela com dados deve considerar:

```txt
loading
empty
error
success
populated
```

Use:

- `Skeleton` para loading previsível;
- `Alert` para erros;
- `EmptyState` ou card de orientação para vazio;
- toast/flash message para confirmação;
- tabela/card/lista para dados preenchidos.

## Animações

Use Motion apenas em Client Components.

Padrões seguros:

```txt
initial opacity/y pequeno
transition curta
whileInView para seções abaixo da dobra
whileHover discreto em cards/botões
AnimatePresence para troca de estados
layout para rearranjos simples
```

Respeite reduced motion quando o projeto tiver suporte.

Evite:

- delays longos;
- animação em tudo;
- movimento que muda layout de forma imprevisível;
- animação que atrapalha clique ou leitura.

## Performance

Verifique:

- evitar client component desnecessário;
- evitar estado global sem necessidade;
- evitar rerender pesado em listas grandes;
- usar memoização apenas quando há problema real;
- evitar imagens sem otimização;
- evitar bibliotecas novas sem justificativa;
- evitar animações pesadas em listas grandes.

## Checklist antes de implementar

```txt
Stack Frontend Check:
- A rota é Next.js App Router?
- O componente pode ser server?
- Onde precisa de client?
- Quais props precisam ser tipadas?
- Quais componentes shadcn já existem?
- Quais tokens Tailwind usar?
- Há imagens? Aspect ratio e sizes definidos?
- Há estados loading/empty/error?
- Há animação? Ela justifica `use client`?
```

## Checklist antes do PR

- [ ] Nenhuma página inteira virou client sem necessidade.
- [ ] Props e dados principais estão tipados.
- [ ] Componentes shadcn existentes foram reaproveitados.
- [ ] Tailwind usa tokens/padrões do projeto.
- [ ] Imagens têm `alt`, aspect ratio e estratégia de performance.
- [ ] Loading, empty e error foram considerados.
- [ ] Motion foi usado apenas onde agrega valor.
- [ ] Mobile foi validado.
- [ ] Acessibilidade básica foi considerada.
- [ ] Lint/build/test foram executados quando disponíveis.

## Integração com outras skills

Use junto com:

- `frontend-design-system` para tokens, grid e consistência;
- `frontend-ux-engineering` para estados, feedback e UX;
- `frontend-design` para identidade visual;
- `react-optimization` para performance React;
- `responsive-design` para breakpoints;
- `accessibility-review` para semântica e foco;
- `test-strategy` para validação.

## Saída esperada no plano

```txt
Next/React/Tailwind/shadcn/Motion:
- Server vs client:
- Componentes envolvidos:
- Tipos/props:
- shadcn/ui:
- Tailwind/tokens:
- Imagens:
- Estados UI:
- Motion/animações:
- Validações:
```

## Saída esperada no fechamento

```txt
Stack Review:
- Server/client preservado:
- Componentes criados/reutilizados:
- Tipagem:
- Tailwind/shadcn:
- Estados UI:
- Imagens/performance:
- Motion:
- Riscos restantes:
```
