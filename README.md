# AMOSTRA 47 — O Início do Fim

> Uma investigação sobre o colapso da humanidade.

Trabalho Prático RA2 — **Detetive** (Equivalência Lógica e Inferência Lógica Aplicadas)
Engenharia de Software · Resolução de Problemas com Lógica Matemática · PUCPR
Prof.ª Maria Angela Roveredo

## A história

Há vários anos, o mundo entrou em colapso após a disseminação de um agente biológico desconhecido, a **Amostra 47**. Durante uma busca por suprimentos, um sobrevivente encontra o **Complexo Helix**, laboratório evacuado na noite em que o surto começou.

Os registros indicam que o desastre talvez não tenha sido um acidente: alguém retirou a Amostra 47 da contenção, registros foram apagados e uma mensagem de emergência foi interrompida.

**Missão:** descobrir **quem** foi responsável pelo vazamento, **qual procedimento/item** permitiu a liberação e **em que setor** tudo começou.

### Estrutura em três atos

1. **A descoberta** — o sobrevivente recupera um terminal parcialmente funcional que revela os sete funcionários e os setores em que trabalhavam.
2. **As contradições** — o jogador investiga ambientes, coleta documentos e registros de acesso que confirmam ou eliminam hipóteses.
3. **A reconstrução** — o jogador identifica o responsável, como a amostra foi liberada e onde começou a propagação, com uma acusação compatível com as pistas.

## Personagens

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

## Itens

Crachá de acesso · Pendrive criptografado · Gravador de áudio · Frasco de contenção · Relatório de acesso · Sensor de pressão

## Locais

Câmara de contenção · Sala de servidores · Laboratório de análises · Túnel de ventilação · Central de segurança · Sala de evacuação

## Caso e prova lógica

O documento completo do caso, com as proposições, as premissas iniciais, o encadeamento da prova e a conclusão final, está em [docs/caso-amostra47.md](docs/caso-amostra47.md).

**Conclusão final:** X ∧ Y ∧ Z ∧ K. Fernando Almeida liberou a Amostra 47 por meio de uma autorização administrativa com a conta da direção, registrada no pendrive criptografado, e tudo começou na Câmara de contenção.

## Entregas

- [ ] Slides (`.pptx`) — abertura, equipe, história, personagens, itens, locais, 10 proposições, premissas iniciais, dedução, premissas finais e conclusão
- [ ] Painel (`.pptx`, slide único conforme template)
- [ ] Jogo em Python (`.py`) — randomização, pontuação, decisões do jogador e final explícito

## Como executar o jogo

```bash
python amostra47.py
```

*(em desenvolvimento)*
