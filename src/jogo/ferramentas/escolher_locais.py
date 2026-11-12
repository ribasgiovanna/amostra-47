"""Escolhe 7 locais acessíveis em cada sala, onde os itens podem aparecer.

Para cada sala (antes e depois do incidente), procura posições em que o jogador
cabe com folga das paredes e dos objetos, que dá para alcançar andando a partir
da porta e que ficam longe das portas. Entre elas, escolhe 7 bem espalhadas
(cada nova é a mais distante das já escolhidas). Salva em
``mapas/locais-itens.json``: {sala: [[x, y], ...]} (posição dos pés, em unidades).

Uso (na pasta src/jogo):
    python ferramentas/escolher_locais.py
"""
import json
import os
import sys
from collections import deque

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pygame  # noqa: E402

from dados import MAPAS  # noqa: E402
from entidades import Mapa, caminho  # noqa: E402

QUANTIDADE = 7
PASSO = 6  # grade da busca (unidades)
FOLGA = 18  # distância mínima de paredes e objetos
LONGE_DA_PORTA = 110


def escolher_locais(mapa, portas, quantidade=QUANTIDADE):
    """Devolve `quantidade` posições (x, y) acessíveis e espalhadas na sala."""
    pes = pygame.Rect(0, 0, 26, 14)  # mesma caixa de colisão dos pés do jogador

    def livre(x, y, folga=0):
        pes.midbottom = (x, y)
        return mapa.livre(pes.inflate(folga * 2, folga * 2))

    largura, altura = mapa.tamanho
    # Acessível: a partir da porta, andando pela grade só por lugares livres.
    inicio = min(((x, y) for x in range(0, largura, PASSO) for y in range(0, altura, PASSO) if livre(x, y)),
                 key=lambda p: (p[0] - portas[0][0]) ** 2 + (p[1] - portas[0][1]) ** 2)
    alcancavel, fila = {inicio}, deque([inicio])
    while fila:
        x, y = fila.popleft()
        for dx, dy in ((PASSO, 0), (-PASSO, 0), (0, PASSO), (0, -PASSO)):
            vizinho = (x + dx, y + dy)
            if vizinho not in alcancavel and 0 <= vizinho[0] < largura and 0 <= vizinho[1] < altura \
                    and livre(*vizinho):
                alcancavel.add(vizinho)
                fila.append(vizinho)
    perto_da_porta = lambda p: any((p[0] - a) ** 2 + (p[1] - b) ** 2 < LONGE_DA_PORTA ** 2 for a, b in portas)
    # Também fora da arte dos objetos (senão o brilho do item fica escondido atrás deles).
    atras_de_objeto = lambda p: any(pygame.Rect(o["retangulo"]).inflate(20, 20).collidepoint(p[0], p[1] - 16)
                                    for o in mapa.objetos)
    candidatos = [p for p in alcancavel if livre(*p, FOLGA) and not perto_da_porta(p) and not atras_de_objeto(p)]
    # Espalhados: começa pelo mais perto do centro e vai pegando o mais distante dos escolhidos.
    centro = (largura / 2, altura / 2)
    escolhidos = [min(candidatos, key=lambda p: (p[0] - centro[0]) ** 2 + (p[1] - centro[1]) ** 2)]
    while len(escolhidos) < quantidade:
        escolhidos.append(max(candidatos, key=lambda p: min((p[0] - a) ** 2 + (p[1] - b) ** 2
                                                             for a, b in escolhidos)))
    return [list(p) for p in escolhidos]


def main():
    pygame.init()
    pygame.display.set_mode((1, 1))
    locais = {}
    for chave, dados in MAPAS.items():
        locais[chave] = escolher_locais(Mapa(dados), dados["portas"])
        print(chave, locais[chave])
    with open(caminho("mapas/locais-itens.json"), "w", encoding="utf-8") as arquivo:
        json.dump(locais, arquivo, indent=1)


if __name__ == "__main__":
    main()
