# Jogo — beta jogável

Vertical slice para testar o jogo de ponta a ponta: quatro personagens jogáveis, três mapas e um item (sensor de pressão, OBJ-06, na Câmara de contenção).

## Como executar

```bash
pip install -r requirements.txt
python src/jogo/amostra47.py
```

Controles: setas ou WASD para andar (diagonais com duas teclas), **E** para interagir, **Tab** para o mapa mental (pistas coletadas e posição no complexo), **Caps Lock** para alternar antes/depois do incidente, **Alt** para o menu de personagens (nos menus, **clique** na opção ou use setas + **E**/Enter), **F11** para alternar tela cheia (em janela, sem borda), **Esc** para fechar menus ou abrir o menu de pausa (Continuar/Sair). O jogo abre no menu principal (Jogar/Game test/Sair). **Game test** pula a cutscene e libera **Caps Lock** e **Alt** para testar salas e personagens; em **Jogar** eles ficam desligados. **Jogar** mostra a cutscene de abertura (`cutscene.py`: imagem e narração em `cutscenes/`; **E**, Enter ou clique avança, **Esc** pula) e depois a Giulia entra na Sala de evacuação.

A câmera acompanha o personagem. Os itens aparecem no mapa só como um brilho branco pulsante; ao se aproximar aparece "Pressione E para interagir". Ao interagir, o jogo pausa, o fundo fica borrado e a arte do item aparece com a descrição abaixo; **E** de novo fecha e retoma o jogo.

## Organização

| Arquivo | Conteúdo |
|---|---|
| `amostra47.py` | Laço principal, HUD, menus e listas de mapas, personagens e itens do menu |
| `dados.py` | Definições de personagens, mapas (máscara de paredes, objetos, início) e itens |
| `entidades.py` | Classes `Mapa`, `Jogador` e `Item` |
| `mapas/` | Mapas vazios (`*-vazia.png`) e máscaras de paredes (`*-paredes.png`, branco = piso) |
| `mapas/objetos/<mapa>/` | Objetos de cada mapa e `objetos.json` (posição, colisão na base e linha de profundidade) |
| `sprites/<personagem>-pixellab/` | Sprites dos personagens jogáveis, gerados no PixelLab |
| `itens/` | Ícones dos itens usados em jogo |
| `ferramentas/importar_pixellab.py` | Converte o .zip do PixelLab para o formato dos sprites |

Para adicionar um personagem: `python src/jogo/ferramentas/importar_pixellab.py ARQUIVO.zip src/jogo/sprites/<nome>-pixellab`, crie a entrada em `PERSONAGENS` (`dados.py`) e ponha a chave em `PERSONAGENS_MENU` (`amostra47.py`). Para um mapa: entrada em `MAPAS`, chave em `MAPAS_MENU` e itens em `ITENS_NO_MAPA`.

## Formato

- Sprites: `parado-<direção>.png` (1 quadro) e `andando-<direção>.png` (tira de quadros quadrados; o lado do quadro é a altura da tira, 80 px nos do PixelLab). Direções: `frente`, `costas`, `lado` (direita), `esquerda` e, opcionais, `frente-direita`, `frente-esquerda`, `costas-direita`, `costas-esquerda`. Sem `esquerda`, o jogo espelha o `lado`.
- Mapas: imagem desenhada em 720 × 720 unidades (as imagens têm 2000 a 2160 px). Os objetos são desenhados na frente ou atrás do personagem conforme a linha de profundidade e colidem só na base.
- `itens/sensor-de-pressao.png`: cópia de `docs/itens/sensor-de-pressao/arte.webp` reduzida para 320 px (exibida só na tela de inspeção).

Os originais em `docs/` não foram alterados.

**Itens:** os 7 itens investigativos e os itens pessoais (`dados.py`, ITENS; o caderno de Fernando é um item só, com as páginas 1 a 5 para folhear ao ampliar, e a 6 fica para o fim; o gravador vem dentro da bolsa da Amie e o sensor dentro da maleta da Clara) aparecem em locais sorteados a cada partida (a foto da família é fixa, na mesa do centro da Central de segurança), entre 7 locais acessíveis por sala (`mapas/locais-itens.json`, gerado por `ferramentas/escolher_locais.py`). Ao achar um item, a personagem comenta ("fala"), e o item vai para o mapa mental com o palpite dela ("palpite"). Se mudar um mapa ou objeto, rode de novo `ferramentas/escolher_locais.py` e `ferramentas/gerar_miniaturas.py`.
