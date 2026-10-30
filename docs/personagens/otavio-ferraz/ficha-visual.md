# AMOSTRA 47 — Ficha visual de Otávio Ferraz

**Personagem:** Otávio Ferraz  
**Função:** estagiário do Complexo Helix  
**Documento:** especificação visual para geração consistente de pixel art (personagem e card)  
**Versão:** 1.0 — 29/10/2026  
**Estilo obrigatório:** [`guia-de-estilo.md`](../guia-de-estilo.md)  
**Âncora visual de apresentação:** card final de **Amie Lin** usado na conversa (fundo azul-carvão, logo AMOSTRA 47 e painéis de HUD); anexar a imagem à IA durante a geração.

> **Fontes e hierarquia:** (1) roteiro do repositório = fatos narrativos; (2) instruções e imagens da usuária = aparência desejada; (3) card pixel art gerado = interpretação gráfica a validar. **Nunca tratar detalhes inventados pelo gerador (idades numéricas, alturas, biografias adicionais, códigos) como fatos oficiais.**

## 1. Papel no enredo — informação confirmada

Otávio é o **estagiário** que circulava por vários setores e conhecia a rotina dos pesquisadores. Um registro de acesso levanta suspeitas inicialmente, mas o relatório confirma que **ele deixou o laboratório antes da liberação** da amostra. Seu álibi é verificado pela lógica da investigação.

**Diretriz narrativa:** um jovem atento, curioso e possivelmente ansioso, não um culpado óbvio nem alguém incompetente por ser estagiário.

## 2. Descrição visual — referências e direções aprováveis

### Cabelo e rosto

- **Cabelo:** preto ou castanho quase preto, **curto e muito bagunçado**, volume irregular no topo e franja em tufos.
- **Óculos:** **grandes, quadrados e de armação preta**, essenciais para reconhecimento; lentes podem ter brilho discreto.
- **Rosto:** jovem adulto, formato relativamente estreito/oval, expressão tímida, curiosa e por vezes insegura.
- **Constituição:** corpo mais esguio que Giovani, braços e ombros discretos, postura um pouco fechada.
- **Idade:** jovem adulto; número mostrado no card gerado é apenas escolha ilustrativa.

### Roupa

- **Peça principal:** blazer **azul-marinho médio-escuro** de estudante/estagiário, com lapelas e bolsos simples.
- **Por baixo:** camisa social branca ou cinza muito claro, gola organizada.
- **Gravata:** **vermelho-terracota/avermelhado escuro**, estreita e simples, marca visual central.
- **Parte inferior:** calça social grafite ou preta, cinto escuro.
- **Calçado:** sapatos sociais ou coturnos discretos pretos, conforme sprite aprovado; sem tênis luminosos.

### Objetos e acessórios

- **Essenciais:** óculos grandes, crachá do Complexo Helix, prancheta de anotações ou pasta simples.
- **Opcionais (para card):** bolsa transversal em couro escuro, caderno e caneta; não acumular todos no corpo do sprite.
- **No sprite principal:** segurar prancheta junto ao corpo e uma mão no bolso para reforçar timidez observadora.
- **Não acrescentar:** armas, dispositivos hackers improváveis, uniforme militar, jaleco obrigatório, capuz cobrindo o cabelo ou visual colegial infantil.

## 3. Silhueta e caráter

**Três marcas visuais principais:**

1. Cabelo preto curto, espigado e desalinhado, com óculos quadrados grandes.
2. Blazer azul-marinho, camisa clara e **gravata vermelho queimado**.
3. Crachá e prancheta/pasta; silhueta esguia.

De pé, discreto, ombros ligeiramente para dentro, segurando pasta/prancheta, observando com atenção. Pose jovem, mas não infantil ou chibi; altura relativa pode ser menor que Angela sem criar escalas de grid diferentes.

## 4. Paleta orientativa

> Estes HEX são **aproximações de direção de arte**, não extrações colorimétricas precisas das imagens. Usar a referência anexada como guia de tonalidade e contraste.

| Função | Cor | HEX aproximado | Aplicação |
|---|---|---|---|
| Contorno | Preto azulado | #192027 | borda externa |
| Cabelo | Carvão castanho | #29272A | mechas |
| Cabelo — luz | Cinza ardósia | #535054 | poucos brilhos |
| Blazer — sombra | Azul noite | #24344C | dobras |
| Blazer — base | Azul petróleo discreto | #345273 | peça principal |
| Blazer — luz | Azul dessaturado | #607794 | luzes pontuais |
| Camisa | Branco frio | #DBDCE0 | pescoço e punhos |
| Gravata | Vermelho telha | #943D31 | ponto focal |
| Calça | Grafite | #34353B | pernas |
| Calçado | Preto couro | #20252A | botas/sapatos |
| Pele — ilustração | Bege pêssego | #C9987E | face/mãos |
| Pasta | Marrom escuro | #564438 | acessório |

**Regras de cor:** O blazer azul e gravata telha devem destacar Otávio sem ficar saturados demais; integrar tudo ao fundo azul carvão dos cards. A cor da gravata é o principal acento.

## 5. Tratamento de pixel art

Além das regras do guia mestre:

- Cabelo irregular em grupos de pixels, sem fios realistas.
- Óculos quadrados grandes sempre reconhecíveis até nos retratos reduzidos.
- Gravata em poucos pixels vermelhos, sem brilho plástico.
- A silhueta é adulta compacta, não criança de uniforme escolar.
- Usar contornos escuros, pixels quadrados nítidos, 2–4 valores por material e silhueta legível em escala pequena.
- O sprite principal e **todos os retratos** devem ter a **mesma técnica de pixel art**; não transformar o retrato ampliado em pintura digital.
- A folha com animações é um **estudo visual**, não sprites prontos para engine até haver grid, alinhamento e transparência verificados.

## 6. Consistência entre vistas

| Elemento | Frente | Perfil | Costas |
|---|---|---|---|
| Cabelo | franja irregular e tufos | topo eriçado | nuca curta sem alterar penteado |
| Óculos | dois quadros escuros grandes | haste preta sobre orelha | ausentes somente quando não visíveis |
| Blazer/gravata | gola e gravata telha centradas | lapela e comprimento | costura e comprimento consistentes |
| Crachá/pasta | posição constante e pasta em uma mão | volume da pasta | cordão e alças coerentes |

**Continuidade obrigatória:** não trocar cores, comprimento de roupas, lado do crachá, posição de acessórios ou penteado entre diferentes poses. Conferir especialmente em turnaround e animação.

## 7. Prompt individual — usar JUNTO do guia mestre e imagem-âncora

> **PERSONAGEM: OTÁVIO FERRAZ.** Estagiário do Complexo Helix em *Amostra 47*. Criar sprite individual **pixel art 2D adulto estilizado** com grid visível, contorno carvão, sombra em blocos e cores dessaturadas idênticas ao padrão do card Amie Lin. Jovem adulto esguio, cabelo curto preto **bagunçado/eriçado**, óculos grandes quadrados de armação preta e expressão curiosa, tímida, atenta. Vestir **blazer azul-marinho**, camisa social clara e **gravata vermelho queimado**, calça grafite, cinto e calçado preto discreto. Crachá do Complexo Helix, segurando prancheta/pasta. Postura levemente retraída, personagem sempre de corpo inteiro e sem cortes. Não transformar em criança, cosplay escolar infantil, cientista de jaleco ou figura hiper-realista. Não inserir evidências inventadas de culpa.

### 7.1 Prompt complementar — ficha/card no mesmo template de Amie Lin

> **MODO CARD DE PERSONAGEM — AMOSTRA 47.** Use a IMAGEM-ÂNCORA (card de Amie Lin enviado pela usuária) como **referência de layout e estilo**, substituindo somente os conteúdos específicos pelo personagem **OTÁVIO FERRAZ** e pela descrição do prompt individual acima. Canvas horizontal **na mesma proporção da referência**; fundo azul-carvão quase preto, HUD científico com bordas finas azul-cinza, logo **AMOSTRA 47 / PERSONAGENS** no topo esquerdo, título com nome e função, quadro com idade *somente se definida oficialmente* (caso contrário omitir a idade), função, setor e afiliação Complexo Helix, além de breve texto de papel narrativo sem revelar pistas indevidas. **Manter exatamente a estrutura do card modelo:** sprite grande de corpo inteiro à esquerda; na faixa superior centro: **TURNAROUND** frente/lado/costas/lado; coluna estreita de **PALETA DE CORES**; coluna direita de **DETALHES E ACESSÓRIOS**; faixa horizontal **RETRATOS**; faixa **EXPRESSÕES**; faixa inferior **SPRITES EM JOGO (EXEMPLOS)** com parado/andando/correndo/agachado/interagindo/anotando quando pertinente. Tipografia pixelada clara e legível em português. A **paleta geral e saturação do fundo** não devem mudar entre personagens. Use a ficha para roupas, cabelo e objetos, sem copiar aparência de Amie. **Retratos, figura principal e mini sprites devem ser todos pixel art 2D nítida do mesmo nível de abstração**, nunca fotos ou pintura semirrealista. Caso o gerador não consiga escrever textos pequenos corretamente, refazer as legendas em editor gráfico em vez de inventar palavras.

## 8. Critérios de aprovação específicos

- [ ] Cabelo curto preto desgrenhado.
- [ ] Óculos grandes **quadrados pretos**, visíveis em todas as vistas úteis.
- [ ] Blazer azul-marinho, camisa clara e gravata vermelha.
- [ ] Silhueta adulta esguia e comportamento observador.
- [ ] Crachá e prancheta como acessórios principais.
- [ ] Sem armas, jaleco obrigatório ou elementos fantasiosos.
- [ ] Pixel art 2D no mesmo grid visual do card modelo.
- [ ] Corpo inteiro não cortado; turnaround e retratos coerentes entre si.
- [ ] Ficha no template da Amie: mesmo fundo, mesma tipografia, mesmos painéis e mesmo grau de simplificação.
- [ ] Nenhum atributo de biografia foi inventado como fato; itens de contexto permanecem plausíveis para o cargo.

## 9. Limites do documento

O papel de estagiário e o álibi estão no caso. O rosto, o cabelo, os óculos, a roupa e a gravata derivam das duas referências ilustradas enviadas e do card produzido. Idade exata e equipamento específico de trabalho não foram fixados na narrativa.

**Status do design:** proposta documentada a partir das instruções e artes produzidas. A aprovação visual final requer comparar com as imagens de referência enviadas pela usuária. Para produção real, especificar depois resolução nativa, grid, alinhamento, pivô, paleta fechada e exportação de PNGs transparentes.
