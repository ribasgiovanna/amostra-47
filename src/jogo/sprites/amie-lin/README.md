# Sprites — Dra. Amie Lin

![Prévia do ciclo de andar: frente, lado e costas](preview-andando.gif)

Sprites de **parado** e **andando**, de frente, lado e costas, no formato da [especificação dos sprites](../../../../docs/personagens/sprites-especificacao.md): quadros de 64 × 64 px, fundo transparente e pés alinhados na linha 59.

| Arquivo | Conteúdo |
|---|---|
| [`amie-sheet.png`](amie-sheet.png) | Folha completa, 384 × 192 px (3 linhas × 6 colunas) |
| `parado-frente.png`, `parado-lado.png`, `parado-costas.png` | Tiras de parado, 2 quadros (128 × 64 px) |
| `andando-frente.png`, `andando-lado.png`, `andando-costas.png` | Tiras de andando, 4 quadros (256 × 64 px) |
| `quadros/` | Os 18 quadros soltos, nomeados `<direção>-<animação>-<n>.png` |
| [`preview-andando.gif`](preview-andando.gif) | Prévia animada do ciclo de andar, ampliada 3× |
| [`PROMPT.md`](../../../../docs/personagens/amie-lin/sprites/PROMPT.md) | Prompt usado para gerar os sprites (fica em `docs/`) |

## Limpeza aplicada

Os arquivos originais vieram com as bordas semitransparentes (nenhum pixel era 100% opaco). Para ficarem nítidos no jogo, cada pixel foi convertido para totalmente opaco ou totalmente transparente (corte em 50% de opacidade). O desenho não mudou.

## Pendências

- A folha usa cerca de 7.600 cores diferentes. Para seguir a regra de paleta limitada do guia de estilo, ela ainda pode ser reduzida para a [paleta da Amie](../../../../docs/personagens/amie-lin/sprites/PROMPT.md#3-paleta-de-cores) num editor de pixel art.
