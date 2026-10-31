# Sprites — Giovani Pistori

![Prévia do ciclo de andar: frente. lado e costas](preview-andando.gif)

Sprites de **parado** e **andando**. de frente. lado e costas. no formato da [especificação dos sprites](../../../../docs/personagens/sprites-especificacao.md): quadros de 64 × 64 px e fundo transparente.

| Arquivo | Conteúdo |
|---|---|
| [`giovani-sheet.png`](giovani-sheet.png) | Folha completa. 384 × 192 px (3 linhas × 6 colunas) |
| `parado-frente.png`. `parado-lado.png`. `parado-costas.png` | Tiras de parado. 2 quadros (128 × 64 px) |
| `andando-frente.png`. `andando-lado.png`. `andando-costas.png` | Tiras de andando. 4 quadros (256 × 64 px) |
| `quadros/` | Os 18 quadros soltos. nomeados `<direção>-<animação>-<n>.png` |
| [`preview-andando.gif`](preview-andando.gif) | Prévia animada do ciclo de andar. ampliada 3× |
| [`PROMPT.md`](../../../../docs/personagens/giovani-pistori/sprites/PROMPT.md) | Prompt usado para gerar os sprites (fica em `docs/`) |

## Limpeza aplicada

Cada pixel foi convertido para totalmente opaco ou totalmente transparente (corte em 50% de opacidade). para os sprites ficarem nítidos no jogo. sem halo nas bordas. O desenho não mudou.

## Pendências

O material enviado se apresenta como **versão 1, não homologada para produção**. Na conferência:

- **Cabelo:** ficou volumoso e bagunçado, médio. A ficha pede cabelo **castanho-escuro curto**, de acabamento simples. Do jeito que está, de frente e de lado ele fica parecido demais com o Fernando.
- **Pernas de frente andando:** nos quadros de andar de frente, as duas pernas quase se fundem numa só.
- **Rádio:** o rádio no peito do colete, uma das marcas dele, quase não aparece.

- A folha usa cerca de 6.684 cores diferentes. Para seguir a regra de paleta limitada do guia de estilo. ela ainda pode ser reduzida para a [paleta do personagem](../../../../docs/personagens/giovani-pistori/sprites/PROMPT.md#3-paleta-de-cores) num editor de pixel art.
