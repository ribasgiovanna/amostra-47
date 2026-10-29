# AMOSTRA 47 — Ficha visual de Clara Costa

**Personagem:** Clara Costa  
**Função:** técnica de contenção do Complexo Helix  
**Documento:** especificação visual para geração consistente de pixel art (personagem e card)  
**Versão:** 1.0 — 29/10/2026  
**Estilo obrigatório:** [`GUIA_ESTILO_SPRITES_AMOSTRA47.md`](../GUIA_ESTILO_SPRITES_AMOSTRA47.md)  
**Âncora visual de apresentação:** card final de **Amie Lin** usado na conversa (fundo azul-carvão, logo AMOSTRA 47 e painéis de HUD); anexar a imagem à IA durante a geração.

> **Fontes e hierarquia:** (1) roteiro do repositório = fatos narrativos; (2) instruções e imagens da usuária = aparência desejada; (3) card pixel art gerado = interpretação gráfica a validar. **Nunca tratar detalhes inventados pelo gerador (idades numéricas, alturas, biografias adicionais, códigos) como fatos oficiais.**

## 1. Papel no enredo — informação confirmada

Clara é a **técnica de contenção** que inspecionava os equipamentos de segurança. Registrou **alterações na pressão e nos parâmetros de contenção** pouco antes do incidente, ajudando a reconstruir a falha na câmara. O documento não estabelece que ela tenha ordenado ou executado a alteração: ela a **detectou e documentou**.

**Diretriz narrativa:** transmitir atenção, disciplina, prudência e familiaridade com procedimentos de risco, sem confundir sua função com segurança armada ou com a virologista Amie.

## 2. Descrição visual — referências e direções aprováveis

### Cabelo e rosto

- **Cabelo:** comprido, cheio e solto, predominância **vermelho-vinho/castanho avermelhado escuro** com faixas/franja frontal **loiro-creme ou pêssego acinzentado**.
- **Textura:** comprimento longo, com camadas suaves; não converter para cabelo curto ou rabo de cavalo.
- **Rosto:** adulto jovem, expressão séria, concentrada e levemente desconfiada; preservar o contraste do cabelo bicolor.
- **Acessório de cabeça:** faixa/visor técnico de lentes **vermelho-âmbar apagado** com headset de comunicação preto; pode ficar na testa, como nas referências, deixando o rosto visível.
- **Idade:** jovem adulta em caráter ilustrativo, sem idade oficial confirmada.

### Roupa

- **Parte superior:** blusa preta/grafite de **gola alta**, mangas longas, silhueta funcional ajustada.
- **Parte inferior:** calça cargo preta **larga**, com bolsos grandes nas laterais, tiras/botões e fivelas discretas.
- **Cinto:** preto com ilhoses/fivela de metal fosco, poucas peças operacionais; não sobrecarregar.
- **Calçado:** coturnos pretos de **sola plataforma robusta** e algumas ferragens cinzas; não salto delicado.
- **Mãos:** luvas pretas sem dedos/tela técnica, com trama simplificada por pixels.
- **Acabamento:** preto industrial gasto; nunca couro plastificado brilhante por toda a roupa.

### Objetos e acessórios

- **Essenciais:** visor/faixa técnico vermelho apagado, headset de comunicação, luvas, cinto e crachá.
- **De contexto:** rádio, pequena maleta de amostras, sensor/terminal portátil e/ou tablet **somente se a ação justificar**.
- **Painel:** visor, headset, luvas, cinto, crachá e coturno como seis itens de apoio, sem desenhar armas.
- **Não acrescentar:** arma de fogo, headset de DJ enorme, óculos de sol permanentes, cabelo rosa-neon, equipamento militar pesado, mutações ou frascos luminosos.

## 3. Silhueta e caráter

**Três marcas visuais principais:**

1. Cabelo **vermelho-vinho longo** com **faixa/franja loiro-creme** frontal.
2. Visor âmbar-vermelho baixo e headset escuro como identidade da função.
3. Roupa preta de gola alta, cargo largo, luvas sem dedos e botas de plataforma.

Em pé, postura alerta e autocontrolada, uma mão próxima ao cinto ou comunicador. Silhueta um pouco mais ampla nas pernas pelos cargos largos, com cabeça e rosto legíveis. A aparência alternativa é funcional, não caricatura cyberpunk.

## 4. Paleta orientativa

> Estes HEX são **aproximações de direção de arte**, não extrações colorimétricas precisas das imagens. Usar a referência anexada como guia de tonalidade e contraste.

| Função | Cor | HEX aproximado | Aplicação |
|---|---|---|---|
| Contorno | Azul carvão | #181D22 | linha externa |
| Preto de tecido | Carvão grafite | #2C2E32 | blusa e calças |
| Sombra cargo | Preto frio | #202328 | dobras profundas |
| Luz cargo | Cinza ardósia | #484B4F | planos expostos |
| Cabelo — base | Vinho escurecido | #743B3C | massa longa |
| Cabelo — sombra | Bordô escuro | #4E2A2D | profundidade |
| Mecha clara | Loiro pêssego opaco | #C9A18A | faixa frontal |
| Mecha — luz | Areia acinzentada | #DFC4AF | clusters mínimos |
| Visor — base | Vermelho ferrugem | #8A4542 | ponto de foco |
| Metal | Cinza aço | #74787D | fivelas e botinas |
| Pele — ilustração | Pêssego dessaturado | #C79377 | rosto e mãos |
| Crachá | Marfim cinza | #C7C9C7 | detalhe de identificação |

**Regras de cor:** **Prioridade do último feedback:** não saturar vermelho do cabelo e visor. Preferir vinho, ferrugem e creme acinzentado. Aplicar o **mesmo color grading azul-carvão frio do card de Amie Lin**, nunca vermelho vivo/coral neon.

## 5. Tratamento de pixel art

Além das regras do guia mestre:

- O rosto e o corpo precisam ser construídos em pixel art 2D legível, **sem retratos semi-realistas**.
- Cabelo bicolor por clusters de cor organizados, sem fio a fio nem brilhos laranja vivos.
- Calça cargo larga e botas plataforma precisam ter contornos quadrados nítidos, sem blur.
- Visor e headset devem permanecer do mesmo lado e na mesma altura nas vistas; não alterar para goggles arredondados de Beatrice.
- Usar contornos escuros, pixels quadrados nítidos, 2–4 valores por material e silhueta legível em escala pequena.
- O sprite principal e **todos os retratos** devem ter a **mesma técnica de pixel art**; não transformar o retrato ampliado em pintura digital.
- A folha com animações é um **estudo visual**, não sprites prontos para engine até haver grid, alinhamento e transparência verificados.

## 6. Consistência entre vistas

| Elemento | Frente | Perfil | Costas |
|---|---|---|---|
| Cabelo | faixa clara diante da face, comprimento longo | mechas longas ultrapassando ombro | vinho longo com pontas claras discretas |
| Visor/headset | visor na testa, fone lateral | faixa e concha sobre o ouvido | arco escuro e posição constante |
| Roupa/cinto | gola alta preta e calça cargo larga | bolsos e cintos com volume | cintos e bolsos sem desaparecer |
| Coturnos | plataforma grossa com peças metálicas | solado espesso | calcanhar e fivelas coerentes |

**Continuidade obrigatória:** não trocar cores, comprimento de roupas, lado do crachá, posição de acessórios ou penteado entre diferentes poses. Conferir especialmente em turnaround e animação.

## 7. Prompt individual — usar JUNTO do guia mestre e imagem-âncora

> **PERSONAGEM: CLARA COSTA.** Técnica de contenção do Complexo Helix em *Amostra 47*. Gerar sprite **pixel art 2D com pixels quadrados visíveis**, aparência de jogo retrô investigativo e o **mesmo template escuro azul-carvão e saturação baixa do card de Amie Lin**. Mulher jovem adulta, cabelo **muito longo em vinho/castanho vermelho apagado**, com **faixa/franja frontal loiro-creme**, expressão séria e observadora. Faixa/visor técnico **vermelho-âmbar dessaturado** sobre a testa conectado a um headset escuro. Blusa preta de gola alta e mangas compridas, **calça cargo preta larga** com bolsos, cinto de trabalho, luvas sem dedos, botas pretas de plataforma grossa com ferragens discretas, crachá. Pose profissional de vigilância de contenção, não militar. **Desaturar vermelhos e pele**; evitar visual laranja, rosa neon, pintura digital, aparência semi-realista ou exagero de acessórios. Manter o corte, roupa e visor consistentes em frente, perfil e costas.

### 7.1 Prompt complementar — ficha/card no mesmo template de Amie Lin

> **MODO CARD DE PERSONAGEM — AMOSTRA 47.** Use a IMAGEM-ÂNCORA (card de Amie Lin enviado pela usuária) como **referência de layout e estilo**, substituindo somente os conteúdos específicos pelo personagem **CLARA COSTA** e pela descrição do prompt individual acima. Canvas horizontal **na mesma proporção da referência**; fundo azul-carvão quase preto, HUD científico com bordas finas azul-cinza, logo **AMOSTRA 47 / PERSONAGENS** no topo esquerdo, título com nome e função, quadro com idade *somente se definida oficialmente* (caso contrário omitir a idade), função, setor e afiliação Complexo Helix, além de breve texto de papel narrativo sem revelar pistas indevidas. **Manter exatamente a estrutura do card modelo:** sprite grande de corpo inteiro à esquerda; na faixa superior centro: **TURNAROUND** frente/lado/costas/lado; coluna estreita de **PALETA DE CORES**; coluna direita de **DETALHES E ACESSÓRIOS**; faixa horizontal **RETRATOS**; faixa **EXPRESSÕES**; faixa inferior **SPRITES EM JOGO (EXEMPLOS)** com parado/andando/correndo/agachado/interagindo/anotando quando pertinente. Tipografia pixelada clara e legível em português. A **paleta geral e saturação do fundo** não devem mudar entre personagens. Use a ficha para roupas, cabelo e objetos, sem copiar aparência de Amie. **Retratos, figura principal e mini sprites devem ser todos pixel art 2D nítida do mesmo nível de abstração**, nunca fotos ou pintura semirrealista. Caso o gerador não consiga escrever textos pequenos corretamente, refazer as legendas em editor gráfico em vez de inventar palavras.

## 8. Critérios de aprovação específicos

- [ ] Vermelho do cabelo é **vinho dessaturado**, não vermelho neon.
- [ ] Faixa/franja **loiro-creme frontal** visível.
- [ ] Cabelo longo e solto em todas as vistas.
- [ ] Visor âmbar-vermelho e headset, não goggles de Beatrice.
- [ ] Gola alta preta, cargo largo, cinto e luvas.
- [ ] Coturnos plataforma e crachá.
- [ ] Fundo e color grading **iguais ao card da Amie**.
- [ ] Expressões, retratos e corpo inteiro em pixel art 2D, sem realismo.
- [ ] Corpo inteiro não cortado; turnaround e retratos coerentes entre si.
- [ ] Ficha no template da Amie: mesmo fundo, mesma tipografia, mesmos painéis e mesmo grau de simplificação.
- [ ] Nenhum atributo de biografia foi inventado como fato; itens de contexto permanecem plausíveis para o cargo.

## 9. Limites do documento

Função e registro de anomalia de contenção vêm do caso. Cabelo, estética alternativa, roupa preta, calça cargo, visor e acessórios vieram das quatro referências da usuária e das versões do card. Idade exata e responsabilidade causal sobre a anomalia não são estabelecidas. **Clara documenta a mudança; não atribuir a ela a autoria sem evidência**.

**Status do design:** proposta documentada a partir das instruções e artes produzidas. A aprovação visual final requer comparar com as imagens de referência enviadas pela usuária. Para produção real, especificar depois resolução nativa, grid, alinhamento, pivô, paleta fechada e exportação de PNGs transparentes.
