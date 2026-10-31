# Sprites de jogo — Dra. Amie Lin

Prompt detalhado para gerar os sprites de **parado** e **andando**, de **frente**, **lado** e **costas**. Formato, tamanhos e checklist geral estão na [especificação dos sprites](../../sprites-especificacao.md).

## Como usar

1. Anexe o card do personagem, [`../ficha-card.webp`](../ficha-card.webp), como referência visual.
2. Cole o **prompt completo** (seção 5). Ele gera a folha inteira de uma vez.
3. Se a folha sair desalinhada ou inconsistente, gere **uma direção por vez** com os prompts da seção 6.
4. Limpe e monte a folha no editor de pixel art, seguindo a especificação, e salve em [`src/jogo/sprites/amie-lin/`](../../../../src/jogo/sprites/amie-lin/) como `amie-sheet.png`.

## 1. Quem é

| | |
|---|---|
| **Função** | Virologista |
| **Idade** | 24 anos |
| **Personalidade** | Virologista tailandesa responsável pelo estudo da Amostra 47. Meticulosa, dedicada e séria, mantém a calma mesmo sob pressão. |
| **Jeito de se mover** | Postura ereta e contida, movimentos econômicos e precisos. Parece sempre estar pensando em algo: cabeça levemente baixa, olhar atento. Nunca ameaçadora. |

## 2. Silhueta e marcas visuais

- Cabelo **muito escuro, longo e solto**, abaixo dos ombros, com mechas frontais emoldurando o rosto.
- **Jaleco off-white até os joelhos, aberto**, sobre **blusa preta de gola alta**.
- Calça escura reta, cinto discreto, **botas pretas** de trabalho.
- **Luvas nitrílicas azul-acinzentadas** nas duas mãos: é o único acento de cor grande.
- **Crachá** preso no lado esquerdo do jaleco e **tablet** na mão direita, junto ao corpo.

## 3. Paleta de cores

Cores da [ficha visual](../ficha-visual.md). São alvos aproximados; o importante é manter o contraste e a baixa saturação.

| Parte | Cor | HEX | Onde usar |
|---|---|---|---|
| Contorno profundo | Azul-carvão | `#1B2024` | contorno e oclusão |
| Cabelo — base | Marrom quase preto | `#292528` | maior volume do cabelo |
| Cabelo — luz | Castanho acinzentado | `#50413D` | poucos clusters de brilho |
| Blusa de gola alta | Grafite | `#2A2B30` | parte superior |
| Jaleco — sombra | Cinza quente | `#9C9A96` | dobras do tecido |
| Jaleco — base | Branco off-white | `#D8D6D0` | massa principal |
| Jaleco — luz | Marfim pálido | `#EFEBE4` | bordas iluminadas |
| Calça e botas | Preto ardósia | `#30343B` | parte inferior |
| Luvas | Azul nitrílico dessaturado | `#617F9E` | acentos controlados |
| Crachá — destaque | Vermelho sinalizado | `#923E39` | mínimo detalhe |
| Pele — referência ilustrativa | Ocre médio quente | `#B9876A` | aproximar do card validado, não padrão étnico |

## 4. Poses

### Parado

| Direção | Como deve ficar |
|---|---|
| **Frente** | De pé, pés juntos na largura do quadril, peso distribuído. Tablet seguro na mão direita, encostado na lateral da coxa; braço esquerdo relaxado ao longo do corpo. Jaleco aberto mostrando a gola alta preta e os bolsos. Mechas do cabelo caindo dos dois lados do rosto. Expressão neutra e concentrada. |
| **Lado** | Perfil virado para a direita. Tablet junto ao corpo, visível na frente da coxa. Cabelo longo forma um volume contínuo da cabeça até abaixo dos ombros, cobrindo a nuca. A barra do jaleco cai até os joelhos com a mesma espessura em toda a peça. |
| **Costas** | De costas. O cabelo longo e escuro cobre parte das costas do jaleco. Costura central do jaleco visível. Botas pretas com a mesma sola da vista de frente. O tablet aparece só como uma borda na lateral, se o ângulo permitir. |

### Andando

| Direção | Como deve ficar |
|---|---|
| **Frente** | Passos curtos e regulares. O braço esquerdo balança pouco; o direito segura o tablet e quase não se mexe. A barra do jaleco abre e fecha levemente a cada passo, mostrando as pernas escuras. |
| **Lado** | Passada curta e firme, tronco reto. A barra do jaleco balança atrás das pernas. O cabelo balança pouco, acompanhando o passo com um quadro de atraso. |
| **Costas** | Passos regulares; o cabelo balança suavemente sobre as costas do jaleco; a barra do jaleco alterna de lado a cada passo. |

## 5. Prompt completo

> **FOLHA DE SPRITES — DRA. AMIE LIN, VIROLOGISTA DO COMPLEXO HELIX.**
>
> **Estilo:** Pixel art 2D retrô, no mesmo estilo dos cards dos personagens e dos mapas de *Amostra 47*: pixels quadrados nítidos, contorno escuro firme, sombras em blocos (2–4 tons por material), cores dessaturadas, sem antialiasing, sem degradê, sem pintura digital, sem 3D. Proporções adultas estilizadas, cabeça um pouco maior para leitura do rosto, mas **não chibi**. Visão de jogo top-down levemente inclinada (3/4 de cima), igual à dos mapas.
>
> **Personagem:** Virologista tailandesa responsável pelo estudo da Amostra 47. Meticulosa, dedicada e séria, mantém a calma mesmo sob pressão. Idade: 24 anos. Cabelo muito escuro, longo e solto, abaixo dos ombros, com mechas frontais emoldurando o rosto. Jaleco off-white até os joelhos, aberto, sobre blusa preta de gola alta. Calça escura reta, cinto discreto, botas pretas de trabalho. Luvas nitrílicas azul-acinzentadas nas duas mãos: é o único acento de cor grande. Crachá preso no lado esquerdo do jaleco e tablet na mão direita, junto ao corpo.
>
> **Jeito e postura:** Postura ereta e contida, movimentos econômicos e precisos. Parece sempre estar pensando em algo: cabeça levemente baixa, olhar atento. Nunca ameaçadora.
>
> **Cores (usar exatamente esta paleta, dessaturada):** contorno profundo #1B2024; cabelo — base #292528; cabelo — luz #50413D; blusa de gola alta #2A2B30; jaleco — sombra #9C9A96; jaleco — base #D8D6D0; jaleco — luz #EFEBE4; calça e botas #30343B; luvas #617F9E; crachá — destaque #923E39; pele — referência ilustrativa #B9876A.
>
> **Layout:** Uma folha de sprites com **3 linhas × 6 colunas**, todos os quadros do mesmo tamanho, personagem centralizado e com os pés na mesma linha de base. Linha 1: **frente** (andando para baixo). Linha 2: **lado**, virado para a **direita**. Linha 3: **costas** (andando para cima). Colunas 1–2: **parado** (no quadro 2 o tronco sobe 1 pixel, como respiração). Colunas 3–6: **andando**, ciclo de 4 quadros: passo com a perna da frente, pernas juntas, passo com a outra perna, pernas juntas; braços balançam em oposição às pernas. Fundo transparente ou cinza neutro liso. Sem cenário, sem texto, sem moldura, sem sombra projetada no chão.
>
> **Poses por linha:**
> - **Linha 1 — de frente.** Parado: De pé, pés juntos na largura do quadril, peso distribuído. Tablet seguro na mão direita, encostado na lateral da coxa; braço esquerdo relaxado ao longo do corpo. Jaleco aberto mostrando a gola alta preta e os bolsos. Mechas do cabelo caindo dos dois lados do rosto. Expressão neutra e concentrada. Andando: Passos curtos e regulares. O braço esquerdo balança pouco; o direito segura o tablet e quase não se mexe. A barra do jaleco abre e fecha levemente a cada passo, mostrando as pernas escuras.
> - **Linha 2 — de lado (virado para a direita).** Parado: Perfil virado para a direita. Tablet junto ao corpo, visível na frente da coxa. Cabelo longo forma um volume contínuo da cabeça até abaixo dos ombros, cobrindo a nuca. A barra do jaleco cai até os joelhos com a mesma espessura em toda a peça. Andando: Passada curta e firme, tronco reto. A barra do jaleco balança atrás das pernas. O cabelo balança pouco, acompanhando o passo com um quadro de atraso.
> - **Linha 3 — de costas.** Parado: De costas. O cabelo longo e escuro cobre parte das costas do jaleco. Costura central do jaleco visível. Botas pretas com a mesma sola da vista de frente. O tablet aparece só como uma borda na lateral, se o ângulo permitir. Andando: Passos regulares; o cabelo balança suavemente sobre as costas do jaleco; a barra do jaleco alterna de lado a cada passo.
>
> **Consistência:** o mesmo personagem, com a mesma roupa, cabelo, cores e acessórios, nos 18 quadros; acessórios sempre do mesmo lado do corpo.
>
> **Não fazer:** uniforme militar, máscara de gás, traje antirradiação, estilo anime ou kawaii, caricatura étnica, cabelo curto ou claro. Nada de fotorealismo, pintura digital, 3D, isometria, anime ou chibi.

## 6. Prompts por direção

Use se a folha completa não sair bem. Gere as três tiras e monte a folha depois.

### Frente

> Tira de sprites em pixel art 2D de **Dra. Amie Lin**, de frente, com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: De pé, pés juntos na largura do quadril, peso distribuído. Tablet seguro na mão direita, encostado na lateral da coxa; braço esquerdo relaxado ao longo do corpo. Jaleco aberto mostrando a gola alta preta e os bolsos. Mechas do cabelo caindo dos dois lados do rosto. Expressão neutra e concentrada. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passos curtos e regulares. O braço esquerdo balança pouco; o direito segura o tablet e quase não se mexe. A barra do jaleco abre e fecha levemente a cada passo, mostrando as pernas escuras. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

### Lado

> Tira de sprites em pixel art 2D de **Dra. Amie Lin**, de lado (virado para a direita), com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: Perfil virado para a direita. Tablet junto ao corpo, visível na frente da coxa. Cabelo longo forma um volume contínuo da cabeça até abaixo dos ombros, cobrindo a nuca. A barra do jaleco cai até os joelhos com a mesma espessura em toda a peça. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passada curta e firme, tronco reto. A barra do jaleco balança atrás das pernas. O cabelo balança pouco, acompanhando o passo com um quadro de atraso. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

### Costas

> Tira de sprites em pixel art 2D de **Dra. Amie Lin**, de costas, com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: De costas. O cabelo longo e escuro cobre parte das costas do jaleco. Costura central do jaleco visível. Botas pretas com a mesma sola da vista de frente. O tablet aparece só como uma borda na lateral, se o ângulo permitir. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passos regulares; o cabelo balança suavemente sobre as costas do jaleco; a barra do jaleco alterna de lado a cada passo. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

## 7. Checklist do personagem

- [ ] As marcas visuais da seção 2 aparecem nas três direções.
- [ ] As cores seguem a paleta da seção 3, sem saturar.
- [ ] O jeito de andar combina com a personalidade (seção 1).
- [ ] Os acessórios ficam sempre do mesmo lado do corpo.
- [ ] Os 18 quadros estão alinhados pelos pés e o ciclo de andar fecha sem pulo.
