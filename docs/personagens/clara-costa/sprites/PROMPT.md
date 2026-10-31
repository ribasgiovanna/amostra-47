# Sprites de jogo — Clara Costa

Prompt detalhado para gerar os sprites de **parado** e **andando**, de **frente**, **lado** e **costas**. Formato, tamanhos e checklist geral estão na [especificação dos sprites](../../sprites-especificacao.md).

## Como usar

1. Anexe o card do personagem, [`../ficha-card.webp`](../ficha-card.webp), como referência visual.
2. Cole o **prompt completo** (seção 5). Ele gera a folha inteira de uma vez.
3. Se a folha sair desalinhada ou inconsistente, gere **uma direção por vez** com os prompts da seção 6.
4. Limpe e monte a folha no editor de pixel art, seguindo a especificação, e salve em [`src/jogo/sprites/clara-costa/`](../../../../src/jogo/sprites/clara-costa/) como `clara-sheet.png`.

## 1. Quem é

| | |
|---|---|
| **Função** | Técnica de contenção |
| **Idade** | 21 anos (do card) |
| **Personalidade** | Técnica de contenção. Meticulosa, reservada e cautelosa; foi quem registrou a alteração na pressão da câmara. |
| **Jeito de se mover** | Alerta e autocontrolada. Postura reta, olhar sério e um pouco desconfiado, uma mão sempre perto do cinto ou do comunicador. |

## 2. Silhueta e marcas visuais

- Cabelo **muito longo, vermelho-vinho**, com **franja/faixa frontal loiro-creme**.
- **Visor técnico vermelho-âmbar** apagado na testa, ligado a um **headset preto** sobre a orelha.
- **Blusa preta de gola alta** e mangas compridas.
- **Calça cargo preta larga**, com bolsos grandes, tiras e fivelas; **cinto preto** com ilhoses.
- **Luvas pretas sem dedos**, **coturnos pretos de plataforma grossa** e **crachá**.

## 3. Paleta de cores

Cores da [ficha visual](../ficha-visual.md). São alvos aproximados; o importante é manter o contraste e a baixa saturação.

| Parte | Cor | HEX | Onde usar |
|---|---|---|---|
| Contorno | Azul carvão | `#181D22` | linha externa |
| Preto de tecido | Carvão grafite | `#2C2E32` | blusa e calças |
| Sombra cargo | Preto frio | `#202328` | dobras profundas |
| Luz cargo | Cinza ardósia | `#484B4F` | planos expostos |
| Cabelo — base | Vinho escurecido | `#743B3C` | massa longa |
| Cabelo — sombra | Bordô escuro | `#4E2A2D` | profundidade |
| Mecha clara | Loiro pêssego opaco | `#C9A18A` | faixa frontal |
| Mecha — luz | Areia acinzentada | `#DFC4AF` | clusters mínimos |
| Visor — base | Vermelho ferrugem | `#8A4542` | ponto de foco |
| Metal | Cinza aço | `#74787D` | fivelas e botinas |
| Pele — ilustração | Pêssego dessaturado | `#C79377` | rosto e mãos |
| Crachá | Marfim cinza | `#C7C9C7` | detalhe de identificação |

## 4. Poses

### Parado

| Direção | Como deve ficar |
|---|---|
| **Frente** | De pé, postura reta. Mão direita apoiada perto do cinto; braço esquerdo relaxado. Franja loiro-creme diante do rosto, visor na testa e fone do headset na lateral. Calça larga deixa as pernas com silhueta mais ampla. |
| **Lado** | Perfil virado para a direita. O cabelo longo passa dos ombros e desce pelas costas. Faixa do visor e concha do headset sobre a orelha bem legíveis. Bolsos e cintos da calça com volume. |
| **Costas** | De costas. Cabelo vinho longo cobrindo as costas, com as pontas claras discretas. Arco escuro do headset na mesma posição. Calcanhar e fivelas dos coturnos coerentes. |

### Andando

| Direção | Como deve ficar |
|---|---|
| **Frente** | Passos firmes e cautelosos. A mão direita fica perto do cinto; o outro braço balança pouco. A calça larga balança a cada passo. |
| **Lado** | Passada média e controlada. O cabelo longo balança atrás com um quadro de atraso; os bolsos da calça acompanham o passo. |
| **Costas** | Passos firmes; o cabelo longo balança de um lado para o outro sobre as costas; os coturnos pesados marcam o passo. |

## 5. Prompt completo

> **FOLHA DE SPRITES — CLARA COSTA, TÉCNICA DE CONTENÇÃO DO COMPLEXO HELIX.**
>
> **Estilo:** Pixel art 2D retrô, no mesmo estilo dos cards dos personagens e dos mapas de *Amostra 47*: pixels quadrados nítidos, contorno escuro firme, sombras em blocos (2–4 tons por material), cores dessaturadas, sem antialiasing, sem degradê, sem pintura digital, sem 3D. Proporções adultas estilizadas, cabeça um pouco maior para leitura do rosto, mas **não chibi**. Visão de jogo top-down levemente inclinada (3/4 de cima), igual à dos mapas.
>
> **Personagem:** Técnica de contenção. Meticulosa, reservada e cautelosa; foi quem registrou a alteração na pressão da câmara. Idade: 21 anos (do card). Cabelo muito longo, vermelho-vinho, com franja/faixa frontal loiro-creme. Visor técnico vermelho-âmbar apagado na testa, ligado a um headset preto sobre a orelha. Blusa preta de gola alta e mangas compridas. Calça cargo preta larga, com bolsos grandes, tiras e fivelas; cinto preto com ilhoses. Luvas pretas sem dedos, coturnos pretos de plataforma grossa e crachá.
>
> **Jeito e postura:** Alerta e autocontrolada. Postura reta, olhar sério e um pouco desconfiado, uma mão sempre perto do cinto ou do comunicador.
>
> **Cores (usar exatamente esta paleta, dessaturada):** contorno #181D22; preto de tecido #2C2E32; sombra cargo #202328; luz cargo #484B4F; cabelo — base #743B3C; cabelo — sombra #4E2A2D; mecha clara #C9A18A; mecha — luz #DFC4AF; visor — base #8A4542; metal #74787D; pele — ilustração #C79377; crachá #C7C9C7.
>
> **Layout:** Uma folha de sprites com **3 linhas × 6 colunas**, todos os quadros do mesmo tamanho, personagem centralizado e com os pés na mesma linha de base. Linha 1: **frente** (andando para baixo). Linha 2: **lado**, virado para a **direita**. Linha 3: **costas** (andando para cima). Colunas 1–2: **parado** (no quadro 2 o tronco sobe 1 pixel, como respiração). Colunas 3–6: **andando**, ciclo de 4 quadros: passo com a perna da frente, pernas juntas, passo com a outra perna, pernas juntas; braços balançam em oposição às pernas. Fundo transparente ou cinza neutro liso. Sem cenário, sem texto, sem moldura, sem sombra projetada no chão.
>
> **Poses por linha:**
> - **Linha 1 — de frente.** Parado: De pé, postura reta. Mão direita apoiada perto do cinto; braço esquerdo relaxado. Franja loiro-creme diante do rosto, visor na testa e fone do headset na lateral. Calça larga deixa as pernas com silhueta mais ampla. Andando: Passos firmes e cautelosos. A mão direita fica perto do cinto; o outro braço balança pouco. A calça larga balança a cada passo.
> - **Linha 2 — de lado (virado para a direita).** Parado: Perfil virado para a direita. O cabelo longo passa dos ombros e desce pelas costas. Faixa do visor e concha do headset sobre a orelha bem legíveis. Bolsos e cintos da calça com volume. Andando: Passada média e controlada. O cabelo longo balança atrás com um quadro de atraso; os bolsos da calça acompanham o passo.
> - **Linha 3 — de costas.** Parado: De costas. Cabelo vinho longo cobrindo as costas, com as pontas claras discretas. Arco escuro do headset na mesma posição. Calcanhar e fivelas dos coturnos coerentes. Andando: Passos firmes; o cabelo longo balança de um lado para o outro sobre as costas; os coturnos pesados marcam o passo.
>
> **Consistência:** o mesmo personagem, com a mesma roupa, cabelo, cores e acessórios, nos 18 quadros; acessórios sempre do mesmo lado do corpo.
>
> **Não fazer:** cabelo curto ou preso, rosa-neon, óculos de sol, headset de DJ enorme, armas, equipamento militar pesado. Nada de fotorealismo, pintura digital, 3D, isometria, anime ou chibi.

## 6. Prompts por direção

Use se a folha completa não sair bem. Gere as três tiras e monte a folha depois.

### Frente

> Tira de sprites em pixel art 2D de **Clara Costa**, de frente, com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: De pé, postura reta. Mão direita apoiada perto do cinto; braço esquerdo relaxado. Franja loiro-creme diante do rosto, visor na testa e fone do headset na lateral. Calça larga deixa as pernas com silhueta mais ampla. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passos firmes e cautelosos. A mão direita fica perto do cinto; o outro braço balança pouco. A calça larga balança a cada passo. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

### Lado

> Tira de sprites em pixel art 2D de **Clara Costa**, de lado (virado para a direita), com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: Perfil virado para a direita. O cabelo longo passa dos ombros e desce pelas costas. Faixa do visor e concha do headset sobre a orelha bem legíveis. Bolsos e cintos da calça com volume. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passada média e controlada. O cabelo longo balança atrás com um quadro de atraso; os bolsos da calça acompanham o passo. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

### Costas

> Tira de sprites em pixel art 2D de **Clara Costa**, de costas, com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: De costas. Cabelo vinho longo cobrindo as costas, com as pontas claras discretas. Arco escuro do headset na mesma posição. Calcanhar e fivelas dos coturnos coerentes. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passos firmes; o cabelo longo balança de um lado para o outro sobre as costas; os coturnos pesados marcam o passo. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

## 7. Checklist do personagem

- [ ] As marcas visuais da seção 2 aparecem nas três direções.
- [ ] As cores seguem a paleta da seção 3, sem saturar.
- [ ] O jeito de andar combina com a personalidade (seção 1).
- [ ] Os acessórios ficam sempre do mesmo lado do corpo.
- [ ] Os 18 quadros estão alinhados pelos pés e o ciclo de andar fecha sem pulo.
