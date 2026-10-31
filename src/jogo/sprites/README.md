# Sprites dos personagens

Sprites de **parado** e **andando**, de frente, lado e costas, de cada personagem. Formato: quadros de 64 × 64 px, fundo transparente, folha de 3 linhas (frente, lado direito, costas) × 6 colunas (2 de parado + 4 de andando). Detalhes na [especificação dos sprites](../../../docs/personagens/sprites-especificacao.md).

| Personagem | Folha | Situação |
|---|---|---|
| [Giulia Pistori](giulia-pistori/) | `giulia-sheet.png` | ✅ versão 2 |
| [Amie Lin](amie-lin/) | `amie-sheet.png` | ✅ |
| [Angela Torres](angela-torres/) | `angela-sheet.png` | ✅ |
| [Beatrice Salles](beatrice-salles/) | `beatrice-sheet.png` | ✅ versão 2 |
| [Otávio Ferraz](otavio-ferraz/) | `otavio-sheet.png` | ✅ |
| [Fernando Almeida](fernando-almeida/) | `fernando-sheet.png` | ⚠️ falta a barriga e o cabelo penteado |
| [Giovani Pistori](giovani-pistori/) | `giovani-sheet.png` | ⚠️ cabelo longo demais |
| [Clara Costa](clara-costa/) | `clara-sheet.png` | ⚠️ falta o visor |

Cada pasta tem um `README.md` com a conferência e as pendências daquele personagem. Os prompts de geração ficam em `docs/personagens/<personagem>/sprites/PROMPT.md`.

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

Pés na linha 60 em todos os personagens, exceto Amie (59) e Angela (61), que ainda podem ser alinhadas.
