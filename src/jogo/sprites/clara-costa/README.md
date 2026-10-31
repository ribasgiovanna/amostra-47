# Sprites — Clara Costa

![Prévia do ciclo de andar: frente. lado e costas](preview-andando.gif)

Sprites de **parado** e **andando**. de frente. lado e costas. no formato da [especificação dos sprites](../../../../docs/personagens/sprites-especificacao.md): quadros de 64 × 64 px e fundo transparente.

| Arquivo | Conteúdo |
|---|---|
| [`clara-sheet.png`](clara-sheet.png) | Folha completa. 384 × 192 px (3 linhas × 6 colunas) |
| `parado-frente.png`. `parado-lado.png`. `parado-costas.png` | Tiras de parado. 2 quadros (128 × 64 px) |
| `andando-frente.png`. `andando-lado.png`. `andando-costas.png` | Tiras de andando. 4 quadros (256 × 64 px) |
| `quadros/` | Os 18 quadros soltos. nomeados `<direção>-<animação>-<n>.png` |
| [`preview-andando.gif`](preview-andando.gif) | Prévia animada do ciclo de andar. ampliada 3× |
| [`PROMPT.md`](../../../../docs/personagens/clara-costa/sprites/PROMPT.md) | Prompt usado para gerar os sprites (fica em `docs/`) |

## Limpeza aplicada

Cada pixel foi convertido para totalmente opaco ou totalmente transparente (corte em 50% de opacidade). para os sprites ficarem nítidos no jogo. sem halo nas bordas. O desenho não mudou.

## Pendências

O material enviado se apresenta como **primeira versão**. Na conferência:

- **Bordas:** vieram 19.499 pixels semitransparentes; já foram corrigidos na limpeza.
- **Visor:** o visor técnico vermelho-âmbar na testa, uma das três marcas visuais dela, não aparece; só o headset é visível.
- **Pernas de frente andando:** como nos outros personagens, as duas pernas se fundem em alguns quadros (o próprio README do material cita os quadros 2 e 4).
- **Rosto:** fica muito escuro e pouco legível de frente; vale clarear um pouco a pele e os olhos.

- A folha usa cerca de 9.147 cores diferentes. Para seguir a regra de paleta limitada do guia de estilo. ela ainda pode ser reduzida para a [paleta do personagem](../../../../docs/personagens/clara-costa/sprites/PROMPT.md#3-paleta-de-cores) num editor de pixel art.
