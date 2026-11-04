"""Entidades da beta: Mapa, Jogador e Item."""

import math
import os

import pygame

PASTA_JOGO = os.path.dirname(os.path.abspath(__file__))


def caminho(relativo):
    return os.path.join(PASTA_JOGO, relativo)


def carregar_tira(arquivo):
    """Corta uma tira horizontal de quadros quadrados (o lado é a altura da tira: 64, 80...)."""
    tira = pygame.image.load(arquivo).convert_alpha()
    lado = tira.get_height()
    return [tira.subsurface((i * lado, 0, lado, lado)) for i in range(tira.get_width() // lado)]


class Mapa:
    def __init__(self, dados):
        self.nome = dados["nome"]
        self.tamanho = dados["tamanho"]
        self.original = pygame.image.load(caminho(dados["imagem"])).convert()
        self.imagem = None
        self.zoom = None
        self.area_andavel = pygame.Rect(dados["area_andavel"])
        self.obstaculos = [pygame.Rect(r) for r in dados["obstaculos"]]
        self.inicio = dados["inicio"]
        # Máscara opcional (branco = piso andável), do mesmo tamanho de "tamanho".
        self.bloqueio = None
        if dados.get("mascara"):
            imagem = pygame.image.load(caminho(dados["mascara"])).convert()
            self.bloqueio = pygame.mask.from_threshold(imagem, (255, 255, 255), (2, 2, 2, 255))
            self.bloqueio.invert()
        # Objetos soltos: imagem, retângulo no mapa e a faixa de baixo ("pé") que colide.
        self.objetos = []
        objetos = dados.get("objetos", [])
        if isinstance(objetos, str):  # lista num JSON dentro da pasta dos objetos
            import json
            with open(os.path.join(caminho(dados["pasta_objetos"]), objetos), encoding="utf-8") as arquivo:
                objetos = json.load(arquivo)
        for objeto in objetos:
            pasta = objeto.get("pasta", dados.get("pasta_objetos"))  # um objeto pode vir de outra pasta
            imagem = pygame.image.load(os.path.join(caminho(pasta), objeto["imagem"])).convert_alpha()
            x, y, largura, altura = objeto["retangulo"]
            # Reduz a arte para a resolução de pixel do mapa e depois amplia sem
            # suavizar, para os objetos não ficarem mais detalhados que o cenário.
            densidade = dados.get("pixels_por_unidade_objetos", 1)
            imagem = pygame.transform.smoothscale(
                imagem, (max(1, round(largura * densidade)), max(1, round(altura * densidade))))
            # "bases": retângulos de colisão em frações da imagem (x, y, largura, altura);
            # sem elas, colide a faixa de baixo ("pe"), com 80% da largura.
            fracoes = objeto.get("bases")
            if fracoes is None:
                fracoes = [(0.1, 1 - objeto["pe"], 0.8, objeto["pe"])]
            bases = [pygame.Rect(round(x + fx * largura), round(y + fy * altura),
                                 round(fw * largura), round(fh * altura)) for fx, fy, fw, fh in fracoes]
            # Linha que decide se o personagem está atrás (pés acima) ou na frente.
            linha = y + altura * objeto["linha"] if "linha" in objeto else max(b.bottom for b in bases)
            self.objetos.append({"original": imagem, "retangulo": objeto["retangulo"],
                                 "bases": bases, "linha": linha})
        # Entre si, os objetos também seguem a profundidade: quem está mais embaixo fica na frente.
        self.objetos.sort(key=lambda objeto: objeto["linha"])
        self.zoom_objetos = None

    def livre(self, retangulo):
        """True se o retângulo estiver dentro do piso e fora dos obstáculos."""
        if self.bloqueio is not None:
            if not pygame.Rect((0, 0), self.bloqueio.get_size()).contains(retangulo):
                return False
            pes = pygame.Mask(retangulo.size, fill=True)
            if self.bloqueio.overlap(pes, retangulo.topleft) is not None:
                return False
            return all(retangulo.collidelist(o["bases"]) == -1 for o in self.objetos)
        return (self.area_andavel.contains(retangulo)
                and retangulo.collidelist(self.obstaculos) == -1)

    def desenhar(self, tela, visao, zoom):
        if self.original.get_width() > 4000:
            # Mapa grande: escala só o pedaço visível, a cada quadro.
            ppu = self.original.get_width() / self.tamanho[0]
            fonte = pygame.Rect(round(visao.x * ppu), round(visao.y * ppu),
                                round(visao.w * ppu), round(visao.h * ppu)).clip(self.original.get_rect())
            pedaco = pygame.transform.smoothscale(self.original.subsurface(fonte),
                                                  (round(fonte.w / ppu * zoom), round(fonte.h / ppu * zoom)))
            tela.blit(pedaco, ((fonte.x / ppu - visao.x) * zoom, (fonte.y / ppu - visao.y) * zoom))
            return
        # Escala a imagem original uma única vez para o zoom atual (nitidez máxima).
        if zoom != self.zoom:
            self.zoom = zoom
            tamanho = (round(self.tamanho[0] * zoom), round(self.tamanho[1] * zoom))
            self.imagem = pygame.transform.smoothscale(self.original, tamanho)
        tela.blit(self.imagem, (-visao.x * zoom, -visao.y * zoom))

    def desenhar_objetos(self, tela, visao, zoom, pes_y, atras):
        """Desenha os objetos atrás (base acima dos pés) ou na frente do personagem."""
        if zoom != self.zoom_objetos:
            self.zoom_objetos = zoom
            for objeto in self.objetos:
                _, _, largura, altura = objeto["retangulo"]
                objeto["imagem"] = pygame.transform.scale(
                    objeto["original"], (round(largura * zoom), round(altura * zoom)))
        for objeto in self.objetos:
            if (objeto["linha"] <= pes_y) == atras:
                x, y, _, _ = objeto["retangulo"]
                tela.blit(objeto["imagem"], ((x - visao.x) * zoom, (y - visao.y) * zoom))


# Direções diagonais opcionais (W+D = "costas-direita", S+A = "frente-esquerda"...).
DIAGONAIS = ("frente-direita", "frente-esquerda", "costas-direita", "costas-esquerda")


class Jogador:
    def __init__(self, dados, posicao):
        self.nome = dados["nome"]
        self.velocidade = dados["velocidade"]
        pasta = caminho(dados["pasta_sprites"])
        self.animacoes = {}
        for direcao in ("frente", "lado", "costas", "esquerda") + DIAGONAIS:
            for estado in ("parado", "andando"):
                arquivo = os.path.join(pasta, f"{estado}-{direcao}.png")
                if direcao not in ("frente", "lado", "costas") and not os.path.exists(arquivo):
                    continue  # opcionais: sem esquerda espelha o "lado"; sem diagonais usa 4 direções
                self.animacoes[(estado, direcao)] = carregar_tira(arquivo)
        self.fps_andando = dados.get("fps_andando", 8)
        self.balanco = dados.get("balanco", True)
        self.direcao = "frente"
        self.espelhado = False  # o "lado" da folha olha para a direita
        self.andando = False
        self.tempo = 0.0
        # Caixa de colisão nos pés (o corpo pode sobrepor paredes visualmente).
        self.pes = pygame.Rect(0, 0, 26, 14)
        self.pes.midbottom = posicao
        self.x, self.y = float(self.pes.x), float(self.pes.y)  # posição sub-pixel

    @property
    def centro(self):
        return self.pes.centerx, self.pes.bottom - 24

    def atualizar(self, dt, teclas, mapa):
        dx = (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) - (teclas[pygame.K_LEFT] or teclas[pygame.K_a])
        dy = (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) - (teclas[pygame.K_UP] or teclas[pygame.K_w])
        self.andando = bool(dx or dy)
        diagonal = f"{'frente' if dy > 0 else 'costas'}-{'direita' if dx > 0 else 'esquerda'}"
        if dx and dy and ("andando", diagonal) in self.animacoes:
            self.direcao, self.espelhado = diagonal, False
        elif dx < 0 and ("andando", "esquerda") in self.animacoes:
            self.direcao, self.espelhado = "esquerda", False
        elif dx:
            self.direcao, self.espelhado = "lado", dx < 0
        elif dy:
            self.direcao = "frente" if dy > 0 else "costas"
            self.espelhado = False  # só o "lado" é espelhado

        passo = self.velocidade * dt
        if dx and dy:
            passo *= 0.7071
        # Move um eixo por vez para deslizar ao longo das paredes.
        for eixo, valor in (("x", dx), ("y", dy)):
            if not valor:
                continue
            x = self.x + valor * passo if eixo == "x" else self.x
            y = self.y + valor * passo if eixo == "y" else self.y
            novo = self.pes.copy()
            novo.topleft = (round(x), round(y))
            if mapa.livre(novo):
                self.pes, self.x, self.y = novo, x, y
        self.tempo += dt

    def desenhar(self, tela, visao, zoom):
        estado = "andando" if self.andando else "parado"
        quadros = self.animacoes[(estado, self.direcao)]
        fps = self.fps_andando if self.andando else 2
        indice = int(self.tempo * fps) % len(quadros)
        quadro = quadros[indice]
        # Fator inteiro mantém os pixels do sprite todos do mesmo tamanho.
        escala = max(1, round(zoom))
        tamanho = quadro.get_width() * escala
        quadro = pygame.transform.scale(quadro, (tamanho, tamanho))
        if self.espelhado:
            quadro = pygame.transform.flip(quadro, True, False)
        # Leve balanço vertical a cada passo.
        balanco = -escala if self.balanco and self.andando and indice % 2 else 0
        base = ((self.pes.centerx - visao.x) * zoom, (self.pes.bottom + 4 - visao.y) * zoom + balanco)
        tela.blit(quadro, quadro.get_rect(midbottom=base))


class Item:
    DISTANCIA_INTERACAO = 40

    def __init__(self, dados, posicao):
        self.id = dados["id"]
        self.nome = dados["nome"]
        self.mensagem = dados["mensagem"]
        # A arte só aparece na tela de inspeção; no mapa o item é um brilho.
        self.imagem = pygame.image.load(caminho(dados["imagem"])).convert_alpha()
        self.posicao = pygame.Vector2(posicao)
        self.coletado = False
        self.tempo = 0.0

    def perto(self, jogador):
        if self.coletado:
            return False
        return self.posicao.distance_to(jogador.centro) <= self.DISTANCIA_INTERACAO

    def atualizar(self, dt):
        self.tempo += dt

    def desenhar(self, tela, visao, zoom, destacado):
        if self.coletado:
            return
        desenhar_brilho(tela, self.posicao, visao, zoom, self.tempo, destacado)


def desenhar_brilho(tela, posicao, visao, zoom, tempo, destacado=False):
    # Brilho branco pulsante indica que há algo para interagir.
    pulso = (math.sin(tempo * 4) + 1) / 2
    raio = round((9 + pulso * 3 + (3 if destacado else 0)) * zoom)
    brilho = pygame.Surface((raio * 4, raio * 4), pygame.SRCALPHA)
    centro = raio * 2
    for r in range(raio * 2, 0, -1):
        alfa = int(255 * (1 - r / (raio * 2)) ** 1.5 * (0.7 + 0.3 * pulso))
        pygame.draw.circle(brilho, (255, 255, 255, alfa), (centro, centro), r)
    # Pequena cintilação em cruz para destacar o brilho em piso claro.
    braco = round((4 + pulso * 4) * zoom)
    espessura = max(2, round(zoom))
    pygame.draw.line(brilho, (255, 255, 255), (centro - braco, centro), (centro + braco, centro), espessura)
    pygame.draw.line(brilho, (255, 255, 255), (centro, centro - braco), (centro, centro + braco), espessura)
    centro_tela = ((posicao.x - visao.x) * zoom, (posicao.y - visao.y) * zoom)
    tela.blit(brilho, brilho.get_rect(center=centro_tela))
