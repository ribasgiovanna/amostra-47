# Especificação dos sprites de jogo

Padrão para os sprites de **parado** e **andando** de todos os personagens, nas direções **frente, lado e costas**. Cada personagem tem o seu prompt em `<personagem>/sprites/PROMPT.md`.

> **Status:** proposta. O guia de estilo ainda não fixava resolução, grid nem pivô; os valores abaixo passam a valer quando o grupo aprovar.

## Formato

| Item | Valor proposto |
|---|---|
| Tamanho de cada quadro | **64 × 64 px** lógicos |
| Altura do personagem | cerca de **56 px**, pés na linha 62 |
| Pivô | centro horizontal, na base dos pés |
| Fundo | **transparente** (PNG) |
| Escala para exibir | só por *nearest-neighbor* (2×, 3×, 4×), nunca suavizado |
| Paleta | a da ficha visual de cada personagem |

## Direções

| Linha | Direção | Observação |
|---|---|---|
| 1 | **Frente** (andando para baixo) | rosto visível |
| 2 | **Lado** (andando para a direita) | o lado esquerdo é gerado espelhando esta linha |
| 3 | **Costas** (andando para cima) | nuca e costas da roupa |

**Cuidado ao espelhar:** detalhes assimétricos trocam de lado (crachá, rádio, headset, mechas de cabelo). Se isso incomodar, gere também a linha "lado esquerdo".

## Animações

| Colunas | Animação | Quadros |
|---|---|---|
| 1–2 | **Parado** | 2 quadros: respiração leve (o tronco sobe 1 px no quadro 2) |
| 3–6 | **Andando** | 4 quadros: passo com a perna da frente → pernas juntas → passo com a outra perna → pernas juntas |

Velocidade sugerida: parado a 2–3 quadros por segundo, andando a 8 quadros por segundo.

## Folha de sprites (sprite sheet)

Uma folha por personagem, com **3 linhas × 6 colunas** de quadros de 64 × 64 px, totalizando **384 × 192 px**:

```
          parado 1  parado 2  andar 1  andar 2  andar 3  andar 4
frente  [        ][        ][       ][       ][       ][       ]
lado    [        ][        ][       ][       ][       ][       ]
costas  [        ][        ][       ][       ][       ][       ]
```

## Arquivos

O **prompt** fica na documentação, em `docs/personagens/<personagem>/sprites/PROMPT.md`.

Os **sprites** ficam no código do jogo, em [`src/jogo/sprites/<personagem>/`](../../src/jogo/sprites/):

| Arquivo | Conteúdo |
|---|---|
| `<nome>-sheet.png` | folha completa 384 × 192 px |
| `parado-frente.png`, `parado-lado.png`, `parado-costas.png` | tiras de parado, 2 quadros (128 × 64 px) |
| `andando-frente.png`, `andando-lado.png`, `andando-costas.png` | tiras de andando, 4 quadros (256 × 64 px) |
| `quadros/` | os 18 quadros soltos, `<direção>-<animação>-<n>.png` |
| `preview-andando.gif` | prévia animada do andar |
| `README.md` | conferência e pendências da folha |

## Como gerar

Geradores de imagem por IA não respeitam grid de pixels com precisão. O caminho mais seguro é:

1. **Anexar o card do personagem** (`ficha-card.webp`) como referência, junto com o prompt.
2. **Gerar uma direção por vez** (frente, depois lado, depois costas), em vez da folha inteira de uma vez.
3. **Limpar em um editor de pixel art** (Aseprite, Piskel ou LibreSprite): reduzir para 64 px de altura por *nearest-neighbor*, remover o fundo, alinhar os pés na mesma linha e montar a folha.
4. **Conferir no tamanho real** (64 px) antes de aprovar.

## Checklist de aprovação

- [ ] Os 18 quadros têm o mesmo tamanho, e os pés estão na mesma linha.
- [ ] Cabelo, roupa, acessórios e cores são iguais em frente, lado e costas.
- [ ] O ciclo de andar fecha: o quadro 4 emenda no quadro 1 sem pulo.
- [ ] O fundo é transparente, sem halo em volta do contorno.
- [ ] O personagem é reconhecível a 64 px pela silhueta.
- [ ] O estilo bate com os cards e os mapas: contorno escuro, sombras em blocos e cores dessaturadas.
