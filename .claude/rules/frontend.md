# Frontend Rules

## Responsabilidade

Use `frontend-specialist` para tarefas de interface, React, componentes, responsividade, acessibilidade, design system e UX engineering.

## Skills obrigatórias por tipo de tarefa

- `frontend-design`: aparência, identidade visual, copy de interface ou revisão estética.
- `frontend-design-system`: tokens, Tailwind, shadcn/ui, cards, grids, tipografia, radius, imagens ou padronização visual.
- `frontend-ux-engineering`: filtros, busca, formulários, loading, skeletons, empty states, erros, navegação mobile, validação ou feedback assíncrono.
- `next-react-tailwind-shadcn-motion`: Next.js, React, TypeScript, Tailwind CSS, shadcn/ui ou Motion.
- `accessibility-review`: formulário, navegação, tabela, dialog, menu, drawer ou mudança de semântica.
- `responsive-design`: impacto em mobile, tablet ou desktop.

## Padrões esperados

- Manter componentes pequenos e claros.
- Evitar estado global quando estado local resolver.
- Preferir Server Components quando não houver interação client.
- Usar Client Components apenas quando houver estado, evento, browser API ou animação.
- Tipar props e estruturas principais com TypeScript.
- Tratar carregamento, erro, sucesso e vazio.
- Usar skeletons quando o layout esperado for previsível.
- Nunca deixar tela em branco quando busca ou filtro não retornar resultado.
- Validar layout em mobile, tablet e desktop.
- Preferir HTML semântico.
- Preservar o padrão visual existente do projeto.
- Evitar cores, spacing e radius arbitrários sem justificativa.
- Reutilizar componentes existentes antes de criar novos.

## Design system

Antes de alterar UI, identifique:

```txt
Tokens de cor:
Tokens de radius:
Escala tipográfica:
Padrão de spacing:
Componentes base:
Padrão de grid:
Padrão de imagem/aspect ratio:
```

Quando houver imagens ou produtos visuais, mantenha a UI ao redor neutra para não competir com o conteúdo.

Padronize aspect ratio:

```txt
Moda / vestuário: 3:4
Produto geral: 1:1
Hero/banner: 16:9 ou 21:9
Avatar: 1:1
```

## UX engineering

Toda tela com dados deve considerar:

```txt
loading
empty
error
success
populated
```

Formulários devem ter label claro, validação antecipada quando fizer sentido, erro perto do campo, estado de envio e feedback final.

Mobile deve considerar touch targets seguros e ações principais acessíveis.

## Imagens e performance

Verifique:

- `alt` útil;
- aspect ratio fixo;
- estratégia de carregamento;
- evitar layout shift;
- prioridade apenas para imagem crítica acima da dobra.

## Motion e microinterações

Use animação apenas com propósito:

- feedback de hover/tap;
- entrada discreta de seção;
- expansão/recolhimento;
- troca de estado;
- confirmação visual de ação.

Evite animação excessiva, delays longos ou movimento que atrapalhe leitura e operação.

## Antes de finalizar

Verifique:

- responsividade;
- acessibilidade básica;
- estados de carregamento, vazio, erro e sucesso;
- consistência visual;
- tokens e componentes reutilizados;
- imagens otimizadas quando houver;
- HTML semântico;
- build, lint e testes quando existirem.
