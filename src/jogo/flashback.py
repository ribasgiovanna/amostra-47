"""Flashback do computador da central: uma cena só para assistir, dentro da engine.

Angela Torres, Beatrice Salles e Amie Lin conversam no Laboratório de análises (antes do
incidente) sobre a ordem de manutenção da ventilação. As falas passam sozinhas depois do
tempo de leitura (E/Enter/clique adianta; Esc pula). Começa e termina no preto.
"""
import pygame

from dados import MAPAS, PERSONAGENS
from entidades import Jogador, Mapa
from cutscene import desenhar_legenda

ALTURA_VISIVEL = 360  # mesma câmera das salas
ESCURECER = 1.0  # segundos do fade de entrada e de saída
PAUSA, LEITURA = 1.4, 40  # depois de escrita, a fala fica PAUSA + letras/LEITURA segundos
LETRAS_POR_SEGUNDO = 45
MAPA = "laboratorio-de-analises"

# Onde cada um fica (pés, em unidades do mapa) e para onde olha: abaixo das bancadas.
ATORES = {
    "angela-torres": ((316, 532), "lado", False),  # olhando para a direita (Beatrice)
    "beatrice-salles": ((404, 532), "lado", True),  # olhando para a esquerda (Angela)
    "amie-lin": ((360, 514), "frente", False),  # entre as duas, um pouco atrás
}

FALAS = [
    ("angela-torres", "Beatrice, preciso que você veja isso. Encontrei esta ordem de manutenção no sistema."),
    ("beatrice-salles", "Ventilação dos túneis... e com o meu nome como responsável técnica?"),
    ("angela-torres", "E com o seu aval. O pedido já consta como aprovado."),
    ("beatrice-salles", "Eu não assinei nada disso. Nunca vi esse papel."),
    ("amie-lin", "Tem certeza, Beatrice? No fim do turno a gente assina tanta coisa sem ler..."),
    ("beatrice-salles", "Tenho. Eu confiro cada ordem que passa pela manutenção. Essa não passou por mim."),
    ("angela-torres", "A origem eletrônica do pedido também não bate com o setor de manutenção."),
    ("beatrice-salles", "Então alguém usou o meu nome. Essa informação foi manipulada."),
    ("amie-lin", "Alguém quer mexer na ventilação sem que ninguém perceba."),
    ("angela-torres", "Vamos guardar isso entre nós, por enquanto. Até descobrirmos quem está por trás disso."),
]


class Flashback:
    def __init__(self):
        self.mapa = Mapa(MAPAS[MAPA])
        self.atores = []
        for chave, (pes, direcao, espelhado) in ATORES.items():
            ator = Jogador(PERSONAGENS[chave], pes)
            ator.direcao, ator.espelhado = direcao, espelhado
            ator.chave = chave
            self.atores.append(ator)
        self.indice = 0
        self.letras = 0.0
        self.lendo = 0.0
        self.tempo = 0.0
        self.saindo = None  # tempo do fade final
        self.terminou = False
        self.ao_escrever = None  # som das letras

    def frase(self):
        return FALAS[self.indice][1]

    def avancar(self):
        if self.tempo < ESCURECER or self.saindo is not None:
            return
        if self.letras < len(self.frase()):
            self.letras = len(self.frase())
        elif self.indice + 1 < len(FALAS):
            self.indice, self.letras, self.lendo = self.indice + 1, 0.0, 0.0
        else:
            self.saindo = 0.0

    def pular(self):
        if self.saindo is None:
            self.saindo = 0.0

    def atualizar(self, dt):
        self.tempo += dt
        for ator in self.atores:
            ator.tempo += dt  # respiração (quadros de parado)
        if self.saindo is not None:
            self.saindo += dt
            self.terminou = self.saindo >= ESCURECER
            return
        if self.tempo < ESCURECER:
            return
        if self.letras < len(self.frase()):
            antes = int(self.letras)
            self.letras = min(len(self.frase()), self.letras + LETRAS_POR_SEGUNDO * dt)
            if self.ao_escrever and any(not c.isspace() and (antes + i) % 2 == 0
                                        for i, c in enumerate(self.frase()[antes:int(self.letras)])):
                self.ao_escrever()
            return
        self.lendo += dt
        if self.lendo >= PAUSA + len(self.frase()) / LEITURA:
            self.avancar()

    def desenhar_hud(self, tela, px):
        """HUD de câmera: cantos, REC piscando, bateria, mira no centro, relógio e FPS."""
        largura, altura = tela.get_size()
        branco = (235, 235, 235)
        linha = max(1, px(2))
        m, braco = px(28), px(70)
        r = pygame.Rect(m, m, largura - 2 * m, altura - 2 * m)
        for (x, y), (dx, dy) in (((r.left, r.top), (1, 1)), ((r.right, r.top), (-1, 1)),
                                 ((r.left, r.bottom), (1, -1)), ((r.right, r.bottom), (-1, -1))):
            pygame.draw.line(tela, branco, (x, y), (x + dx * braco, y), linha)
            pygame.draw.line(tela, branco, (x, y), (x, y + dy * braco), linha)
        if getattr(self, "fonte_hud", (None,))[0] != px(15):
            self.fonte_hud = (px(15), pygame.font.SysFont("consolas", px(15)))
        fonte = self.fonte_hud[1]
        # REC
        topo = r.top + px(18)
        if pygame.time.get_ticks() // 600 % 2 == 0:
            pygame.draw.circle(tela, (220, 40, 40), (r.left + px(24), topo + fonte.get_height() // 2), px(6))
        tela.blit(fonte.render("REC", True, branco), (r.left + px(38), topo))
        # bateria
        bat = pygame.Rect(0, 0, px(30), px(14))
        bat.topright = (r.right - px(24), topo + px(2))
        pygame.draw.rect(tela, branco, bat, max(1, px(1)))
        pygame.draw.rect(tela, branco, bat.inflate(-px(6), -px(6)).move(px(1), 0))
        pygame.draw.rect(tela, branco, pygame.Rect(bat.left - px(3), bat.centery - px(3), px(3), px(6)))
        # mira
        c = pygame.Rect(0, 0, px(140), px(90))
        c.center = (largura // 2, altura // 2)
        b = px(30)
        for (x, y), (dx, dy) in (((c.left, c.top), (1, 1)), ((c.right, c.top), (-1, 1)),
                                 ((c.left, c.bottom), (1, -1)), ((c.right, c.bottom), (-1, -1))):
            pygame.draw.line(tela, branco, (x, y), (x + dx * b, y), linha)
            pygame.draw.line(tela, branco, (x, y), (x, y + dy * b), linha)
        pygame.draw.line(tela, branco, (c.centerx - px(8), c.centery), (c.centerx + px(8), c.centery), linha)
        pygame.draw.line(tela, branco, (c.centerx, c.centery - px(8)), (c.centerx, c.centery + px(8)), linha)
        # relógio e FPS embaixo
        t = int(self.tempo * 30)
        relogio = f"{t // 108000:02d}:{t // 1800 % 60:02d}:{t // 30 % 60:02d}:{t % 30:02d}"
        base = r.bottom - px(18) - fonte.get_height()
        pygame.draw.rect(tela, branco, pygame.Rect(r.left + px(20), base, px(4), fonte.get_height()))
        tela.blit(fonte.render(relogio, True, branco), (r.left + px(34), base))
        fps = fonte.render("CAM 03   30 FPS", True, branco)
        tela.blit(fps, fps.get_rect(topright=(r.right - px(20), base)))

    def desenhar(self, tela, px, caixa):
        largura, altura = tela.get_size()
        zoom = altura / ALTURA_VISIVEL
        visao = pygame.Rect(0, 0, round(largura / zoom), round(altura / zoom))
        # As três um pouco acima do centro, para a caixa de texto não cobrir ninguém.
        meio_x = sum(a.pes.centerx for a in self.atores) / len(self.atores)
        meio_y = sum(a.pes.bottom for a in self.atores) / len(self.atores)
        visao.center = (round(meio_x), round(meio_y + visao.height * 0.12))
        visao.clamp_ip(pygame.Rect((0, 0), self.mapa.tamanho))
        tela.fill((0, 0, 0))
        self.mapa.desenhar(tela, visao, zoom)
        topo = min(a.pes.bottom for a in self.atores)
        self.mapa.desenhar_objetos(tela, visao, zoom, topo, atras=True)
        for ator in sorted(self.atores, key=lambda a: a.pes.bottom):
            ator.desenhar(tela, visao, zoom)
        self.mapa.desenhar_objetos(tela, visao, zoom, topo, atras=False)
        # Gravação da câmera de segurança: preto e branco, bordas escuras e o HUD por cima.
        tela.blit(pygame.transform.grayscale(tela), (0, 0))
        borda = pygame.Surface((largura, altura), pygame.SRCALPHA)
        for i in range(12):
            espessura = px(6)
            pygame.draw.rect(borda, (0, 0, 0, 150 - i * 12), borda.get_rect().inflate(-i * 2 * espessura, -i * 2 * espessura), espessura)
        tela.blit(borda, (0, 0))
        self.desenhar_hud(tela, px)
        if self.tempo >= ESCURECER:
            # Caixinha pequena da abertura (sem retrato): "Nome: fala".
            nome = PERSONAGENS[FALAS[self.indice][0]]["nome"].split()[0] + ": "
            if getattr(self, "fonte_legenda", (None,))[0] != px(16):
                self.fonte_legenda = (px(16), pygame.font.SysFont("consolas", px(16)))
            desenhar_legenda(tela, px, self.fonte_legenda[1], nome + self.frase(), len(nome) + self.letras)
        escuro = 0.0
        if self.tempo < ESCURECER:
            escuro = 1 - self.tempo / ESCURECER
        if self.saindo is not None:
            escuro = min(1.0, self.saindo / ESCURECER)
        if escuro > 0:
            veu = pygame.Surface((largura, altura))
            veu.set_alpha(round(255 * escuro))
            tela.blit(veu, (0, 0))
