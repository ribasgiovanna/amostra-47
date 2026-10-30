# Itens investigativos — AMOSTRA 47

O caso tem **sete itens investigativos**. Cada um revela uma informação específica e ajuda a confirmar ou eliminar pelo menos uma hipótese. A arte segue o [guia de estilo dos objetos](guia-de-estilo.md).

## Visão geral

| ID | Item | Proposição | Personagem ligado | Local sugerido* |
|---|---|---|---|---|
| OBJ-01 | [Crachá de acesso](cracha-de-acesso/) | — | [Giovani Pistori](../personagens/giovani-pistori/) | [Central de segurança](../locais/central-de-seguranca/) (confirmado) |
| OBJ-02 | [Pendrive criptografado](pendrive-criptografado/) | Z | [Angela Torres](../personagens/angela-torres/) | [Sala de servidores](../locais/sala-de-servidores/) |
| OBJ-03 | [Gravador de áudio](gravador-de-audio/) | Q | [Amie Lin](../personagens/amie-lin/) | [Laboratório de análises](../locais/laboratorio-de-analises/), dentro da bolsa de campo |
| OBJ-04 | [Frasco de contenção](frasco-de-contencao/) | — | [Clara Costa](../personagens/clara-costa/) | [Câmara de contenção](../locais/camara-de-contencao/) |
| OBJ-05 | [Relatório de acesso](relatorio-de-acesso/) | W | [Otávio Ferraz](../personagens/otavio-ferraz/) | [Central de segurança](../locais/central-de-seguranca/) |
| OBJ-06 | [Sensor de pressão](sensor-de-pressao/) | U | [Clara Costa](../personagens/clara-costa/) | [Câmara de contenção](../locais/camara-de-contencao/), dentro da maleta de amostras |
| OBJ-07 | [Ordem de manutenção da ventilação](ordem-de-manutencao/) | V | [Beatrice Salles](../personagens/beatrice-salles/) | [Túnel de ventilação](../locais/tunel-de-ventilacao/) |

\* O caso não define em que sala cada item é encontrado. A coluna mostra a sugestão mais coerente com os mapas, que ainda precisa ser confirmada.

## Itens pessoais

Cada funcionário deixou um item pessoal. Alguns guardam um item investigativo dentro.

| # | Item pessoal | Dona/dono | Onde | Contém |
|---|---|---|---|---|
| 1 | [Bolsa de campo](pessoais/bolsa-de-campo/) | Amie Lin | Laboratório de análises | Gravador de áudio |
| 2 | [Crachá de acesso](cracha-de-acesso/) (frente e verso) | Giovani Pistori | Central de segurança | — (é o próprio OBJ-01) |
| 3 | [Óculos de proteção quebrados](pessoais/oculos-de-protecao/) | Beatrice Salles | Túnel de ventilação (dutos) | — |
| 4 | [Maleta de amostras](pessoais/maleta-de-amostras/) | Clara Costa | Câmara de contenção | Sensor de pressão |
| 5 | [Gravata](pessoais/gravata/) | Otávio Ferraz | Sala de evacuação | — |
| 6 | [Caderno de anotações](pessoais/caderno-de-simbolos/) (**obrigatório**) | Angela Torres | a definir | Dicionário dos símbolos lógicos |
| 7 | [Caderno de Fernando](pessoais/caderno-do-fernando/) ⚠️ | Fernando Almeida | Páginas espalhadas (qualquer local) | Seis páginas de anotações suspeitas |

## Estrutura

```
docs/itens/
├── README.md            ← este índice
├── guia-de-estilo.md    ← guia de arte dos objetos (vale para todos)
├── <item>/
│   ├── README.md        ← o que revela e papel na prova
│   └── arte.webp        ← arte de inspeção/inventário
└── pessoais/<item>/     ← itens pessoais dos funcionários
    ├── README.md
    └── arte-*.webp
```

## Pendências

- Confirmar em que local cada item é encontrado e quais itens só aparecem depois de outros.
- Trocar o símbolo que reproduz o logo da Umbrella (*Resident Evil*) no crachá, na ordem de manutenção e na sinalização por um símbolo próprio do Complexo Helix.
- Produzir as versões de mundo (top-down) e os PNGs transparentes de cada item.
