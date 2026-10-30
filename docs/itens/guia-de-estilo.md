# AMOSTRA 47 — Guia de direção de arte dos objetos investigativos

**Projeto:** *Amostra 47 — O Início do Fim*  
**Tipo:** bíblia visual, especificação de produção e prompts reutilizáveis  
**Versão:** 1.0 — 29/10/2026  
**Referências de estilo:** [`guia-de-estilo.md`](../personagens/guia-de-estilo.md) e [`guia-de-estilo.md`](../locais/guia-de-estilo.md)  
**Fonte de narrativa:** `README.md` e `docs/caso-amostra47.md` do repositório

> **Objetivo:** criar uma coleção coerente de objetos 2D para um jogo investigativo ambientado no Complexo Helix. Cada objeto deve ter uma versão pequena vista **de cima (bird's-eye / top-down)**, compatível com os mapas, e uma versão maior de **inventário/exame**, compatível com o pixel art dos personagens. Nunca confundir ilustração conceitual com asset técnico pronto para a engine.

## 1. O que é canônico e o que é proposta de arte

A documentação do caso enumera **sete itens investigativos oficiais**: crachá de acesso, pendrive criptografado, gravador de áudio, frasco de contenção, relatório de acesso, sensor de pressão e ordem de manutenção da ventilação. A ordem de manutenção é a evidência ligada a Beatrice Salles (proposição V).

Os nomes, a função das pistas e as relações lógicas descritas abaixo vêm da história. **Cores, tamanho, material aparente, modelo do objeto e posição nos mapas são propostas artísticas**, sujeitas à validação. A documentação não determina dimensões finais, localização fixa das pistas, layout de inventário nem textos completos dos documentos.

## 2. Linguagem visual obrigatória

- **Estilo:** pixel art 2D retrô, profissional e legível, sem fotorealismo, renderização suave, vetor ou 3D.
- **Contorno:** escuro, firme e em pixels quadrados aparentes; sem antialiasing perceptível.
- **Volume:** formas simplificadas, com sombras por blocos (clusters) e **2–4 valores por material**.
- **Cor:** baixa a média saturação, predominantemente branco/cinza clínico, ardósia, grafite e metais frios; vermelho de emergência e verde biológico só como acentos.
- **Universo:** corporação científica sofisticada, tecnologia utilitária, abandono e falhas após um incidente biológico; evitar fantasia medieval, steampunk dominante e neon cyberpunk.
- **Silhueta:** cada item deve ser reconhecível mesmo pequeno. Não encher as bordas de microtextura.
- **Continuidade:** os sete itens devem parecer feitos pelo mesmo artista e caber visualmente dentro dos seis cenários oficiais e ao lado dos sprites humanos.

### Paleta de referência (alvos sugeridos, não cores canônicas)

| Função | HEX | Uso |
|---|---|---|
| Quase-preto de contorno | `#1C2329` | contorno e oclusão |
| Azul-carvão | `#2B3943` | dispositivos e sombras |
| Metal grafite | `#45545D` | estrutura |
| Aço frio | `#7B8C94` | bordas e tampas |
| Cinza clínico | `#BAC6C9` | superfícies claras |
| Branco envelhecido | `#E1E4DF` | papel e etiquetas |
| Vermelho de alerta | `#93463F` | selos/indicadores |
| Verde biológico apagado | `#5C756C` | luz de status/vestígios |
| Amarelo técnico fosco | `#B89A60` | avisos e ferragens pontuais |

**Regra:** contraste e legibilidade têm prioridade sobre fidelidade literal aos HEX. Não usar manchas vermelhas chamativas em todos os objetos. Nas artes atuais, os respingos vermelhos ficam restritos ao **frasco de contenção** e ao **crachá de acesso**; os demais usam o vermelho só em indicadores, faixas e destaques.

## 3. Duas saídas por objeto

### A — Sprite de mundo / coleta

- **Câmera:** top-down ortográfica, objeto visto de cima como nos mapas; **não isométrico**.
- **Leitura:** silhueta reconhecível sobre piso claro ou escuro.
- **Composição:** um único objeto central, sem chão, sem sombra projetada externa e sem cenário incorporado.
- **Destino:** arquivo PNG com fundo transparente, recorte justo, pixels alinhados; escala final a estabelecer no jogo.
- **Detalhes:** privilegiar forma e um acento identificador; não depender de texto minúsculo.

### B — Ícone ampliado / tela de inspeção

- **Câmera:** visão superior ou três-quartos **discreta** para mostrar volume e componentes, mas mantendo a estética 2D em pixels; sem perspectiva realista.
- **Leitura:** formas, etiquetas maiores e superfícies examináveis; ângulo canônico deve ser fixado após aprovação.
- **Composição:** item isolado e central; sem cenário ou moldura incorporada à arte.
- **Destino:** PNG transparente para uso sobre a interface de inventário.
- **Documentos:** o texto legível (protocolos, assinatura, data, registro etc.) deve ser composto **separadamente como interface**, a partir do roteiro aprovado. A imagem do papel não deve inventar fatos nem prometer texto pixelado perfeitamente legível.

### Resolução e escala

O repositório **não define** tamanho de sprites, grid, pixels por tile, engine, sistema de inventário ou proporção de UI. Para um primeiro teste de produção, são **opções a validar**, e não requisitos: ícones de chão 32×32 ou 48×48 pixels lógicos; inventário 96×96 ou 128×128 pixels lógicos. Fazer upscale somente por *nearest-neighbor* e confirmar a legibilidade no tamanho real.

## 4. Matriz narrativa dos sete itens

| ID sugerido | Objeto | Função narrativa confirmada | Elemento visual proposto | Cuidado com alucinações |
|---|---|---|---|---|
| OBJ-01 | Crachá de acesso | Reconstruir entradas e horários dos setores restritos | Cartão branco envelhecido em porta-crachá grafite com mosquetão; foto em silhueta sobre fundo vermelho, código de barras e símbolo Helix no canto; respingos vermelhos discretos | Não inventar nome, matrícula ou acesso específico como fato |
| OBJ-02 | Pendrive criptografado | Cópia parcial dos registros; contém evidência decisiva da conta da direção | Pendrive industrial grafite com parafusos, faixa vermelha de lacre e conector USB metálico | Não colocar o nome do culpado gravado nele |
| OBJ-03 | Gravador de áudio | Registra conversa anterior ao alarme geral | Gravador digital portátil grafite com detalhes vermelhos, dois microfones no topo, tela com forma de onda, botões de reproduzir/gravar/parar e alto-falante | Não inventar o diálogo ou remetentes |
| OBJ-04 | Frasco de contenção | Auxilia a reconstruir se houve retirada manual da amostra | Vial cilíndrico de vidro **vazio**, tampa metálica rosqueada, base de metal, etiqueta de risco biológico rasgada e respingos vermelhos | Não retratar mutação/fórmula química não especificada |
| OBJ-05 | Relatório de acesso | Contém registros de horários, setores e tentativas de entrada | Folhas em prancheta grafite com detalhes vermelhos; símbolo de risco biológico, tabela com linhas destacadas em vermelho e bloco com ícone de câmera | Não inventar nomes, datas e horários concretos |
| OBJ-06 | Sensor de pressão | Indica alterações nas condições da câmara | Manômetro analógico de metal com parafusos, ponteiro vermelho, faixa vermelha de alerta no mostrador e conexão rosqueada | Não inventar pressão numérica canônica |
| OBJ-07 | Ordem de manutenção da ventilação | Apresenta inconsistências; investigação indica que **não foi solicitada por Beatrice** | Formulário corporativo Helix em prancheta cor de cobre gasta, clipe metálico, campos e caixas de seleção em branco | Não forjar assinatura de Beatrice nem atribuir emissão a outra pessoa sem base |

**Importante:** a localização dos itens nos seis ambientes **ainda não é fixada pelo repositório**. A ambientação pode sugerir pistas, mas o documento não estabelece coordenadas nem qual sala recebe cada item. Não criar consequências ou revelações novas na arte.

## 5. Diretrizes específicas por objeto

### OBJ-01 — Crachá de acesso

- Cartão retangular vertical dentro de porta-crachá rígido grafite, com mosquetão metálico no topo.
- Versão de mundo: bloco claro com o quadro vermelho da foto como acento; não tentar renderizar retrato minúsculo realista.
- Versão de inspeção (arte atual): foto em silhueta escura sobre fundo vermelho, código de barras abstrato, linhas de texto ilegíveis e símbolo Helix no canto superior direito. Campos reais, se necessários, devem ser renderizados na UI.

### OBJ-02 — Pendrive criptografado

- Corpo industrial grafite com parafusos aparentes e uma faixa vermelha translúcida como lacre de segurança.
- Versão de mundo: silhueta comprida facilmente reconhecível e conector visível.
- Versão de inspeção (arte atual): vista em três-quartos discreta, conector USB metálico exposto e desgaste leve no corpo.

### OBJ-03 — Gravador de áudio

- Eletrônico portátil retangular grafite, com bordas vermelhas, dois microfones no topo e alto-falante perfurado.
- Versão de mundo: tela clara pequena e botão de gravação vermelho como acento.
- Versão de inspeção (arte atual): tela com forma de onda e ponto de gravação, botões de reproduzir, gravar e parar; nenhuma palavra na tela.

### OBJ-04 — Frasco de contenção

- Vial cilíndrico de vidro com tampa metálica rosqueada e base de metal. **O frasco está vazio**, o que reforça a pergunta sobre a retirada da amostra.
- Etiqueta de risco biológico rasgada e respingos vermelhos no vidro.
- Versão de mundo: forma simples que se destaque do piso; interior pouco saturado.
- Versão de inspeção (arte atual): vidro translúcido sugerido por **clusters**, não transparência pintada realista; sem organismo monstruoso.

### OBJ-05 — Relatório de acesso

- Pilha de folhas em prancheta grafite com detalhes vermelhos nas bordas e clipe metálico.
- Versão de mundo: prancheta vista de cima, canto da folha dobrado discreto.
- Versão de inspeção (arte atual): símbolo de risco biológico no cabeçalho, tabela estilizada com algumas linhas e status destacados em vermelho e bloco inferior com ícone de câmera de vigilância; dados reais colocados posteriormente na UI.

### OBJ-06 — Sensor de pressão

- Manômetro analógico de metal, com aro parafusado, mostrador claro, ponteiro vermelho e faixa vermelha de alerta, preso a uma conexão rosqueada de tubulação.
- Versão de mundo: mostrador contrastante e conexão discernível.
- Versão de inspeção (arte atual): escala sem números, para não fixar um valor de pressão; sinais de desgaste e ferrugem leves.

### OBJ-07 — Ordem de manutenção da ventilação

- **Elemento chave:** documento operacional corporativo, não um pergaminho antigo.
- Versão de mundo: papel claro em prancheta cor de cobre, com o clipe metálico no topo bem visível.
- Versão de inspeção (arte atual): cabeçalho com símbolo e nome HELIX, código de barras, quadro de campos, quatro linhas com caixas de seleção e área de observações, todos **em branco ou ilegíveis**; papel manchado pelo manuseio.
- **Não escrever assinatura de Beatrice** na imagem: o fato confirmado é justamente que a ordem suspeita não partiu dela. Não inserir assinatura de Fernando, número de protocolo ou data fictícia como se fossem evidência.

## 6. Prompt mestre para versão de mundo

> Crie **um único sprite de objeto** para o jogo *Amostra 47 — O Início do Fim*, usando a ficha do objeto fornecida abaixo e as referências visuais do projeto. Câmera **bird's-eye view top-down ortográfica**, visão de cima sem inclinação isométrica. Estética pixel art 2D retrô com pixels quadrados nítidos, contorno escuro uniforme, blocos de sombra bem organizados, paleta industrial fria e dessaturada (branco clínico, ardósia, cinza, aço), acentos controlados de alerta. O objeto pertence ao Complexo Helix, uma instalação de pesquisa corporativa em colapso biológico. Representar **apenas um objeto**, inteiro, isolado, com silhueta legível e sem elementos decorativos externos. Fundo transparente quando possível. Não mostrar cenário, personagem, moldura, texto longo, brilho neon, efeitos fotográficos, 3D, isometria, anime ou excesso de detalhes. **Objeto:** [COLAR OBJETO E CARACTERÍSTICAS DA MATRIZ]. Não adicionar conteúdo narrativo inexistente.

## 7. Prompt mestre para versão de inventário

> Crie um **ícone de inventário ampliado e examinável**, em pixel art 2D, do **MESMO objeto já aprovado** como sprite de chão, para o jogo *Amostra 47*. Preserve forma, materiais, cores e elementos marcantes entre as duas versões. Usar visão superior ou inclinação mínima aprovada, clusters de pixels nítidos, contorno escuro e até 2–4 níveis de sombra por material. O objeto deve preencher bem o enquadramento, isolado em fundo transparente, sem cenário, personagem ou moldura de UI incorporada. O resultado deve ser consistente com a arte dos personagens e dos seis mapas do Complexo Helix. Evitar 3D realista, gradientes suaves, alta saturação, palavras inventadas, supostos valores de sensores, nomes de funcionários, assinaturas e datas fictícias. **Objeto:** [COLAR A MESMA FICHA DO OBJETO].

## 8. Prompt individual prioritário — ordem de manutenção

> **OBJ-07 — ORDEM DE MANUTENÇÃO DA VENTILAÇÃO.** Gerar em pixel art 2D, estilo Amostra 47, uma ordem de serviço corporativa do Complexo Helix. Folha retangular de papel branco acinzentado encaixada numa prancheta tecnológica cinza grafite, clipe metálico simples, linhas de campos técnicos, um ícone pequeno de ventilação e discreta marca vermelha de setor de manutenção. Papel parcialmente amassado pelo abandono, com desgaste leve e realista em pixels. Para sprite de mundo: vista absolutamente top-down, forma reconhecível, sem texto legível. Para inspeção: visualização ampliada, campos de solicitante e autorização **não preenchidos**, nenhuma assinatura identificável, nenhuma data inventada. Paleta fria, pouco saturada, contornos escuros e pixels quadrados de alta legibilidade, fundo transparente e sem cenário. Não parecer pergaminho, carta antiga ou documento com sangue. A pista indica que a ordem **não foi solicitada por Beatrice Salles**, mas isso não deve ser revelado de forma literal na arte.

## 9. Outros objetos interativos e cenário (fora dos sete itens)

Estes são **assets ambientais propostos**, não evidências canônicas adicionais: terminal de computador, portas automáticas, leitor de crachá, câmera de segurança, mesa, cadeira, armário, estação de análise, monitor, válvula, ventilador industrial, duto, estante, caixas de suprimentos e sinalização. Produzir em tiles/props independentes para composição dos ambientes. Classificar como **decorativo**, **obstáculo** ou **interativo**, sem estabelecer novas pistas pela simples existência do objeto.

## 10. Checklist de qualidade

- [ ] Objeto corresponde ao nome e função documentados?
- [ ] Top-down verdadeiro para sprite de chão? Sem inclinação isométrica?
- [ ] Contorno pixelado, textura por clusters e paleta dessaturada?
- [ ] Silhueta legível em escala de jogo?
- [ ] Sprite de mundo e ícone de inventário representam o **mesmo** design?
- [ ] Fundo transparente ou versão limpa para recorte?
- [ ] Nenhum fato de roteiro, assinatura, data, diálogo ou medição foi inventado?
- [ ] Elemento interativo está legível sem depender de texto pequeno?
- [ ] PNG técnico foi revisado em pixels lógicos, transparência e escala antes de integrar na engine?

## 11. Organização no repositório

Cada guia fica junto do conteúdo que descreve:

```text
docs/
  personagens/guia-de-estilo.md
  locais/guia-de-estilo.md
  itens/
    guia-de-estilo.md
    <objeto>/
      README.md             # o que revela e papel na prova
      arte.webp             # versão de inspeção/inventário
```

Quando as versões de mundo (top-down) e os PNGs técnicos forem produzidos, eles podem ir para `assets/objetos/mundo/` e `assets/objetos/inventario/`.

## 12. Estado das artes

| ID | Objeto | Arquivo | Inspeção (arte atual) | Mundo (top-down) |
|---|---|---|---|---|
| OBJ-01 | Crachá de acesso | [`cracha-de-acesso/arte.webp`](cracha-de-acesso/arte.webp) | ✅ | pendente |
| OBJ-02 | Pendrive criptografado | [`pendrive-criptografado/arte.webp`](pendrive-criptografado/arte.webp) | ✅ | pendente |
| OBJ-03 | Gravador de áudio | [`gravador-de-audio/arte.webp`](gravador-de-audio/arte.webp) | ✅ | pendente |
| OBJ-04 | Frasco de contenção | [`frasco-de-contencao/arte.webp`](frasco-de-contencao/arte.webp) | ✅ | pendente |
| OBJ-05 | Relatório de acesso | [`relatorio-de-acesso/arte.webp`](relatorio-de-acesso/arte.webp) | ✅ | pendente |
| OBJ-06 | Sensor de pressão | [`sensor-de-pressao/arte.webp`](sensor-de-pressao/arte.webp) | ✅ | pendente |
| OBJ-07 | Ordem de manutenção da ventilação | [`ordem-de-manutencao/arte.webp`](ordem-de-manutencao/arte.webp) | ✅ | pendente |

As versões de mundo pequenas aparecem só na [prancha de cenários e objetos](../locais/prancha-cenarios-e-objetos.webp), ainda não como arquivos separados.

**Pendências:**

- O símbolo no canto do crachá, no cabeçalho da ordem de manutenção e na sinalização da prancha reproduz o logo da Umbrella (*Resident Evil*). Substituir por um símbolo próprio do Complexo Helix.
- As artes estão em `.webp` com fundo branco; os PNGs transparentes de produção ainda precisam ser preparados.

**Estado atual:** diretriz de produção; os assets precisam de aprovação visual e preparação técnica antes de serem declarados sprites finais do jogo.
