# Skill: Frontend Design System

## Objetivo

Projetar e revisar interfaces como um sistema visual consistente, escalável e manutenível no código.

Use esta skill quando a tarefa envolver Tailwind CSS, shadcn/ui, tokens de design, componentes compartilhados, páginas de catálogo, dashboards, painel admin, landing pages, cards, grid, tipografia, radius, cores, imagens ou consistência visual.

## Quando usar

Use obrigatoriamente quando a issue envolver:

- criação ou alteração de componentes visuais reutilizáveis;
- design system;
- Tailwind theme, CSS variables ou tokens;
- shadcn/ui ou biblioteca de componentes;
- catálogo, cards, grids, dashboard ou painel admin;
- imagens comerciais ou cards de produto;
- padronização visual entre telas;
- redesign ou migração visual.

## Princípios centrais

### 1. Interface como sistema vivo

A UI não deve ser um conjunto de estilos soltos.

Antes de implementar, identifique:

```txt
Tokens existentes:
Componentes base:
Padrões de radius:
Padrões de spacing:
Padrões tipográficos:
Padrões de imagem:
Padrões de grid:
```

Se não houver padrão, proponha o menor padrão necessário para a issue.

Não crie um design system completo se a issue só pede uma tela.

### 2. Tokens de design

Centralize decisões visuais em tokens sempre que possível.

Tokens esperados:

```txt
background
surface
surface-muted
border
text
text-muted
primary
primary-foreground
secondary
secondary-foreground
success
warning
danger
radius
shadow
spacing
```

Com Tailwind, prefira usar classes que representem tokens do projeto em vez de cores arbitrárias espalhadas.

Evite:

```txt
bg-[#f2f2f2]
text-[#333]
rounded-[13px]
mt-[17px]
```

Exceto quando houver justificativa clara e pontual.

### 3. Palco neutro para produto visual

Quando a UI exibir imagens, roupas, produtos, tecidos, texturas ou fotografias com cores fortes, a interface ao redor deve ser neutra.

Regra:

```txt
Produto vibrante -> UI neutra
Produto neutro   -> UI pode ter mais personalidade
```

A interface não deve competir com a imagem do produto.

Use fundos como:

- branco;
- cinza claro;
- preto;
- neutros suaves;
- superfícies discretas.

### 4. Geometria e bordas

Defina uma linguagem geométrica consistente.

Exemplo:

```txt
Botões: 8px
Inputs: 8px
Cards: 12px
Modais: 16px
Avatares: full
```

Não misture radius aleatório sem intenção.

Se usar shadcn/ui, preserve a coerência com `--radius` e variantes dos componentes.

### 5. Aspect ratio padronizado

Cards e catálogos não devem quebrar o grid por imagens de tamanhos diferentes.

Regras sugeridas:

```txt
Moda / vestuário: 3:4
Produto geral: 1:1
Banner / hero: 16:9 ou 21:9
Avatar: 1:1
Documento / preview vertical: 3:4
```

Use wrappers com `aspect-*`, `object-cover` e `overflow-hidden`.

### 6. Imagens com fidelidade e performance

Imagens comerciais precisam preservar textura, caimento, iluminação e nitidez sem destruir performance.

Quando aplicável:

- use `next/image` em Next.js;
- use `sizes` correto;
- use containers com aspect ratio fixo;
- prefira formatos modernos quando o pipeline permitir;
- evite layout shift;
- use `priority` apenas para imagem crítica acima da dobra;
- use `loading="lazy"` para imagens abaixo da dobra quando aplicável.

Em HTML puro ou casos especiais, considerar `<picture>` com WebP/AVIF e fallback.

### 7. Escala tipográfica

Defina hierarquia clara.

Base recomendada:

```txt
body: 16px
small: 14px
caption: 12px
subtitle: 20px
section title: 24px ou 28px
H1: 32px a 48px, conforme a tela
```

Pesos:

```txt
Regular: leitura
Medium: labels e navegação
Semibold: subtítulos e ações
Bold: títulos, preços e pontos de decisão
```

Evite excesso de tamanhos e pesos em uma mesma tela.

### 8. Grid e composição

Use layout previsível.

Para desktop, prefira:

- container centralizado;
- grid de 12 colunas quando houver composição complexa;
- grids responsivos para cards;
- alinhamentos consistentes.

Com Tailwind:

```txt
max-w-7xl mx-auto px-4 sm:px-6 lg:px-8
grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4
```

### 9. Lei da proximidade

Itens relacionados devem estar próximos.

Exemplo em card de produto:

```txt
Imagem
Nome + categoria
Preço + status
Ação principal
```

O espaço interno entre título, preço e botão deve ser menor que o espaço entre cards diferentes.

### 10. shadcn/ui como base, não prisão

Use shadcn/ui para acelerar componentes acessíveis e consistentes.

Mas não aceite visual genérico automaticamente.

Para cada componente shadcn usado, confirme:

- variante correta;
- tamanho correto;
- estado disabled/loading;
- acessibilidade;
- consistência com tokens;
- copy de ação clara.

## Checklist antes de implementar

```txt
Design System Check:
- Tokens existentes identificados?
- Paleta coerente?
- Radius consistente?
- Tipografia padronizada?
- Aspect ratio definido quando houver imagens?
- Grid e spacing previsíveis?
- Componentes shadcn usados com variantes corretas?
- UI compete com imagens/produto?
- Há risco de estilo inline/arbitrário espalhado?
```

## Checklist antes do PR

- [ ] Não há cores arbitrárias sem justificativa.
- [ ] Radius segue padrão.
- [ ] Tipografia tem hierarquia clara.
- [ ] Espaçamento respeita proximidade lógica.
- [ ] Cards e imagens têm aspect ratio consistente.
- [ ] Layout não quebra em mobile/tablet/desktop.
- [ ] Componentes shadcn seguem variantes coerentes.
- [ ] Imagens não causam layout shift óbvio.
- [ ] A UI não compete com o conteúdo principal.
- [ ] A alteração não criou design system exagerado para uma issue pequena.

## Integração com outras skills

Use junto com:

- `frontend-design` para direção visual e identidade;
- `next-react-tailwind-shadcn-motion` para implementação na stack;
- `frontend-ux-engineering` para estados, interação e feedback;
- `responsive-design` para breakpoints;
- `accessibility-review` para semântica e navegação assistiva;
- `minimal-diff-review` para evitar redesign fora do escopo.

## Saída esperada no plano

```txt
Frontend Design System:
- Tokens/padrões existentes:
- Paleta:
- Radius:
- Tipografia:
- Grid/spacing:
- Imagens/aspect ratio:
- Componentes shadcn envolvidos:
- Riscos de inconsistência:
```

## Saída esperada no fechamento

```txt
Design System Review:
- Tokens usados/preservados:
- Componentes reutilizados:
- Consistência de radius/tipografia/spacing:
- Aspect ratio/imagens:
- Responsividade:
- Riscos restantes:
```
