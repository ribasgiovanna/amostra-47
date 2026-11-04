"""Cutscene de abertura: a imagem do Complexo Helix descendo devagar com a narração da Giulia.

A narração fica em ``cutscenes/abertura.txt`` (uma frase por caixa de texto) e a imagem
em ``cutscenes/abertura-helix.webp``. A imagem aparece inteira na largura, um pouco
ampliada, e desliza bem devagar do céu até a entrada, acompanhando as frases: na última,
mostra a Giulia diante da porta. No fim, a tela escurece e o jogo começa.
"""
import random
import re

import pygame

from entidades import caminho

LETRAS_POR_SEGUNDO = 45
SAIDA = 1.0  # segundos do fade para o preto no fim
CONTEMPLAR = 3.0  # segundos mostrando a Giulia sem caixa, depois da última frase
AMPLIACAO = 1.5  # a imagem fica 1,5x maior que a tela, para sobrar altura para deslizar
SUAVIDADE = 0.25  # quanto menor, mais devagar a câmera alcança o ponto da frase atual

# Caixa de texto: tamanho fixo (unidades de interface, base 540 px de altura).
CAIXA_LARGURA, CAIXA_ALTURA = 720, 124
VERDES = [(46, 78, 40), (66, 104, 50), (96, 138, 62), (138, 170, 78)]


def separar_frases(texto):
    frases = []
    for paragrafo in texto.splitlines():
        partes = re.split(r"(?<=[.!?…])\s+(?=[A-ZÀ-Ú0-9“\"…])", paragrafo.strip())
        frases += [p for p in partes if p]
    return frases


def quebrar(fonte, texto, largura):
    linhas, atual = [], ""
    for palavra in texto.split():
        teste = f"{atual} {palavra}".strip()
        if fonte.size(teste)[0] <= largura or not atual:
            atual = teste
        else:
            linhas.append(atual)
            atual = palavra
    return linhas + ([atual] if atual else [])


def desenhar_moldura(px):
    """Moldura da caixa (desenhada uma vez): vidro escuro esverdeado, borda fina e musgo em pixels."""
    largura, altura = px(CAIXA_LARGURA), px(CAIXA_ALTURA)
    pixel = px(3)  # tamanho do "pixel" do musgo, para combinar com a pixel art
    folga = 6 * pixel  # espaço acima da caixa para o musgo que cresce sobre a borda
    superficie = pygame.Surface((largura, altura + folga), pygame.SRCALPHA)
    caixa = pygame.Rect(0, folga, largura, altura)
    superficie.fill((14, 22, 19, 205), caixa)
    pygame.draw.rect(superficie, (88, 112, 92), caixa, 1)
    sorteio = random.Random(47)  # sempre o mesmo musgo

    def bloco(cor, x, y):
        superficie.fill(cor, (x, y, pixel, pixel))

    def tufo(x, colunas, altura_max):
        # Musgo sobre a borda de cima: mais alto no meio do tufo.
        for c in range(colunas):
            meio = 1 - abs(c - colunas / 2) / (colunas / 2 + 0.01)
            h = max(1, round(altura_max * meio + sorteio.uniform(-0.8, 0.8)))
            for k in range(h):
                topo = k == h - 1
                cor = VERDES[sorteio.randint(2, 3)] if topo else VERDES[min(3, k // 2 + sorteio.randint(0, 1))]
                bloco(cor, x + c * pixel, folga - k * pixel)

    def lateral(x, quantos, chance):
        # Musgo descendo pela borda lateral.
        for c in range(quantos):
            if sorteio.random() < chance * (1 - c / quantos):
                bloco(VERDES[sorteio.randint(0, 2)], x, folga + c * pixel)

    def fio(x, comprimento):
        # Fio de trepadeira pendurado na borda de cima, por dentro da caixa.
        for k in range(comprimento):
            bloco(VERDES[1], x, folga + k * pixel)
        bloco(VERDES[2], x + pixel, folga + (comprimento - 1) * pixel)

    tufo(0, 18, 5)
    tufo(int(largura * 0.36) // pixel * pixel, 9, 2)
    tufo(int(largura * 0.63) // pixel * pixel, 6, 2)
    tufo(largura - 14 * pixel, 14, 6)
    lateral(0, 12, 0.95)
    lateral(largura - pixel, 16, 0.95)
    fio(5 * pixel, 4)
    fio(largura - 9 * pixel, 6)
    return superficie, folga


class CaixaTexto:
    """Caixa de diálogo de tamanho fixo (vidro verde-escuro com musgo), usada na cutscene e no jogo."""

    def __init__(self):
        self.moldura = None  # (escala, superfície, folga), refeita se a tela mudar

    def desenhar(self, tela, px, nome, frase, letras, seta):
        if self.moldura is None or self.moldura[0] != px(100):
            self.moldura = (px(100), *desenhar_moldura(px))
            self.fonte = pygame.font.SysFont("consolas", px(16))
            self.fonte_nome = pygame.font.SysFont("consolas", px(14), bold=True)
            self.fonte_dica = pygame.font.SysFont("consolas", px(13))
        _, moldura, folga = self.moldura
        largura_tela, altura_tela = tela.get_size()
        lugar = moldura.get_rect(midbottom=(largura_tela // 2, altura_tela - px(18)))
        tela.blit(moldura, lugar)
        caixa = pygame.Rect(lugar.x, lugar.y + folga, lugar.width, lugar.height - folga)
        rotulo_nome = self.fonte_nome.render(nome.upper(), True, (150, 190, 120))
        tela.blit(rotulo_nome, (caixa.x + px(14), caixa.y + px(10)))
        linhas = quebrar(self.fonte, frase, caixa.width - px(28))
        altura_linha = self.fonte.get_linesize()
        # Escreve letra por letra, mas quebra as linhas pela frase inteira (não pulam).
        restante = int(letras)
        for i, linha in enumerate(linhas):
            if restante <= 0:
                break
            rotulo = self.fonte.render(linha[:restante], True, (226, 230, 222))
            restante -= len(linha) + 1
            tela.blit(rotulo, (caixa.x + px(14), caixa.y + px(30) + i * altura_linha))
        if seta:
            marca = self.fonte_dica.render("▼", True, (150, 190, 120))
            tela.blit(marca, marca.get_rect(bottomright=(caixa.right - px(10), caixa.bottom - px(6))))


class Cutscene:
    def __init__(self):
        self.imagem = pygame.image.load(caminho("cutscenes/abertura-helix.webp")).convert()
        with open(caminho("cutscenes/abertura.txt"), encoding="utf-8") as arquivo:
            self.frases = separar_frases(arquivo.read())
        self.indice = 0
        self.letras = 0.0
        self.descida = 0.0  # 0 = topo da imagem, 1 = base (porta)
        self.tempo_total = 0.0
        self.saindo = None  # tempo do fade final para o preto
        self.contemplando = None  # tempo mostrando a Giulia sem caixa, no fim
        self.terminou = False
        self.ao_escrever = None  # função chamada enquanto as letras aparecem (som)
        self.caixa = CaixaTexto()

    def atual_completa(self):
        return self.letras >= len(self.frases[self.indice])

    def pular(self):
        """Esc (ou fim da narração): escurece até o preto e termina."""
        if self.saindo is None:
            self.saindo = 0.0

    def avancar(self):
        """E/Enter/clique: completa a frase sendo escrita ou passa para a próxima."""
        if self.saindo is not None:
            return
        if not self.atual_completa():
            self.letras = len(self.frases[self.indice])
            return
        if self.indice == len(self.frases) - 1:
            # Última frase: a caixa some e a Giulia fica à vista antes do fade.
            if self.contemplando is None:
                self.contemplando = 0.0
            else:
                self.pular()  # E de novo encurta a espera
            return
        self.indice += 1
        self.letras = 0.0

    def atualizar(self, dt):
        self.tempo_total += dt
        # A câmera persegue, devagar, a altura correspondente à frase atual.
        alvo = self.indice / max(1, len(self.frases) - 1)
        self.descida += (alvo - self.descida) * min(1.0, dt * SUAVIDADE)
        if self.saindo is not None:
            self.saindo += dt
            if self.saindo >= SAIDA:
                self.terminou = True
            return
        if self.contemplando is not None:
            self.descida += (alvo - self.descida) * min(1.0, dt * 1.5)  # termina de chegar na porta
            self.contemplando += dt
            if self.contemplando >= CONTEMPLAR:
                self.pular()
            return
        antes = int(self.letras)
        self.letras = min(len(self.frases[self.indice]), self.letras + LETRAS_POR_SEGUNDO * dt)
        # "Tic" a cada duas letras novas (espaços não contam), se o jogo deu um som.
        novas = self.frases[self.indice][antes:int(self.letras)]
        if self.ao_escrever and any(not c.isspace() and (antes + i) % 2 == 0 for i, c in enumerate(novas)):
            self.ao_escrever()

    def desenhar(self, tela, px):
        tamanho = largura_tela, altura_tela = tela.get_size()
        # Pedaço da imagem na proporção da tela, centrado na largura; desce com a narração.
        iw, ih = self.imagem.get_size()
        largura = iw / AMPLIACAO
        altura = min(ih, largura * altura_tela / largura_tela)
        x = (iw - largura) / 2
        y = (ih - altura) * self.descida
        pedaco = self.imagem.subsurface(pygame.Rect(round(x), round(y), round(largura), round(altura)))
        tela.blit(pygame.transform.smoothscale(pedaco, tamanho), (0, 0))
        if self.contemplando is None:
            self.desenhar_caixa(tela, px)
        escuro = 0.0
        if self.indice == 0 and self.tempo_total < 1.2:
            escuro = 1 - self.tempo_total / 1.2  # entra do preto
        if self.saindo is not None:
            escuro = min(1.0, self.saindo / SAIDA)  # sai para o preto
        if escuro:
            veu = pygame.Surface(tamanho)
            veu.set_alpha(round(255 * escuro))
            tela.blit(veu, (0, 0))

    def desenhar_caixa(self, tela, px):
        seta = self.atual_completa() and int(self.tempo_total * 2) % 2 == 0
        self.caixa.desenhar(tela, px, "Giulia", self.frases[self.indice], self.letras, seta)
        self.fonte_dica = self.caixa.fonte_dica
        largura_tela = tela.get_width()
        dica = self.fonte_dica.render("E continuar · Esc pular", True, (200, 210, 196))
        lugar_dica = dica.get_rect(topright=(largura_tela - px(14), px(12)))
        fundo = pygame.Surface(lugar_dica.inflate(px(12), px(6)).size, pygame.SRCALPHA)
        fundo.fill((14, 22, 19, 190))
        tela.blit(fundo, lugar_dica.inflate(px(12), px(6)))
        tela.blit(dica, lugar_dica)
