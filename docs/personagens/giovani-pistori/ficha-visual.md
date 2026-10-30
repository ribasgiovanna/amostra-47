# AMOSTRA 47 — Ficha visual de Giovani Pistori

**Personagem:** Giovani Pistori  
**Função:** chefe de segurança do Complexo Helix  
**Documento:** especificação visual para geração consistente de pixel art (personagem e card)  
**Versão:** 1.0 — 29/10/2026  
**Estilo obrigatório:** [`guia-de-estilo.md`](../guia-de-estilo.md)  
**Âncora visual de apresentação:** card final de **Amie Lin** usado na conversa (fundo azul-carvão, logo AMOSTRA 47 e painéis de HUD); anexar a imagem à IA durante a geração.

> **Fontes e hierarquia:** (1) roteiro do repositório = fatos narrativos; (2) instruções e imagens da usuária = aparência desejada; (3) card pixel art gerado = interpretação gráfica a validar. **Nunca tratar detalhes inventados pelo gerador (idades numéricas, alturas, biografias adicionais, códigos) como fatos oficiais.**

## 1. Papel no enredo — informação confirmada

Giovani liderava a **segurança do Complexo Helix**, supervisionando acessos físicos, câmeras e protocolos. Sabe sobre interrupções da vigilância, zonas de acesso e ausência de arrombamento da câmara. Sua atuação ajuda a diferenciar uso de credenciais internas de invasão externa.

**Diretriz narrativa:** personagem confiável enquanto profissional, capaz de transmitir tensão e cansaço sem parecer necessariamente um agressor ou suspeito óbvio.

## 2. Descrição visual — referências e direções aprováveis

### Cabelo e rosto

- **Cabelo:** castanho-escuro, **curto**, com leve textura e acabamento simples de corte masculino; nunca penteado longo.
- **Barba:** barba curta e cheia, aparada de forma prática, conectando maxilar, queixo e bigode.
- **Rosto:** feições adultas marcadas, sobrancelhas definidas e olhar atento; expressão normalmente séria, com variações de alerta e desconfiança.
- **Constituição:** ombros largos, braços fortes, físico atlético e compacto; não exagerar em musculatura de super-herói.
- **Idade:** adulto; número dos cards gerados é apenas indicação ilustrativa.

### Roupa

- **Parte superior:** camiseta preta ou cinza-carvão de manga curta, sem estampa civil visível, sob **colete tático funcional** escuro de segurança privada.
- **Parte inferior:** calças cargo pretas/grafite com bolsos discretos; cinto robusto.
- **Calçado:** coturnos táticos pretos de solado grosso.
- **Detalhes de identificação:** crachá do Complexo Helix preso ao colete ou em cordão curto; marca de setor discreta sem logotipos reais de polícia.
- **Luvas:** opcionais em operação, nunca peça que apague totalmente as mãos na arte principal.

### Objetos e acessórios

- **Essenciais:** rádio comunicador, auricular/escuta, relógio de pulso, crachá.
- **Complementares:** lanterna tática, alças de equipamento e pequeno coldre utilitário **sem arma visível**.
- **Painel de acessórios:** mostrar rádio, fone, lanterna, coturno e relógio como itens individuais.
- **Não acrescentar:** fuzil, pistola, distintivo policial verdadeiro, armadura futurista, máscara, sangue ou aparência de tropa militar de guerra.

## 3. Silhueta e caráter

**Três marcas visuais principais:**

1. Cabelo escuro curto e barba curta aparada, com sobrancelhas/olhar de vigilância.
2. Ombros largos, camiseta preta e colete tático de segurança.
3. Crachá/rádio e coturnos escuros.

Em pé, postura de vigia, ombros firmes e cabeça levemente virada para o lado, como quem observa câmeras e corredores. Mãos relaxadas; em variação, uma mão pode segurar a alça do colete ou rádio.

## 4. Paleta orientativa

> Estes HEX são **aproximações de direção de arte**, não extrações colorimétricas precisas das imagens. Usar a referência anexada como guia de tonalidade e contraste.

| Função | Cor | HEX aproximado | Aplicação |
|---|---|---|---|
| Contorno | Preto azulado | #181C21 | borda externa |
| Camiseta | Carvão | #292B2D | massa superior |
| Colete — sombra | Preto técnico | #1F2529 | bolsos e velcros |
| Colete — luz | Ardósia | #40484D | volumes e costuras |
| Calça cargo | Grafite profundo | #303438 | parte inferior |
| Botas | Preto couro | #222327 | calçado |
| Cabelo e barba | Castanho escuro | #382F2C | cabelo/barba |
| Pele — ilustração | Bege quente contido | #C38F71 | ajustar ao retrato de referência |
| Sombra de pele | Marrom quente | #91674E | volume do rosto |
| Metal/crachá | Cinza aço | #899097 | detalhes pontuais |
| Acento do setor | Vermelho queimado | #8D4640 | sinais mínimos |

**Regras de cor:** Evitar preto puro uniforme: colete, calça e camiseta precisam ter diferentes valores de grafite. Nenhuma saturação militar chamativa ou LEDs neon.

## 5. Tratamento de pixel art

Além das regras do guia mestre:

- Definir barba por clusters escuros, evitando textura de pelos individualizados.
- Colete deve ter bolsos e placas legíveis sem centenas de detalhes.
- Ombros e braços fortes precisam caber no mesmo sistema de proporções adultas estilizadas dos outros personagens.
- Não introduzir arma ou uniformes reais de polícia a partir das fotos referenciais.
- Usar contornos escuros, pixels quadrados nítidos, 2–4 valores por material e silhueta legível em escala pequena.
- O sprite principal e **todos os retratos** devem ter a **mesma técnica de pixel art**; não transformar o retrato ampliado em pintura digital.
- A folha com animações é um **estudo visual**, não sprites prontos para engine até haver grid, alinhamento e transparência verificados.

## 6. Consistência entre vistas

| Elemento | Frente | Perfil | Costas |
|---|---|---|---|
| Cabelo/barba | corte curto e barba uniforme | perfil mostra maxilar e costeleta | nuca curta sem alteração de corte |
| Colete | painel frontal e duas alças | espessura visível | alças e bolsas traseiras coerentes |
| Rádio | preso sempre ao mesmo lado | antena e fio opcionais com proporção estável | posicionamento constante |
| Calça/coturnos | bolsos e solado preto | volume do calçado | barras e bolsos simétricos |

**Continuidade obrigatória:** não trocar cores, comprimento de roupas, lado do crachá, posição de acessórios ou penteado entre diferentes poses. Conferir especialmente em turnaround e animação.

## 7. Prompt individual — usar JUNTO do guia mestre e imagem-âncora

> **PERSONAGEM: GIOVANI PISTORI.** Chefe de segurança do Complexo Helix no jogo *Amostra 47*. Fazer sprite **pixel art 2D nítido e pouco saturado**, corpo inteiro e no estilo do card âncora Amie Lin. Homem adulto, forte e de ombros largos, com cabelo castanho-escuro curto, sobrancelhas marcadas, barba e bigode curtos/aparados, semblante sério e atento. Camiseta grafite de manga curta, colete tático preto funcional com compartimentos discretos, calça cargo grafite, cinto escuro e coturnos pesados. Crachá e rádio bem visíveis, auricular discreto e relógio no pulso; segurar leve a alça do colete. Contorno preto-azulado, iluminação contida, sombra em blocos e pixels quadrados sem antialiasing. Homem da segurança de **laboratório privado**, não policial identificado, não soldado de guerra. Não gerar armas, pose de ataque ou realismo fotográfico.

### 7.1 Prompt complementar — ficha/card no mesmo template de Amie Lin

> **MODO CARD DE PERSONAGEM — AMOSTRA 47.** Use a IMAGEM-ÂNCORA (card de Amie Lin enviado pela usuária) como **referência de layout e estilo**, substituindo somente os conteúdos específicos pelo personagem **GIOVANI PISTORI** e pela descrição do prompt individual acima. Canvas horizontal **na mesma proporção da referência**; fundo azul-carvão quase preto, HUD científico com bordas finas azul-cinza, logo **AMOSTRA 47 / PERSONAGENS** no topo esquerdo, título com nome e função, quadro com idade *somente se definida oficialmente* (caso contrário omitir a idade), função, setor e afiliação Complexo Helix, além de breve texto de papel narrativo sem revelar pistas indevidas. **Manter exatamente a estrutura do card modelo:** sprite grande de corpo inteiro à esquerda; na faixa superior centro: **TURNAROUND** frente/lado/costas/lado; coluna estreita de **PALETA DE CORES**; coluna direita de **DETALHES E ACESSÓRIOS**; faixa horizontal **RETRATOS**; faixa **EXPRESSÕES**; faixa inferior **SPRITES EM JOGO (EXEMPLOS)** com parado/andando/correndo/agachado/interagindo/anotando quando pertinente. Tipografia pixelada clara e legível em português. A **paleta geral e saturação do fundo** não devem mudar entre personagens. Use a ficha para roupas, cabelo e objetos, sem copiar aparência de Amie. **Retratos, figura principal e mini sprites devem ser todos pixel art 2D nítida do mesmo nível de abstração**, nunca fotos ou pintura semirrealista. Caso o gerador não consiga escrever textos pequenos corretamente, refazer as legendas em editor gráfico em vez de inventar palavras.

## 8. Critérios de aprovação específicos

- [ ] Barba curta e cabelo escuro curto de acordo com as referências.
- [ ] Ombros e braços firmes, sem exagero superheroico.
- [ ] Colete tático escuro distinto da camiseta.
- [ ] Crachá e rádio comunicador presentes e legíveis.
- [ ] Calça cargo e coturnos funcionais.
- [ ] Nenhuma arma/desenho de polícia real foi inventado.
- [ ] Expressão de vigilância, não expressão de vilão.
- [ ] Corpo inteiro não cortado; turnaround e retratos coerentes entre si.
- [ ] Ficha no template da Amie: mesmo fundo, mesma tipografia, mesmos painéis e mesmo grau de simplificação.
- [ ] Nenhum atributo de biografia foi inventado como fato; itens de contexto permanecem plausíveis para o cargo.

## 9. Limites do documento

O cargo e envolvimento nos acessos/câmeras vêm do caso. Cabelo, barba e vestuário foram elaborados a partir das três referências fotográficas e do card gerado; idade, altura, nome de corpo policial e treinamento militar **não foram definidos como cânone**.

**Status do design:** proposta documentada a partir das instruções e artes produzidas. A aprovação visual final requer comparar com as imagens de referência enviadas pela usuária. Para produção real, especificar depois resolução nativa, grid, alinhamento, pivô, paleta fechada e exportação de PNGs transparentes.
