"""Converte o export (.zip) do criador de personagens do PixelLab para sprites do jogo.

Gera, para cada direção exportada, `parado-<direção>.png` e `andando-<direção>.png`
(tira de quadros), em quadros de 80 x 80: o personagem de 64 px com folga em cima,
para a cabeça não ser cortada quando sobe na caminhada. Os pés ficam na última linha.

Uso:
    python ferramentas/importar_pixellab.py ARQUIVO.zip PASTA_SAIDA
"""
import io
import json
import os
import sys
import zipfile

from PIL import Image

TAMANHO = 80  # quadro de saída; o personagem do PixelLab tem 64 px
# Direção do PixelLab -> nome usado em entidades.py.
DIRECOES = {
    "south": "frente",
    "north": "costas",
    "east": "lado",
    "west": "esquerda",
    "south-east": "frente-direita",
    "south-west": "frente-esquerda",
    "north-east": "costas-direita",
    "north-west": "costas-esquerda",
}


def main(arquivo_zip, pasta_saida):
    with zipfile.ZipFile(arquivo_zip) as pacote:
        abrir = lambda nome: Image.open(io.BytesIO(pacote.read(nome))).convert("RGBA")
        estado = json.loads(pacote.read("metadata.json"))["states"][0]
        quadros = estado["frames"]
        caminhada = next(iter(quadros["animations"].values()), {})
        os.makedirs(pasta_saida, exist_ok=True)
        for direcao, nome in DIRECOES.items():
            if direcao not in quadros["rotations"]:
                continue
            original = abrir(quadros["rotations"][direcao])
            pes = original.getbbox()[3]
            parado = Image.new("RGBA", (TAMANHO, TAMANHO))
            parado.paste(original, ((TAMANHO - original.width) // 2, TAMANHO - pes))
            parado.save(os.path.join(pasta_saida, f"parado-{nome}.png"))
            if direcao not in caminhada:
                continue
            imagens = [abrir(arquivo) for arquivo in caminhada[direcao]]
            largura = imagens[0].width
            base = max(imagem.getbbox()[3] for imagem in imagens)
            x0, y0 = (largura - TAMANHO) // 2, base - TAMANHO
            tira = Image.new("RGBA", (TAMANHO * len(imagens), TAMANHO))
            for i, imagem in enumerate(imagens):
                tira.paste(imagem.crop((x0, y0, x0 + TAMANHO, y0 + TAMANHO)), (i * TAMANHO, 0))
            tira.save(os.path.join(pasta_saida, f"andando-{nome}.png"))
            print(f"{direcao:10} -> {nome:16} {len(imagens)} quadros")


if __name__ == "__main__":
    main(*sys.argv[1:3])
