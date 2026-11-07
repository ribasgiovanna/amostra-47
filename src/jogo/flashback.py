"""Flashback do computador da central: uma cena só para assistir, dentro da engine.

Angela Torres, Beatrice Salles e Amie Lin conversam no Laboratório de análises (antes do
incidente) sobre a ordem de manutenção da ventilação. As falas passam sozinhas depois do
tempo de leitura (E/Enter/clique adianta; Esc pula). Começa e termina no preto.
"""
import pygame

from dados import MAPAS, PERSONAGENS
from entidades import Jogador, Mapa

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
        # Tom de lembrança: sépia leve e bordas escuras.
        tom = pygame.Surface((largura, altura), pygame.SRCALPHA)
        tom.fill((120, 85, 40, 80))
        tela.blit(tom, (0, 0))
        borda = pygame.Surface((largura, altura), pygame.SRCALPHA)
        for i in range(12):
            espessura = px(6)
            pygame.draw.rect(borda, (0, 0, 0, 150 - i * 12), borda.get_rect().inflate(-i * 2 * espessura, -i * 2 * espessura), espessura)
        tela.blit(borda, (0, 0))
        if self.tempo >= ESCURECER:
            chave = FALAS[self.indice][0]
            seta = self.letras >= len(self.frase()) and pygame.time.get_ticks() // 500 % 2 == 0
            caixa.desenhar(tela, px, PERSONAGENS[chave]["nome"].split()[0], self.frase(), self.letras, seta)
        escuro = 0.0
        if self.tempo < ESCURECER:
            escuro = 1 - self.tempo / ESCURECER
        if self.saindo is not None:
            escuro = min(1.0, self.saindo / ESCURECER)
        if escuro > 0:
            veu = pygame.Surface((largura, altura))
            veu.set_alpha(round(255 * escuro))
            tela.blit(veu, (0, 0))
