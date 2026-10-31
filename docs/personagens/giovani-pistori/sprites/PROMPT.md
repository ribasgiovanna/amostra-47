# Sprites de jogo — Giovani Pistori

Prompt detalhado para gerar os sprites de **parado** e **andando**, de **frente**, **lado** e **costas**. Formato, tamanhos e checklist geral estão na [especificação dos sprites](../../sprites-especificacao.md).

## Como usar

1. Anexe o card do personagem, [`../ficha-card.webp`](../ficha-card.webp), como referência visual.
2. Cole o **prompt completo** (seção 5). Ele gera a folha inteira de uma vez.
3. Se a folha sair desalinhada ou inconsistente, gere **uma direção por vez** com os prompts da seção 6.
4. Limpe e monte a folha no editor de pixel art, seguindo a especificação, e salve em [`src/jogo/sprites/giovani-pistori/`](../../../../src/jogo/sprites/giovani-pistori/) como `giovani-sheet.png`.

## 1. Quem é

| | |
|---|---|
| **Função** | Chefe de segurança |
| **Idade** | 30 anos (do card) |
| **Personalidade** | Chefe de segurança do Complexo Helix e pai solo de Giulia. Disciplinado, observador e direto; carrega cansaço e tensão, mas é confiável. |
| **Jeito de se mover** | Postura de vigia: ombros firmes, peito aberto, cabeça levemente virada como quem observa corredores e câmeras. Movimentos seguros e econômicos, sem nada de agressivo. |

## 2. Silhueta e marcas visuais

- Homem forte, **ombros largos**, físico atlético (sem exagero de super-herói).
- Cabelo **castanho-escuro curto** e **barba curta aparada** unida ao bigode.
- **Camiseta carvão de manga curta** sob **colete tático preto** de segurança privada.
- **Calça cargo grafite**, cinto escuro e **coturnos pretos** pesados.
- **Rádio** preso no lado esquerdo do peito do colete, **auricular** na orelha direita, **relógio** no pulso esquerdo e **crachá** no colete.

## 3. Paleta de cores

Cores da [ficha visual](../ficha-visual.md). São alvos aproximados; o importante é manter o contraste e a baixa saturação.

| Parte | Cor | HEX | Onde usar |
|---|---|---|---|
| Contorno | Preto azulado | `#181C21` | borda externa |
| Camiseta | Carvão | `#292B2D` | massa superior |
| Colete — sombra | Preto técnico | `#1F2529` | bolsos e velcros |
| Colete — luz | Ardósia | `#40484D` | volumes e costuras |
| Calça cargo | Grafite profundo | `#303438` | parte inferior |
| Botas | Preto couro | `#222327` | calçado |
| Cabelo e barba | Castanho escuro | `#382F2C` | cabelo/barba |
| Pele — ilustração | Bege quente contido | `#C38F71` | ajustar ao retrato de referência |
| Sombra de pele | Marrom quente | `#91674E` | volume do rosto |
| Metal/crachá | Cinza aço | `#899097` | detalhes pontuais |
| Acento do setor | Vermelho queimado | `#8D4640` | sinais mínimos |

## 4. Poses

### Parado

| Direção | Como deve ficar |
|---|---|
| **Frente** | De pé, pés afastados na largura dos ombros, peso firme. Mão direita segurando de leve a alça do colete; braço esquerdo relaxado. Rádio e crachá bem visíveis no colete. Cabeça levemente virada, olhar atento. |
| **Lado** | Perfil virado para a direita, peito projetado e ombros largos. Mostra a espessura do colete, o maxilar com barba e a costeleta. Coturnos com solado grosso bem visíveis. |
| **Costas** | De costas, ombros largos. Alças e bolsos traseiros do colete coerentes com a frente. Nuca curta, sem mudar o corte. Bolsos da calça cargo simétricos. |

### Andando

| Direção | Como deve ficar |
|---|---|
| **Frente** | Passos largos e firmes, de quem faz ronda. Braços balançam pouco e de forma controlada. O rádio fica sempre no mesmo lado. |
| **Lado** | Passada longa e pesada, com o calcanhar marcando o chão. Tronco reto, olhar para a frente. Bolsos da calça e alças do colete com leve balanço. |
| **Costas** | Passos firmes e regulares, ombros quase parados. O colete mantém a forma; só os braços e as pernas se movem. |

## 5. Prompt completo

> **FOLHA DE SPRITES — GIOVANI PISTORI, CHEFE DE SEGURANÇA DO COMPLEXO HELIX.**
>
> **Estilo:** Pixel art 2D retrô, no mesmo estilo dos cards dos personagens e dos mapas de *Amostra 47*: pixels quadrados nítidos, contorno escuro firme, sombras em blocos (2–4 tons por material), cores dessaturadas, sem antialiasing, sem degradê, sem pintura digital, sem 3D. Proporções adultas estilizadas, cabeça um pouco maior para leitura do rosto, mas **não chibi**. Visão de jogo top-down levemente inclinada (3/4 de cima), igual à dos mapas.
>
> **Personagem:** Chefe de segurança do Complexo Helix e pai solo de Giulia. Disciplinado, observador e direto; carrega cansaço e tensão, mas é confiável. Idade: 30 anos (do card). Homem forte, ombros largos, físico atlético (sem exagero de super-herói). Cabelo castanho-escuro curto e barba curta aparada unida ao bigode. Camiseta carvão de manga curta sob colete tático preto de segurança privada. Calça cargo grafite, cinto escuro e coturnos pretos pesados. Rádio preso no lado esquerdo do peito do colete, auricular na orelha direita, relógio no pulso esquerdo e crachá no colete.
>
> **Jeito e postura:** Postura de vigia: ombros firmes, peito aberto, cabeça levemente virada como quem observa corredores e câmeras. Movimentos seguros e econômicos, sem nada de agressivo.
>
> **Cores (usar exatamente esta paleta, dessaturada):** contorno #181C21; camiseta #292B2D; colete — sombra #1F2529; colete — luz #40484D; calça cargo #303438; botas #222327; cabelo e barba #382F2C; pele — ilustração #C38F71; sombra de pele #91674E; metal/crachá #899097; acento do setor #8D4640.
>
> **Layout:** Uma folha de sprites com **3 linhas × 6 colunas**, todos os quadros do mesmo tamanho, personagem centralizado e com os pés na mesma linha de base. Linha 1: **frente** (andando para baixo). Linha 2: **lado**, virado para a **direita**. Linha 3: **costas** (andando para cima). Colunas 1–2: **parado** (no quadro 2 o tronco sobe 1 pixel, como respiração). Colunas 3–6: **andando**, ciclo de 4 quadros: passo com a perna da frente, pernas juntas, passo com a outra perna, pernas juntas; braços balançam em oposição às pernas. Fundo transparente ou cinza neutro liso. Sem cenário, sem texto, sem moldura, sem sombra projetada no chão.
>
> **Poses por linha:**
> - **Linha 1 — de frente.** Parado: De pé, pés afastados na largura dos ombros, peso firme. Mão direita segurando de leve a alça do colete; braço esquerdo relaxado. Rádio e crachá bem visíveis no colete. Cabeça levemente virada, olhar atento. Andando: Passos largos e firmes, de quem faz ronda. Braços balançam pouco e de forma controlada. O rádio fica sempre no mesmo lado.
> - **Linha 2 — de lado (virado para a direita).** Parado: Perfil virado para a direita, peito projetado e ombros largos. Mostra a espessura do colete, o maxilar com barba e a costeleta. Coturnos com solado grosso bem visíveis. Andando: Passada longa e pesada, com o calcanhar marcando o chão. Tronco reto, olhar para a frente. Bolsos da calça e alças do colete com leve balanço.
> - **Linha 3 — de costas.** Parado: De costas, ombros largos. Alças e bolsos traseiros do colete coerentes com a frente. Nuca curta, sem mudar o corte. Bolsos da calça cargo simétricos. Andando: Passos firmes e regulares, ombros quase parados. O colete mantém a forma; só os braços e as pernas se movem.
>
> **Consistência:** o mesmo personagem, com a mesma roupa, cabelo, cores e acessórios, nos 18 quadros; acessórios sempre do mesmo lado do corpo.
>
> **Não fazer:** armas, coldre com arma, distintivo de polícia, uniforme militar de guerra, armadura futurista, pose de ataque. Nada de fotorealismo, pintura digital, 3D, isometria, anime ou chibi.

## 6. Prompts por direção

Use se a folha completa não sair bem. Gere as três tiras e monte a folha depois.

### Frente

> Tira de sprites em pixel art 2D de **Giovani Pistori**, de frente, com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: De pé, pés afastados na largura dos ombros, peso firme. Mão direita segurando de leve a alça do colete; braço esquerdo relaxado. Rádio e crachá bem visíveis no colete. Cabeça levemente virada, olhar atento. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passos largos e firmes, de quem faz ronda. Braços balançam pouco e de forma controlada. O rádio fica sempre no mesmo lado. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

### Lado

> Tira de sprites em pixel art 2D de **Giovani Pistori**, de lado (virado para a direita), com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: Perfil virado para a direita, peito projetado e ombros largos. Mostra a espessura do colete, o maxilar com barba e a costeleta. Coturnos com solado grosso bem visíveis. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passada longa e pesada, com o calcanhar marcando o chão. Tronco reto, olhar para a frente. Bolsos da calça e alças do colete com leve balanço. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

### Costas

> Tira de sprites em pixel art 2D de **Giovani Pistori**, de costas, com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: De costas, ombros largos. Alças e bolsos traseiros do colete coerentes com a frente. Nuca curta, sem mudar o corte. Bolsos da calça cargo simétricos. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passos firmes e regulares, ombros quase parados. O colete mantém a forma; só os braços e as pernas se movem. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

## 7. Checklist do personagem

- [ ] As marcas visuais da seção 2 aparecem nas três direções.
- [ ] As cores seguem a paleta da seção 3, sem saturar.
- [ ] O jeito de andar combina com a personalidade (seção 1).
- [ ] Os acessórios ficam sempre do mesmo lado do corpo.
- [ ] Os 18 quadros estão alinhados pelos pés e o ciclo de andar fecha sem pulo.
