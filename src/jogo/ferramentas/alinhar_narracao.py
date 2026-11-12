"""Alinha cada frase de ``cutscenes/abertura.txt`` a um trecho da narração gravada.

Uso: python ferramentas/alinhar_narracao.py "<áudio da narração>"
Copia o áudio para ``cutscenes/abertura-narracao.mp3`` e gera ``cutscenes/abertura-tempos.json``
com, para cada frase, ``[início, fim da fala]`` em segundos.

Sem reconhecimento de voz: acha as pausas do áudio (trechos de silêncio) e escolhe, por
programação dinâmica, em quais pausas as frases trocam, de modo que a duração de cada
trecho combine com o tamanho da frase e as trocas caiam nas pausas mais longas.
Para corrigir à mão, edite o JSON (os números são segundos do áudio).
"""
import json
import math
import os
import shutil
import sys

import numpy as np
import pygame

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cutscene import separar_frases  # noqa: E402

PASTA_JOGO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JANELA = 0.05  # segundos por amostra de energia
PAUSA_MINIMA = 0.15  # silêncio mais curto que isso não conta como pausa
PESO_PAUSA = 1.5  # o quanto preferir trocar de frase nas pausas longas


def energia(arquivo):
    pygame.mixer.init(44100, -16, 1)
    som = pygame.mixer.Sound(arquivo)
    a = pygame.sndarray.array(som).astype(float)
    if a.ndim > 1:
        a = a.mean(axis=1)
    passo = int(44100 * JANELA)
    n = len(a) // passo
    return np.sqrt((a[:n * passo].reshape(n, passo) ** 2).mean(axis=1))


def pausas(e):
    """(meio, duração, começo, fim) de cada trecho silencioso, em segundos."""
    limiar = max(np.percentile(e, 10) * 3, np.percentile(e, 50) * 0.2)
    quieto = e < limiar
    trechos, i = [], 0
    while i < len(e):
        if quieto[i]:
            j = i
            while j < len(e) and quieto[j]:
                j += 1
            dur = (j - i) * JANELA
            if dur >= PAUSA_MINIMA:
                trechos.append(((i + j) / 2 * JANELA, dur, i * JANELA, j * JANELA))
            i = j
        else:
            i += 1
    return trechos, limiar


def main(arquivo):
    with open(os.path.join(PASTA_JOGO, "cutscenes", "abertura.txt"), encoding="utf-8") as f:
        frases = separar_frases(f.read())
    e = energia(arquivo)
    total = len(e) * JANELA
    trechos, limiar = pausas(e)
    falando = np.nonzero(e >= limiar)[0]
    inicio_fala, fim_fala = falando[0] * JANELA, (falando[-1] + 1) * JANELA
    # Pontos de troca possíveis: começo, pausas e fim.
    pontos = [inicio_fala] + [t[0] for t in trechos if inicio_fala < t[0] < fim_fala] + [fim_fala]
    peso_pausa = [0.0] + [t[1] for t in trechos if inicio_fala < t[0] < fim_fala] + [0.0]
    # Frases só de pontuação ("…") valem como uma pausa curta.
    letras = [max(3, sum(c.isalnum() for c in f)) for f in frases]
    taxa = sum(letras) / (fim_fala - inicio_fala)  # letras por segundo, na média
    n, p = len(frases), len(pontos)
    INF = float("inf")
    custo = [[INF] * p for _ in range(n + 1)]
    volta = [[-1] * p for _ in range(n + 1)]
    custo[0][0] = 0.0
    for k in range(1, n + 1):
        esperado = letras[k - 1] / taxa
        for j in range(1, p):
            melhor, de = INF, -1
            for i in range(j):
                if custo[k - 1][i] == INF:
                    continue
                dur = pontos[j] - pontos[i]
                if dur > esperado * 4 + 6:
                    continue
                c = custo[k - 1][i] + math.log((dur + 0.5) / (esperado + 0.5)) ** 2
                if j < p - 1:
                    c -= PESO_PAUSA * min(peso_pausa[j], 2.0) * 0.3
                if c < melhor:
                    melhor, de = c, i
            custo[k][j], volta[k][j] = melhor, de
    # Termina obrigatoriamente no fim da fala.
    limites, j = [p - 1], p - 1
    for k in range(n, 0, -1):
        j = volta[k][j]
        limites.append(j)
    limites.reverse()
    tempos = []
    for k in range(n):
        ini, fim = pontos[limites[k]], pontos[limites[k + 1]]
        # O fim da fala é o começo do silêncio que separa da próxima frase.
        fim_real = next((t[2] for t in trechos if abs(t[0] - fim) < 1e-6), fim)
        tempos.append([round(ini, 2), round(max(ini + 0.3, fim_real), 2)])
    destino = os.path.join(PASTA_JOGO, "cutscenes", "abertura-narracao.mp3")
    if os.path.abspath(arquivo) != os.path.abspath(destino):
        shutil.copyfile(arquivo, destino)
    with open(os.path.join(PASTA_JOGO, "cutscenes", "abertura-tempos.json"), "w", encoding="utf-8") as f:
        json.dump({"duracao": round(total, 2), "frases": tempos}, f, ensure_ascii=False, indent=1)
    for (ini, fim), frase in zip(tempos, frases):
        print(f"{ini:7.2f} {fim:7.2f}  {frase[:70]}")
    print(f"{n} frases, {len(trechos)} pausas, áudio de {total:.1f} s")


if __name__ == "__main__":
    main(sys.argv[1])
