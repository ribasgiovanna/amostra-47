# Sprites de jogo — Angela Torres

Prompt detalhado para gerar os sprites de **parado** e **andando**, de **frente**, **lado** e **costas**. Formato, tamanhos e checklist geral estão na [especificação dos sprites](../../sprites-especificacao.md).

## Como usar

1. Anexe o card do personagem, [`../ficha-card.webp`](../ficha-card.webp), como referência visual.
2. Cole o **prompt completo** (seção 5). Ele gera a folha inteira de uma vez.
3. Se a folha sair desalinhada ou inconsistente, gere **uma direção por vez** com os prompts da seção 6.
4. Limpe e monte a folha no editor de pixel art, seguindo a especificação, e salve em [`src/jogo/sprites/angela-torres/`](../../../../src/jogo/sprites/angela-torres/) como `angela-sheet.png`.

## 1. Quem é

| | |
|---|---|
| **Função** | Engenheira de sistemas |
| **Idade** | 38 anos (do card) |
| **Personalidade** | Engenheira de sistemas do complexo. É o lado solar da equipe: simpática, bem-humorada e calorosa, sem perder a autoridade técnica. |
| **Jeito de se mover** | Alta e leve. Postura aberta e convidativa, sorriso fácil. Movimentos soltos e confiantes, sem parecer infantil. |

## 2. Silhueta e marcas visuais

- Mulher **alta e magra**, silhueta alongada, mais velha que as pesquisadoras jovens.
- Cabelo **pixie bem curto**, volumoso e texturizado, **loiro areia acinzentado**.
- **Óculos finos** de aro arredondado e **argolas douradas** pequenas nas orelhas.
- **Jaleco off-white aberto**, com as **mangas dobradas**, sobre **gola alta preta**.
- **Calça cargo verde-oliva escura** folgada, **botas pretas** de sola grossa, **crachá** no cordão central e **tablet** junto ao peito.

## 3. Paleta de cores

Cores da [ficha visual](../ficha-visual.md). São alvos aproximados; o importante é manter o contraste e a baixa saturação.

| Parte | Cor | HEX | Onde usar |
|---|---|---|---|
| Contorno | Azul carvão | `#1B2024` | contorno profundo |
| Cabelo — base | Loiro acinzentado | `#BBA88E` | massa principal |
| Cabelo — sombra | Taupe escuro | `#8A7767` | clusters internos |
| Cabelo — luz | Areia pálido | `#D9CAB4` | poucos realces |
| Óculos | Bronze discreto | `#77634F` | armação e brincos |
| Blusa | Preto grafite | `#27292E` | gola alta |
| Jaleco — sombra | Cinza bege | `#A3A09B` | dobras |
| Jaleco — base | Marfim apagado | `#D8D4CC` | principal |
| Calça cargo | Oliva carvão | `#494B40` | volume principal |
| Botas | Preto frio | `#27282B` | calçado |
| Pele — ilustração | Bege quente suave | `#C79578` | retratos do card |
| Acento de tela | Verde terminal opaco | `#60745E` | somente equipamento |

## 4. Poses

### Parado

| Direção | Como deve ficar |
|---|---|
| **Frente** | De pé, peso levemente numa perna. Tablet abraçado junto ao peito com o braço direito; braço esquerdo relaxado. Sorriso caloroso, óculos e argolas visíveis. Bolsos da calça cargo à mostra. |
| **Lado** | Perfil virado para a direita, silhueta alta e fina. Mostra a nuca curta do pixie, o aro dos óculos e a argola sobrepostos. Jaleco com a barra na mesma altura da vista de frente. |
| **Costas** | De costas. Cabelo curto e texturizado, nunca longo. Costura traseira do jaleco e mangas dobradas coerentes. Calça oliva e botas com o mesmo tom e solado. |

### Andando

| Direção | Como deve ficar |
|---|---|
| **Frente** | Passos longos e leves, com um balanço alegre nos ombros. O braço livre balança solto; o tablet continua junto ao peito. |
| **Lado** | Passada longa, pernas compridas. O jaleco aberto esvoaça um pouco atrás. Cabeça erguida. |
| **Costas** | Passos longos; o jaleco balança de um lado para o outro; o cabelo curto quase não se mexe. |

## 5. Prompt completo

> **FOLHA DE SPRITES — ANGELA TORRES, ENGENHEIRA DE SISTEMAS DO COMPLEXO HELIX.**
>
> **Estilo:** Pixel art 2D retrô, no mesmo estilo dos cards dos personagens e dos mapas de *Amostra 47*: pixels quadrados nítidos, contorno escuro firme, sombras em blocos (2–4 tons por material), cores dessaturadas, sem antialiasing, sem degradê, sem pintura digital, sem 3D. Proporções adultas estilizadas, cabeça um pouco maior para leitura do rosto, mas **não chibi**. Visão de jogo top-down levemente inclinada (3/4 de cima), igual à dos mapas.
>
> **Personagem:** Engenheira de sistemas do complexo. É o lado solar da equipe: simpática, bem-humorada e calorosa, sem perder a autoridade técnica. Idade: 38 anos (do card). Mulher alta e magra, silhueta alongada, mais velha que as pesquisadoras jovens. Cabelo pixie bem curto, volumoso e texturizado, loiro areia acinzentado. Óculos finos de aro arredondado e argolas douradas pequenas nas orelhas. Jaleco off-white aberto, com as mangas dobradas, sobre gola alta preta. Calça cargo verde-oliva escura folgada, botas pretas de sola grossa, crachá no cordão central e tablet junto ao peito.
>
> **Jeito e postura:** Alta e leve. Postura aberta e convidativa, sorriso fácil. Movimentos soltos e confiantes, sem parecer infantil.
>
> **Cores (usar exatamente esta paleta, dessaturada):** contorno #1B2024; cabelo — base #BBA88E; cabelo — sombra #8A7767; cabelo — luz #D9CAB4; óculos #77634F; blusa #27292E; jaleco — sombra #A3A09B; jaleco — base #D8D4CC; calça cargo #494B40; botas #27282B; pele — ilustração #C79578; acento de tela #60745E.
>
> **Layout:** Uma folha de sprites com **3 linhas × 6 colunas**, todos os quadros do mesmo tamanho, personagem centralizado e com os pés na mesma linha de base. Linha 1: **frente** (andando para baixo). Linha 2: **lado**, virado para a **direita**. Linha 3: **costas** (andando para cima). Colunas 1–2: **parado** (no quadro 2 o tronco sobe 1 pixel, como respiração). Colunas 3–6: **andando**, ciclo de 4 quadros: passo com a perna da frente, pernas juntas, passo com a outra perna, pernas juntas; braços balançam em oposição às pernas. Fundo transparente ou cinza neutro liso. Sem cenário, sem texto, sem moldura, sem sombra projetada no chão.
>
> **Poses por linha:**
> - **Linha 1 — de frente.** Parado: De pé, peso levemente numa perna. Tablet abraçado junto ao peito com o braço direito; braço esquerdo relaxado. Sorriso caloroso, óculos e argolas visíveis. Bolsos da calça cargo à mostra. Andando: Passos longos e leves, com um balanço alegre nos ombros. O braço livre balança solto; o tablet continua junto ao peito.
> - **Linha 2 — de lado (virado para a direita).** Parado: Perfil virado para a direita, silhueta alta e fina. Mostra a nuca curta do pixie, o aro dos óculos e a argola sobrepostos. Jaleco com a barra na mesma altura da vista de frente. Andando: Passada longa, pernas compridas. O jaleco aberto esvoaça um pouco atrás. Cabeça erguida.
> - **Linha 3 — de costas.** Parado: De costas. Cabelo curto e texturizado, nunca longo. Costura traseira do jaleco e mangas dobradas coerentes. Calça oliva e botas com o mesmo tom e solado. Andando: Passos longos; o jaleco balança de um lado para o outro; o cabelo curto quase não se mexe.
>
> **Consistência:** o mesmo personagem, com a mesma roupa, cabelo, cores e acessórios, nos 18 quadros; acessórios sempre do mesmo lado do corpo.
>
> **Não fazer:** cabelo médio, longo ou em rabo de cavalo, visual de cirurgiã, cabos saindo do corpo, LEDs exagerados, aparência infantil. Nada de fotorealismo, pintura digital, 3D, isometria, anime ou chibi.

## 6. Prompts por direção

Use se a folha completa não sair bem. Gere as três tiras e monte a folha depois.

### Frente

> Tira de sprites em pixel art 2D de **Angela Torres**, de frente, com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: De pé, peso levemente numa perna. Tablet abraçado junto ao peito com o braço direito; braço esquerdo relaxado. Sorriso caloroso, óculos e argolas visíveis. Bolsos da calça cargo à mostra. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passos longos e leves, com um balanço alegre nos ombros. O braço livre balança solto; o tablet continua junto ao peito. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

### Lado

> Tira de sprites em pixel art 2D de **Angela Torres**, de lado (virado para a direita), com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: Perfil virado para a direita, silhueta alta e fina. Mostra a nuca curta do pixie, o aro dos óculos e a argola sobrepostos. Jaleco com a barra na mesma altura da vista de frente. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passada longa, pernas compridas. O jaleco aberto esvoaça um pouco atrás. Cabeça erguida. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

### Costas

> Tira de sprites em pixel art 2D de **Angela Torres**, de costas, com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: De costas. Cabelo curto e texturizado, nunca longo. Costura traseira do jaleco e mangas dobradas coerentes. Calça oliva e botas com o mesmo tom e solado. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passos longos; o jaleco balança de um lado para o outro; o cabelo curto quase não se mexe. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

## 7. Checklist do personagem

- [ ] As marcas visuais da seção 2 aparecem nas três direções.
- [ ] As cores seguem a paleta da seção 3, sem saturar.
- [ ] O jeito de andar combina com a personalidade (seção 1).
- [ ] Os acessórios ficam sempre do mesmo lado do corpo.
- [ ] Os 18 quadros estão alinhados pelos pés e o ciclo de andar fecha sem pulo.
