# Locais — Complexo Helix

O Complexo Helix foi evacuado na noite em que a Amostra 47 escapou. O sobrevivente escolhe quais ambientes investigar, e cada um guarda pistas próprias. Algumas informações só se revelam depois que outra evidência é encontrada.

Os mapas são pixel art 2D em vista de cima (*top-down*), seguindo a [direção de arte dos cenários](DIRECAO_DE_ARTE_CENARIOS_AMOSTRA47.md).

## Ambientes

| # | Local | O que guarda | Personagens | Proposições |
|---|---|---|---|---|
| 1 | [Câmara de contenção](camara-de-contencao/) | O tanque rompido; o setor onde tudo começou | Clara, Amie, Giovani | K, U, T |
| 2 | [Sala de servidores](sala-de-servidores/) | Registros do sistema e comando com conta da direção | Angela | R, S, Z |
| 3 | [Laboratório de análises](laboratorio-de-analises/) | O experimento interrompido | Amie, Fernando, Otávio | P, Q |
| 4 | [Túnel de ventilação](tunel-de-ventilacao/) | Rota de propagação; ordem de manutenção | Beatrice | V |
| 5 | [Central de segurança](central-de-seguranca/) | Câmeras, crachás e relatório de acesso | Giovani, Otávio | W, T |
| 6 | [Sala de evacuação](sala-de-evacuacao/) | Comunicados de emergência e objetos abandonados | Todos | — |

## Estrutura

```
docs/locais/
├── README.md                                ← este índice
├── DIRECAO_DE_ARTE_CENARIOS_AMOSTRA47.md    ← direção de arte (vale para todos os mapas)
└── <local>/
    ├── README.md                            ← descrição do espaço, pistas e papel na prova
    └── mapa.webp                            ← mapa top-down (1254 × 1254)
```

## Fontes

- **Fatos do caso** (função de cada local, evidências e premissas) vêm de [`../caso-amostra47.md`](../caso-amostra47.md).
- **Descrição dos espaços** vem dos mapas.
- Quando o caso não diz em qual sala uma pista é encontrada, a página do local avisa que a ligação ainda precisa ser confirmada.

## Pendências

- Definir em qual local fica cada item investigativo: crachá, pendrive, gravador de áudio, frasco de contenção, relatório de acesso e sensor de pressão.
- Definir quais pistas dependem de outras para serem reveladas.
- Definir pistas de apoio para a Sala de evacuação.
- O terminal central da Central de segurança mostra o logo da Umbrella, de *Resident Evil*. A direção de arte pede inspiração no jogo, mas um logo de marca registrada deve ser trocado por um símbolo próprio do Complexo Helix.
