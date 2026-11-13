"""Gera o executável do jogo para Windows (não precisa de Python para rodar).

Uso, a partir da pasta a47:
    pip install pyinstaller
    python src/jogo/ferramentas/gerar_exe.py

Resultado: dist/Amostra 47/Amostra 47.exe (mande a pasta "Amostra 47" inteira, zipada).
Rode de novo a cada atualização do jogo.
"""

import os
import sys

import PyInstaller.__main__
import pygame

JOGO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # src/jogo
RAIZ = os.path.dirname(os.path.dirname(JOGO))  # a47
NOME = "Amostra 47"
PASTAS = ["cutscenes", "fontes", "itens", "mapas", "sons", "sprites"]
# Pacotes do ambiente que o jogo não usa (evita um executável gigante).
FORA = ["numpy", "scipy", "matplotlib", "PIL", "torch", "faster_whisper", "ctranslate2", "av",
        "pandas", "tkinter", "IPython", "jupyter", "notebook", "setuptools", "pkg_resources"]


def gerar_icone(destino):
    """Ícone do .exe a partir da arte do crachá."""
    pygame.init()
    imagem = pygame.image.load(os.path.join(JOGO, "itens", "cracha-de-acesso.png"))
    lado = max(imagem.get_size())
    quadrado = pygame.Surface((lado, lado), pygame.SRCALPHA)
    quadrado.blit(imagem, imagem.get_rect(center=(lado // 2, lado // 2)))
    png = destino.replace(".ico", ".png")
    pygame.image.save(pygame.transform.smoothscale(quadrado, (256, 256)), png)
    # .ico com um PNG de 256×256 dentro (aceito pelo Windows a partir do Vista).
    dados = open(png, "rb").read()
    cabecalho = (b"\0\0\1\0\1\0" + bytes([0, 0, 0, 0]) + (1).to_bytes(2, "little") + (32).to_bytes(2, "little")
                 + len(dados).to_bytes(4, "little") + (22).to_bytes(4, "little"))
    open(destino, "wb").write(cabecalho + dados)
    os.remove(png)


def main():
    build = os.path.join(RAIZ, "build")
    os.makedirs(build, exist_ok=True)
    icone = os.path.join(build, "amostra47.ico")
    gerar_icone(icone)
    argumentos = [
        os.path.join(JOGO, "amostra47.py"),
        "--name", NOME,
        "--noconsole",
        "--noconfirm",
        "--clean",
        "--icon", icone,
        "--distpath", os.path.join(RAIZ, "dist"),
        "--workpath", build,
        "--specpath", build,
        "--paths", JOGO,
        "--collect-binaries", "imageio_ffmpeg",  # ffmpeg dos vídeos da abertura e do final
        "--hidden-import", "imageio_ffmpeg",
    ]
    for pasta in PASTAS:
        argumentos += ["--add-data", f"{os.path.join(JOGO, pasta)}{os.pathsep}{pasta}"]
    for modulo in FORA:
        argumentos += ["--exclude-module", modulo]
    PyInstaller.__main__.run(argumentos)
    print(f"\nPronto: {os.path.join(RAIZ, 'dist', NOME, NOME + '.exe')}")


if __name__ == "__main__":
    sys.exit(main())
