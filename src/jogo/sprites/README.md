# Sprites dos personagens

Sprites de **parado** e **andando**, de frente, lado e costas, de cada personagem. Formato: quadros de 64 × 64 px, fundo transparente, folha de 3 linhas (frente, lado direito, costas) × 6 colunas (2 de parado + 4 de andando). Detalhes na [especificação dos sprites](../../../docs/personagens/sprites-especificacao.md).

| Personagem | Folha |
|---|---|
| [Giulia Pistori](giulia-pistori/) | `giulia-sheet.png` |
| [Amie Lin](amie-lin/) | `amie-sheet.png` |
| [Angela Torres](angela-torres/) | `angela-sheet.png` |
| [Beatrice Salles](beatrice-salles/) | `beatrice-sheet.png` |
| [Otávio Ferraz](otavio-ferraz/) | `otavio-sheet.png` |
| [Fernando Almeida](fernando-almeida/) | `fernando-sheet.png` |
| [Giovani Pistori](giovani-pistori/) | `giovani-sheet.png` |
| [Clara Costa](clara-costa/) | `clara-sheet.png` |

Cada pasta tem um `README.md` com os arquivos e a conferência técnica daquele personagem. Os prompts de geração ficam em `docs/personagens/<personagem>/sprites/PROMPT.md`.

## Estrutura

```
src/jogo/sprites/<personagem>/
├── <nome>-sheet.png        ← folha completa (384 × 192 px)
├── parado-frente.png       ← tiras de parado (2 quadros)
├── parado-lado.png
├── parado-costas.png
├── andando-frente.png      ← tiras de andando (4 quadros)
├── andando-lado.png
├── andando-costas.png
├── quadros/                ← os 18 quadros soltos
├── preview-andando.gif     ← prévia animada
└── README.md
```
