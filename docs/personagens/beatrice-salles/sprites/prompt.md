# Sprites de jogo — Beatrice Salles

Prompt detalhado para gerar os sprites de **parado** e **andando**, de **frente**, **lado** e **costas**. Formato, tamanhos e checklist geral estão na [especificação dos sprites](../../sprites-especificacao.md).

## Como usar

1. Anexe o card do personagem, [`../ficha-card.webp`](../ficha-card.webp), como referência visual.
2. Cole o **prompt completo** (seção 5). Ele gera a folha inteira de uma vez.
3. Se a folha sair desalinhada ou inconsistente, gere **uma direção por vez** com os prompts da seção 6.
4. Limpe e monte a folha no editor de pixel art, seguindo a especificação, e salve em [`src/jogo/sprites/beatrice-salles/`](../../../../src/jogo/sprites/beatrice-salles/) como `beatrice-sheet.png`.

## 1. Quem é

| | |
|---|---|
| **Função** | Técnica de manutenção |
| **Idade** | 24 anos (do card) |
| **Personalidade** | Técnica de manutenção. Prática, independente e observadora; parece séria, mas cuida de todos à sua maneira. |
| **Jeito de se mover** | Prática e ágil, com familiaridade de quem trabalha com as mãos. Peso apoiado numa perna, braços relaxados, nada de pose de combate. |

## 2. Silhueta e marcas visuais

- **Goggles circulares de bronze** sempre sobre a cabeça.
- Cabelo **quase preto em rabo de cavalo bagunçado**, com **mechas vermelho-cobre** na nuca e nas pontas.
- **Jardineira curta (short) de veludo cotelê marrom-caramelo**, com bolso frontal, alças largas e barras dobradas, sobre **blusa grafite de manga comprida** arregaçada.
- **Cinto de couro** com bolsas utilitárias, poucas ferramentas e um **frasco transparente** no lado direito.
- **Luvas escuras** de trabalho e **coturnos marrom-escuros** de cano médio e sola grossa.

## 3. Paleta de cores

Cores da [ficha visual](../ficha-visual.md). São alvos aproximados; o importante é manter o contraste e a baixa saturação.

| Parte | Cor | HEX | Onde usar |
|---|---|---|---|
| Contorno profundo | Carvão amarronzado | `#24201F` | bordas externas e oclusão |
| Blusa | Grafite | `#303033` | manga e parte superior interna |
| Sombra da jardineira | Marrom-escuro | `#553824` | dobras profundas do veludo |
| Base da jardineira | Castanho terroso | `#795030` | principal massa de tecido |
| Luz da jardineira | Caramelo envelhecido | `#A16C3D` | faces expostas e costuras |
| Couro das botas e cinto | Espresso | `#3D2925` | acessórios de couro |
| Metal e goggles | Bronze envelhecido | `#B48848` | aro, fivelas e rebites |
| Reflexo metálico | Ouro fosco | `#D0AD70` | pontos de brilho controlados |
| Mecha de cabelo | Vermelho-cobre | `#A04432` | nuca e pontas internas |
| Base do cabelo | Castanho quase preto | `#2B2222` | fios principais |
| Pele ilustrativa (não canônica) | Bege quente | `#C79577` | somente se aprovado |

## 4. Poses

### Parado

| Direção | Como deve ficar |
|---|---|
| **Frente** | De pé, peso apoiado na perna direita. Braços relaxados, mãos com luvas escuras. Dois aros redondos dos goggles visíveis sobre a cabeça. Bolso frontal e as duas alças da jardineira legíveis. |
| **Lado** | Perfil virado para a direita. Rabo de cavalo com fios soltos. Goggles em perspectiva, com a correia. Bolsas e ferramenta do cinto na lateral. Sola grossa dos coturnos. |
| **Costas** | De costas. Mechas cobre visíveis na nuca, rabo volumoso. Correia escura dos goggles sobre o cabelo. Alças da jardineira cruzadas nas costas. Bolsas do cinto na mesma posição. |

### Andando

| Direção | Como deve ficar |
|---|---|
| **Frente** | Passo ágil e decidido. O frasco e as ferramentas do cinto balançam de leve. Braços se movem soltos. |
| **Lado** | Passada rápida e prática. O rabo de cavalo balança atrás; as bolsas do cinto acompanham o passo. |
| **Costas** | Passos rápidos; o rabo de cavalo balança de um lado para o outro; as alças da jardineira se mantêm cruzadas. |

## 5. Prompt completo

> **FOLHA DE SPRITES — BEATRICE SALLES, TÉCNICA DE MANUTENÇÃO DO COMPLEXO HELIX.**
>
> **Estilo:** Pixel art 2D retrô, no mesmo estilo dos cards dos personagens e dos mapas de *Amostra 47*: pixels quadrados nítidos, contorno escuro firme, sombras em blocos (2–4 tons por material), cores dessaturadas, sem antialiasing, sem degradê, sem pintura digital, sem 3D. Proporções adultas estilizadas, cabeça um pouco maior para leitura do rosto, mas **não chibi**. Visão de jogo top-down levemente inclinada (3/4 de cima), igual à dos mapas.
>
> **Personagem:** Técnica de manutenção. Prática, independente e observadora; parece séria, mas cuida de todos à sua maneira. Idade: 24 anos (do card). Goggles circulares de bronze sempre sobre a cabeça. Cabelo quase preto em rabo de cavalo bagunçado, com mechas vermelho-cobre na nuca e nas pontas. Jardineira curta (short) de veludo cotelê marrom-caramelo, com bolso frontal, alças largas e barras dobradas, sobre blusa grafite de manga comprida arregaçada. Cinto de couro com bolsas utilitárias, poucas ferramentas e um frasco transparente no lado direito. Luvas escuras de trabalho e coturnos marrom-escuros de cano médio e sola grossa.
>
> **Jeito e postura:** Prática e ágil, com familiaridade de quem trabalha com as mãos. Peso apoiado numa perna, braços relaxados, nada de pose de combate.
>
> **Cores (usar exatamente esta paleta, dessaturada):** contorno profundo #24201F; blusa #303033; sombra da jardineira #553824; base da jardineira #795030; luz da jardineira #A16C3D; couro das botas e cinto #3D2925; metal e goggles #B48848; reflexo metálico #D0AD70; mecha de cabelo #A04432; base do cabelo #2B2222; pele ilustrativa (não canônica) #C79577.
>
> **Layout:** Uma folha de sprites com **3 linhas × 6 colunas**, todos os quadros do mesmo tamanho, personagem centralizado e com os pés na mesma linha de base. Linha 1: **frente** (andando para baixo). Linha 2: **lado**, virado para a **direita**. Linha 3: **costas** (andando para cima). Colunas 1–2: **parado** (no quadro 2 o tronco sobe 1 pixel, como respiração). Colunas 3–6: **andando**, ciclo de 4 quadros: passo com a perna da frente, pernas juntas, passo com a outra perna, pernas juntas; braços balançam em oposição às pernas. Fundo transparente ou cinza neutro liso. Sem cenário, sem texto, sem moldura, sem sombra projetada no chão.
>
> **Poses por linha:**
> - **Linha 1 — de frente.** Parado: De pé, peso apoiado na perna direita. Braços relaxados, mãos com luvas escuras. Dois aros redondos dos goggles visíveis sobre a cabeça. Bolso frontal e as duas alças da jardineira legíveis. Andando: Passo ágil e decidido. O frasco e as ferramentas do cinto balançam de leve. Braços se movem soltos.
> - **Linha 2 — de lado (virado para a direita).** Parado: Perfil virado para a direita. Rabo de cavalo com fios soltos. Goggles em perspectiva, com a correia. Bolsas e ferramenta do cinto na lateral. Sola grossa dos coturnos. Andando: Passada rápida e prática. O rabo de cavalo balança atrás; as bolsas do cinto acompanham o passo.
> - **Linha 3 — de costas.** Parado: De costas. Mechas cobre visíveis na nuca, rabo volumoso. Correia escura dos goggles sobre o cabelo. Alças da jardineira cruzadas nas costas. Bolsas do cinto na mesma posição. Andando: Passos rápidos; o rabo de cavalo balança de um lado para o outro; as alças da jardineira se mantêm cruzadas.
>
> **Consistência:** o mesmo personagem, com a mesma roupa, cabelo, cores e acessórios, nos 18 quadros; acessórios sempre do mesmo lado do corpo.
>
> **Não fazer:** jardineira comprida, cabelo solto ou em coque, armas, capacete, máscara, steampunk fantasioso, estilo anime. Nada de fotorealismo, pintura digital, 3D, isometria, anime ou chibi.

## 6. Prompts por direção

Use se a folha completa não sair bem. Gere as três tiras e monte a folha depois.

### Frente

> Tira de sprites em pixel art 2D de **Beatrice Salles**, de frente, com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: De pé, peso apoiado na perna direita. Braços relaxados, mãos com luvas escuras. Dois aros redondos dos goggles visíveis sobre a cabeça. Bolso frontal e as duas alças da jardineira legíveis. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passo ágil e decidido. O frasco e as ferramentas do cinto balançam de leve. Braços se movem soltos. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

### Lado

> Tira de sprites em pixel art 2D de **Beatrice Salles**, de lado (virado para a direita), com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: Perfil virado para a direita. Rabo de cavalo com fios soltos. Goggles em perspectiva, com a correia. Bolsas e ferramenta do cinto na lateral. Sola grossa dos coturnos. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passada rápida e prática. O rabo de cavalo balança atrás; as bolsas do cinto acompanham o passo. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

### Costas

> Tira de sprites em pixel art 2D de **Beatrice Salles**, de costas, com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: De costas. Mechas cobre visíveis na nuca, rabo volumoso. Correia escura dos goggles sobre o cabelo. Alças da jardineira cruzadas nas costas. Bolsas do cinto na mesma posição. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passos rápidos; o rabo de cavalo balança de um lado para o outro; as alças da jardineira se mantêm cruzadas. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

## 7. Checklist do personagem

- [ ] As marcas visuais da seção 2 aparecem nas três direções.
- [ ] As cores seguem a paleta da seção 3, sem saturar.
- [ ] O jeito de andar combina com a personalidade (seção 1).
- [ ] Os acessórios ficam sempre do mesmo lado do corpo.
- [ ] Os 18 quadros estão alinhados pelos pés e o ciclo de andar fecha sem pulo.
