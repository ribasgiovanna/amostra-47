"""Sintetiza os sons do jogo (sem gravações) e salva em ``sons/``.

- ``tic-1..3.wav``: "tic" das letras na caixa de texto (três alturas, para variar);
- ``pista.wav``: pista coletada (duas notas de sino, com eco);
- ``menu-mover.wav``: batida grave de bumbo ao passar entre opções do menu;
- ``menu-confirmar.wav``: bipe curto, mais agudo que a batida, ao escolher uma opção;
- ``ambiente.wav``: zumbido do laboratório em loop (rede elétrica + ventilação), 8 s.

Uso (na pasta src/jogo):
    python ferramentas/gerar_sons.py
"""
import os
import wave

import numpy as np

TAXA = 44100
PASTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sons")
sorteio = np.random.default_rng(47)


def salvar(nome, onda, volume=0.8):
    onda = onda / (np.abs(onda).max() or 1) * volume
    dados = (np.clip(onda, -1, 1) * 32767).astype(np.int16)
    with wave.open(os.path.join(PASTA, nome), "wb") as arquivo:
        arquivo.setnchannels(1)
        arquivo.setsampwidth(2)
        arquivo.setframerate(TAXA)
        arquivo.writeframes(dados.tobytes())
    print(nome, f"{len(onda) / TAXA:.2f}s")


def tempo(segundos):
    return np.arange(int(segundos * TAXA)) / TAXA


def suavizar(onda, janela):
    """Passa-baixa simples (média móvel)."""
    return np.convolve(onda, np.ones(janela) / janela, mode="same")


def tic(frequencia):
    t = tempo(0.035)
    # Triângulo curto com queda rápida: um clique suave, tipo terminal antigo.
    tri = 2 * np.abs(2 * ((t * frequencia) % 1) - 1) - 1
    envelope = np.exp(-t * 140) * np.minimum(1, t * 2000)
    return suavizar(tri * envelope, 6)


def sino(frequencia, duracao):
    t = tempo(duracao)
    harmonicos = (np.sin(2 * np.pi * frequencia * t) + 0.35 * np.sin(2 * np.pi * frequencia * 2.01 * t)
                  + 0.15 * np.sin(2 * np.pi * frequencia * 3.02 * t))
    return harmonicos * np.exp(-t * 5) * np.minimum(1, t * 400)


def pista():
    primeira, segunda = sino(659.25, 0.9), sino(987.77, 1.1)  # mi e si
    onda = np.zeros(int(1.6 * TAXA))
    onda[:len(primeira)] += primeira
    atraso = int(0.12 * TAXA)
    onda[atraso:atraso + len(segunda)] += segunda
    # Eco curto, como numa sala vazia.
    for atraso, ganho in ((0.09, 0.35), (0.19, 0.18)):
        n = int(atraso * TAXA)
        onda[n:] += onda[:-n] * ganho
    return onda


def ambiente():
    duracao = 8.0  # as frequências fecham ciclos inteiros em 8 s, então o loop não emenda
    t = tempo(duracao)
    rede = (np.sin(2 * np.pi * 60 * t) + 0.5 * np.sin(2 * np.pi * 120 * t) + 0.12 * np.sin(2 * np.pi * 180 * t))
    pulsar = 1.0  # volume constante (sem "respirar")
    # Ventilação: ruído filtrado, com as pontas cruzadas para o loop ficar contínuo.
    extra = int(0.5 * TAXA)
    ruido = suavizar(sorteio.normal(size=len(t) + extra), 40)
    ruido = suavizar(ruido, 40)
    mistura = np.linspace(0, 1, extra)
    ventilacao = ruido[:len(t)].copy()
    ventilacao[:extra] = ruido[len(t):] * (1 - mistura) + ventilacao[:extra] * mistura
    ventilacao /= np.abs(ventilacao).max()
    # Chiado de lâmpada fluorescente, bem baixo.
    lampada = np.sign(np.sin(2 * np.pi * 120 * t)) * 0.04
    return rede * 0.55 * pulsar + ventilacao * 0.5 + lampada


def menu_mover():
    # Batida de bumbo baixinha: a altura despenca de 140 Hz para 50 Hz, com um ataque curto.
    t = tempo(0.16)
    frequencia = 50 + 90 * np.exp(-t * 35)
    fase = 2 * np.pi * np.cumsum(frequencia) / TAXA
    corpo = np.sin(fase) * np.exp(-t * 22)
    ataque = suavizar(sorteio.normal(size=len(t)), 8) * np.exp(-t * 400) * 0.3
    return (corpo + ataque) * np.minimum(1, t * 2000)


def menu_confirmar():
    # Bipe curto e seco, mais agudo que a batida de trocar de opção: 330 Hz (mi) com oitava.
    t = tempo(0.11)
    fase = 2 * np.pi * 330 * t
    onda = np.sin(fase) + 0.35 * np.sin(2 * fase) + 0.1 * np.sin(3 * fase)
    envelope = np.minimum(1, t * 1500) * np.exp(-t * 32)  # começa na hora e some rápido
    return suavizar(onda * envelope, 3)


def main():
    os.makedirs(PASTA, exist_ok=True)
    for n, frequencia in enumerate((780, 860, 940), 1):
        salvar(f"tic-{n}.wav", tic(frequencia), 0.6)
    salvar("pista.wav", pista(), 0.7)
    salvar("menu-mover.wav", menu_mover(), 0.6)
    salvar("menu-confirmar.wav", menu_confirmar(), 0.7)
    salvar("ambiente.wav", ambiente(), 0.6)


if __name__ == "__main__":
    main()
