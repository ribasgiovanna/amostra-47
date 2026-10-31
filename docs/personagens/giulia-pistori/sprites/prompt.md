# Sprites de jogo — Giulia Pistori

Prompt detalhado para gerar os sprites de **parado** e **andando**, de **frente**, **lado** e **costas**. Formato, tamanhos e checklist geral estão na [especificação dos sprites](../../sprites-especificacao.md).

## Como usar

1. Anexe o card da personagem, [`../ficha-card.webp`](../ficha-card.webp), como referência visual.
2. Cole o **prompt completo** (seção 5). Ele gera a folha inteira de uma vez.
3. Se a folha sair desalinhada ou inconsistente, gere **uma direção por vez** com os prompts da seção 6.
4. Limpe e monte a folha no editor de pixel art, seguindo a especificação, e salve em [`src/jogo/sprites/giulia-pistori/`](../../../../src/jogo/sprites/giulia-pistori/) como `giulia-sheet.png`.

## 1. Quem é

| | |
|---|---|
| **Função** | Protagonista |
| **Idade** | 21 anos |
| **Personalidade** | Filha de Giovani Pistori e de uma estrangeira que sumiu quando ela nasceu. Anos depois do surto, vai sozinha ao Complexo Helix descobrir o que aconteceu com o pai. Indignada, em luto e determinada. |
| **Jeito de se mover** | Firme e um pouco tensa, de quem entra num lugar perigoso sabendo dos riscos. Passos decididos, olhar atento. Casual e urbana, nada de pose heroica ou de modelo. |

## 2. Silhueta e marcas visuais

- **Cachos loiro-mel muito volumosos**, com a **raiz um pouco mais escura**, franja de cachos e comprimento um pouco abaixo dos ombros: a marca principal da silhueta.
- Pele morena clara dourada, **sardas** discretas no nariz, **sobrancelhas escuras e marcadas** como as do pai, expressão séria.
- **Cardigã oversized de tricô marrom-chocolate**, longo e aberto, com botões escuros e punhos canelados, sobre **camiseta preta**.
- **Calça jeans wide-leg preta desbotada** até o chão e **tênis de lona preto com faixa lateral e sola brancas**, sem logotipo.
- **Ecobag de lona creme** sempre no **ombro direito**.

## 3. Paleta de cores

Cores da [ficha visual](../ficha-visual.md). São alvos aproximados; o importante é manter o contraste e a baixa saturação.

| Parte | Cor | HEX | Onde usar |
|---|---|---|---|
| Contorno | Carvão | `#1E1F22` | linha externa |
| Cabelo — base | Loiro-mel | `#C49A5C` | massa dos cachos |
| Cabelo — sombra | Castanho dourado | `#8A6438` | interior dos cachos |
| Cabelo — luz | Areia dourada | `#E2C48E` | pontas iluminadas |
| Cabelo — raiz | Castanho escuro | `#5A4030` | raiz e sobrancelhas |
| Pele — base | Dourado quente | `#C69272` | rosto e mãos |
| Pele — sombra | Marrom quente | `#9A6A50` | volume do rosto |
| Sardas | Canela | `#8E5A42` | poucos pixels |
| Cardigã — base | Marrom-chocolate | `#6B4A36` | peça principal |
| Cardigã — sombra | Marrom profundo | `#4A3226` | dobras e punhos |
| Camiseta | Preto | `#232326` | parte superior |
| Calça — base | Preto desbotado | `#3A3B40` | pernas |
| Calça — luz | Cinza-chumbo | `#55575D` | vincos |
| Tênis | Preto e branco | `#1F1F22 / #E6E3DC` | calçado |
| Ecobag | Creme | `#E2D8C3` | bolsa |

## 4. Poses

### Parado

| Direção | Como deve ficar |
|---|---|
| **Frente** | De pé, pés levemente afastados. Mão esquerda no bolso do cardigã; mão direita segurando a alça da ecobag no ombro direito. Cardigã aberto mostrando a camiseta preta. Cachos volumosos emoldurando o rosto, franja sobre a testa, sobrancelhas escuras e olhar sério. |
| **Lado** | Perfil virado para a direita. Volume arredondado dos cachos para trás e para cima. Cardigã longo até o meio da coxa, manga larga. A ecobag aparece na lateral do quadril. Calça larga cobrindo quase todo o tênis, sola branca visível. |
| **Costas** | De costas. Massa de cachos cobrindo a nuca e o alto das costas. Costas lisas do cardigã, barra e punhos iguais à frente. Alça da ecobag cruzando o ombro direito. |

### Andando

| Direção | Como deve ficar |
|---|---|
| **Frente** | Passos decididos e um pouco cautelosos. A mão continua na alça da ecobag; o outro braço balança pouco. A calça larga balança a cada passo e a sola branca dos tênis aparece. |
| **Lado** | Passada média e firme, tronco levemente à frente. Os cachos balançam com um quadro de atraso; o cardigã e a ecobag acompanham o passo. |
| **Costas** | Passos firmes; os cachos balançam sobre os ombros; a ecobag balança levemente no ombro direito. |

## 5. Prompt completo

> **FOLHA DE SPRITES — GIULIA PISTORI, PROTAGONISTA DO COMPLEXO HELIX.**
>
> **Estilo:** Pixel art 2D retrô, no mesmo estilo dos cards dos personagens e dos mapas de *Amostra 47*: pixels quadrados nítidos, contorno escuro firme, sombras em blocos (2–4 tons por material), cores dessaturadas, sem antialiasing, sem degradê, sem pintura digital, sem 3D. Proporções adultas estilizadas, cabeça um pouco maior para leitura do rosto, mas **não chibi**. Visão de jogo top-down levemente inclinada (3/4 de cima), igual à dos mapas.
>
> **Personagem:** Filha de Giovani Pistori e de uma estrangeira que sumiu quando ela nasceu. Anos depois do surto, vai sozinha ao Complexo Helix descobrir o que aconteceu com o pai. Indignada, em luto e determinada. Idade: 21 anos. Cachos loiro-mel muito volumosos, com a raiz um pouco mais escura, franja de cachos e comprimento um pouco abaixo dos ombros: a marca principal da silhueta. Pele morena clara dourada, sardas discretas no nariz, sobrancelhas escuras e marcadas como as do pai, expressão séria. Cardigã oversized de tricô marrom-chocolate, longo e aberto, com botões escuros e punhos canelados, sobre camiseta preta. Calça jeans wide-leg preta desbotada até o chão e tênis de lona preto com faixa lateral e sola brancas, sem logotipo. Ecobag de lona creme sempre no ombro direito.
>
> **Jeito e postura:** Firme e um pouco tensa, de quem entra num lugar perigoso sabendo dos riscos. Passos decididos, olhar atento. Casual e urbana, nada de pose heroica ou de modelo.
>
> **Cores (usar exatamente esta paleta, dessaturada):** contorno #1E1F22; cabelo — base #C49A5C; cabelo — sombra #8A6438; cabelo — luz #E2C48E; cabelo — raiz #5A4030; pele — base #C69272; pele — sombra #9A6A50; sardas #8E5A42; cardigã — base #6B4A36; cardigã — sombra #4A3226; camiseta #232326; calça — base #3A3B40; calça — luz #55575D; tênis #1F1F22 / #E6E3DC; ecobag #E2D8C3.
>
> **Layout:** Uma folha de sprites com **3 linhas × 6 colunas**, todos os quadros do mesmo tamanho, personagem centralizado e com os pés na mesma linha de base. Linha 1: **frente** (andando para baixo). Linha 2: **lado**, virado para a **direita**. Linha 3: **costas** (andando para cima). Colunas 1–2: **parado** (no quadro 2 o tronco sobe 1 pixel, como respiração). Colunas 3–6: **andando**, ciclo de 4 quadros: passo com a perna da frente, pernas juntas, passo com a outra perna, pernas juntas; braços balançam em oposição às pernas. Fundo transparente ou cinza neutro liso. Sem cenário, sem texto, sem moldura, sem sombra projetada no chão.
>
> **Poses por linha:**
> - **Linha 1 — de frente.** Parado: De pé, pés levemente afastados. Mão esquerda no bolso do cardigã; mão direita segurando a alça da ecobag no ombro direito. Cardigã aberto mostrando a camiseta preta. Cachos volumosos emoldurando o rosto, franja sobre a testa, sobrancelhas escuras e olhar sério. Andando: Passos decididos e um pouco cautelosos. A mão continua na alça da ecobag; o outro braço balança pouco. A calça larga balança a cada passo e a sola branca dos tênis aparece.
> - **Linha 2 — de lado (virado para a direita).** Parado: Perfil virado para a direita. Volume arredondado dos cachos para trás e para cima. Cardigã longo até o meio da coxa, manga larga. A ecobag aparece na lateral do quadril. Calça larga cobrindo quase todo o tênis, sola branca visível. Andando: Passada média e firme, tronco levemente à frente. Os cachos balançam com um quadro de atraso; o cardigã e a ecobag acompanham o passo.
> - **Linha 3 — de costas.** Parado: De costas. Massa de cachos cobrindo a nuca e o alto das costas. Costas lisas do cardigã, barra e punhos iguais à frente. Alça da ecobag cruzando o ombro direito. Andando: Passos firmes; os cachos balançam sobre os ombros; a ecobag balança levemente no ombro direito.
>
> **Consistência:** o mesmo personagem, com a mesma roupa, cabelo, cores e acessórios, nos 18 quadros; acessórios sempre do mesmo lado do corpo.
>
> **Não fazer:** jaleco, colete, uniforme, armas, maquiagem marcada, piercing ou joias chamativas, logotipos de marcas reais, semelhança com qualquer pessoa real, cabelo liso ou escuro. Nada de fotorealismo, pintura digital, 3D, isometria, anime ou chibi.

## 6. Prompts por direção

Use se a folha completa não sair bem. Gere as três tiras e monte a folha depois.

### Frente

> Tira de sprites em pixel art 2D de **Giulia Pistori**, de frente, com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: De pé, pés levemente afastados. Mão esquerda no bolso do cardigã; mão direita segurando a alça da ecobag no ombro direito. Cardigã aberto mostrando a camiseta preta. Cachos volumosos emoldurando o rosto, franja sobre a testa, sobrancelhas escuras e olhar sério. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passos decididos e um pouco cautelosos. A mão continua na alça da ecobag; o outro braço balança pouco. A calça larga balança a cada passo e a sola branca dos tênis aparece. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

### Lado

> Tira de sprites em pixel art 2D de **Giulia Pistori**, de lado (virado para a direita), com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: Perfil virado para a direita. Volume arredondado dos cachos para trás e para cima. Cardigã longo até o meio da coxa, manga larga. A ecobag aparece na lateral do quadril. Calça larga cobrindo quase todo o tênis, sola branca visível. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passada média e firme, tronco levemente à frente. Os cachos balançam com um quadro de atraso; o cardigã e a ecobag acompanham o passo. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

### Costas

> Tira de sprites em pixel art 2D de **Giulia Pistori**, de costas, com **6 quadros lado a lado** do mesmo tamanho: 2 de parado e 4 de andando. Mesmo estilo, cores e roupa da folha completa e do card anexado. Parado: De costas. Massa de cachos cobrindo a nuca e o alto das costas. Costas lisas do cardigã, barra e punhos iguais à frente. Alça da ecobag cruzando o ombro direito. Andando (4 quadros: passo, pernas juntas, outro passo, pernas juntas): Passos firmes; os cachos balançam sobre os ombros; a ecobag balança levemente no ombro direito. Pés na mesma linha de base em todos os quadros. Fundo transparente, sem cenário, sem texto.

## 7. Checklist do personagem

- [ ] As marcas visuais da seção 2 aparecem nas três direções.
- [ ] As cores seguem a paleta da seção 3, sem saturar.
- [ ] O jeito de andar combina com a personalidade (seção 1).
- [ ] Os acessórios ficam sempre do mesmo lado do corpo.
- [ ] Os 18 quadros estão alinhados pelos pés e o ciclo de andar fecha sem pulo.
