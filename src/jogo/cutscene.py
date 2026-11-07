"""Cutscene de abertura: a Giulia caminhando pela floresta e, no fim, o Complexo Helix.

A narração fica em ``cutscenes/abertura.txt`` (uma frase por caixa de texto). Com a
narração gravada (``cutscenes/abertura-narracao.mp3`` e os tempos de cada frase em
``abertura-tempos.json``, gerados por ``ferramentas/alinhar_narracao.py``), cada frase
aparece junto com o trecho falado e é escrita no ritmo da fala, sem bipes; E só completa
o texto. Sem esses arquivos, as frases passam sozinhas com tempo para ler (E adianta).

1. Floresta: ``mapas/floresta-loop.png`` repete na vertical sem fim. O jogador anda com a
   Giulia para cima (W/seta), podendo ir para os lados só dentro da trilha.
2. Na frase ``CORTE_HELIX`` a tela corta para ``cutscenes/abertura-helix.webp``, que desliza
   devagar do céu até a entrada, como antes. No fim, a tela escurece e o jogo começa.
"""
import json
import os
import random
import re

import pygame

from entidades import Jogador, caminho

LETRAS_POR_SEGUNDO = 45
SAIDA = 1.0  # segundos do fade para o preto no fim
CONTEMPLAR = 3.0  # segundos mostrando a Giulia sem caixa, depois da última frase
AMPLIACAO = 1.5  # a imagem fica 1,5x maior que a tela, para sobrar altura para deslizar
SUAVIDADE = 0.25  # quanto menor, mais devagar a câmera alcança o ponto da frase atual
# Tempo de leitura: depois de escrita, a frase fica PAUSA + letras/LEITURA segundos.
PAUSA, LEITURA = 1.2, 50
CORTE_HELIX = "Às vezes, ele permanece"  # início da frase em que a floresta corta para o Helix
CORTE = 1.2  # segundos do corte (escurece e clareia) da floresta para o Helix
ESPERA_NARRACAO = 1.0  # segundos depois do início (entrando do preto) até a voz começar
# Floresta: trilha andável (em pixels da imagem) e altura visível do mundo, igual à das salas.
TRILHA = (368, 520)
LARGURA_FLORESTA = 887  # largura do mundo da floresta; a imagem em si pode ter resolução maior
ALTURA_VISIVEL = 500  # maior = mais zoom out (as salas usam 360); limitado para a imagem cobrir a largura

# Caixa de texto: tamanho fixo (unidades de interface, base 540 px de altura).
CAIXA_LARGURA, CAIXA_ALTURA = 720, 124
# Retratos de quem fala (boca fechada e aberta), por nome mostrado na caixa.
RETRATOS = {"Giulia": "sprites/giulia-pistori/retrato-boca-{}.png"}
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
        self.retratos = {}  # (nome, altura) -> (boca fechada, boca aberta)

    def retrato(self, nome, altura):
        if nome not in RETRATOS:
            return None
        if (nome, altura) not in self.retratos:
            quadros = []
            for boca in ("fechada", "aberta"):
                imagem = pygame.image.load(caminho(RETRATOS[nome].format(boca))).convert_alpha()
                largura = round(imagem.get_width() * altura / imagem.get_height())
                quadros.append(pygame.transform.smoothscale(imagem, (largura, altura)))
            self.retratos[(nome, altura)] = quadros
        return self.retratos[(nome, altura)]

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
        # Retrato dentro da caixa, à esquerda (o texto vai para o lado); a boca mexe enquanto escreve.
        quadros = self.retrato(nome, caixa.height - px(14))
        if quadros:
            falando = letras < len(frase) and int(letras / 9) % 2 == 1
            rosto = quadros[1 if falando else 0]
            lugar_rosto = rosto.get_rect(midleft=(caixa.x + px(10), caixa.centery))
            tela.blit(rosto, lugar_rosto)
            caixa = pygame.Rect(lugar_rosto.right, caixa.y, caixa.right - lugar_rosto.right, caixa.height)
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


def desenhar_legenda(tela, px, fonte, frase, letras):
    """Caixinha menor da abertura, sem retrato nem nome (a narradora só é revelada depois)."""
    largura_tela, altura_tela = tela.get_size()
    largura = min(largura_tela - px(40), px(560))
    linhas = quebrar(fonte, frase, largura - px(32))
    altura_linha = fonte.get_linesize()
    caixa = pygame.Rect(0, 0, largura, len(linhas) * altura_linha + px(20))
    caixa.midbottom = (largura_tela // 2, altura_tela - px(22))
    fundo = pygame.Surface(caixa.size, pygame.SRCALPHA)
    pygame.draw.rect(fundo, (12, 20, 14, 200), fundo.get_rect(), border_radius=px(6))
    pygame.draw.rect(fundo, (150, 190, 120, 140), fundo.get_rect(), 1, border_radius=px(6))
    tela.blit(fundo, caixa)
    restante = int(letras)
    for i, linha in enumerate(linhas):
        if restante <= 0:
            break
        # Cada linha fica centrada pela linha inteira, para o texto não "andar" enquanto escreve.
        x = caixa.centerx - fonte.size(linha)[0] // 2
        tela.blit(fonte.render(linha[:restante], True, (226, 230, 222)), (x, caixa.y + px(10) + i * altura_linha))
        restante -= len(linha) + 1


class TrilhaFloresta:
    """Faz o papel do mapa para o Jogador: só a trilha é livre, e ela não tem fim."""

    def livre(self, retangulo):
        return TRILHA[0] <= retangulo.left and retangulo.right <= TRILHA[1]


class SoParaFrente:
    """Teclas do jogo sem as de andar para baixo (na floresta só se anda para frente)."""

    def __init__(self, teclas):
        self.teclas = teclas

    def __getitem__(self, tecla):
        return False if tecla in (pygame.K_DOWN, pygame.K_s) else self.teclas[tecla]


class VideoAbertura:
    """Toca ``cutscenes/abertura-video.mp4`` quadro a quadro (via ffmpeg), seguindo o relógio do áudio."""

    def __init__(self, arquivo):
        import imageio_ffmpeg
        self.quadros = imageio_ffmpeg.read_frames(arquivo)
        meta = next(self.quadros)
        self.tamanho = tuple(meta["size"])
        self.fps = meta["fps"]
        self.duracao = meta["duration"]
        self.n = -1
        self.superficie = None

    def quadro(self, t):
        alvo = int(max(0.0, t) * self.fps)
        while self.n < alvo:
            try:
                dados = next(self.quadros)
            except StopIteration:
                break
            self.n += 1
            if self.n >= alvo:  # quadros atrasados são pulados sem converter
                self.superficie = pygame.image.frombuffer(dados, self.tamanho, "RGB")
        return self.superficie

    def fechar(self):
        self.quadros.close()


class Cutscene:
    def __init__(self, giulia=None):
        self.imagem = pygame.image.load(caminho("cutscenes/abertura-helix.webp")).convert()
        self.floresta = pygame.image.load(caminho("mapas/floresta-loop.png")).convert()
        self.floresta_escalada = None  # (zoom, superfície) refeita se a tela mudar
        with open(caminho("cutscenes/abertura.txt"), encoding="utf-8") as arquivo:
            self.frases = separar_frases(arquivo.read())
        self.corte = next((i for i, f in enumerate(self.frases) if f.startswith(CORTE_HELIX)), len(self.frases))
        self.trilha = TrilhaFloresta()
        self.giulia = None
        if giulia:
            self.giulia = Jogador(giulia, (sum(TRILHA) // 2, 0))
            self.giulia.direcao = "costas"
        self.cortando = None  # tempo do corte floresta -> Helix
        self.lendo = 0.0  # segundos com a frase atual já toda escrita
        self.indice = 0
        self.letras = 0.0
        self.descida = 0.0  # 0 = topo da imagem, 1 = base (porta)
        self.tempo_total = 0.0
        self.saindo = None  # tempo do fade final para o preto
        self.contemplando = None  # tempo mostrando a Giulia sem caixa, no fim
        self.terminou = False
        self.ao_escrever = None  # função chamada enquanto as letras aparecem (som)
        self.caixa = CaixaTexto()
        # Vídeo da abertura (no lugar da floresta e do Helix); depois dele, já dentro do complexo.
        self.video = None
        arquivo_video = caminho("cutscenes/abertura-video.mp4")
        if os.path.exists(arquivo_video):
            try:
                self.video = VideoAbertura(arquivo_video)
                self.corte = len(self.frases)  # sem corte para o Helix: o vídeo mostra tudo
            except Exception as erro:  # sem imageio-ffmpeg: volta para a floresta
                print("[cutscene] vídeo indisponível:", erro)
        # Narração gravada: [início, fim da fala] de cada frase, em segundos do áudio.
        self.tempos = None
        self.narracao = None
        self.canal = None
        self.volume = 1.0
        arquivo_tempos = caminho("cutscenes/abertura-tempos.json")
        if os.path.exists(arquivo_tempos):
            with open(arquivo_tempos, encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            if len(dados["frases"]) == len(self.frases):
                self.tempos, self.duracao = dados["frases"], dados["duracao"]
                try:
                    # Pela música do mixer: get_pos() dá a posição real do áudio, e o texto e o
                    # vídeo seguem essa posição (sem atraso de carregamento nem deriva).
                    pygame.mixer.music.load(caminho("cutscenes/abertura-narracao.mp3"))
                    self.narracao = True
                except pygame.error:
                    self.narracao = None  # sem áudio: segue o relógio mesmo assim, em silêncio
            else:
                print("[cutscene] abertura-tempos.json não bate com abertura.txt; rode alinhar_narracao.py")

    def atual_completa(self):
        return self.letras >= len(self.frases[self.indice])

    def pular(self):
        """Esc (ou fim da narração): escurece até o preto e termina."""
        if self.saindo is None:
            self.saindo = 0.0
            if self.canal:
                pygame.mixer.music.fadeout(round(SAIDA * 1000))

    def avancar(self):
        """E/Enter/clique: completa a frase sendo escrita ou passa para a próxima."""
        if self.saindo is not None or self.cortando is not None:
            return
        if not self.atual_completa():
            self.letras = len(self.frases[self.indice])
            return
        if self.tempos:
            return  # com narração, quem passa as frases é o áudio
        if self.indice == len(self.frases) - 1:
            # Última frase: a caixa some e a Giulia fica à vista antes do fade.
            if self.contemplando is None:
                self.contemplando = 0.0
            else:
                self.pular()  # E de novo encurta a espera
            return
        if self.indice + 1 == self.corte and self.cortando is None:
            self.cortando = 0.0  # a frase muda no meio do corte, já no preto
            return
        self.indice += 1
        self.letras = 0.0
        self.lendo = 0.0

    @property
    def na_floresta(self):
        return self.indice < self.corte

    def atualizar(self, dt, teclas=None):
        self.tempo_total += min(dt, 0.1)  # um quadro travado (carregando) não adianta o texto
        if self.na_floresta and self.giulia and teclas is not None and not self.video:
            self.giulia.atualizar(dt, SoParaFrente(teclas), self.trilha)
        if self.cortando is not None:
            self.cortando += dt
            if self.cortando >= CORTE / 2 and self.na_floresta:
                self.indice, self.letras, self.lendo = self.corte, 0.0, 0.0
            if self.cortando >= CORTE:
                self.cortando = None
            return
        # Helix: a câmera persegue, devagar, a altura correspondente à frase atual.
        alvo = max(0, self.indice - self.corte) / max(1, len(self.frases) - 1 - self.corte)
        self.descida += (alvo - self.descida) * min(1.0, dt * SUAVIDADE)
        if self.saindo is not None:
            self.saindo += dt
            if self.saindo >= SAIDA:
                self.terminou = True
                if self.video:
                    self.video.fechar()
            return
        if self.contemplando is not None:
            self.descida += (alvo - self.descida) * min(1.0, dt * 1.5)  # termina de chegar na porta
            self.contemplando += dt
            if self.contemplando >= CONTEMPLAR:
                self.pular()
            return
        if self.tempos:
            self.seguir_narracao(dt)
            return
        if self.atual_completa():
            # Passa sozinha depois do tempo de leitura.
            self.lendo += dt
            if self.lendo >= PAUSA + len(self.frases[self.indice]) / LEITURA:
                self.avancar()
            return
        antes = int(self.letras)
        self.letras = min(len(self.frases[self.indice]), self.letras + LETRAS_POR_SEGUNDO * dt)
        # "Tic" a cada duas letras novas (espaços não contam), se o jogo deu um som.
        novas = self.frases[self.indice][antes:int(self.letras)]
        if self.ao_escrever and any(not c.isspace() and (antes + i) % 2 == 0 for i, c in enumerate(novas)):
            self.ao_escrever()

    def seguir_narracao(self, dt):
        """Frase atual e letras pelo relógio do áudio (sem bipes: a voz já está falando)."""
        agora = self.relogio()
        if agora < 0:
            return
        if self.canal is None and self.narracao:
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.play()
            self.canal = True
            self.tempo_total = self.tempo_total - agora  # o relógio recomeça junto com o áudio
            agora = 0.0
        if self.video and agora >= max(self.duracao, self.video.duracao):
            self.pular()  # fim do vídeo: escurece e entra no complexo
            return
        if agora >= self.duracao + 0.5:
            self.contemplando = 0.0  # acabou a fala: a caixa some e a Giulia fica à vista
            return
        # Corte floresta -> Helix: começa meio corte antes, para a troca cair no início da frase.
        if self.corte < len(self.frases) and self.na_floresta and self.cortando is None \
                and agora >= self.tempos[self.corte][0] - CORTE / 2:
            self.cortando = 0.0
            return
        proxima = self.indice + 1
        if proxima < len(self.frases) and proxima != self.corte and agora >= self.tempos[proxima][0]:
            self.indice, self.letras, self.lendo = proxima, 0.0, 0.0
        inicio, fim = self.tempos[self.indice]
        frase = self.frases[self.indice]
        velocidade = max(12.0, len(frase) / max(0.4, (fim - inicio) * 0.85))  # no ritmo da fala, um pouco à frente
        self.letras = max(0.0, min(len(frase), (agora - inicio) * velocidade))  # pela posição do áudio

    def desenhar_floresta(self, tela):
        largura_tela, altura_tela = tela.get_size()
        zoom = max(altura_tela / ALTURA_VISIVEL, largura_tela / LARGURA_FLORESTA)  # sem faixas pretas nos lados
        if self.floresta_escalada is None or self.floresta_escalada[0] != zoom:
            w, h = self.floresta.get_size()
            fator = zoom * LARGURA_FLORESTA / w  # a imagem pode ser maior que a escala do mundo
            self.floresta_escalada = (zoom, pygame.transform.smoothscale(self.floresta, (round(w * fator), round(h * fator))))
        imagem = self.floresta_escalada[1]
        altura_imagem = imagem.get_height()
        # Câmera: trilha no meio da tela; a Giulia um pouco abaixo do centro, para ver o caminho à frente.
        pes_y = self.giulia.pes.bottom if self.giulia else -self.tempo_total * 40
        visao = pygame.Rect(0, 0, 0, 0)
        visao.x = round(sum(TRILHA) / 2 - largura_tela / zoom / 2)
        visao.y = round(pes_y - altura_tela / zoom * 0.55)  # acima da caixa de texto
        x = round(-visao.x * zoom)
        y = -(round(visao.y * zoom) % altura_imagem)
        while y < altura_tela:
            tela.blit(imagem, (x, y))
            y += altura_imagem
        if self.giulia:
            self.giulia.desenhar(tela, visao, zoom)

    def relogio(self):
        """Segundos do áudio (e do vídeo) desde que a voz começou."""
        espera = 0.0 if self.video else ESPERA_NARRACAO
        if self.canal and pygame.mixer.music.get_busy():
            posicao = pygame.mixer.music.get_pos()
            # Confia na posição do áudio quando ela é plausível (o driver "dummy" não anda).
            if posicao >= 0 and abs(posicao / 1000 - (self.tempo_total - espera)) < 1.5:
                return posicao / 1000
        return self.tempo_total - espera

    def desenhar(self, tela, px):
        if self.video:
            tela.fill((0, 0, 0))
            quadro = self.video.quadro(self.relogio())
            if quadro:
                escala = min(tela.get_width() / quadro.get_width(), tela.get_height() / quadro.get_height())
                imagem = pygame.transform.smoothscale(quadro, (round(quadro.get_width() * escala), round(quadro.get_height() * escala)))
                tela.blit(imagem, imagem.get_rect(center=tela.get_rect().center))
            self.desenhar_por_cima(tela, px)
            return
        if self.na_floresta:
            self.desenhar_floresta(tela)
            self.desenhar_por_cima(tela, px)
            return
        tamanho = largura_tela, altura_tela = tela.get_size()
        # Pedaço da imagem na proporção da tela, centrado na largura; desce com a narração.
        iw, ih = self.imagem.get_size()
        largura = iw / AMPLIACAO
        altura = min(ih, largura * altura_tela / largura_tela)
        x = (iw - largura) / 2
        y = (ih - altura) * self.descida
        pedaco = self.imagem.subsurface(pygame.Rect(round(x), round(y), round(largura), round(altura)))
        tela.blit(pygame.transform.smoothscale(pedaco, tamanho), (0, 0))
        self.desenhar_por_cima(tela, px)

    def desenhar_por_cima(self, tela, px):
        """Caixa de texto e escurecimentos (entrada, corte para o Helix e saída)."""
        tamanho = tela.get_size()
        if self.contemplando is None and self.cortando is None:
            self.desenhar_caixa(tela, px)
        escuro = 0.0
        if self.cortando is not None:
            escuro = 1 - abs(self.cortando / (CORTE / 2) - 1)
        if self.indice == 0 and self.tempo_total < 1.2:
            escuro = 1 - self.tempo_total / 1.2  # entra do preto
        if self.saindo is not None:
            escuro = min(1.0, self.saindo / SAIDA)  # sai para o preto
        if escuro:
            veu = pygame.Surface(tamanho)
            veu.set_alpha(round(255 * escuro))
            tela.blit(veu, (0, 0))

    def desenhar_caixa(self, tela, px):
        if self.tempos:  # abertura narrada: legenda pequena, sem a Giulia
            if getattr(self, "fonte_legenda", (None,))[0] != px(16):
                self.fonte_legenda = (px(16), pygame.font.SysFont("consolas", px(16)))
            desenhar_legenda(tela, px, self.fonte_legenda[1], self.frases[self.indice], self.letras)
            return
        seta = self.atual_completa() and int(self.tempo_total * 2) % 2 == 0
        self.caixa.desenhar(tela, px, "Giulia", self.frases[self.indice], self.letras, seta)
