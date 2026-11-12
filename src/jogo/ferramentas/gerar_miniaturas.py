"""Gera as miniaturas das salas (com os objetos) usadas no mapa mental.

Cada sala é desenhada inteira, com os objetos por cima, numa resolução baixa
(LADO x LADO), e salva em ``mapas/miniaturas/<chave>.png``.

Uso (na pasta src/jogo):
    python ferramentas/gerar_miniaturas.py
"""
import os
import sys

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pygame  # noqa: E402

from dados import MAPAS  # noqa: E402
from entidades import Mapa, caminho  # noqa: E402

LADO = 144  # pixels de cada miniatura (baixa qualidade de propósito)


def main():
    pygame.init()
    pygame.display.set_mode((1, 1))
    pasta = caminho("mapas/miniaturas")
    os.makedirs(pasta, exist_ok=True)
    for chave, dados in MAPAS.items():
        mapa = Mapa(dados)
        largura, altura = mapa.tamanho
        zoom = 2  # desenha numa resolução média e depois reduz
        tela = pygame.Surface((largura * zoom, altura * zoom))
        visao = pygame.Rect(0, 0, largura, altura)
        mapa.desenhar(tela, visao, zoom)
        mapa.desenhar_objetos(tela, visao, zoom, 10 ** 6, atras=True)
        mini = pygame.transform.smoothscale(tela, (LADO, round(LADO * altura / largura)))
        pygame.image.save(mini, os.path.join(pasta, f"{chave}.png"))
        print(chave)


if __name__ == "__main__":
    main()
