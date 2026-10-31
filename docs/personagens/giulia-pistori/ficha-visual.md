# AMOSTRA 47 — Ficha visual de Giulia Pistori

**Personagem:** Giulia Pistori  
**Função:** protagonista; filha de Giovani Pistori  
**Documento:** especificação visual para geração consistente de pixel art (personagem e card)  
**Versão:** 1.0 — 30/10/2026  
**Estilo obrigatório:** [`guia-de-estilo.md`](../guia-de-estilo.md)  
**Âncora visual de apresentação:** card final de **Amie Lin** (fundo azul-carvão, logo AMOSTRA 47 e painéis de HUD); anexar a imagem à IA durante a geração.

> **Fontes e hierarquia:** (1) roteiro do repositório = fatos narrativos; (2) instruções e referências da usuária = aparência desejada (cabelo, rosto e roupa); (3) card pixel art gerado = interpretação gráfica a validar. As fotos de referência são de pessoas reais e servem só como direção de estilo: **a Giulia não deve se parecer com nenhuma pessoa real específica.**

## 1. Papel no enredo — informação confirmada

Giulia é a **protagonista**. Filha de Giovani Pistori, chefe de segurança do Complexo Helix, e de uma estrangeira que sumiu logo depois do nascimento dela. Foi criada pelo pai, com a ajuda de uma vizinha idosa. Anos depois do surto, aos **21 anos**, encontra uma mensagem truncada no computador do pai e vai investigar o complexo por conta própria.

**Diretriz narrativa:** ela não é funcionária do laboratório nem soldada. É uma jovem comum, de fora, que entra num lugar perigoso movida pela indignação e pelo luto. A aparência deve destacá-la do elenco do complexo, que usa jalecos, coletes e uniformes.

## 2. Descrição visual — herança da mãe e do pai

A Giulia mistura os traços dos dois: da **mãe estrangeira** vêm os cachos dourados e as sardas; do **pai** vêm o cabelo escuro na raiz, as sobrancelhas marcadas e o olhar sério e atento.

### Cabelo e rosto

- **Cabelo:** **cacheado e muito volumoso**, cachos pequenos e médios bem definidos, comprimento um pouco abaixo dos ombros, com franja de cachos caindo sobre a testa. Cor **loiro-mel dourado**, com a **raiz um pouco mais escura, castanha** (herança do pai). É a marca principal da silhueta dela. Na foto de infância do crachá do pai, ela já tinha cachos claros.
- **Pele:** morena clara, de tom **dourado e quente**.
- **Sardas:** discretas, no nariz e nas maçãs do rosto (herança da mãe).
- **Sobrancelhas:** **escuras e marcadas**, como as de Giovani.
- **Olhos:** castanho-claros, quase âmbar.
- **Rosto:** traços suaves, lábios cheios, expressão **séria e determinada**, com um fundo de tristeza. Nada de pose de modelo, maquiagem chamativa ou expressão sedutora.
- **Idade:** 21 anos (canônico).

### Roupa (a partir da referência de outfit)

- **Peça central:** **cardigã oversized de tricô grosso marrom-chocolate**, longo até o meio da coxa, com botões escuros, mangas compridas e largas com punho canelado. Usado aberto.
- **Por baixo:** **camiseta preta** justa e lisa.
- **Parte inferior:** **calça jeans wide-leg preta desbotada** (cinza-chumbo), cintura alta, comprimento até o chão.
- **Calçado:** **tênis de lona preto, com faixa lateral branca e sola branca**, sem logotipo de marca.
- **Bolsa:** **ecobag de lona creme** grande, pendurada no ombro.

### Objetos e acessórios

- **Essenciais:** ecobag de lona creme.
- **De história:** o **crachá do pai**, que ela encontra no começo do jogo, pode passar a ficar preso na alça da ecobag.
- **Opcionais:** óculos de sol redondos de armação fina, usados no topo da cabeça (só no card, não nos sprites).
- **Não acrescentar:** jaleco, colete tático, uniforme, armas, piercing ou joias chamativas, maquiagem marcada, logotipos de marcas reais.

## 3. Silhueta e caráter

**Três marcas visuais principais:**

1. **Cachos loiro-mel volumosos**, que formam uma silhueta arredondada e larga na cabeça.
2. **Cardigã marrom oversized** sobre camiseta preta.
3. **Calça wide-leg preta** e **tênis pretos de sola branca**, com a **ecobag creme** no ombro.

Em pé, postura firme e um pouco tensa, uma das mãos no bolso do cardigã ou segurando a alça da ecobag. Passos decididos, olhar atento. A silhueta é casual e urbana, diferente de todos os funcionários do complexo.

## 4. Paleta orientativa

> Estes HEX são **aproximações de direção de arte**. Manter a baixa saturação do jogo; o dourado do cabelo e o creme da bolsa são os pontos de luz.

| Função | Cor | HEX aproximado | Aplicação |
|---|---|---|---|
| Contorno | Carvão | #1E1F22 | linha externa |
| Cabelo — base | Loiro-mel | #C49A5C | massa dos cachos |
| Cabelo — sombra | Castanho dourado | #8A6438 | interior dos cachos |
| Cabelo — luz | Areia dourada | #E2C48E | pontas iluminadas |
| Cabelo — raiz | Castanho escuro | #5A4030 | raiz e sobrancelhas |
| Pele — base | Dourado quente | #C69272 | rosto e mãos |
| Pele — sombra | Marrom quente | #9A6A50 | volume do rosto |
| Sardas | Canela | #8E5A42 | poucos pixels |
| Cardigã — base | Marrom-chocolate | #6B4A36 | peça principal |
| Cardigã — sombra | Marrom profundo | #4A3226 | dobras e punhos |
| Camiseta | Preto | #232326 | parte superior |
| Calça — base | Preto desbotado | #3A3B40 | pernas |
| Calça — luz | Cinza-chumbo | #55575D | vincos |
| Tênis | Preto e branco | #1F1F22 / #E6E3DC | calçado |
| Ecobag | Creme | #E2D8C3 | bolsa |

**Regras de cor:** o marrom do cardigã e o dourado dos cachos dominam; preto embaixo. Evitar loiro-platinado, laranja saturado e pele acinzentada.

## 5. Tratamento de pixel art

- **Cachos:** construídos em blocos arredondados de 2–3 tons, não fio a fio. O volume precisa ser legível mesmo em 64 px.
- **Sardas:** no máximo 2 ou 3 pixels de cada lado do nariz no card; nos sprites podem sumir.
- **Cardigã:** a textura do tricô aparece só com algumas linhas verticais e o punho canelado, sem ruído.
- **Calça:** caimento largo, cobrindo quase todo o tênis; a sola branca precisa aparecer.
- Contorno escuro, pixels quadrados nítidos, 2–4 valores por material, sem antialiasing. Mesmo nível de abstração dos outros personagens.

## 6. Consistência entre vistas

| Elemento | Frente | Perfil | Costas |
|---|---|---|---|
| Cabelo | franja de cachos e volume dos dois lados do rosto | volume arredondado para trás e para cima | massa de cachos cobrindo a nuca e o alto das costas |
| Cardigã | aberto, mostrando a camiseta preta e os botões | comprimento até o meio da coxa, manga larga | costas lisas, barra e punhos iguais |
| Ecobag | alça no ombro direito, bolsa ao lado do quadril | bolsa visível na lateral | alça cruzando o ombro direito |
| Calça e tênis | barra larga até o chão, sola branca | caimento largo | mesma barra e sola |

**Continuidade obrigatória:** a ecobag fica sempre no ombro direito. Não trocar a cor do cabelo, o comprimento do cardigã nem a largura da calça entre as vistas.

## 7. Prompt individual — usar JUNTO do guia mestre e imagem-âncora

> **PERSONAGEM: GIULIA PISTORI.** Protagonista do jogo *Amostra 47 — O Início do Fim*. Criar **sprite individual 2D em pixel art**, corpo inteiro, com o mesmo pixel grid aparente, contorno escuro, proporções adultas estilizadas e sombras em clusters da imagem-âncora aprovada. Mulher de 21 anos, sobrevivente num mundo pós-colapso, que vai investigar o laboratório onde o pai morreu. **Cabelo cacheado muito volumoso, loiro-mel dourado com a raiz um pouco mais escura**, cachos pequenos e médios bem definidos, franja de cachos, comprimento um pouco abaixo dos ombros. Pele morena clara dourada, sardas discretas no nariz, **sobrancelhas escuras e marcadas**, olhos castanho-claros, lábios cheios, expressão séria e determinada. **Cardigã oversized de tricô marrom-chocolate**, longo e aberto, com botões escuros e punhos canelados, sobre **camiseta preta**. **Calça jeans wide-leg preta desbotada** até o chão e **tênis de lona preto com faixa lateral e sola brancas**, sem logotipo. **Ecobag de lona creme** no ombro direito. Paleta dessaturada e quente. Não usar jaleco, uniforme, colete, armas, maquiagem marcada, joias chamativas nem logotipos de marcas. Não se parecer com nenhuma pessoa real. Não fazer pintura digital, 3D, anime ou chibi.

### 7.1 Prompt complementar — ficha/card no mesmo template de Amie Lin

> **MODO CARD DE PERSONAGEM — AMOSTRA 47.** Use a IMAGEM-ÂNCORA (card de Amie Lin) como **referência de layout e estilo**, substituindo só os conteúdos pela personagem **GIULIA PISTORI** descrita acima. Canvas horizontal na mesma proporção; fundo azul-carvão quase preto, HUD com bordas finas azul-cinza, logo **AMOSTRA 47 / PERSONAGENS** no topo esquerdo, título **GIULIA PISTORI — PROTAGONISTA**, quadro com idade **21**, papel **Protagonista**, origem **Filha de Giovani Pistori** e um breve texto: *"Anos depois do surto, encontra uma mensagem truncada no computador do pai e decide descobrir sozinha o que aconteceu no Complexo Helix."* Manter a estrutura do card: sprite grande de corpo inteiro à esquerda; **TURNAROUND** frente/lado/costas/lado; **PALETA DE CORES**; **DETALHES** (cardigã, ecobag, tênis, crachá do pai, óculos de sol); **RETRATOS**; **EXPRESSÕES** (neutra, determinada, desconfiada, triste, surpresa, irritada); **SPRITES EM JOGO** (parada, andando, correndo, agachada, interagindo, examinando item). Tipografia pixelada legível em português. Tudo em pixel art 2D do mesmo nível de abstração, nunca foto ou pintura semirrealista.

## 8. Critérios de aprovação específicos

- [ ] Cachos loiro-mel volumosos, com raiz mais escura, legíveis em todas as vistas.
- [ ] Mistura visível de traços: cachos e sardas da mãe; sobrancelhas escuras e olhar sério do pai.
- [ ] Cardigã marrom oversized aberto sobre camiseta preta.
- [ ] Calça wide-leg preta e tênis pretos de sola branca, sem logotipo.
- [ ] Ecobag creme sempre no ombro direito.
- [ ] Expressão determinada, não sedutora nem de modelo.
- [ ] Não se parece com nenhuma pessoa real específica.
- [ ] Silhueta claramente diferente dos funcionários do complexo.

## 9. Limites do documento

Idade, parentesco e papel na história vêm do repositório. Cabelo, rosto e roupa foram definidos a partir das referências enviadas pela usuária, usadas só como direção de estilo. A herança dos traços (cachos e sardas da mãe; raiz escura, sobrancelhas e olhar do pai) é uma decisão de design deste documento. Cor exata dos olhos e altura não são canônicas. As fotos de referência não fazem parte do repositório.
