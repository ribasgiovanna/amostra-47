# Personagens — AMOSTRA 47

Sete funcionários estavam ligados ao Complexo Helix na noite em que a Amostra 47 foi liberada. Cada um fornece uma peça do caso, e nenhuma evidência isolada entrega a solução.

Esta pasta reúne, para cada personagem, a história e o papel na investigação, a ficha visual (`.md`) e o card em pixel art (`.webp`).

## Elenco

| # | Personagem | Função | Papel no caso | Proposições |
|---|---|---|---|---|
| 1 | [Dra. Amie Lin](amie-lin/) | Virologista | Fonte: alerta científico | P |
| 2 | [Giovani Pistori](giovani-pistori/) | Chefe de segurança | Fonte: sem arrombamento → sem invasão | T (≡ ¬A) |
| 3 | [Angela Torres](angela-torres/) | Engenheira de sistemas | Fonte: comando com conta da direção | S |
| 4 | [Dr. Fernando Almeida](fernando-almeida/) ⚠️ | Diretor científico | Responsável (solução do caso) | Q, Y |
| 5 | [Otávio Ferraz](otavio-ferraz/) | Estagiário | Suspeito descartado: álibi confirmado | W, O |
| 6 | [Clara Costa](clara-costa/) | Técnica de contenção | Fonte: alteração na contenção | U |
| 7 | [Beatrice Salles](beatrice-salles/) | Técnica de manutenção | Suspeita descartada: ordem não partiu dela | V, B |

⚠️ A página de Fernando Almeida revela a solução do caso.

## Estrutura

```
docs/personagens/
├── README.md                          ← este índice
├── guia-de-estilo.md   ← guia mestre de pixel art (vale para todos)
└── <personagem>/
    ├── README.md                      ← história, papel na investigação e na prova lógica
    ├── ficha-visual.md                ← especificação visual, paleta, prompts e critérios
    └── ficha-card.webp                ← card: turnaround, retratos, expressões e sprites
```

## Fontes e cânone

- **Fatos narrativos** (nome, função, evidência, papel na prova) vêm de [`../caso-amostra47.md`](../caso-amostra47.md).
- **Aparência** vem das fichas visuais e dos cards, que seguem o [guia de estilo](guia-de-estilo.md).
- **Idades** mostradas nos cards são ilustrativas e não fazem parte do cânone.

## Pendências de arte

- Os cards de Giovani Pistori e Fernando Almeida trazem a afiliação "Complexo Amostra 47"; os demais usam "Complexo Helix", nome do laboratório no caso.
- O guia de estilo ainda não define resolução nativa, grid, pivô nem exportação dos sprites para o jogo.
