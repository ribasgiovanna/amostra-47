# Sprites — Dr. Fernando Almeida

![Prévia do ciclo de andar: frente. lado e costas](preview-andando.gif)

Sprites de **parado** e **andando**. de frente. lado e costas. no formato da [especificação dos sprites](../../../../docs/personagens/sprites-especificacao.md): quadros de 64 × 64 px e fundo transparente.

| Arquivo | Conteúdo |
|---|---|
| [`fernando-sheet.png`](fernando-sheet.png) | Folha completa. 384 × 192 px (3 linhas × 6 colunas) |
| `parado-frente.png`. `parado-lado.png`. `parado-costas.png` | Tiras de parado. 2 quadros (128 × 64 px) |
| `andando-frente.png`. `andando-lado.png`. `andando-costas.png` | Tiras de andando. 4 quadros (256 × 64 px) |
| `quadros/` | Os 18 quadros soltos. nomeados `<direção>-<animação>-<n>.png` |
| [`preview-andando.gif`](preview-andando.gif) | Prévia animada do ciclo de andar. ampliada 3× |
| [`PROMPT.md`](../../../../docs/personagens/fernando-almeida/sprites/PROMPT.md) | Prompt usado para gerar os sprites (fica em `docs/`) |

## Limpeza aplicada

Cada pixel foi convertido para totalmente opaco ou totalmente transparente (corte em 50% de opacidade). para os sprites ficarem nítidos no jogo. sem halo nas bordas. O desenho não mudou.

## Pendências

O material enviado se apresenta como **primeira versão para teste**. Na conferência:

- **Barriga de chope:** não aparece, nem de frente nem de lado; ele ficou com corpo magro. É uma das três marcas visuais da ficha dele e precisa aparecer **principalmente de lado**.
- **Cabelo:** ficou bagunçado e volumoso. A ficha pede cabelo "old money", **penteado para trás e para o lado**, com volume controlado.
- **Mão no bolso:** a mão esquerda no bolso do jaleco, que faz parte do jeito dele, não está clara.

- A folha usa cerca de 8.218 cores diferentes. Para seguir a regra de paleta limitada do guia de estilo. ela ainda pode ser reduzida para a [paleta do personagem](../../../../docs/personagens/fernando-almeida/sprites/PROMPT.md#3-paleta-de-cores) num editor de pixel art.
