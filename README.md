# AMOSTRA 47 — O Início do Fim

> Uma investigação sobre o colapso da humanidade.

Trabalho Prático RA2 — **Detetive** (Equivalência Lógica e Inferência Lógica Aplicadas)
Engenharia de Software · Resolução de Problemas com Lógica Matemática · PUCPR
Prof.ª Maria Angela Roveredo

## Integrantes

| # | Nome completo |
|---|---|
| 1 | Ana Beatriz Patussi Reolon |
| 2 | Ana Clara Ernandes |
| 3 | Emelize Bonfim Mlot |
| 4 | Giovanna Ribas dos Reis |
| 5 | Otavio Brito Fonseca |

Os nomes devem estar exatamente como no grupo DETETIVE do Canvas.

## A história

Há vários anos, o mundo entrou em colapso após a disseminação de um agente biológico desconhecido, a **Amostra 47**. O surto começou no **Complexo Helix**, um laboratório de pesquisa que foi trancado na noite do incidente: ninguém conseguiu fugir, e todos os funcionários morreram.

Anos depois, **Giulia Pistori**, filha do chefe de segurança Giovani Pistori, recebe uma pista: se quiser descobrir o que aconteceu com o pai, precisa ir até o Complexo Helix, onde há indícios de que o surto começou. Indignada e em conflito com o rumo da morte do pai, ela decide investigar.

Os registros indicam que o desastre talvez não tenha sido um acidente: alguém retirou a Amostra 47 da contenção, registros foram apagados e uma mensagem de emergência foi interrompida.

A investigação acontece no presente, nas ruínas do complexo. Durante o jogo, **flashbacks jogáveis** mostram momentos de antes do acidente.

**Missão:** descobrir **quem** foi responsável pelo vazamento, **qual procedimento/item** permitiu a liberação e **em que setor** tudo começou.

### Estrutura em três atos

1. **A descoberta** — Giulia recupera um terminal parcialmente funcional que revela os sete funcionários e os setores em que trabalhavam.
2. **As contradições** — o jogador investiga ambientes, coleta documentos e registros de acesso que confirmam ou eliminam hipóteses.
3. **A reconstrução** — o jogador identifica o responsável, como a amostra foi liberada e onde começou a propagação, com uma acusação compatível com as pistas.

## Personagens

**Protagonista:** Giulia Pistori, filha de Giovani Pistori.

Os sete funcionários abaixo morreram no incidente:

| # | Nome | Função | Papel na investigação |
|---|------|--------|-----------------------|
| 1 | Dra. Amie Lin | Virologista | Alerta científico sobre os riscos de antecipar o experimento |
| 2 | Giovani Pistori | Chefe de segurança | Acessos físicos e interrupção das câmeras |
| 3 | Angela Torres | Engenheira de sistemas | Alterações nos registros e origem de comandos administrativos |
| 4 | Dr. Fernando Almeida | Diretor científico | Associado à decisão de antecipar o experimento |
| 5 | Otávio Ferraz | Estagiário | Álibi a ser confrontado com os registros de acesso |
| 6 | Clara Costa | Técnica de contenção | Documenta a alteração dos parâmetros de contenção |
| 7 | Beatrice Salles | Técnica de manutenção | A ordem de manutenção da ventilação não partiu dela |

Nenhuma evidência isolada entrega a solução: o jogador precisa cruzar pistas, verificar contradições e descartar hipóteses.

História, papel na prova lógica, ficha visual e card de cada personagem: [docs/personagens](docs/personagens/README.md).

## Itens

Crachá de acesso · Pendrive criptografado · Gravador de áudio · Frasco de contenção · Relatório de acesso · Sensor de pressão · Ordem de manutenção da ventilação

O que cada item revela, sua arte e seu papel na prova lógica: [docs/itens](docs/itens/README.md).

## Locais

Câmara de contenção · Sala de servidores · Laboratório de análises · Túnel de ventilação · Central de segurança · Sala de evacuação

Descrição de cada espaço, pistas encontradas nele e mapa: [docs/locais](docs/locais/README.md).

## Caso e prova lógica

O documento completo do caso, com as proposições, as premissas iniciais, o encadeamento da prova e a conclusão final, está em [docs/caso-amostra47.md](docs/caso-amostra47.md).

**Conclusão final:** X ∧ Y ∧ Z ∧ K. Fernando Almeida liberou a Amostra 47 por meio de uma autorização administrativa com a conta da direção, registrada no pendrive criptografado, e tudo começou na Câmara de contenção.

## Entregas

Cada entrega tem sua pasta em [`entregas/`](entregas/README.md).

- [ ] Slides (`.pptx`) em [`entregas/slides/`](entregas/slides/): abertura, equipe, história, personagens, itens, locais, 10 proposições, premissas iniciais, dedução, premissas finais e conclusão
- [ ] Painel (`.pptx`, slide único conforme template) em [`entregas/painel/`](entregas/painel/)
- [ ] Jogo em Python (`.py`) em [`entregas/jogo/`](entregas/jogo/): randomização, pontuação, decisões do jogador e final explícito

## Estrutura do repositório

```
├── README.md
├── docs/
│   ├── caso-amostra47.md       ← história, proposições e prova lógica
│   ├── personagens/            ← guia de estilo + uma pasta por personagem
│   ├── locais/                 ← guia de estilo + prancha + uma pasta por local
│   └── itens/                  ← guia de estilo + uma pasta por item
└── entregas/
    ├── slides/
    ├── painel/
    └── jogo/
```

Padrão de nomes: pastas e arquivos em `minusculas-com-hifen`. Cada pasta de seção tem um `README.md` de índice e um `guia-de-estilo.md`. Cada elemento tem a sua subpasta com um `README.md` e a imagem (`ficha-card.webp`, `mapa.webp` ou `arte.webp`).

## Como executar o jogo

```bash
python entregas/jogo/amostra47.py
```

*(em desenvolvimento)*
