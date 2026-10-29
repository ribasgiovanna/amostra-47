# AMOSTRA 47 — Guia mestre de direção artística para sprites

**Projeto:** *Amostra 47 — O Início do Fim*  
**Tipo de documento:** especificação visual e prompt contextual reutilizável  
**Versão:** 1.0 — 23/10/2026  
**Status:** direção visual de referência; detalhes técnicos de produção ainda a validar.

## 1. Contexto narrativo obrigatório

*Amostra 47* é um jogo narrativo de investigação e lógica matemática ambientado após o colapso da humanidade, provocado pela disseminação de um agente biológico desconhecido. Um sobrevivente investiga o Complexo Helix, laboratório científico abandonado na noite do incidente, para reconstruir a origem do desastre. Os personagens são funcionários do complexo: cientistas, segurança, tecnologia, contenção e manutenção.

**Consequência para o design:** cada sprite deve comunicar uma profissão, ter visual crível para uma instalação de pesquisa e preservar o tom sombrio de mistério e ficção científica pós-apocalíptica. Não transformar o universo inteiro em fantasia steampunk. Elementos de latão/couro podem fazer parte do estilo *individual* de um personagem, sem se tornar uniforme obrigatório do elenco.

## 2. Referências e hierarquia de autoridade

1. **Referência de pixel art enviada pelo projeto:** personagem de corpo inteiro, proporções compactas mas não infantis, pixels aparentes, contornos escuros, volumes formados por blocos discretos de cor, fundo neutro. É a âncora para a **técnica visual**.
2. **Sprite/folha de Beatrice produzida e aprovada como ponto de partida:** âncora para **escala aparente, densidade de detalhes, renderização e apresentação**. Não copiar seu figurino para outras profissões.
3. **Ficha individual do personagem:** fonte de verdade sobre **traços físicos, figurino, acessórios e paleta pessoais**.
4. **README e `docs/caso-amostra47.md` do repositório:** fonte de verdade para **nome, função e relevância narrativa**. Não inventar novos fatos de enredo.

**Importante:** texto sozinho não garante sprites idênticos. Sempre anexar a mesma referência visual aprovada junto com o prompt quando a ferramenta suportar imagens. A geração anterior é uma *concept sheet* em pixel art; suas poses múltiplas não são automaticamente frames técnicos prontos para engine.

## 3. Gramática visual fixa

- **Linguagem:** pixel art retrô de jogo narrativo 2D, com pixel grid consistente e pixels quadrados definidos.
- **Proporções:** corpo inteiro, adulto estilizado de proporções compactas/semi-realistas; cabeça um pouco maior para leitura facial, mas **não chibi/kawaii**.
- **Silhueta:** imediatamente reconhecível; peças profissionais e 2 a 4 elementos de identidade individual bem separados.
- **Contorno:** escuro, firme e legível, com variação controlada conforme iluminação. Evitar linhas vetoriais suaves.
- **Luz e volume:** massas de cor planas com 2–4 níveis de valor por material, sombreamento por clusters de pixels; oclusão discreta nas dobras, botas, cabelos e sobreposições.
- **Texturas:** sugestões de tecido, couro, metal, poeira ou desgaste por poucos pixels estrategicamente posicionados. Evitar ruído/pixels aleatórios e microdetalhes ilegíveis.
- **Cores:** paleta limitada e levemente dessaturada, contraste suficiente com o fundo, pretos/ardósia e tons industriais; acentos restritos por personagem.
- **Atmosfera:** laboratório de risco biológico, tecnologia utilizada e degradada, tensão, investigação; nada de brilho mágico ou fantasia heroica.
- **Apresentação-padrão:** um sprite frontal em pé, corpo inteiro e sem cortes, alinhado no centro, fundo sólido cinza neutro ou transparente, iluminação coerente, sem cenário complexo, textos ou marcas-d'água.
- **Ângulos adicionais:** frente, perfil, costas e três quartos somente quando solicitados; manter identidade, roupa, proporções e cores em todos.

### Restrições de produção

Não há resolução final, grid mestre, dimensões de colisão, pivô, FPS ou escala de engine definidos no repositório. **Não inventar esses valores como requisitos oficiais.** Quando forem definidos, documentar e aplicá-los uniformemente. Para uso em engine, revisar sprites em escala nativa e preparar PNG transparente com recorte e alinhamento consistentes; uma imagem de apresentação não substitui uma sprite sheet estruturada.

## 4. O que não pode acontecer

- Não migrar para pintura digital, realismo fotográfico, anime, desenho vetorial liso, 3D ou cartoon infantil.
- Não usar efeitos de desfoque, antialiasing visível, degradês contínuos, excesso de partículas ou filtros que escondam os pixels.
- Não trocar o design do personagem entre ângulos ou imagens (cor do cabelo, acessórios, formato das botas, comprimento da roupa).
- Não acrescentar máscaras, armas, mutações, uniformes militares ou dispositivos sem especificação do personagem.
- Não apresentar expressões e poses como **sprites de animação prontos** sem alinhamento técnico e conferência frame a frame.
- Não revelar visualmente o culpado com sinais caricatos de maldade; a trama deve permanecer investigativa.

## 5. Prompt contextual mestre — copiar e reutilizar

> Você é o artista de pixel art responsável pela identidade dos personagens do jogo **Amostra 47 — O Início do Fim**. O jogo é um mistério investigativo de ficção científica pós-apocalíptica ambientado no laboratório Complexo Helix, após um incidente biológico. Crie **um sprite individual de corpo inteiro** do personagem descrito na FICHA DO PERSONAGEM abaixo.
>
> **CONTINUIDADE DE ESTILO OBRIGATÓRIA:** reproduza a gramática técnica da REFERÊNCIA VISUAL ANEXADA: pixel art 2D retrô com pixels quadrados nítidos, contorno escuro definido, proporções adultas estilizadas e compactas, silhueta legível, sombreamento em clusters bem organizados, poucos valores por material, cores dessaturadas e acabamento limpo. O resultado deve parecer parte da **mesma coleção** de sprites da referência, com densidade de detalhe e tratamento de luz equivalentes. Use a referência como guia de **linguagem gráfica**, nunca como justificativa para copiar cabelo, roupas ou acessórios de outro personagem.
>
> **ENQUADRAMENTO:** personagem inteiro, da cabeça à sola do calçado, em pé, pose neutra e funcional, enquadramento central com espaço ao redor, fundo sólido cinza neutro ou transparente, sem texto e sem cenário. Preservar todas as particularidades presentes na ficha individual.
>
> **DESIGN:** cada peça e acessório precisa fazer sentido para a função do personagem dentro do Complexo Helix. Priorizar 2–4 marcas de reconhecimento visual, leitura da silhueta e legibilidade em escala reduzida. Não inventar detalhes narrativos ou atributos físicos que contradigam a ficha.
>
> **EVITAR:** anime, kawaii, chibi exagerado, vetor, 3D, pintura digital, fotorealismo, pixels borrados, excesso de microtextura, exagero steampunk sem fundamento, elementos aleatórios de ficção científica e acessórios não solicitados.
>
> **FICHA DO PERSONAGEM:**
> - Nome: [NOME]
> - Função no Complexo Helix: [FUNÇÃO]
> - Idade aparente (se definida): [IDADE OU NÃO ESPECIFICADA]
> - Aparência física: [TRAÇOS CONHECIDOS; NÃO INVENTAR OUTROS]
> - Cabelo: [COR, CORTE, ESTILO]
> - Parte superior: [ROUPA]
> - Parte inferior: [ROUPA]
> - Calçado: [CALÇADO]
> - Acessórios obrigatórios: [ITENS]
> - Silhueta e postura: [DESCRIÇÃO]
> - Cores principais / acentos: [PALETA]
> - Sinais sutis de uso: [DESGASTE PERMITIDO]
> - Elementos proibidos específicos: [O QUE NÃO ADICIONAR]
>
> **SAÍDA:** produzir somente a imagem de um sprite individual, não uma colagem, não uma folha com diversas poses, a menos que isso seja solicitado explicitamente.

## 6. Prompts de continuação

**Turnaround:** “Usando exatamente o sprite aprovado como modelo imutável, crie frente, perfil, costas e três quartos. Mantenha identidade, medidas relativas, cabelo, cores, costuras e posição de acessórios. Não redesenhe a personagem.”

**Expressões:** “Usando o rosto do sprite aprovado como referência, produza uma folha de expressões [listar]. Mantenha cabelo, goggles/óculos se houver, formato facial, paleta e pixel grid. Não introduza nova roupa ou maquiagem.”

**Animação:** “Planeje os frames de [ação] a partir do sprite aprovado. Mostre poses-chave consistentes. Isto é um estudo de animação, não declare que está pronto para engine sem grid, alinhamento e verificação de transparência.”

## 7. Checklist de aceite

- [ ] O personagem está de corpo inteiro e sem cortes?
- [ ] Os pixels são nítidos, sem blur ou bordas pintadas?
- [ ] Contorno, clusters de sombra e proporções combinam com a imagem-âncora?
- [ ] Figurino, rosto, cabelo e acessórios seguem integralmente a ficha?
- [ ] A função profissional é legível sem recorrer a rótulos?
- [ ] A silhueta se diferencia das demais?
- [ ] Paleta limitada, com destaque cromático controlado?
- [ ] O design funciona quando reduzido?
- [ ] Nenhum elemento não solicitado ou fato de história foi inventado?
- [ ] A saída é realmente um sprite isolado, não uma concept sheet, quando essa foi a solicitação?

## 8. Personagens documentados no caso

Dra. Amie Lin (virologista); Giovani Pistori (chefe de segurança); Angela Torres (engenheira de sistemas); Dr. Fernando Almeida (diretor científico); Otávio Ferraz (estagiário); Clara Costa (técnica de contenção); Beatrice Salles (técnica de manutenção).

As características visuais de quem ainda não recebeu ficha individual **permanecem indefinidas**; não herdar os elementos únicos de Beatrice.
