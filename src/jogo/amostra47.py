"""AMOSTRA 47 — beta jogável (vertical slice).

Um personagem, um mapa e um item. Execute com:
    python src/jogo/amostra47.py
"""

import json
import math
import random
import sys
from types import SimpleNamespace

import pygame

from dados import ITENS, MAPAS, PERSONAGENS
from cutscene import CaixaTexto, Cutscene
from entidades import Item, Jogador, Mapa, caminho, desenhar_brilho

# Conteúdo desta beta: troque as chaves para usar outro personagem/mapa/item.
PERSONAGEM = "otavio-ferraz"
# Depois da cutscene de abertura, o jogo começa com a Giulia nesta sala (entrando pela porta).
PERSONAGEM_INICIO = "giulia-pistori"
SALA_INICIO = "sala-de-evacuacao-pos-incidente"
# Personagens jogáveis do menu (Alt abre; 1, 2... trocam).
PERSONAGENS_MENU = ["otavio-ferraz", "clara-costa", "giulia-pistori", "amie-lin", "beatrice-salles", "angela-torres", "giovani-pistori", "fernando-almeida"]
# Salas do jogo, com os itens de cada uma. A primeira é onde o jogo começa.
# Andar até uma porta e apertar E abre a lista de salas da mesma fase (antes ou depois do
# incidente); Caps Lock (no Game test) alterna entre antes e depois na mesma sala.
MAPAS_MENU = ["camara-de-contencao", "sala-de-servidores", "sala-de-evacuacao", "laboratorio-de-analises", "tunel-de-ventilacao", "central-de-seguranca", "camara-de-contencao-pos-incidente", "sala-de-servidores-pos-incidente", "sala-de-evacuacao-pos-incidente", "laboratorio-de-analises-pos-incidente", "tunel-de-ventilacao-pos-incidente", "central-de-seguranca-pos-incidente"]
# Itens: cada partida sorteia, para cada item, um dos 7 locais de uma das salas
# (ferramentas/escolher_locais.py gera mapas/locais-itens.json com os locais).
with open(caminho("mapas/locais-itens.json"), encoding="utf-8") as _arquivo:
    LOCAIS_ITENS = json.load(_arquivo)
SALAS_BASE = [c for c in MAPAS_MENU if not c.endswith("-pos-incidente")]
OBTER = 2.2  # segundos da animação de conseguir um item

# O jogo desenha na resolução real da janela (sem esticar uma tela menor).
# O zoom sai da altura: a câmera sempre mostra ALTURA_VISIVEL unidades do mapa.
JANELA_INICIAL = (1280, 720)
ALTURA_VISIVEL = 360
ALTURA_BASE_UI = 540  # tamanhos de fonte e margens abaixo valem para esta altura
FPS = 60
TECLAS_INTERAGIR = (pygame.K_e,)
DISTANCIA_PORTA = 12  # folga (unidades) além do ponto mais perto que os pés alcançam da porta
# Mapa mental (Tab): miniaturas das salas (ferramentas/gerar_miniaturas.py), lado a lado.
SALAS_MAPA_MENTAL = [
    ["central-de-seguranca", "sala-de-servidores", "laboratorio-de-analises"],
    ["camara-de-contencao", "sala-de-evacuacao", "tunel-de-ventilacao"],
]
INICIO = 2.0  # segundos do fade do menu principal ao escolher Jogar
FADE = 0.35  # segundos para escurecer (e o mesmo para clarear)


def pos_incidente(chave):
    return chave.endswith("-pos-incidente")


def quebrar_texto(fonte, texto, largura):
    linhas, atual = [], ""
    for palavra in texto.split():
        teste = f"{atual} {palavra}".strip()
        if fonte.size(teste)[0] <= largura:
            atual = teste
        else:
            linhas.append(atual)
            atual = palavra
    return linhas + [atual]


def borrar(superficie, fator=10):
    """Desfoque barato: reduz e amplia de volta."""
    pequena = pygame.transform.smoothscale(
        superficie, (superficie.get_width() // fator, superficie.get_height() // fator))
    return pygame.transform.smoothscale(pequena, superficie.get_size())


def ativar_dpi_real():
    """No Windows com escala de tela (ex.: 125%), evita que o sistema estique e borre a janela."""
    if sys.platform == "win32":
        try:
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        except (AttributeError, OSError):
            pass


def posicionar_janela(posicao):
    """Move a janela (None = centralizar). Ignora se o SDL não permitir."""
    try:
        from pygame._sdl2.video import WINDOWPOS_CENTERED, Window
        Window.from_display_module().position = posicao or WINDOWPOS_CENTERED
    except (ImportError, AttributeError, pygame.error):
        pass


# Menus do sistema: (chave, texto do botão).
MENUS_SISTEMA = {
    "principal": [("jogar", "Jogar"), ("teste", "Game test"), ("sair", "Sair")],
    "pausa": [("continuar", "Continuar"), ("menu", "Menu principal"), ("sair", "Sair")],
}


class Jogo:
    def __init__(self):
        ativar_dpi_real()
        # Buffer de áudio pequeno: os sons de menu saem na hora, sem atraso.
        pygame.mixer.pre_init(44100, -16, 2, 256)
        pygame.init()
        # Sons sintetizados (ferramentas/gerar_sons.py); sem saída de áudio, o jogo segue mudo.
        self.sons = {}
        try:
            pygame.mixer.init()
            for nome in ("tic-1", "tic-2", "tic-3", "pista", "ambiente", "menu-mover", "menu-confirmar"):
                self.sons[nome] = pygame.mixer.Sound(caminho(f"sons/{nome}.wav"))
            self.sons["ambiente"].set_volume(0.04)
            self.sons["pista"].set_volume(0.55)
            for n in (1, 2, 3):
                self.sons[f"tic-{n}"].set_volume(0.18)
            self.sons["menu-mover"].set_volume(0.5)
            self.sons["menu-confirmar"].set_volume(0.6)
        except (pygame.error, FileNotFoundError) as erro:
            print(f"[som] sem áudio: {erro}")
            self.sons = {}
        self.ambiente_tocando = False
        self.iniciando = None  # tempo do fade do menu principal ao escolher Jogar
        pygame.display.set_caption("Amostra 47 — beta")
        self.tamanho_janela = JANELA_INICIAL
        self.tela_cheia = False
        self.relogio = pygame.time.Clock()
        self.aplicar_modo()

        self.personagem = PERSONAGEM
        self.menu_personagens = False  # menu de troca de personagem aberto (jogo pausado)
        self.inspecionando = None  # item aberto na tela de inspeção (jogo pausado)
        self.fundo_borrado = None
        self.menu_mapas = False  # menu de troca de mapas aberto (jogo pausado)
        self.cursor = 0  # opção destacada no menu aberto (mouse ou setas + Enter)
        self.botoes_menu = []  # retângulos clicáveis das opções do menu aberto
        self.destinos = []  # salas listadas no menu da porta
        self.fade = None  # troca de sala em andamento: [fase, tempo, destino]
        # Menu principal ("principal", na abertura) ou de pausa ("pausa", no Esc); None = jogando.
        self.menu_sistema = "principal"
        self.cutscene = None  # cutscene de abertura em andamento
        self.pistas = {}  # pistas coletadas no jogo todo: chave do item -> sala onde foi achada
        self.mapa_mental = False  # menu do mapa mental aberto (Tab)
        self.miniaturas = {}  # chave da sala -> imagem pequena
        self.pista_aberta = 0  # pista mostrada no mapa mental
        self.imagens_pistas = {}
        self.aba_mental = "pistas"  # aba do mapa mental: "pistas" ou "notas"
        self.anotacoes = ""  # o que o jogador escreveu no caderno do mapa mental
        self.abas_mental = {}  # aba -> retângulo clicável
        self.dialogo = None  # fala ao achar um item: {"item", "letras"}
        self.obtendo = None  # animação de conseguir o item: {"item", "t", "arte"}
        self.caixa = CaixaTexto()
        self.sortear_itens()
        self.modo_teste = False  # "Game test": Tab e Alt liberados para testar salas e personagens
        self.carregar_mapa(MAPAS_MENU[0])
        self.rodando = True

    def carregar_mapa(self, chave, manter_posicao=False, na_porta=False):
        """Troca de mapa: recria mapa, jogador (mesmo visual) e itens."""
        posicao = self.jogador.pes.midbottom if manter_posicao else None
        self.chave_mapa = chave
        self.mapa = Mapa(MAPAS[chave])
        if na_porta and MAPAS[chave].get("portas"):
            posicao = MAPAS[chave]["portas"][0]
        self.jogador = Jogador(PERSONAGENS[self.personagem], posicao or self.mapa.inicio)
        self.itens = []
        base = chave.removesuffix("-pos-incidente")
        for item, dados in ITENS.items():
            if chave in dados.get("fixo", {}):
                posicao_item = dados["fixo"][chave]  # lugar fixo (foto da família)
            elif self.locais_itens.get(item, ("", 0))[0] == base:
                x, y = LOCAIS_ITENS[chave][self.locais_itens[item][1]]
                posicao_item = (x, y - 16)  # brilho um pouco acima dos pés
            else:
                continue
            novo = Item(dados, posicao_item)
            novo.chave = item
            novo.coletado = item in self.pistas  # já pega antes: não volta a aparecer
            self.itens.append(novo)
        self.mensagem = f"{self.jogador.nome} entra na {self.nome_sala(chave)}. Procure pistas."
        # Para cada porta, o quanto os pés conseguem chegar perto do meio dela.
        self.alcance_portas = [self.menor_distancia(meio) for meio in MAPAS[chave].get("brilho_portas", [])]

    def sortear_itens(self):
        """Nova partida: cada item vai para um local sorteado (sala e um dos 7 pontos dela)."""
        vagas = [(sala, i) for sala in SALAS_BASE for i in range(len(LOCAIS_ITENS[sala]))]
        sorteados = [chave for chave, dados in ITENS.items() if "fixo" not in dados and "dentro_de" not in dados]
        self.locais_itens = dict(zip(sorteados, random.sample(vagas, len(sorteados))))

    def nome_sala(self, chave):
        """Nome para mostrar; na história (com a Giulia) não precisa do "(pós-incidente)"."""
        nome = MAPAS[chave]["nome"]
        return nome if self.modo_teste else nome.replace(" (pós-incidente)", "")

    def menor_distancia(self, ponto):
        """Menor distância entre os pés (num lugar livre) e o ponto, procurando em volta dele."""
        pes = self.jogador.pes.copy()
        melhor = 999
        for dy in range(-140, 141, 3):
            for dx in range(-60, 61, 3):
                d = (dx * dx + dy * dy) ** 0.5
                if d < melhor:
                    pes.midbottom = (ponto[0] + dx, ponto[1] + dy)
                    if self.mapa.livre(pes):
                        melhor = d
        return melhor

    def porta_proxima(self):
        """Meio da porta encostada no jogador (onde brilha), ou None."""
        x, y = self.jogador.pes.midbottom
        brilhos = MAPAS[self.chave_mapa].get("brilho_portas", [])
        return next((meio for meio, alcance in zip(brilhos, self.alcance_portas)
                     if ((x - meio[0]) ** 2 + (y - meio[1]) ** 2) ** 0.5 <= alcance + DISTANCIA_PORTA), None)

    def abrir_menu_porta(self):
        """Lista as outras salas da mesma fase (antes ou depois do incidente)."""
        fase = pos_incidente(self.chave_mapa)
        self.destinos = [c for c in MAPAS_MENU if pos_incidente(c) == fase and c != self.chave_mapa]
        self.menu_mapas, self.menu_personagens, self.cursor = True, False, 0

    def ir_para(self, chave):
        """Começa a troca de sala: escurece, carrega a sala e clareia com o jogador na porta."""
        self.fade = ["escurecendo", 0.0, chave]

    def aplicar_modo(self):
        if self.tela_cheia:
            # Tela cheia em janela: janela sem borda do tamanho da área de trabalho.
            self.tela = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0], pygame.NOFRAME)
            posicionar_janela((0, 0))
        else:
            self.tela = pygame.display.set_mode(self.tamanho_janela, pygame.RESIZABLE)
            posicionar_janela(None)
        self.ajustar_escala()

    def ajustar_escala(self):
        """Recalcula zoom e fontes para o tamanho atual da tela."""
        self.largura, self.altura = self.tela.get_size()
        self.zoom = self.altura / ALTURA_VISIVEL
        # A interface encolhe também em janelas estreitas (base 960 x 540), para nada sair da tela.
        self.ui = min(self.altura / ALTURA_BASE_UI, self.largura / (ALTURA_BASE_UI * 16 / 9))
        self.fonte = pygame.font.SysFont("consolas", self.px(16))
        self.fonte_pequena = pygame.font.SysFont("consolas", self.px(12))
        self.fonte_grande = pygame.font.SysFont("consolas", self.px(20), bold=True)
        self.fonte_titulo = pygame.font.SysFont("consolas", self.px(28), bold=True)
        # Letra de anotação à mão (Patrick Hand, licença OFL em fontes/).
        self.fonte_mao = pygame.font.Font(caminho("fontes/PatrickHand-Regular.ttf"), self.px(19))

    def px(self, valor):
        """Converte uma medida de interface (base 540 px) para a tela atual."""
        return max(1, round(valor * self.ui))

    def item_proximo(self):
        return next((item for item in self.itens if item.perto(self.jogador)), None)

    def camera(self):
        """Retângulo do mundo visível, centrado no personagem e preso ao mapa."""
        visao = pygame.Rect(0, 0, round(self.largura / self.zoom), round(self.altura / self.zoom))
        visao.center = self.jogador.centro
        visao.clamp_ip(pygame.Rect((0, 0), self.mapa.tamanho))
        return visao

    def interagir(self):
        if self.inspecionando:
            self.inspecionando = None  # fecha a inspeção e retoma o jogo
            return
        item = self.item_proximo()
        if not item and self.porta_proxima():
            self.abrir_menu_porta()
        elif item:
            # Primeiro a personagem comenta o item (sem saber o que é); E de novo pega.
            self.dialogo = {"item": item, "letras": 0.0}

    def avancar_dialogo(self):
        """E na fala: completa o texto; se já está completo, pega o item (animação)."""
        item = self.dialogo["item"]
        fala = ITENS[item.chave]["fala"]
        if self.dialogo["letras"] < len(fala):
            self.dialogo["letras"] = len(fala)
            return
        self.dialogo = None
        item.coletado = True
        self.pistas[item.chave] = self.chave_mapa
        self.pista_aberta = len(self.pistas) - 1
        self.tocar("pista")
        self.obtendo = {"item": item, "t": 0.0, "arte": pygame.image.load(caminho(ITENS[item.chave]["imagem"])).convert_alpha()}
        print(f"[coleta] {item.id} {item.nome}")

    def trocar_personagem(self, chave):
        """Troca o jogador mantendo posição e direção."""
        self.personagem = chave
        antigo = self.jogador
        novo = Jogador(PERSONAGENS[chave], antigo.pes.midbottom)
        novo.pes, novo.x, novo.y = antigo.pes.copy(), antigo.x, antigo.y
        novo.direcao, novo.espelhado = antigo.direcao, antigo.espelhado
        if ("parado", novo.direcao) not in novo.animacoes:
            novo.direcao, novo.espelhado = "lado", True  # "esquerda" sem tira própria
        elif novo.direcao == "lado" and novo.espelhado and ("parado", "esquerda") in novo.animacoes:
            novo.direcao, novo.espelhado = "esquerda", False  # tem tira própria da esquerda
        self.jogador = novo
        self.mensagem = f"Agora jogando com {novo.nome}."

    def opcoes_menu(self):
        """Chaves das opções do menu aberto."""
        if self.menu_sistema:
            return [c for c, _ in MENUS_SISTEMA[self.menu_sistema]]
        return self.destinos if self.menu_mapas else PERSONAGENS_MENU

    def algum_menu(self):
        return bool(self.menu_sistema or self.menu_mapas or self.menu_personagens or self.mapa_mental)

    def tecla_esc(self):
        """Esc fecha o que estiver aberto; no jogo, abre o menu de pausa."""
        if self.menu_sistema == "pausa":
            self.menu_sistema = None
        elif self.menu_sistema:
            return  # no menu principal, Esc não faz nada
        elif self.inspecionando:
            self.inspecionando = None
        elif self.mapa_mental and self.aba_mental == "notas":
            self.aba_mental = "pistas"
        elif self.mapa_mental:
            self.mapa_mental = False
        elif self.menu_mapas or self.menu_personagens:
            self.menu_mapas = self.menu_personagens = False
        else:
            self.menu_sistema, self.cursor = "pausa", 0

    def tratar_eventos(self):
        for evento in pygame.event.get():
            if self.iniciando is not None and evento.type != pygame.QUIT:
                continue  # escurecendo para começar: ignora teclas e cliques
            if evento.type == pygame.QUIT:
                self.rodando = False
            elif evento.type == pygame.VIDEORESIZE and not self.tela_cheia:
                self.tamanho_janela = evento.size
                self.ajustar_escala()
            elif evento.type == pygame.TEXTINPUT:
                if self.mapa_mental and self.aba_mental == "notas" and not self.inspecionando and not self.menu_sistema:
                    self.anotacoes = (self.anotacoes + evento.text)[:4000]
            elif self.mapa_mental and not self.menu_sistema and evento.type == pygame.MOUSEBUTTONDOWN \
                    and evento.button == 1:
                for aba, retangulo in self.abas_mental.items():
                    if retangulo.collidepoint(evento.pos) and aba != self.aba_mental:
                        self.aba_mental = aba
                        self.tocar("menu-mover")
            elif self.dialogo and not self.menu_sistema and evento.type == pygame.MOUSEBUTTONDOWN \
                    and evento.button == 1:
                self.avancar_dialogo()
            elif self.cutscene and evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                self.cutscene.avancar()
            elif self.cutscene and evento.type == pygame.KEYDOWN and evento.key != pygame.K_F11:
                if evento.key == pygame.K_ESCAPE:
                    self.cutscene.pular()
                elif evento.key in (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE, *TECLAS_INTERAGIR):
                    self.cutscene.avancar()
            elif evento.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN) and (
                    self.algum_menu() and not self.mapa_mental):
                # O mouse destaca a opção sob o ponteiro; o clique esquerdo escolhe.
                for i, botao in enumerate(self.botoes_menu):
                    if botao.collidepoint(evento.pos):
                        if self.cursor != i:
                            self.cursor = i
                            self.tocar("menu-mover")  # som no mesmo instante em que o destaque muda
                        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                            self.escolher_no_menu(i)
                        break
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    if not self.fade:
                        self.tecla_esc()
                elif evento.key == pygame.K_F11:
                    self.tela_cheia = not self.tela_cheia
                    self.aplicar_modo()
                    if self.inspecionando:
                        self.fundo_borrado = None  # refeito no novo tamanho
                elif self.fade or self.obtendo:
                    continue  # troca de sala ou animação de item em andamento
                elif self.dialogo:
                    if evento.key in (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE, *TECLAS_INTERAGIR):
                        self.avancar_dialogo()
                elif self.menu_sistema and evento.key not in (
                        pygame.K_UP, pygame.K_w, pygame.K_DOWN, pygame.K_s,
                        pygame.K_RETURN, pygame.K_KP_ENTER, *TECLAS_INTERAGIR):
                    continue  # no menu principal/pausa só navegação e confirmação
                elif evento.key == pygame.K_TAB and not self.inspecionando:
                    # Mapa mental: pistas coletadas e onde o personagem está.
                    self.mapa_mental = not self.mapa_mental
                    self.menu_mapas = self.menu_personagens = False
                    self.pista_aberta = max(0, len(self.pistas) - 1)  # abre na mais recente
                elif self.mapa_mental:
                    # Setas (ou A/D) passam as pistas, uma por vez; E mostra a pista em tela cheia.
                    if self.aba_mental == "notas" and not self.inspecionando:
                        # Anotações: as letras chegam por TEXTINPUT; aqui só apagar e pular linha.
                        if evento.key == pygame.K_BACKSPACE:
                            self.anotacoes = self.anotacoes[:-1]
                        elif evento.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                            self.anotacoes += "\n"
                    elif evento.key == pygame.K_n and not self.inspecionando:
                        self.aba_mental = "notas"
                        self.tocar("menu-mover")
                    elif evento.key in TECLAS_INTERAGIR and self.inspecionando:
                        self.inspecionando = None  # volta ao mapa mental
                    elif evento.key in TECLAS_INTERAGIR and self.pistas:
                        self.pista_aberta %= len(self.pistas)
                        chave = list(self.pistas)[self.pista_aberta]
                        item = ITENS[chave]
                        if chave not in self.imagens_pistas:
                            self.imagens_pistas[chave] = pygame.image.load(caminho(item["imagem"])).convert_alpha()
                        self.inspecionando = SimpleNamespace(imagem=self.imagens_pistas[chave], id=item["id"],
                                                             nome="", mensagem=f"“{item['palpite']}”",
                                                             paginas=[pygame.image.load(caminho(pag)).convert_alpha()
                                                                      for pag in item.get("paginas", [])],
                                                             pagina=0)
                        self.fundo_borrado = borrar(self.tela)
                    elif self.inspecionando:
                        # Caderno: setas ou A/D folheiam as páginas.
                        paginas = self.inspecionando.paginas
                        passo = {pygame.K_LEFT: -1, pygame.K_a: -1, pygame.K_RIGHT: 1, pygame.K_d: 1}.get(evento.key)
                        if paginas and passo:
                            self.inspecionando.pagina = (self.inspecionando.pagina + passo) % len(paginas)
                            self.tocar("menu-mover")
                    elif self.pistas and evento.key in (pygame.K_LEFT, pygame.K_a, pygame.K_UP, pygame.K_w):
                        self.pista_aberta = (self.pista_aberta - 1) % len(self.pistas)
                        self.tocar("menu-mover")
                    elif self.pistas and evento.key in (pygame.K_RIGHT, pygame.K_d, pygame.K_DOWN, pygame.K_s):
                        self.pista_aberta = (self.pista_aberta + 1) % len(self.pistas)
                        self.tocar("menu-mover")
                elif evento.key == pygame.K_CAPSLOCK and self.modo_teste and not self.inspecionando:
                    # Alterna antes/depois do incidente na mesma sala, no mesmo lugar.
                    self.menu_mapas = self.menu_personagens = False
                    self.carregar_mapa(MAPAS[self.chave_mapa]["par"], manter_posicao=True)
                elif evento.key in (pygame.K_LALT, pygame.K_RALT) and self.modo_teste and not self.inspecionando:
                    self.menu_personagens, self.menu_mapas = not self.menu_personagens, False
                    self.cursor = PERSONAGENS_MENU.index(self.personagem)
                elif self.algum_menu() and evento.key in (
                        pygame.K_UP, pygame.K_w, pygame.K_DOWN, pygame.K_s):
                    opcoes = self.opcoes_menu()
                    passo = -1 if evento.key in (pygame.K_UP, pygame.K_w) else 1
                    self.cursor = (self.cursor + passo) % len(opcoes)
                    self.tocar("menu-mover")  # junto com a tecla, no mesmo evento
                elif self.algum_menu() and evento.key in (
                        pygame.K_RETURN, pygame.K_KP_ENTER, *TECLAS_INTERAGIR):
                    self.escolher_no_menu(self.cursor)  # Enter ou E confirma
                elif (self.menu_mapas or self.menu_personagens) and pygame.K_1 <= evento.key <= pygame.K_9:
                    self.escolher_no_menu(evento.key - pygame.K_1)
                elif evento.key in TECLAS_INTERAGIR:
                    self.interagir()

    def escolher_no_menu(self, indice):
        """Escolhe a opção do menu aberto e fecha o menu."""
        opcoes = self.opcoes_menu()
        if not 0 <= indice < len(opcoes):
            return
        self.tocar("menu-confirmar")
        if self.menu_sistema:
            if opcoes[indice] == "sair":
                self.rodando = False
            if opcoes[indice] == "menu":
                # Volta ao menu principal (a partida atual é descartada).
                self.menu_sistema, self.cursor = "principal", 0
                self.cutscene = self.fade = self.inspecionando = self.dialogo = self.obtendo = None
                self.mapa_mental = self.menu_mapas = self.menu_personagens = False
                return
            if opcoes[indice] == "jogar":
                # Escurece o menu por ~2 s antes da cutscene (ver atualizar).
                if self.iniciando is None:
                    self.iniciando = 0.0
                return
            elif opcoes[indice] == "teste":
                # Game test: sem cutscene, com Tab (antes/depois) e Alt (personagens) liberados.
                self.modo_teste = True
                self.pistas = {}
                self.anotacoes = ""
                self.sortear_itens()
                self.personagem = PERSONAGEM
                self.carregar_mapa(MAPAS_MENU[0])
            self.menu_sistema = None  # "jogar", "teste" ou "continuar"
            return
        if self.menu_mapas:
            self.ir_para(opcoes[indice])
        else:
            self.trocar_personagem(opcoes[indice])
        self.menu_mapas = self.menu_personagens = False

    def tocar(self, nome):
        if nome in self.sons:
            self.sons[nome].play()

    def atualizar_ambiente(self):
        """Zumbido do laboratório em loop durante a partida (não no menu principal nem na cutscene)."""
        if "ambiente" not in self.sons:
            return
        jogando = self.menu_sistema != "principal" and not self.cutscene
        if jogando and not self.ambiente_tocando:
            self.sons["ambiente"].play(loops=-1)  # já entra no volume final, sem crescer
        elif not jogando and self.ambiente_tocando:
            self.sons["ambiente"].fadeout(600)
        self.ambiente_tocando = jogando

    def atualizar(self, dt, teclas):
        if self.iniciando is not None:
            # "Jogar": depois do fade do menu, começa a cutscene.
            self.iniciando += dt
            if self.iniciando >= INICIO:
                self.iniciando = None
                self.menu_sistema = None
                self.modo_teste = False
                self.pistas = {}
                self.anotacoes = ""
                self.sortear_itens()
                self.cutscene = Cutscene()
                self.cutscene.ao_escrever = lambda: self.tocar(f"tic-{random.randint(1, 3)}")
            return
        self.atualizar_ambiente()
        if self.cutscene:
            self.cutscene.atualizar(dt)
            if self.cutscene.terminou:
                # Fim da abertura: a Giulia entra na primeira sala, clareando do preto.
                self.cutscene = None
                self.personagem = PERSONAGEM_INICIO
                self.carregar_mapa(SALA_INICIO, na_porta=True)
                self.fade = ["clareando", 0.0, None]
            return
        if self.fade:
            self.fade[1] += dt
            if self.fade[1] >= FADE:
                if self.fade[0] == "escurecendo":
                    self.carregar_mapa(self.fade[2], na_porta=True)
                    self.fade = ["clareando", 0.0, None]
                else:
                    self.fade = None
            return
        if self.dialogo and not self.algum_menu():
            fala = ITENS[self.dialogo["item"].chave]["fala"]
            antes = int(self.dialogo["letras"])
            self.dialogo["letras"] = min(len(fala), self.dialogo["letras"] + 45 * dt)
            if any(not c.isspace() and (antes + i) % 2 == 0 for i, c in enumerate(fala[antes:int(self.dialogo["letras"])])):
                self.tocar(f"tic-{random.randint(1, 3)}")
            return
        if self.obtendo and not self.algum_menu():
            self.obtendo["t"] += dt
            if self.obtendo["t"] >= OBTER:
                contido = ITENS[self.obtendo["item"].chave].get("contem")
                self.obtendo = None
                if contido and contido not in self.pistas:
                    dados = ITENS[contido]
                    dentro = SimpleNamespace(chave=contido, id=dados["id"], nome=dados["nome"], coletado=False)
                    self.dialogo = {"item": dentro, "letras": 0.0}
            return
        if self.inspecionando or self.algum_menu():
            return  # pausado
        self.jogador.atualizar(dt, teclas, self.mapa)
        for item in self.itens:
            item.atualizar(dt)

    def desenhar_caixa(self, texto, fonte, cor, centro):
        rotulo = fonte.render(texto, True, cor)
        fundo = rotulo.get_rect(center=centro).inflate(self.px(10), self.px(4))
        fundo.clamp_ip(self.tela.get_rect())
        caixa = pygame.Surface(fundo.size, pygame.SRCALPHA)
        caixa.fill((60, 60, 66, 150))
        self.tela.blit(caixa, fundo)
        self.tela.blit(rotulo, rotulo.get_rect(center=fundo.center))

    def desenhar_jogo(self):
        visao = self.camera()
        self.tela.fill((0, 0, 0))
        self.mapa.desenhar(self.tela, visao, self.zoom)
        proximo = self.item_proximo()
        porta = self.porta_proxima()
        if porta and not (self.menu_mapas or self.fade):
            # Perto de uma porta, ela brilha como os itens.
            desenhar_brilho(self.tela, pygame.Vector2(porta), visao, self.zoom, pygame.time.get_ticks() / 1000, True)
        pes_y = self.jogador.pes.bottom
        self.mapa.desenhar_objetos(self.tela, visao, self.zoom, pes_y, atras=True)
        self.jogador.desenhar(self.tela, visao, self.zoom)
        self.mapa.desenhar_objetos(self.tela, visao, self.zoom, pes_y, atras=False)
        # Brilho dos itens por cima de tudo (a foto da família fica em cima da mesa).
        for item in self.itens:
            item.desenhar(self.tela, visao, self.zoom, item is proximo)

        if proximo and not (self.dialogo or self.obtendo):
            x = (proximo.posicao.x - visao.x) * self.zoom
            y = (proximo.posicao.y - visao.y - 40) * self.zoom
            self.desenhar_caixa("Pressione E para interagir", self.fonte_grande, (255, 255, 255), (x, y))

        if not (self.dialogo or self.obtendo):
            self.desenhar_caixa(self.mensagem, self.fonte, (230, 230, 230), (self.largura // 2, self.altura - self.px(20)))

    def desenhar_menu(self, titulo, opcoes, atual, dica, veu=True):
        """Menu sobre o jogo: botões clicáveis, com a opção atual em verde."""
        if veu:
            escuro = pygame.Surface(self.tela.get_size(), pygame.SRCALPHA)
            escuro.fill((0, 0, 0, 170))
            self.tela.blit(escuro, (0, 0))
        meio = self.largura // 2
        rotulo = self.fonte_titulo.render(titulo, True, (255, 255, 255))
        # Espaçamento das linhas encolhe para a lista caber na tela.
        topo = min(self.px(140), self.altura // 8)
        passo = min(self.px(36), (self.altura - topo - self.px(110)) // len(opcoes))
        self.tela.blit(rotulo, rotulo.get_rect(midtop=(meio, topo)))
        # Cada opção é um botão: o ponteiro destaca (cinza claro) e o clique escolhe.
        largura = max(self.fonte_grande.size(nome + "  (atual)")[0] for _, nome in opcoes) + self.px(20)
        self.botoes_menu = []
        for i, (chave, nome) in enumerate(opcoes):
            botao = pygame.Rect(0, 0, largura, passo - self.px(4))
            botao.midtop = (meio, topo + self.px(56) + i * passo)
            self.botoes_menu.append(botao)
            destacado = i == self.cursor
            fundo = pygame.Surface(botao.size, pygame.SRCALPHA)
            fundo.fill((150, 150, 158, 110) if destacado else (70, 70, 76, 110))
            self.tela.blit(fundo, botao)
            if destacado:
                pygame.draw.rect(self.tela, (200, 200, 206), botao, 1)
            texto = nome + ("  (atual)" if chave == atual else "")
            cor = (255, 255, 255) if destacado else (120, 255, 140) if chave == atual else (230, 230, 230)
            linha = self.fonte_grande.render(texto, True, cor)
            self.tela.blit(linha, linha.get_rect(center=botao.center))
        rotulo = self.fonte.render(dica, True, (190, 190, 196))
        self.tela.blit(rotulo, rotulo.get_rect(midtop=(meio, topo + self.px(80) + len(opcoes) * passo)))

    def miniatura(self, chave):
        if chave not in self.miniaturas:
            self.miniaturas[chave] = pygame.image.load(caminho(f"mapas/miniaturas/{chave}.png")).convert()
        return self.miniaturas[chave]

    def desenhar_mapa_mental(self):
        """Tab: salas lado a lado com a posição atual e as pistas, uma por vez."""
        veu = pygame.Surface(self.tela.get_size(), pygame.SRCALPHA)
        veu.fill((6, 10, 8, 235))
        self.tela.blit(veu, (0, 0))
        margem = self.px(24)
        titulo = self.fonte_titulo.render("Mapa mental", True, (226, 230, 222))
        self.tela.blit(titulo, (margem, margem))
        topo = margem + titulo.get_height() + self.px(14)

        # Salas: grade de miniaturas (versão da fase atual), a atual contornada.
        sufixo = "-pos-incidente" if pos_incidente(self.chave_mapa) else ""
        colunas, linhas = len(SALAS_MAPA_MENTAL[0]), len(SALAS_MAPA_MENTAL)
        espaco, legenda = self.px(8), 2 * self.fonte_pequena.get_linesize()  # nome pode ocupar 2 linhas
        barra_altura = self.px(46)  # espaço da "progressão da verdade" embaixo da grade
        lado = min((int(self.largura * 0.52) - (colunas - 1) * espaco) // colunas,
                   (self.altura - topo - margem - barra_altura - linhas * (legenda + espaco)) // linhas)
        for l, fileira in enumerate(SALAS_MAPA_MENTAL):
            for c, sala in enumerate(fileira):
                chave = sala + sufixo
                quadro = pygame.Rect(margem + c * (lado + espaco), topo + l * (lado + legenda + espaco * 2), lado, lado)
                # Amplia sem suavizar: a miniatura fica pixelada, de propósito.
                self.tela.blit(pygame.transform.scale(self.miniatura(chave), quadro.size), quadro)
                atual = chave == self.chave_mapa
                if not atual:
                    sombra = pygame.Surface(quadro.size, pygame.SRCALPHA)
                    sombra.fill((0, 0, 0, 90))
                    self.tela.blit(sombra, quadro)
                pygame.draw.rect(self.tela, (150, 190, 120) if atual else (60, 76, 64), quadro,
                                 max(1, self.px(2)) if atual else 1)
                for n, linha in enumerate(quebrar_texto(self.fonte_pequena, self.nome_sala(chave), lado)[:2]):
                    nome = self.fonte_pequena.render(linha, True, (226, 196, 142) if atual else (150, 160, 150))
                    self.tela.blit(nome, nome.get_rect(midtop=(quadro.centerx, quadro.bottom + self.px(3)
                                                               + n * self.fonte_pequena.get_linesize())))
                if atual:
                    pes_x, pes_y = self.jogador.pes.midbottom
                    ponto = (quadro.x + pes_x / self.mapa.tamanho[0] * lado,
                             quadro.y + pes_y / self.mapa.tamanho[1] * lado)
                    pulso = (math.sin(pygame.time.get_ticks() / 250) + 1) / 2
                    pygame.draw.circle(self.tela, (226, 196, 142), ponto, self.px(5 + 3 * pulso), max(1, self.px(1)))
                    pygame.draw.circle(self.tela, (226, 196, 142), ponto, self.px(3))
        direita = margem + colunas * lado + (colunas - 1) * espaco
        self.desenhar_progresso(pygame.Rect(margem, topo + linhas * (lado + legenda + espaco * 2),
                                            direita - margem, barra_altura))

        # Abas: pistas ou anotações.
        x = direita + self.px(32)
        largura = self.largura - x - margem
        self.abas_mental = {}
        ax = x
        for aba, texto in (("pistas", f"Pistas ({len(self.pistas)})"), ("notas", "Anotações")):
            ativa = aba == self.aba_mental
            rotulo = self.fonte_grande.render(texto, True, (150, 190, 120) if ativa else (110, 124, 112))
            retangulo = rotulo.get_rect(topleft=(ax, topo)).inflate(self.px(14), self.px(6))
            retangulo.topleft = (ax, topo)
            if ativa:
                pygame.draw.rect(self.tela, (20, 32, 26), retangulo)
            pygame.draw.rect(self.tela, (88, 112, 92) if ativa else (44, 56, 48), retangulo, 1)
            self.tela.blit(rotulo, rotulo.get_rect(center=retangulo.center))
            self.abas_mental[aba] = retangulo
            ax = retangulo.right + self.px(8)
        y = topo + retangulo.height + self.px(12)
        if self.aba_mental == "notas":
            self.desenhar_anotacoes(pygame.Rect(x, y, largura, self.altura - y - margem - self.px(28)))
        elif not self.pistas:
            vazio = self.fonte.render("Nenhuma pista coletada ainda.", True, (170, 176, 168))
            self.tela.blit(vazio, (x, y))
        else:
            self.pista_aberta %= len(self.pistas)
            chave, onde = list(self.pistas.items())[self.pista_aberta]
            item = ITENS[chave]
            arte = self.imagens_pistas.get(chave)
            if arte is None:
                arte = self.imagens_pistas[chave] = pygame.image.load(caminho(item["imagem"])).convert_alpha()
            lado_arte = min(largura, self.px(190))
            arte = pygame.transform.smoothscale(arte, (lado_arte, round(lado_arte * arte.get_height() / arte.get_width())))
            moldura = arte.get_rect(midtop=(x + largura // 2, y))
            pygame.draw.rect(self.tela, (14, 22, 19), moldura.inflate(self.px(12), self.px(12)))
            pygame.draw.rect(self.tela, (88, 112, 92), moldura.inflate(self.px(12), self.px(12)), 1)
            self.tela.blit(arte, moldura)
            y = moldura.bottom + self.px(16)
            # O que a Giulia acha que é (ela não sabe o que o item revela).
            for linha in quebrar_texto(self.fonte_grande, f"“{item['palpite']}”", largura):
                texto = self.fonte_grande.render(linha, True, (226, 230, 222))
                self.tela.blit(texto, (x, y))
                y += texto.get_height()
            y += self.px(6)
            for linha in quebrar_texto(self.fonte, f"{item['id']} · encontrado em: {self.nome_sala(onde)}", largura):
                local = self.fonte.render(linha, True, (150, 160, 150))
                self.tela.blit(local, (x, y))
                y += local.get_height()
            if len(self.pistas) > 1:
                passar = self.fonte.render(f"<  {self.pista_aberta + 1} / {len(self.pistas)}  >",
                                           True, (150, 190, 120))
                self.tela.blit(passar, passar.get_rect(midbottom=(x + largura // 2, self.altura - margem - self.px(24))))
        if self.aba_mental == "notas":
            texto_dica = "Esc volta às pistas · Tab fecha"
        else:
            texto_dica = ("A/D passar · E ampliar · " if self.pistas else "") + "N anotações · Tab fecha"
        dica = self.fonte_pequena.render(texto_dica, True, (190, 196, 188))
        self.tela.blit(dica, dica.get_rect(bottomright=(self.largura - margem, self.altura - margem)))

    def desenhar_progresso(self, area):
        """Progressão da verdade: quanto dos itens do caso já foi encontrado."""
        porcentagem = round(100 * len(self.pistas) / max(1, len(ITENS)))
        rotulo = self.fonte.render("Progressão da verdade", True, (190, 196, 188))
        valor = self.fonte_grande.render(f"{porcentagem}%", True, (226, 196, 142))
        self.tela.blit(rotulo, (area.x, area.y))
        self.tela.blit(valor, valor.get_rect(topright=(area.right, area.y - self.px(2))))
        barra = pygame.Rect(area.x, area.y + rotulo.get_height() + self.px(6), area.width, self.px(8))
        pygame.draw.rect(self.tela, (20, 32, 26), barra)
        cheio = barra.copy()
        cheio.width = round(barra.width * porcentagem / 100)
        pygame.draw.rect(self.tela, (150, 190, 120), cheio)
        pygame.draw.rect(self.tela, (88, 112, 92), barra, 1)

    def desenhar_anotacoes(self, area):
        """Caderno de folhas pautadas onde o jogador escreve, com letra de mão."""
        sombra = area.move(self.px(4), self.px(4))
        pygame.draw.rect(self.tela, (0, 0, 0), sombra)
        pygame.draw.rect(self.tela, (238, 230, 206), area)
        fonte = self.fonte_mao
        altura_linha = fonte.get_linesize() + self.px(2)
        topo_texto = area.y + self.px(14)
        # Pauta azul, margem vermelha e a espiral do caderno.
        margem_x = area.x + self.px(40)
        y = topo_texto + altura_linha
        while y < area.bottom - self.px(6):
            pygame.draw.line(self.tela, (150, 176, 206), (area.x + self.px(6), y), (area.right - self.px(6), y))
            y += altura_linha
        pygame.draw.line(self.tela, (214, 120, 112), (margem_x, area.y), (margem_x, area.bottom), max(1, self.px(1)))
        for furo_y in range(area.y + self.px(14), area.bottom - self.px(8), self.px(22)):
            pygame.draw.circle(self.tela, (40, 44, 42), (area.x + self.px(14), furo_y), self.px(4))
            pygame.draw.arc(self.tela, (150, 156, 160), pygame.Rect(area.x - self.px(4), furo_y - self.px(5),
                                                                    self.px(20), self.px(10)), 0.6, 3.6, max(1, self.px(2)))
        # Texto: cada parágrafo quebrado na largura da folha; mostra as últimas linhas se não couber.
        largura_texto = area.right - margem_x - self.px(16)
        linhas = []
        for paragrafo in self.anotacoes.split("\n"):
            linhas += quebrar_texto(fonte, paragrafo, largura_texto) or [""]
        cabem = max(1, (area.bottom - topo_texto - self.px(8)) // altura_linha)
        linhas = linhas[-cabem:]
        x_texto = margem_x + self.px(10)
        if not self.anotacoes:
            vazio = fonte.render("Escreva aqui o que for importante...", True, (160, 150, 128))
            self.tela.blit(vazio, (x_texto, topo_texto + altura_linha - fonte.get_ascent() - self.px(3)))
        for n, linha in enumerate(linhas):
            texto = fonte.render(linha, True, (34, 52, 110))
            self.tela.blit(texto, (x_texto, topo_texto + (n + 1) * altura_linha - fonte.get_ascent() - self.px(3)))
        if pygame.time.get_ticks() // 500 % 2 == 0:  # cursor piscando no fim do texto
            ultima = linhas[-1] if linhas and self.anotacoes else ""
            cx = x_texto + fonte.size(ultima)[0] + self.px(2)
            cy = topo_texto + len(linhas if self.anotacoes else [""]) * altura_linha
            pygame.draw.line(self.tela, (34, 52, 110), (cx, cy - fonte.get_ascent()), (cx, cy - self.px(3)), max(1, self.px(2)))

    def desenhar_obtencao(self):
        """Animação de conseguir o item, sem texto: surge no centro com raios e voa para o mapa mental."""
        t = self.obtendo["t"]
        suave = lambda x: 1 - (1 - max(0.0, min(1.0, x))) ** 3
        escuro = suave(t / 0.3) if t < 1.8 else 1 - suave((t - 1.8) / 0.4)
        veu = pygame.Surface(self.tela.get_size(), pygame.SRCALPHA)
        veu.fill((6, 10, 8, round(170 * escuro)))
        self.tela.blit(veu, (0, 0))
        centro = pygame.Vector2(self.largura / 2, self.altura / 2)
        destino = pygame.Vector2(self.largura - self.px(40), self.px(40))  # canto do mapa mental
        lado_cheio = self.px(200)
        if t < 0.45:  # surge crescendo e passa um pouco do tamanho
            escala = suave(t / 0.35) * (1.12 if t < 0.35 else 1.12 - 0.12 * (t - 0.35) / 0.1)
            posicao = centro
        elif t < 1.3:  # flutua
            escala = 1.0
            posicao = centro + pygame.Vector2(0, math.sin((t - 0.45) * 6) * self.px(4))
        else:  # encolhe e voa para o canto
            k = suave((t - 1.3) / 0.5)
            escala = 1.0 - 0.85 * k
            posicao = centro.lerp(destino, k)
        # Raios girando atrás do item (somem quando ele começa a voar).
        if t < 1.4:
            forca = min(1.0, t / 0.3) * (1 if t < 1.2 else 1 - (t - 1.2) / 0.2)
            raios = pygame.Surface(self.tela.get_size(), pygame.SRCALPHA)
            for n in range(12):
                angulo = t * 0.8 + n * math.pi / 6
                largura = 0.09
                comprimento = self.px(230) * (0.8 + 0.2 * math.sin(t * 3 + n))
                pontos = [posicao, posicao + pygame.Vector2(math.cos(angulo - largura), math.sin(angulo - largura)) * comprimento,
                          posicao + pygame.Vector2(math.cos(angulo + largura), math.sin(angulo + largura)) * comprimento]
                pygame.draw.polygon(raios, (226, 196, 142, round(60 * forca)), pontos)
            self.tela.blit(raios, (0, 0))
            z = self.zoom * 3 * forca + 0.01  # brilho grande, no mesmo desenho dos itens no mapa
            desenhar_brilho(self.tela, posicao / z, pygame.Rect(0, 0, 1, 1), z, t, True)
        lado = max(1, round(lado_cheio * escala))
        arte = pygame.transform.smoothscale(self.obtendo["arte"], (lado, lado))
        self.tela.blit(arte, arte.get_rect(center=posicao))
        # Chegada no canto: um anel que se abre.
        if t > 1.75:
            k = min(1.0, (t - 1.75) / 0.45)
            pygame.draw.circle(self.tela, (150, 190, 120), destino, self.px(8 + 26 * k), max(1, self.px(3 * (1 - k))))

    def desenhar_inspecao(self):
        item = self.inspecionando
        if self.fundo_borrado is None:
            self.desenhar_jogo()
            self.fundo_borrado = borrar(self.tela)
        self.tela.blit(self.fundo_borrado, (0, 0))
        veu = pygame.Surface(self.tela.get_size(), pygame.SRCALPHA)
        veu.fill((0, 0, 0, 120))
        self.tela.blit(veu, (0, 0))

        meio = self.largura // 2
        lado = self.px(280)
        paginas = getattr(item, "paginas", None)
        if paginas:
            # Caderno aberto na página atual, mantendo a proporção da página.
            pagina = paginas[item.pagina]
            escala = min(self.largura * 0.8 / pagina.get_width(), lado / pagina.get_height())
            arte = pygame.transform.smoothscale(pagina, (round(pagina.get_width() * escala), round(pagina.get_height() * escala)))
            self.tela.blit(arte, arte.get_rect(midtop=(meio, self.px(20))))
            if len(paginas) > 1:
                contador = self.fonte_grande.render(f"<   página {item.pagina + 1} / {len(paginas)}   >", True, (150, 190, 120))
                self.tela.blit(contador, contador.get_rect(midbottom=(meio, self.altura - self.px(40))))
        else:
            arte = pygame.transform.smoothscale(item.imagem, (lado, lado))
            self.tela.blit(arte, arte.get_rect(midtop=(meio, self.px(20))))
        titulo = self.fonte_titulo.render(f"{item.id} — {item.nome}" if item.nome else item.id, True, (255, 255, 255))
        self.tela.blit(titulo, titulo.get_rect(midtop=(meio, self.px(315))))
        largura_texto = min(self.largura - self.px(80), self.px(800))
        for i, linha in enumerate(quebrar_texto(self.fonte_grande, item.mensagem, largura_texto)):
            texto = self.fonte_grande.render(linha, True, (225, 225, 225))
            self.tela.blit(texto, texto.get_rect(midtop=(meio, self.px(362 + i * 26))))
        dica = self.fonte.render(("A/D folheia · " if len(getattr(item, "paginas", None) or []) > 1 else "") + "Pressione E para continuar",
                                 True, (190, 190, 196))
        self.tela.blit(dica, dica.get_rect(midbottom=(meio, self.altura - self.px(16))))

    def desenhar(self):
        if self.cutscene:
            self.cutscene.desenhar(self.tela, self.px)
        elif self.menu_sistema == "principal":
            self.tela.fill((0, 0, 0))  # menu principal sem fundo
            self.desenhar_menu("Amostra 47", MENUS_SISTEMA["principal"], None,
                               "Clique ou E para escolher", veu=False)
            if self.iniciando is not None:
                veu = pygame.Surface(self.tela.get_size())
                veu.set_alpha(round(255 * min(1.0, self.iniciando / INICIO)))
                self.tela.blit(veu, (0, 0))
        elif self.menu_sistema == "pausa":
            self.desenhar_jogo()
            self.desenhar_menu("Pausa", MENUS_SISTEMA["pausa"], None, "Clique ou E para escolher · Esc para voltar")
        elif self.mapa_mental and not self.inspecionando:
            self.desenhar_jogo()
            self.desenhar_mapa_mental()
        elif self.inspecionando:
            self.desenhar_inspecao()
        else:
            self.desenhar_jogo()
            if self.menu_mapas:
                self.desenhar_menu("Ir para", [(c, self.nome_sala(c)) for c in self.destinos],
                                   self.chave_mapa, "Clique ou E para escolher · Esc para fechar")
            elif self.menu_personagens:
                self.desenhar_menu("Trocar personagem", [(c, PERSONAGENS[c]["nome"]) for c in PERSONAGENS_MENU],
                                   self.personagem, "Clique ou E para escolher · Esc para fechar")
            if self.dialogo:
                fala = ITENS[self.dialogo["item"].chave]["fala"]
                seta = self.dialogo["letras"] >= len(fala) and pygame.time.get_ticks() // 500 % 2 == 0
                self.caixa.desenhar(self.tela, self.px, self.jogador.nome.split()[0], fala, self.dialogo["letras"], seta)
            if self.obtendo:
                self.desenhar_obtencao()
        if self.fade:
            # Escurece até o preto e depois clareia na sala nova.
            t = min(1.0, self.fade[1] / FADE)
            veu = pygame.Surface(self.tela.get_size())
            veu.set_alpha(round(255 * (t if self.fade[0] == "escurecendo" else 1 - t)))
            self.tela.blit(veu, (0, 0))
        pygame.display.flip()

    def executar(self):
        while self.rodando:
            dt = self.relogio.tick(FPS) / 1000
            self.tratar_eventos()
            self.atualizar(dt, pygame.key.get_pressed())
            self.desenhar()
        pygame.quit()


if __name__ == "__main__":
    Jogo().executar()
    sys.exit()
