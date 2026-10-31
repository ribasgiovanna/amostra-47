# Sprites de jogo — Otávio Ferraz

Prompt detalhado para gerar os sprites de **parado** e **andando**, de **frente**, **lado** e **costas**. Formato, tamanhos e checklist geral estão na [especificação dos sprites](../../sprites-especificacao.md).

## Como usar

1. Anexe o card do personagem, [`../ficha-card.webp`](../ficha-card.webp), como referência visual.
2. Cole o **prompt completo** (seção 5). Ele gera a folha inteira de uma vez.
3. Se a folha sair desalinhada ou inconsistente, gere **uma direção por vez** com os prompts da seção 6.
4. Limpe e monte a folha no editor de pixel art, seguindo a especificação, e salve em [`src/jogo/sprites/otavio-ferraz/`](../../../../src/jogo/sprites/otavio-ferraz/) como `otavio-sheet.png`.

## 1. Quem é

| | |
|---|---|
| **Função** | Estagiário |
| **Idade** | cerca de 21 anos (do card) |
| **Personalidade** | Estagiário de pesquisa. Curioso, analítico e um pouco ansioso; circula por todos os setores e repara em detalhes. |
| **Jeito de se mover** | Tímido e observador: ombros levemente para dentro, postura um pouco fechada, cabeça curiosa. Jovem adulto, nunca infantil. |

## 2. Silhueta e marcas visuais

- Jovem **esguio**, ombros e braços discretos.
- Cabelo **preto, curto e muito bagunçado**, com tufos no topo e na franja.
- **Óculos grandes, quadrados, de armação preta**: marca principal do rosto.
- **Blazer azul-marinho** sobre **camisa branca** e **gravata estreita vermelho-telha**.
- **Calça grafite**, cinto escuro, **sapatos pretos**, **crachá** e **prancheta** segura junto ao corpo com a mão direita; a mão esquerda no bolso.

## 3. Paleta de cores

Cores da [ficha visual](../ficha-visual.md). São alvos aproximados; o importante é manter o contraste e a baixa saturação.

| Parte | Cor | HEX | Onde usar |
|---|---|---|---|
| Contorno | Preto azulado | `#192027` | borda externa |
| Cabelo | Carvão castanho | `#29272A` | mechas |
| Cabelo — luz | Cinza ardósia | `#535054` | poucos brilhos |
| Blazer — sombra | Azul noite | `#24344C` | dobras |
| Blazer — base | Azul petróleo discreto | `#345273` | peça principal |
| Blazer — luz | Azul dessaturado | `#607794` | luzes pontuais |
| Camisa | Branco frio | `#DBDCE0` | pescoço e punhos |
| Gravata | Vermelho telha | `#943D31` | ponto focal |
| Calça | Grafite | `#34353B` | pernas |
| Calçado | Preto couro | `#20252A` | botas/sapatos |
| Pele — ilustração | Bege pêssego | `#C9987E` | face/mãos |
| Pasta | Marrom escuro | `#564438` | acessório |

## 4. Poses

### Parado

| Direção | Como deve ficar |
|---|---|
| **Frente** | De pé, ombros levemente para dentro. Prancheta junto ao peito na mão direita; mão esquerda no bolso da calça. Gravata vermelha centralizada e bem visível. Óculos grandes refletindo um brilho discreto. |
| **Lado** | Perfil virado para a direita, postura um pouco curvada. Mostra a lapela do blazer, a haste preta dos óculos sobre a orelha e o volume do topo do cabelo. |
| **Costas** | De costas. Nuca curta sem mudar o penteado, tufos visíveis no topo. Costura e comprimento do blazer coerentes com a frente. |

### Andando

| Direção | Como deve ficar |
|---|---|
| **Frente** | Passos curtos e rápidos, um pouco apressados. Cabeça levemente baixa, olhar atento. A prancheta continua junto ao peito. |
| **Lado** | Passada curta, tronco levemente inclinado para a frente, como quem está sempre com pressa. A gravata balança de leve. |
| **Costas** | Passos curtos e rápidos; os ombros sobem e descem um pouco; o cabelo bagunçado quase não muda. |

## 5. Prompt completo

> **FOLHA DE SPRITES — OTÁVIO FERRAZ, ESTAGIÁRIO DO COMPLEXO HELIX.**
>
> **Estilo:** Pixel art 2D retrô, no mesmo estilo dos cards dos personagens e dos mapas de *Amostra 47*: pixels quadrados nítidos, contorno escuro firme, sombras em blocos (2–4 tons por material), cores dessaturadas, sem antialiasing, sem degradê, sem pintura digital, sem 3D. Proporções adultas estilizadas, cabeça um pouco maior para leitura do rosto, mas **não chibi**. Visão de jogo top-down levemente inclinada (3/4 de cima), igual à dos mapas.
>
> **Personagem:** Estagiário de pesquisa. Curioso, analítico e um pouco ansioso; circula por todos os setores e repara em detalhes. Idade: cerca de 21 anos (do card). Jovem esguio, ombros e braços discretos. Cabelo preto, curto e muito bagunçado, com tufos no topo e na franja. Óculos grandes, quadrados, de armação preta: marca principal do rosto. Blazer azul-marinho sobre camisa branca e gravata estreita vermelho-telha. Calça grafite, cinto escuro, sapatos pretos, crachá e prancheta segura junto ao corpo com a mão direita; a mão esquerda no bolso.
>
> **Jeito e postura:** Tímido e observador: ombros levemente para dentro, postura um pouco fechada, cabeça curiosa. Jovem adulto, nunca infantil.
>
> **Cores (usar exatamente esta paleta, dessaturada):** contorno #192027; cabelo #29272A; cabelo — luz #535054; blazer — sombra #24344C; blazer — base #345273; blazer — luz #607794; camisa #DBDCE0; gravata #943D31; calça #34353B; calçado #20252A; pele — ilustração #C9987E; pasta #564438.
>
> **Layout:** Uma folha de sprites com **3 linhas × 6 colunas**, todos os quadros do mesmo tamanho, personagem centralizado e com os pés na mesma linha de base. Linha 1: **frente** (andando para baixo). Linha 2: **lado**, virado para a **direita**. Linha 3: **costas** (andando para cima). Colunas 1–2: **parado** (no quadro 2 o tronco sobe 1 pixel, como respiração). Colunas 3–6: **andando**, ciclo de 4 quadros: passo com a perna da frente, pernas juntas, passo com a outra perna, pernas juntas; braços balançam em oposição às pernas. Fundo transparente ou cinza neutro liso. Sem cenário, sem texto, sem moldura, sem sombra projetada no chão.
>
> **Poses por linha:**
> - **Linha 1 — de frente.** Parado: De pé, ombros levemente para dentro. Prancheta junto ao peito na mão direita; mão esquerda no bolso da calça. Gravata vermelha centralizada e bem visível. Óculos grandes refletindo um brilho discreto. Andando: Passos curtos e rápidos, um pouco apressados. Cabeça levemente baixa, olhar atento. A prancheta continua junto ao peito.
> - **Linha 2 — de lado (virado para a direita).** Parado: Perfil virado para a direita, postura um pouco curvada. Mostra a lapela do blazer, a haste preta dos óculos sobre a orelha e o volume do topo do cabelo. Andando: Passada curta, tronco levemente inclinado para a frente, como quem está sempre com pressa. A gravata balança de leve.
> - **Linha 3 — de costas.** Parado: De costas. Nuca curta sem mudar o penteado, tufos visíveis no topo. Costura e comprimento do blazer coerentes com a frente. Andando: Passos curtos e rápidos; os ombros sobem e descem um pouco; o cabelo bagunçado quase não muda.
>
> **Consistência:** o mesmo personagem, com a mesma roupa, cabelo, cores e acessórios, nos 18 quadros; acessórios sempre do mesmo lado do corpo.
>
> **Não fazer:** visual infantil ou colegial, jaleco, capuz, dispositivos de hacker, armas, uniforme militar. Nada de fotorealismo, pintura digital, 3D, isometria, anime ou chibi.

## 6. Prompts por direção

Use se a folha completa não sair bem. Gere as três tiras e monte a folha depois.

### Frente

> Tira de sprites em pixel art 2D de **Otávio Ferraz**, de frente, com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: De pé, ombros levemente para dentro. Prancheta junto ao peito na mão direita; mão esquerda no bolso da calça. Gravata vermelha centralizada e bem visível. Óculos grandes refletindo um brilho discreto. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passos curtos e rápidos, um pouco apressados. Cabeça levemente baixa, olhar atento. A prancheta continua junto ao peito. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

### Lado

> Tira de sprites em pixel art 2D de **Otávio Ferraz**, de lado (virado para a direita), com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: Perfil virado para a direita, postura um pouco curvada. Mostra a lapela do blazer, a haste preta dos óculos sobre a orelha e o volume do topo do cabelo. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passada curta, tronco levemente inclinado para a frente, como quem está sempre com pressa. A gravata balança de leve. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

### Costas

> Tira de sprites em pixel art 2D de **Otávio Ferraz**, de costas, com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: De costas. Nuca curta sem mudar o penteado, tufos visíveis no topo. Costura e comprimento do blazer coerentes com a frente. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passos curtos e rápidos; os ombros sobem e descem um pouco; o cabelo bagunçado quase não muda. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

## 7. Checklist do personagem

- [ ] As marcas visuais da seção 2 aparecem nas três direções.
- [ ] As cores seguem a paleta da seção 3, sem saturar.
- [ ] O jeito de andar combina com a personalidade (seção 1).
- [ ] Os acessórios ficam sempre do mesmo lado do corpo.
- [ ] Os 18 quadros estão alinhados pelos pés e o ciclo de andar fecha sem pulo.
