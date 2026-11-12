"""Prepara o mapa da floresta da abertura para repetir na vertical sem emenda.

Uso: python ferramentas/preparar_floresta.py "<imagem original>"
Gera ``mapas/floresta-loop.png``. As primeiras FAIXA linhas viram uma mistura gradual
das últimas linhas com as primeiras, e a imagem perde FAIXA linhas de altura: assim a
borda de baixo continua exatamente na de cima.
"""
import os
import sys

import numpy as np
import pygame

FAIXA = 80  # linhas (na escala original de 887 px de largura) usadas na transição do loop
LARGURA_BASE = 887  # largura do mapa original; as coordenadas da cutscene usam essa escala
ESCALA = 3  # imagens maiores (upscale) são reduzidas para LARGURA_BASE * ESCALA

PASTA_JOGO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    original = pygame.image.load(sys.argv[1])
    w, h = original.get_size()
    if w > LARGURA_BASE * ESCALA:
        original = pygame.transform.smoothscale(original, (LARGURA_BASE * ESCALA, round(h * LARGURA_BASE * ESCALA / w)))
    faixa = FAIXA * original.get_width() // LARGURA_BASE
    a = pygame.surfarray.array3d(original).transpose(1, 0, 2).astype(float)  # (altura, largura, 3)
    altura = a.shape[0]
    saida = a[:altura - faixa].copy()
    peso = (np.arange(faixa) / faixa)[:, None, None]
    saida[:faixa] = a[altura - faixa:] * (1 - peso) + a[:faixa] * peso
    imagem = pygame.surfarray.make_surface(saida.round().astype(np.uint8).transpose(1, 0, 2))
    destino = os.path.join(PASTA_JOGO, "mapas", "floresta-loop.png")
    pygame.image.save(imagem, destino)
    print(destino, imagem.get_size())


if __name__ == "__main__":
    main()
