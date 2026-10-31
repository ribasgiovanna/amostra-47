# Sprites de jogo — Dr. Fernando Almeida

Prompt detalhado para gerar os sprites de **parado** e **andando**, de **frente**, **lado** e **costas**. Formato, tamanhos e checklist geral estão na [especificação dos sprites](../../sprites-especificacao.md).

## Como usar

1. Anexe o card do personagem, [`../ficha-card.webp`](../ficha-card.webp), como referência visual.
2. Cole o **prompt completo** (seção 5). Ele gera a folha inteira de uma vez.
3. Se a folha sair desalinhada ou inconsistente, gere **uma direção por vez** com os prompts da seção 6.
4. Limpe e monte a folha no editor de pixel art, seguindo a especificação, e salve em [`src/jogo/sprites/fernando-almeida/`](../../../../src/jogo/sprites/fernando-almeida/) como `fernando-sheet.png`.

## 1. Quem é

| | |
|---|---|
| **Função** | Diretor científico |
| **Idade** | 45 anos (do card) |
| **Personalidade** | Diretor científico e herdeiro do Complexo Helix. Em público parece um chefe educado, gentil e um pouco atrapalhado. (O jogador não deve perceber a culpa pela aparência.) |
| **Jeito de se mover** | Cordial e respeitável, levemente desajeitado, como quem vai explicar uma pesquisa e se distrai no meio da fala. Pose aberta e um pouco assimétrica. |

## 2. Silhueta e marcas visuais

- Homem de meia-idade, cabelo **castanho-escuro "old money"**, penteado para trás e para o lado, com ondas leves.
- **Barba e bigode cheios, bem aparados**; **óculos** de armação escura fina.
- **Barriga de chope moderada**, visível também de lado, sem caricatura.
- **Jaleco off-white** até perto dos joelhos sobre **gola alta escura**, que não esconde a barriga.
- **Calça social escura**, cinto clássico, **sapatos pretos**, **crachá** no cordão, **canetas** no bolso do jaleco e **tablet** na mão direita; a mão esquerda no bolso do jaleco.

## 3. Paleta de cores

Cores da [ficha visual](../ficha-visual.md). São alvos aproximados; o importante é manter o contraste e a baixa saturação.

| Parte | Cor | HEX | Onde usar |
|---|---|---|---|
| Contorno | Carvão azulado | `#1D2226` | silhueta |
| Cabelo | Castanho espresso | `#3F332D` | base |
| Luz do cabelo | Castanho noz | `#756153` | volume penteado |
| Barba | Marrom profundo | `#3B302C` | maxilar |
| Jaleco — sombra | Cinza quente | `#A39F9B` | dobras |
| Jaleco — base | Marfim técnico | `#D5D2CA` | peça principal |
| Blusa | Grafite quase preto | `#2B292C` | gola alta |
| Calça | Carvão marrom | `#343238` | pernas |
| Cinto/sapatos | Couro preto | `#252428` | detalhes |
| Pele — ilustração | Bege quente | `#C99576` | rosto/mãos |
| Óculos | Marrom escuro | `#51443E` | armação |
| Detalhe administrativo | Bordô dessaturado | `#88413C` | mínimo acento |

## 4. Poses

### Parado

| Direção | Como deve ficar |
|---|---|
| **Frente** | De pé, ombros levemente inclinados. Tablet na mão direita; mão esquerda no bolso do jaleco. Jaleco aberto mostrando a gola alta e o volume da barriga. Rosto simpático, óculos visíveis. |
| **Lado** | Perfil virado para a direita. A barriga aparece com clareza na silhueta, mas contida. Cabelo penteado para trás e linha do maxilar com barba nítidas. Jaleco do mesmo comprimento da frente. |
| **Costas** | De costas. Nuca curta e alinhada. Jaleco cai naturalmente sobre a cintura, com costura traseira visível. Sapatos sociais pretos. |

### Andando

| Direção | Como deve ficar |
|---|---|
| **Frente** | Passo calmo e um pouco pesado, com um balanço suave do tronco. A mão esquerda continua no bolso; o braço do tablet balança pouco. |
| **Lado** | Passada média e tranquila. A barriga e o jaleco acompanham o passo com um leve balanço. Postura relaxada, nada ameaçadora. |
| **Costas** | Passos lentos e regulares; o jaleco balança suavemente; os ombros se movem pouco. |

## 5. Prompt completo

> **FOLHA DE SPRITES — DR. FERNANDO ALMEIDA, DIRETOR CIENTÍFICO DO COMPLEXO HELIX.**
>
> **Estilo:** Pixel art 2D retrô, no mesmo estilo dos cards dos personagens e dos mapas de *Amostra 47*: pixels quadrados nítidos, contorno escuro firme, sombras em blocos (2–4 tons por material), cores dessaturadas, sem antialiasing, sem degradê, sem pintura digital, sem 3D. Proporções adultas estilizadas, cabeça um pouco maior para leitura do rosto, mas **não chibi**. Visão de jogo top-down levemente inclinada (3/4 de cima), igual à dos mapas.
>
> **Personagem:** Diretor científico e herdeiro do Complexo Helix. Em público parece um chefe educado, gentil e um pouco atrapalhado. (O jogador não deve perceber a culpa pela aparência.) Idade: 45 anos (do card). Homem de meia-idade, cabelo castanho-escuro "old money", penteado para trás e para o lado, com ondas leves. Barba e bigode cheios, bem aparados; óculos de armação escura fina. Barriga de chope moderada, visível também de lado, sem caricatura. Jaleco off-white até perto dos joelhos sobre gola alta escura, que não esconde a barriga. Calça social escura, cinto clássico, sapatos pretos, crachá no cordão, canetas no bolso do jaleco e tablet na mão direita; a mão esquerda no bolso do jaleco.
>
> **Jeito e postura:** Cordial e respeitável, levemente desajeitado, como quem vai explicar uma pesquisa e se distrai no meio da fala. Pose aberta e um pouco assimétrica.
>
> **Cores (usar exatamente esta paleta, dessaturada):** contorno #1D2226; cabelo #3F332D; luz do cabelo #756153; barba #3B302C; jaleco — sombra #A39F9B; jaleco — base #D5D2CA; blusa #2B292C; calça #343238; cinto/sapatos #252428; pele — ilustração #C99576; óculos #51443E; detalhe administrativo #88413C.
>
> **Layout:** Uma folha de sprites com **3 linhas × 6 colunas**, todos os quadros do mesmo tamanho, personagem centralizado e com os pés na mesma linha de base. Linha 1: **frente** (andando para baixo). Linha 2: **lado**, virado para a **direita**. Linha 3: **costas** (andando para cima). Colunas 1–2: **parado** (no quadro 2 o tronco sobe 1 pixel, como respiração). Colunas 3–6: **andando**, ciclo de 4 quadros: passo com a perna da frente, pernas juntas, passo com a outra perna, pernas juntas; braços balançam em oposição às pernas. Fundo transparente ou cinza neutro liso. Sem cenário, sem texto, sem moldura, sem sombra projetada no chão.
>
> **Poses por linha:**
> - **Linha 1 — de frente.** Parado: De pé, ombros levemente inclinados. Tablet na mão direita; mão esquerda no bolso do jaleco. Jaleco aberto mostrando a gola alta e o volume da barriga. Rosto simpático, óculos visíveis. Andando: Passo calmo e um pouco pesado, com um balanço suave do tronco. A mão esquerda continua no bolso; o braço do tablet balança pouco.
> - **Linha 2 — de lado (virado para a direita).** Parado: Perfil virado para a direita. A barriga aparece com clareza na silhueta, mas contida. Cabelo penteado para trás e linha do maxilar com barba nítidas. Jaleco do mesmo comprimento da frente. Andando: Passada média e tranquila. A barriga e o jaleco acompanham o passo com um leve balanço. Postura relaxada, nada ameaçadora.
> - **Linha 3 — de costas.** Parado: De costas. Nuca curta e alinhada. Jaleco cai naturalmente sobre a cintura, com costura traseira visível. Sapatos sociais pretos. Andando: Passos lentos e regulares; o jaleco balança suavemente; os ombros se movem pouco.
>
> **Consistência:** o mesmo personagem, com a mesma roupa, cabelo, cores e acessórios, nos 18 quadros; acessórios sempre do mesmo lado do corpo.
>
> **Não fazer:** traços de vilão, sorriso maligno, olhos brilhantes, seringas ou símbolos ameaçadores, físico atlético, esconder a barriga. Nada de fotorealismo, pintura digital, 3D, isometria, anime ou chibi.

## 6. Prompts por direção

Use se a folha completa não sair bem. Gere as três tiras e monte a folha depois.

### Frente

> Tira de sprites em pixel art 2D de **Dr. Fernando Almeida**, de frente, com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: De pé, ombros levemente inclinados. Tablet na mão direita; mão esquerda no bolso do jaleco. Jaleco aberto mostrando a gola alta e o volume da barriga. Rosto simpático, óculos visíveis. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passo calmo e um pouco pesado, com um balanço suave do tronco. A mão esquerda continua no bolso; o braço do tablet balança pouco. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

### Lado

> Tira de sprites em pixel art 2D de **Dr. Fernando Almeida**, de lado (virado para a direita), com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: Perfil virado para a direita. A barriga aparece com clareza na silhueta, mas contida. Cabelo penteado para trás e linha do maxilar com barba nítidas. Jaleco do mesmo comprimento da frente. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passada média e tranquila. A barriga e o jaleco acompanham o passo com um leve balanço. Postura relaxada, nada ameaçadora. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

### Costas

> Tira de sprites em pixel art 2D de **Dr. Fernando Almeida**, de costas, com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: De costas. Nuca curta e alinhada. Jaleco cai naturalmente sobre a cintura, com costura traseira visível. Sapatos sociais pretos. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passos lentos e regulares; o jaleco balança suavemente; os ombros se movem pouco. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

## 7. Checklist do personagem

- [ ] As marcas visuais da seção 2 aparecem nas três direções.
- [ ] As cores seguem a paleta da seção 3, sem saturar.
- [ ] O jeito de andar combina com a personalidade (seção 1).
- [ ] Os acessórios ficam sempre do mesmo lado do corpo.
- [ ] Os 18 quadros estão alinhados pelos pés e o ciclo de andar fecha sem pulo.
