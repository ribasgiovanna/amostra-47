"""Sintetiza os sons do jogo (sem gravações) e salva em ``sons/``.

- ``tic-1..3.wav``: "tic" das letras na caixa de texto (três alturas, para variar);
- ``pista.wav``: pista coletada (duas notas de sino, com eco);
- ``menu-mover.wav``: batida grave de bumbo ao passar entre opções do menu;
- ``menu-confirmar.wav``: bipe curto, mais agudo que a batida, ao escolher uma opção;
- ``tecla-1..3.wav``: toque macio ao escrever nas anotações;
- ``ambiente.wav``: zumbido do laboratório em loop (rede elétrica + ventilação), 8 s;
- ``floresta.wav``: floresta em loop (vento, folhas, pássaros e insetos), 40 s.

Uso (na pasta src/jogo):
    python ferramentas/gerar_sons.py            # todos
    python ferramentas/gerar_sons.py floresta   # só a floresta
"""
import os
import sys
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


def tecla(frequencia):
    # Toque de escrever: um "tic" leve e agudo de tecla, curtinho, sem peso grave.
    t = tempo(0.025)
    clique = np.sin(2 * np.pi * frequencia * t) * np.exp(-t * 260)
    estalo = suavizar(sorteio.normal(size=len(t)), 2) * np.exp(-t * 900) * 0.35
    return (clique + estalo) * np.minimum(1, t * 6000)


def ruido_em_loop(rng, n, filtro):
    """Ruído filtrado que emenda sem clique no fim do loop (pontas cruzadas)."""
    extra = int(1.0 * TAXA)
    ruido = filtro(rng.normal(size=n + extra))
    mistura = np.linspace(0, 1, extra)
    saida = ruido[:n].copy()
    saida[:extra] = ruido[n:] * (1 - mistura) + saida[:extra] * mistura
    return saida / (np.abs(saida).max() or 1)


def passa_baixa(onda, corte):
    """Filtro de um polo (mais suave que a média móvel), via FFT para ser rápido."""
    espectro = np.fft.rfft(onda)
    f = np.fft.rfftfreq(len(onda), 1 / TAXA)
    return np.fft.irfft(espectro / np.sqrt(1 + (f / corte) ** 2), len(onda))


def passa_faixa(onda, baixo, alto):
    espectro = np.fft.rfft(onda)
    f = np.fft.rfftfreq(len(onda), 1 / TAXA)
    espectro[(f < baixo) | (f > alto)] = 0
    return np.fft.irfft(espectro, len(onda))


def colocar(destino, som, inicio):
    """Soma o som em ``destino`` a partir de ``inicio``, dando a volta no fim (loop)."""
    idx = (inicio + np.arange(len(som))) % len(destino)
    np.add.at(destino, idx, som)


def floresta():
    rng = np.random.default_rng(470)
    duracao = 40.0
    t = tempo(duracao)
    n = len(t)
    # Vento: ruído grave que sobe e desce devagar (ciclos inteiros em 40 s).
    vento = ruido_em_loop(rng, n, lambda r: passa_baixa(r, 350))
    vento *= 0.55 + 0.25 * np.sin(2 * np.pi * t / 20) + 0.2 * np.sin(2 * np.pi * t / 8 + 1)
    # Folhas: rajadas de chiado agudo que acompanham o vento.
    folhas = np.zeros(n)
    for _ in range(26):
        d = rng.uniform(0.6, 2.2)
        tt = tempo(d)
        envelope = np.sin(np.pi * tt / d) ** 2
        rajada = passa_faixa(rng.normal(size=len(tt)), 1500, 6000) * envelope * rng.uniform(0.3, 1)
        colocar(folhas, rajada, rng.integers(n))
    # Pássaros: frases de 2 a 6 pios com subida/descida de altura.
    passaros = np.zeros(n)
    for _ in range(16):
        base = rng.uniform(2200, 4200)
        inicio = rng.integers(n)
        for k in range(rng.integers(2, 7)):
            d = rng.uniform(0.05, 0.16)
            tt = tempo(d)
            curva = base * (1 + rng.uniform(-0.25, 0.35) * tt / d)
            fase = 2 * np.pi * np.cumsum(curva) / TAXA
            pio = np.sin(fase) * np.sin(np.pi * tt / d) ** 1.5
            pio += 0.3 * np.sin(2 * fase) * np.sin(np.pi * tt / d) ** 2  # harmônico
            colocar(passaros, pio * rng.uniform(0.25, 0.7), inicio + int(k * TAXA * rng.uniform(0.12, 0.25)))
    # Insetos: zumbido agudo pulsando (grilos), bem baixo e contínuo.
    pulso = (np.sin(2 * np.pi * 32 * t) > 0.2).astype(float)
    pulso = suavizar(pulso, 60) * (0.6 + 0.4 * np.sin(2 * np.pi * t / 10) ** 2)
    insetos = np.sin(2 * np.pi * 4600 * t) * pulso
    return vento * 0.5 + folhas * 0.12 + passaros * 0.35 + insetos * 0.04


def main():
    os.makedirs(PASTA, exist_ok=True)
    if sys.argv[1:] == ["floresta"]:
        salvar("floresta.wav", floresta(), 0.6)
        return
    for n, frequencia in enumerate((780, 860, 940), 1):
        salvar(f"tic-{n}.wav", tic(frequencia), 0.6)
    salvar("pista.wav", pista(), 0.7)
    salvar("menu-mover.wav", menu_mover(), 0.6)
    salvar("menu-confirmar.wav", menu_confirmar(), 0.7)
    salvar("ambiente.wav", ambiente(), 0.6)
    salvar("floresta.wav", floresta(), 0.6)
    for n, frequencia in enumerate((1900, 2150, 2400), 1):
        salvar(f"tecla-{n}.wav", tecla(frequencia), 0.5)


if __name__ == "__main__":
    main()
