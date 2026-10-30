# AMOSTRA 47 — Ficha visual de Dra. Amie Lin

**Personagem:** Dra. Amie Lin  
**Função:** virologista do Complexo Helix  
**Documento:** especificação visual para geração consistente de pixel art (personagem e card)  
**Versão:** 1.0 — 29/10/2026  
**Estilo obrigatório:** [`guia-de-estilo.md`](../guia-de-estilo.md)  
**Âncora visual de apresentação:** card final de **Amie Lin** usado na conversa (fundo azul-carvão, logo AMOSTRA 47 e painéis de HUD); anexar a imagem à IA durante a geração.

> **Fontes e hierarquia:** (1) roteiro do repositório = fatos narrativos; (2) instruções e imagens da usuária = aparência desejada; (3) card pixel art gerado = interpretação gráfica a validar. **Nunca tratar detalhes inventados pelo gerador (idades numéricas, alturas, biografias adicionais, códigos) como fatos oficiais.**

## 1. Papel no enredo — informação confirmada

Amie é a **virologista responsável pelo estudo da Amostra 47**. Conhecia os riscos do agente, tinha autorização para acessar a câmara de contenção e registrou um **alerta científico contra a antecipação do experimento**. Seu relatório integra as evidências da investigação. O acesso autorizado à câmara não prova participação na liberação.

**Diretriz narrativa:** comunicar preparo técnico, atenção aos protocolos e serenidade diante da pressão. Não retratá-la como responsável pelo incidente apenas por trabalhar diretamente com a amostra.

## 2. Descrição visual — referências e direções aprováveis

### Cabelo e rosto

- **Nacionalidade:** **tailandesa**, conforme definição da criadora do projeto. Retratar uma pessoa específica, sem recorrer a caricaturas étnicas ou a um “rosto tailandês” padronizado.
- **Cabelo:** muito escuro, quase preto, comprido e solto, com leve volume e pontas discretamente onduladas; repartição suave próxima do meio, com mechas frontais.
- **Rosto:** feições adultas suaves, olhos castanhos e levemente amendoados, sobrancelhas definidas e expressão calma/analítica, inspiradas nas referências enviadas. A caracterização deve seguir **os retratos aprovados**, não supostas regras faciais de nacionalidade.
- **Idade:** jovem adulta na arte atual; o número exibido em cards anteriores é **interpretação gráfica, não dado confirmado no enredo**.

### Roupa

- **Peça central:** jaleco de laboratório **branco envelhecido/off-white**, até a região dos joelhos, lapelas e bolsos funcionais, aberto na frente.
- **Por baixo:** blusa preta ou grafite de **gola alta**, ajustada e sem estampas; visual discreto.
- **Parte inferior:** calças escuras de corte reto, com cinto simples; podem conter poucos bolsos utilitários, sem estética militar exagerada.
- **Calçado:** botas pretas de trabalho/laboratório, robustas e sem salto alto chamativo.
- **Mãos:** luvas nitrílicas **azul-acinzentadas** na ficha de trabalho; se a cena exigir mãos sem luvas, manter o mesmo modelo de mãos e proporção.

### Objetos e acessórios

- **Essenciais:** jaleco, crachá do Complexo Helix, prancheta/tablet de pesquisa e luvas nitrílicas na versão de laboratório.
- **Equipamento de contexto:** óculos transparentes de segurança, caneta no bolso e suporte com tubos de amostra **somente no painel de acessórios/ação**, nunca em grande quantidade no sprite principal.
- **Uso correto:** proteção facial apenas quando a atividade exigir; não obscurecer o rosto em todos os retratos.
- **Não acrescentar:** máscara de gás constante, armas, mutações, símbolos místicos, traje antirradiação exagerado ou elementos que pareçam revelar culpa.

## 3. Silhueta e caráter

**Três marcas visuais principais:**

1. Cabelo longo castanho quase preto e expressão serena, com traços fiéis à referência da personagem.
2. Jaleco branco sobre gola alta preta, calça escura e botas pretas.
3. Crachá e pequenos acentos azul-acinzentados das luvas/equipamentos científicos.

Em pé, postura firme e contida, segurando discretamente um tablet ou prancheta. Sua silhueta é vertical e limpa; o jaleco cria duas linhas claras ao redor do torso. Priorizar competência e cautela, não frieza excessiva.

## 4. Paleta orientativa

> Estes HEX são **aproximações de direção de arte**, não extrações colorimétricas precisas das imagens. Usar a referência anexada como guia de tonalidade e contraste.

| Função | Cor | HEX aproximado | Aplicação |
|---|---|---|---|
| Contorno profundo | Azul-carvão | #1B2024 | contorno e oclusão |
| Cabelo — base | Marrom quase preto | #292528 | maior volume do cabelo |
| Cabelo — luz | Castanho acinzentado | #50413D | poucos clusters de brilho |
| Blusa de gola alta | Grafite | #2A2B30 | parte superior |
| Jaleco — sombra | Cinza quente | #9C9A96 | dobras do tecido |
| Jaleco — base | Branco off-white | #D8D6D0 | massa principal |
| Jaleco — luz | Marfim pálido | #EFEBE4 | bordas iluminadas |
| Calça e botas | Preto ardósia | #30343B | parte inferior |
| Luvas | Azul nitrílico dessaturado | #617F9E | acentos controlados |
| Crachá — destaque | Vermelho sinalizado | #923E39 | mínimo detalhe |
| Pele — referência ilustrativa | Ocre médio quente | #B9876A | aproximar do card validado, não padrão étnico |

**Regras de cor:** Dominância de preto/grafite e off-white; azul nitrílico é o único acento visível grande. Evitar pele excessivamente alaranjada, cabelo preto sem leitura e branco estourado.

## 5. Tratamento de pixel art

Além das regras do guia mestre:

- O jaleco precisa manter **bordas quadradas** e volumes resolvidos em 2–4 níveis de valor.
- O cabelo longo deve ser construído em massas claras, não com fios realistas ou brilho fotográfico.
- Traços faciais simplificados em pixels, preservando a identidade do retrato de referência.
- Luvas azuis pouco saturadas; elementos finos como crachá e caneta são indicados por clusters e não por linhas suaves.
- Usar contornos escuros, pixels quadrados nítidos, 2–4 valores por material e silhueta legível em escala pequena.
- O sprite principal e **todos os retratos** devem ter a **mesma técnica de pixel art**; não transformar o retrato ampliado em pintura digital.
- A folha com animações é um **estudo visual**, não sprites prontos para engine até haver grid, alinhamento e transparência verificados.

## 6. Consistência entre vistas

| Elemento | Frente | Perfil | Costas |
|---|---|---|---|
| Cabelo | mechas frontais e comprimento abaixo dos ombros | volume contínuo junto ao pescoço | cabelo longo cobrindo parcialmente costas do jaleco |
| Jaleco | abertura sobre gola alta preta e bolsos | barra e tecido com espessura constante | costura central/recorte coerente e comprimento idêntico |
| Crachá | preso à roupa em posição constante | cordão visível junto ao torso | cordão oculto pela silhueta quando necessário |
| Luvas/Calçado | luvas e botas reconhecíveis | sem trocar a altura das botas | mesma cor e sola de botas |

**Continuidade obrigatória:** não trocar cores, comprimento de roupas, lado do crachá, posição de acessórios ou penteado entre diferentes poses. Conferir especialmente em turnaround e animação.

## 7. Prompt individual — usar JUNTO do guia mestre e imagem-âncora

> **PERSONAGEM: DRA. AMIE LIN.** Virologista tailandesa do Complexo Helix no jogo *Amostra 47 — O Início do Fim*. Criar **sprite individual 2D em pixel art**, corpo inteiro, com o mesmo pixel grid aparente, contorno escuro, proporções estilizadas adultas e sombras em clusters da imagem-âncora aprovada. Mulher jovem adulta de postura calma e analítica, aparência individual baseada nas referências visuais fornecidas, sem estereótipos étnicos. Cabelo muito escuro, longo e solto, com leve volume e mechas frontais. Jaleco de laboratório off-white até os joelhos sobre blusa preta de gola alta, calça escura, cinto discreto e botas pretas de trabalho. Crachá visível, pequenas canetas no bolso, luvas nitrílicas azul-acinzentadas, prancheta/tablet na mão. Paleta dessaturada e industrial. Rosto legível, séria sem parecer ameaçadora. **Não** substituir o jaleco por uniforme militar, não exagerar equipamentos biológicos, não fazer pintura digital ou retrato semi-realista. Não confundir com Clara, Angela ou Fernando.

### 7.1 Prompt complementar — ficha/card no mesmo template de Amie Lin

> **MODO CARD DE PERSONAGEM — AMOSTRA 47.** Use a IMAGEM-ÂNCORA (card de Amie Lin enviado pela usuária) como **referência de layout e estilo**, substituindo somente os conteúdos específicos pelo personagem **DRA. AMIE LIN** e pela descrição do prompt individual acima. Canvas horizontal **na mesma proporção da referência**; fundo azul-carvão quase preto, HUD científico com bordas finas azul-cinza, logo **AMOSTRA 47 / PERSONAGENS** no topo esquerdo, título com nome e função, quadro com idade *somente se definida oficialmente* (caso contrário omitir a idade), função, setor e afiliação Complexo Helix, além de breve texto de papel narrativo sem revelar pistas indevidas. **Manter exatamente a estrutura do card modelo:** sprite grande de corpo inteiro à esquerda; na faixa superior centro: **TURNAROUND** frente/lado/costas/lado; coluna estreita de **PALETA DE CORES**; coluna direita de **DETALHES E ACESSÓRIOS**; faixa horizontal **RETRATOS**; faixa **EXPRESSÕES**; faixa inferior **SPRITES EM JOGO (EXEMPLOS)** com parado/andando/correndo/agachado/interagindo/anotando quando pertinente. Tipografia pixelada clara e legível em português. A **paleta geral e saturação do fundo** não devem mudar entre personagens. Use a ficha para roupas, cabelo e objetos, sem copiar aparência de Amie. **Retratos, figura principal e mini sprites devem ser todos pixel art 2D nítida do mesmo nível de abstração**, nunca fotos ou pintura semirrealista. Caso o gerador não consiga escrever textos pequenos corretamente, refazer as legendas em editor gráfico em vez de inventar palavras.

## 8. Critérios de aprovação específicos

- [ ] Cabelo longo e escuro, sem clarear ou encurtar.
- [ ] Aparência corresponde às referências de Amie, com identidade tailandesa tratada sem caricatura.
- [ ] Jaleco longo off-white **sobre gola alta preta**.
- [ ] Calças e botas escuras de laboratório.
- [ ] Crachá, tablet/prancheta e luvas em azul dessaturado.
- [ ] Expressão calma, observadora e séria, não vilanesca.
- [ ] Traços do rosto e jaleco continuam visivelmente **pixel art 2D**.
- [ ] Corpo inteiro não cortado; turnaround e retratos coerentes entre si.
- [ ] Ficha no template da Amie: mesmo fundo, mesma tipografia, mesmos painéis e mesmo grau de simplificação.
- [ ] Nenhum atributo de biografia foi inventado como fato; itens de contexto permanecem plausíveis para o cargo.

## 9. Limites do documento

Nacionalidade e referências de aparência foram fornecidas pela usuária; profissão, alerta científico e papel na investigação constam do caso. **Idade exata, altura e cor exata dos olhos não foram declaradas como cânone**; os detalhes apresentados em artes geradas são referência visual revisável.

**Status do design:** proposta documentada a partir das instruções e artes produzidas. A aprovação visual final requer comparar com as imagens de referência enviadas pela usuária. Para produção real, especificar depois resolução nativa, grid, alinhamento, pivô, paleta fechada e exportação de PNGs transparentes.
