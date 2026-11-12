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
from cutscene import CaixaTexto, Cutscene, VideoAbertura, desenhar_legenda
from flashback import Flashback
from entidades import Item, Jogador, Mapa, caminho, desenhar_brilho

# Conteúdo desta beta: troque as chaves para usar outro personagem/mapa/item.
PERSONAGEM = "otavio-ferraz"
# Depois da cutscene de abertura, o jogo começa com a Giulia nesta sala (entrando pela porta).
PERSONAGEM_INICIO = "giulia-pistori"
SALA_INICIO = "sala-de-evacuacao-pos-incidente"
FACHADA = "fachada-do-complexo"  # depois da abertura; a porta leva para SALA_INICIO
GERADOR = (234, 274)  # na fachada: ponto de interação do gerador (liga a energia do complexo)
# Personagens jogáveis do menu (Alt abre; 1, 2... trocam).
# Suspeitos da aba "Culpado" do mapa mental (só um chute por partida).
SUSPEITOS = ["giovani-pistori", "angela-torres", "amie-lin", "beatrice-salles", "clara-costa",
             "otavio-ferraz", "fernando-almeida"]
CULPADO = "fernando-almeida"
# O chute também pede onde e como (docs/caso-amostra47.md: alteração manual dos parâmetros na
# Câmara de contenção, com autorização administrativa da direção e sem arrombamento).
LOCAIS_CHUTE = ["Câmara de contenção", "Laboratório de análises", "Túnel de ventilação",
                "Sala de servidores", "Central de segurança", "Sala de evacuação"]
ONDE = "Câmara de contenção"
MINIMO_CHUTE = 30  # % da verdade descoberta para poder acusar
COMO_CHUTE = [
    "Arrombou a câmara e levou a amostra à força",
    "Alterou a contenção com uma autorização da direção",
    "Sabotou a ventilação para espalhar o agente",
    "Facilitou uma invasão externa sem câmeras",
    "Deixou um frasco mal lacrado (um acidente)",
    "Desligou os geradores e trancou as portas",
]
COMO = COMO_CHUTE[1]
# Etapas do chute: (título, pergunta, opções em texto); quem usa os SUSPEITOS.
ETAPAS_CHUTE = [
    ("Quem", "Quem liberou a Amostra 47?", None),
    ("Onde", "Em qual setor tudo começou?", LOCAIS_CHUTE),
    ("Como", "Como a amostra foi liberada?", COMO_CHUTE),
]
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
AVISO = 4.0  # segundos do aviso no topo da tela (ex.: "Premissas atualizadas")
# Post-it preso na primeira página das anotações: as premissas auxiliares (as outras vêm dos itens).
POST_IT = [
    "Y = Fernando Almeida foi responsável pela liberação da Amostra 47.",
    "O = Otávio Ferraz foi responsável pela liberação da Amostra 47.",
    "B = Beatrice Salles foi responsável pela liberação da Amostra 47.",
    "G = Giovani Pistori foi responsável pela liberação da Amostra 47.",
    "I = Houve uma invasão externa responsável pela liberação da amostra.",
    "A = Houve arrombamento da câmara de contenção.",
]
TECLA_GRAVACAO = pygame.K_r  # toca/para as gravações na inspeção (E volta)
DISTANCIA_PORTA = 12  # folga (unidades) além do ponto mais perto que os pés alcançam da porta
# Mapa mental (Tab): miniaturas das salas (ferramentas/gerar_miniaturas.py), lado a lado.
SALAS_MAPA_MENTAL = [
    ["central-de-seguranca", "sala-de-servidores", "laboratorio-de-analises"],
    ["camara-de-contencao", "sala-de-evacuacao", "tunel-de-ventilacao"],
]
INICIO = 2.0  # segundos do fade do menu principal ao escolher Jogar
FADE = 0.35  # segundos para escurecer (e o mesmo para clarear)
# Computador da central de segurança: só funciona depois de pegar o pendrive e abre o flashback.
COMPUTADOR = {"central-de-seguranca-pos-incidente": (360, 190), "central-de-seguranca": (360, 190)}  # mesa de cima, sob o painel
PENDRIVE = "pendrive-criptografado"
CRACHA = "cracha-de-acesso"  # o crachá do Giovani também é preciso para acessar as câmeras
ORDEM = "ordem-de-manutencao"
ENTRAR_FLASHBACK = 1.0  # segundos escurecendo antes do flashback


def pos_incidente(chave):
    return chave.endswith("-pos-incidente")


def quebrar_texto(fonte, texto, largura):
    linhas, atual = [], ""
    for palavra in texto.split():
        teste = f"{atual} {palavra}".strip()
        if fonte.size(teste)[0] <= largura:
            atual = teste
            continue
        if atual:
            linhas.append(atual)
        # Palavra mais larga que a linha: quebra no meio, letra por letra.
        atual = ""
        for letra in palavra:
            if atual and fonte.size(atual + letra)[0] > largura:
                linhas.append(atual)
                atual = ""
            atual += letra
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
    "principal": [("jogar", "Jogar"), ("teste", "Game test"), ("volume", "Opções"), ("sair", "Sair")],
    "pausa": [("continuar", "Continuar"), ("volume", "Opções"), ("menu", "Menu principal"), ("sair", "Sair")],
    "volume": [("efeitos", "Efeitos sonoros"), ("musica", "Música"), ("voltar", "Voltar")],
}
# Volume de cada som com os controles no máximo; o menu de volume multiplica por
# "efeitos" (tiques e barulhos) ou "musica" (o ambiente).
VOLUMES_BASE = {
    "ambiente": 0.04, "floresta": 0.25, "pista": 0.55, "menu-mover": 0.5, "menu-confirmar": 0.6,
    "tic-1": 0.07, "tic-2": 0.07, "tic-3": 0.07,  # "tic" das falas, bem baixo
    "tecla-1": 0.05, "tecla-2": 0.05, "tecla-3": 0.05,  # digitar nas anotações, bem baixinho
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
            for nome in ("tic-1", "tic-2", "tic-3", "pista", "ambiente", "menu-mover", "menu-confirmar",
                         "tecla-1", "tecla-2", "tecla-3", "floresta"):
                self.sons[nome] = pygame.mixer.Sound(caminho(f"sons/{nome}.wav"))
        except (pygame.error, FileNotFoundError) as erro:
            print(f"[som] sem áudio: {erro}")
            self.sons = {}
        self.ambiente_tocando = None  # nome do som de ambiente em loop, ou None
        self.volume = {"efeitos": 1.0, "musica": 1.0}  # controles do menu de volume (0 a 1)
        self.volume_origem = "principal"  # menu de onde se abriu o de volume
        self.aplicar_volumes()
        self.iniciando = None  # tempo do fade do menu principal ao escolher Jogar
        pygame.display.set_caption("Amostra 47 — beta")
        self.tamanho_janela = JANELA_INICIAL
        self.tela_cheia = False
        self.relogio = pygame.time.Clock()
        self.aplicar_modo()

        self.personagem = PERSONAGEM
        self.menu_personagens = False  # menu de troca de personagem aberto (jogo pausado)
        self.inspecionando = None  # item aberto na tela de inspeção (jogo pausado)
        self.gravacoes = {}  # áudios dos itens (gravador), carregados na primeira vez
        self.canal_gravacao = None  # canal tocando uma gravação agora
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
        self.aba_mental = "pistas"  # aba do mapa mental: "pistas", "notas" ou "culpado"
        self.aviso = None  # aviso no topo da tela: {"texto", "t"}
        self.tutorial_inicio = False  # painel de controles logo depois da introdução
        self.final = None  # revelação narrada depois de acertar o culpado: {"t": segundos}
        self.chute = None  # suspeito escolhido na aba "Culpado" (uma vez por partida)
        self.cursor_suspeito = 0
        self.etapa_chute = 0  # 0 = quem, 1 = onde, 2 = como
        self.respostas_chute = [0, 0, 0]  # opção marcada em cada etapa
        self.confirmando_chute = None  # None, ou opção marcada no aviso: 0 = sim, 1 = não
        self.botoes_suspeitos = []
        self.botoes_aviso = []
        self.anotacoes = ""  # o que o jogador escreveu no caderno do mapa mental
        self.pagina_notas = None  # página aberta no caderno; None = a última (onde se escreve)
        self.abas_mental = {}  # aba -> retângulo clicável
        self.paginas_notas_total = 1
        self.apagando = 0.0  # tempo segurando Backspace nas anotações
        self.dialogo = None  # fala ao achar um item: {"item", "letras"}
        self.obtendo = None  # animação de conseguir o item: {"item", "t", "arte"}
        self.conversa = None  # falas soltas: {"falas": [(nome, texto)], "i", "letras", "fim"}
        self.flashback = None  # cena do computador da central em andamento
        self.indo_flashback = None  # tempo escurecendo antes do flashback
        self.flashback_visto = False
        self.energia_ligada = False
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
        self.jogador.escala *= MAPAS[chave].get("escala_personagens", 1.0)
        self.jogador.velocidade *= MAPAS[chave].get("velocidade_personagens", 1.0)
        if self.energia_ligada:
            self.mapa.ligar("gerador")  # ex.: fachada, vista de mais longe
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

    def premissas(self, chave):
        """Premissas do item; depois de ver as câmeras (flashback), as atualizadas, se houver."""
        item = ITENS[chave]
        if self.flashback_visto and "premissas_cameras" in item:
            return item["premissas_cameras"]
        return item.get("premissas", [])

    def camera(self):
        """Retângulo do mundo visível, centrado no personagem e preso ao mapa."""
        visao = pygame.Rect(0, 0, round(self.largura / self.zoom), round(self.altura / self.zoom))
        visao.center = self.jogador.centro
        visao.clamp_ip(pygame.Rect((0, 0), self.mapa.tamanho))
        return visao

    def computador_disponivel(self):
        """Ponto do computador da central, se ele já puder ser usado nesta sala."""
        if self.flashback_visto or PENDRIVE not in self.pistas or CRACHA not in self.pistas:
            return None
        return COMPUTADOR.get(self.chave_mapa)

    def gerador_proximo(self):
        """Gerador da fachada ainda desligado e ao alcance."""
        if self.chave_mapa != FACHADA or self.energia_ligada:
            return False
        return pygame.Vector2(GERADOR).distance_to(self.jogador.centro) <= Item.DISTANCIA_INTERACAO + 10

    def ligar_gerador(self):
        self.energia_ligada = True
        self.mapa.ligar("gerador")
        self.tocar("menu-mover")
        self.falar([(self.jogador.nome.split()[0], "Pronto... a energia voltou. Agora a porta deve abrir.")])

    def computador_proximo(self):
        ponto = self.computador_disponivel()
        if ponto and pygame.Vector2(ponto).distance_to(self.jogador.centro) <= Item.DISTANCIA_INTERACAO:
            return ponto
        return None

    def falar(self, falas, fim=None):
        """Caixa de texto com uma ou mais falas; ``fim`` é chamada depois da última."""
        self.conversa = {"falas": falas, "i": 0, "letras": 0.0, "fim": fim}

    def avancar_conversa(self):
        conversa = self.conversa
        texto = conversa["falas"][conversa["i"]][1]
        if conversa["letras"] < len(texto):
            conversa["letras"] = len(texto)
            return
        conversa["i"] += 1
        conversa["letras"] = 0.0
        if conversa["i"] >= len(conversa["falas"]):
            self.conversa = None
            if conversa["fim"]:
                conversa["fim"]()

    def comecar_flashback(self):
        self.flashback_visto = True
        self.indo_flashback = 0.0
        print("[flashback] início")

    def fim_flashback(self):
        """Volta à central clareando; a Giulia comenta conforme já tenha (ou não) a ordem."""
        self.flashback = None
        self.fade = ["clareando", 0.0, None]
        nome = self.jogador.nome.split()[0]
        if ORDEM in self.pistas:
            falas = [(nome, "Então ela não assinou aquele papel?")]
        else:
            falas = [(nome, "Tenho que encontrar esse papel...")]
        self.falar(falas)
        self.aviso = {"texto": "Premissas atualizadas", "t": 0.0}

    def interagir(self):
        if self.inspecionando:
            self.fechar_inspecao()  # fecha a inspeção e retoma o jogo
            return
        item = self.item_proximo()
        if not item and self.computador_proximo():
            self.falar([(self.jogador.nome.split()[0], "Vamos ver...")], fim=self.comecar_flashback)
        elif not item and self.gerador_proximo():
            self.ligar_gerador()
        elif not item and self.porta_proxima():
            if self.chave_mapa == FACHADA and not self.energia_ligada:
                self.falar([(self.jogador.nome.split()[0],
                             "Está trancada... sem energia, ela não abre. Deve ter um gerador por aqui.")])
            elif self.chave_mapa == FACHADA:
                self.ir_para(SALA_INICIO)  # entra no complexo
            else:
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

    def aplicar_volumes(self):
        for nome, som in self.sons.items():
            som.set_volume(VOLUMES_BASE.get(nome, 0.5) * self.volume["musica" if nome in ("ambiente", "floresta") else "efeitos"])

    def mudar_volume(self, tipo, passo):
        """Muda um volume em passos de 10% (entre 0 e 100%) e toca um som de exemplo."""
        self.volume[tipo] = round(min(1.0, max(0.0, self.volume[tipo] + passo)), 1)
        self.aplicar_volumes()
        if tipo == "efeitos":
            self.tocar("menu-mover")

    def tecla_esc(self):
        """Esc fecha o que estiver aberto; no jogo, abre o menu de pausa."""
        if self.menu_sistema == "volume":
            self.menu_sistema, self.cursor = self.volume_origem, 2 if self.volume_origem == "principal" else 1
        elif self.menu_sistema == "pausa":
            self.menu_sistema = None
        elif self.menu_sistema:
            return  # no menu principal, Esc não faz nada
        elif self.inspecionando:
            self.fechar_inspecao()
        elif self.mapa_mental and self.confirmando_chute is not None:
            self.confirmando_chute = None
        elif self.mapa_mental and self.aba_mental in ("notas", "culpado"):
            self.aba_mental = "pistas"
        elif self.mapa_mental:
            self.mapa_mental = False
        elif self.menu_mapas or self.menu_personagens:
            self.menu_mapas = self.menu_personagens = False
        else:
            self.menu_sistema, self.cursor = "pausa", 0

    def tratar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEWHEEL and self.inspecionando and not self.menu_sistema:
                self.ampliar_folha(evento.y)  # roda do mouse: zoom na folha
                continue
            if self.tutorial_inicio and evento.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                if getattr(evento, "key", None) in (*TECLAS_INTERAGIR, pygame.K_RETURN, pygame.K_ESCAPE) \
                        or evento.type == pygame.MOUSEBUTTONDOWN:
                    self.tutorial_inicio = False
                    self.tocar("menu-confirmar")
                continue
            if self.final and evento.type != pygame.QUIT:
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    self.fim_final()
                continue
            if self.iniciando is not None and evento.type != pygame.QUIT:
                continue  # escurecendo para começar: ignora teclas e cliques
            if evento.type == pygame.QUIT:
                self.rodando = False
            elif evento.type == pygame.VIDEORESIZE and not self.tela_cheia:
                self.tamanho_janela = evento.size
                self.ajustar_escala()
            elif evento.type == pygame.TEXTINPUT:
                if self.mapa_mental and self.aba_mental == "notas" and not self.inspecionando and not self.menu_sistema:
                    self.anotacoes = (self.anotacoes + evento.text)[:20000]
                    self.pagina_notas = None
                    self.tocar(f"tecla-{random.randint(1, 3)}")
            elif self.mapa_mental and not self.menu_sistema and evento.type == pygame.MOUSEBUTTONDOWN \
                    and evento.button == 1:
                if self.aba_mental == "culpado" and not self.inspecionando:
                    self.clicar_culpado(evento.pos)
                for aba, retangulo in self.abas_mental.items():
                    if self.confirmando_chute is not None:
                        break
                    if retangulo.collidepoint(evento.pos) and aba != self.aba_mental:
                        self.aba_mental = aba
                        self.tocar("menu-mover")
            elif self.dialogo and not self.menu_sistema and evento.type == pygame.MOUSEBUTTONDOWN \
                    and evento.button == 1:
                self.avancar_dialogo()
            elif self.indo_flashback is not None and evento.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN) \
                    and getattr(evento, "key", None) != pygame.K_F11:
                continue  # escurecendo para o flashback
            elif self.flashback and evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                self.flashback.avancar()
            elif self.flashback and evento.type == pygame.KEYDOWN and evento.key != pygame.K_F11:
                if evento.key == pygame.K_ESCAPE:
                    self.flashback.pular()
                elif evento.key in (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE, *TECLAS_INTERAGIR):
                    self.flashback.avancar()
            elif self.conversa and not self.menu_sistema and not self.fade \
                    and evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                self.avancar_conversa()
            elif self.cutscene and (evento.type == pygame.MOUSEBUTTONDOWN
                                    or (evento.type == pygame.KEYDOWN and evento.key != pygame.K_F11)):
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    self.cutscene.pular()  # Esc pula a abertura inteira; as falas não se adiantam
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
                elif self.conversa and not self.menu_sistema:
                    if evento.key in (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE, *TECLAS_INTERAGIR):
                        self.avancar_conversa()
                elif self.menu_sistema == "volume" and evento.key in (pygame.K_LEFT, pygame.K_a, pygame.K_RIGHT, pygame.K_d):
                    tipo = ("efeitos", "musica", None)[self.cursor]
                    if tipo:
                        self.mudar_volume(tipo, -0.1 if evento.key in (pygame.K_LEFT, pygame.K_a) else 0.1)
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
                            self.pagina_notas = None
                            self.tocar("tecla-1")
                        elif evento.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                            self.anotacoes += "\n"
                            self.pagina_notas = None
                            self.tocar("tecla-2")
                        elif evento.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_PAGEUP, pygame.K_PAGEDOWN):
                            # Setas viram as páginas do caderno (letras não, que são para escrever).
                            total = self.paginas_notas_total
                            atual = total - 1 if self.pagina_notas is None else self.pagina_notas
                            atual += -1 if evento.key in (pygame.K_LEFT, pygame.K_PAGEUP) else 1
                            if 0 <= atual < total:
                                self.pagina_notas = None if atual == total - 1 else atual
                                self.tocar("menu-mover")
                    elif self.aba_mental == "culpado" and not self.inspecionando:
                        self.tecla_culpado(evento.key)
                    elif evento.key == pygame.K_n and not self.inspecionando:
                        self.aba_mental = "notas"
                        self.tocar("menu-mover")
                    elif evento.key == pygame.K_c and not self.inspecionando:
                        self.aba_mental = "culpado"
                        self.tocar("menu-mover")
                    elif evento.key == TECLA_GRAVACAO and self.inspecionando and self.inspecionando.audio:
                        self.tocar_gravacao()
                    elif evento.key in TECLAS_INTERAGIR and self.inspecionando:
                        self.fechar_inspecao()  # volta ao mapa mental
                    elif evento.key in TECLAS_INTERAGIR and self.pistas:
                        self.pista_aberta %= len(self.pistas)
                        chave = list(self.pistas)[self.pista_aberta]
                        item = ITENS[chave]
                        if chave not in self.imagens_pistas:
                            self.imagens_pistas[chave] = pygame.image.load(caminho(item["imagem"])).convert_alpha()
                        self.inspecionando = SimpleNamespace(imagem=self.imagens_pistas[chave], id=item["id"],
                                                             nome=item["nome"], mensagem=f"“{item['palpite']}”",
                                                             texto=item.get("texto", []),
                                                             paginas=[pygame.image.load(caminho(pag)).convert_alpha()
                                                                      for pag in item.get("paginas", [])],
                                                             pagina=0, audio=item.get("audio"),
                                                             premissas=self.premissas(chave),
                                                             zoom=1.0, rolagem=0.0, lado=0.5)
                        self.fundo_borrado = borrar(self.tela)
                    elif self.inspecionando:
                        # Caderno: setas ou A/D folheiam as páginas.
                        paginas = self.inspecionando.paginas
                        if evento.key in (pygame.K_EQUALS, pygame.K_PLUS, pygame.K_KP_PLUS, pygame.K_MINUS, pygame.K_KP_MINUS):
                            self.ampliar_folha(1 if evento.key in (pygame.K_EQUALS, pygame.K_PLUS, pygame.K_KP_PLUS) else -1)
                        passo = {pygame.K_LEFT: -1, pygame.K_a: -1, pygame.K_RIGHT: 1, pygame.K_d: 1}.get(evento.key)
                        if len(paginas) > 1 and passo:
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
        if self.menu_sistema == "volume":
            escolha = opcoes[indice]
            if escolha == "voltar":
                self.tecla_esc()
            else:  # E ou clique: sobe 10%; passou de 100%, volta para 0
                self.mudar_volume(escolha, -1.0 if self.volume[escolha] >= 1.0 else 0.1)
            return
        if self.menu_sistema:
            if opcoes[indice] == "volume":
                self.volume_origem, self.menu_sistema, self.cursor = self.menu_sistema, "volume", 0
                return
            if opcoes[indice] == "sair":
                self.rodando = False
            if opcoes[indice] == "menu":
                # Volta ao menu principal (a partida atual é descartada).
                self.menu_sistema, self.cursor = "principal", 0
                self.fechar_inspecao()
                if self.cutscene:
                    pygame.mixer.music.stop()  # narração da abertura
                self.cutscene = self.fade = self.inspecionando = self.dialogo = self.obtendo = None
                self.conversa = self.flashback = self.indo_flashback = None
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
                self.chute = self.confirmando_chute = None
                self.etapa_chute, self.respostas_chute = 0, [0, 0, 0]
                self.flashback_visto = False
                self.energia_ligada = False
                self.sortear_itens()
                # Teste: já começa com todos os itens (anotados na sala onde estariam).
                for chave in ITENS:
                    sala = self.locais_itens.get(chave, ("central-de-seguranca",))[0]
                    self.pistas[chave] = sala if sala in MAPAS else "central-de-seguranca"
                self.personagem = PERSONAGEM
                self.carregar_mapa(MAPAS_MENU[0])
            self.menu_sistema = None  # "jogar", "teste" ou "continuar"
            return
        if self.menu_mapas:
            self.ir_para(opcoes[indice])
        else:
            self.trocar_personagem(opcoes[indice])
        self.menu_mapas = self.menu_personagens = False

    def opcoes_chute(self, etapa):
        """Textos das opções de uma etapa do chute."""
        if etapa == 0:
            return [PERSONAGENS[chave]["nome"] for chave in SUSPEITOS]
        return ETAPAS_CHUTE[etapa][2]

    def progresso_verdade(self):
        """Porcentagem da verdade descoberta (itens do caso encontrados)."""
        return round(100 * len(self.pistas) / max(1, len(ITENS)))

    def pode_chutar(self):
        return self.progresso_verdade() >= MINIMO_CHUTE

    def tecla_culpado(self, tecla):
        """Aba "Culpado": W/S escolhem, E passa para a próxima etapa (quem, onde, como) e,
        na última, abre o aviso; Backspace volta uma etapa. No aviso, A/D (ou W/S) e E."""
        cima = tecla in (pygame.K_UP, pygame.K_w, pygame.K_LEFT, pygame.K_a)
        baixo = tecla in (pygame.K_DOWN, pygame.K_s, pygame.K_RIGHT, pygame.K_d)
        confirmar = tecla in (pygame.K_RETURN, pygame.K_KP_ENTER, *TECLAS_INTERAGIR)
        if self.pode_tentar_de_novo() and confirmar:
            self.tentar_de_novo()
            return
        if self.chute or not self.pode_chutar():
            return  # já chutou (só mostra o resultado) ou ainda falta descobrir mais
        if self.confirmando_chute is not None:
            if cima or baixo:
                self.confirmando_chute = 1 - self.confirmando_chute
                self.tocar("menu-mover")
            elif confirmar:
                self.responder_aviso(self.confirmando_chute == 0)
            return
        etapa = self.etapa_chute
        if cima or baixo:
            total = len(self.opcoes_chute(etapa))
            self.respostas_chute[etapa] = (self.respostas_chute[etapa] + (-1 if cima else 1)) % total
            self.tocar("menu-mover")
        elif confirmar:
            self.escolher_chute(self.respostas_chute[etapa])
        elif tecla == pygame.K_BACKSPACE and etapa > 0:
            self.etapa_chute -= 1
            self.tocar("menu-mover")

    def escolher_chute(self, opcao):
        self.respostas_chute[self.etapa_chute] = opcao
        if self.etapa_chute < len(ETAPAS_CHUTE) - 1:
            self.etapa_chute += 1
        else:
            self.confirmando_chute = 1  # começa no "não", para evitar chute sem querer
        self.tocar("menu-confirmar")

    def acertou_tudo(self):
        return bool(self.chute) and (self.chute["quem"], self.chute["onde"], self.chute["como"]) == (CULPADO, ONDE, COMO)

    def pode_tentar_de_novo(self):
        """Errou o chute: com 100% da verdade, pode tentar quantas vezes quiser."""
        return bool(self.chute) and not self.acertou_tudo() and self.progresso_verdade() >= 100

    def tentar_de_novo(self):
        self.chute = self.confirmando_chute = None
        self.etapa_chute, self.respostas_chute = 0, [0, 0, 0]
        self.tocar("menu-confirmar")

    def clicar_culpado(self, posicao):
        if self.pode_tentar_de_novo():
            self.tentar_de_novo()
            return
        if self.chute or not self.pode_chutar():
            return
        if self.confirmando_chute is not None:
            for i, botao in enumerate(self.botoes_aviso):
                if botao.collidepoint(posicao):
                    self.responder_aviso(i == 0)
            return
        for i, botao in enumerate(self.botoes_suspeitos):
            if botao.collidepoint(posicao):
                self.escolher_chute(i)

    def responder_aviso(self, sim):
        self.confirmando_chute = None
        self.tocar("menu-confirmar")
        if sim:
            quem, onde, como = self.respostas_chute
            self.chute = {"quem": SUSPEITOS[quem], "onde": LOCAIS_CHUTE[onde], "como": COMO_CHUTE[como]}
            print(f"[chute] {self.chute}")
            if (self.chute["quem"], self.chute["onde"], self.chute["como"]) == (CULPADO, ONDE, COMO):
                self.iniciar_final()

    def iniciar_final(self):
        """Acertou o culpado: a Giulia narra o que aconteceu, com a legenda da abertura."""
        with open(caminho("cutscenes/final-tempos.json"), encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        with open(caminho("cutscenes/final.txt"), encoding="utf-8") as arquivo:
            frases = [linha.strip() for linha in arquivo if linha.strip()]
        self.final = {"t": 0.0, "frases": frases, "tempos": dados["frases"], "duracao": dados["duracao"], "video": None}
        try:
            self.final["video"] = VideoAbertura(caminho("cutscenes/final-video.mp4"))
        except Exception as erro:
            print(f"[final] sem vídeo: {erro}")
        try:
            pygame.mixer.music.load(caminho("cutscenes/final-narracao.mp3"))
            pygame.mixer.music.set_volume(self.volume["efeitos"])
            pygame.mixer.music.play()
        except pygame.error:
            pass  # sem áudio: a legenda segue pelo relógio

    def atualizar_final(self, dt):
        self.final["t"] += min(dt, 0.1)
        pos = pygame.mixer.music.get_pos() / 1000 if pygame.mixer.get_init() else -1
        if pos > 0 and abs(pos - self.final["t"]) < 1.5:
            self.final["t"] = pos  # segue o relógio do áudio
        if self.final["t"] >= self.final["duracao"]:
            self.fim_final()

    def fim_final(self):
        pygame.mixer.music.stop()
        if self.final["video"]:
            self.final["video"].fechar()
        self.final = None

    def desenhar_final(self):
        video = self.final["video"]
        quadro = video.quadro(self.final["t"]) if video else None
        if quadro:
            self.tela.fill((0, 0, 0))
            escala = min(self.tela.get_width() / quadro.get_width(), self.tela.get_height() / quadro.get_height())
            imagem = pygame.transform.smoothscale(quadro, (round(quadro.get_width() * escala), round(quadro.get_height() * escala)))
            self.tela.blit(imagem, imagem.get_rect(center=self.tela.get_rect().center))
        else:
            self.desenhar_jogo()
            veu = pygame.Surface(self.tela.get_size())
            veu.set_alpha(200)
            self.tela.blit(veu, (0, 0))
        t, tempos = self.final["t"], self.final["tempos"]
        atual = None
        for i, (inicio, fim) in enumerate(tempos):
            if t >= inicio:
                atual = i
        if atual is None or t > tempos[-1][1] + 1.5:
            return
        frase = self.final["frases"][atual]
        inicio, fim = tempos[atual]
        letras = len(frase) * min(1.0, (t - inicio) / max(0.1, (fim - inicio) * 0.85))
        px = self.px
        if getattr(self, "fonte_legenda", (None,))[0] != px(16):
            self.fonte_legenda = (px(16), pygame.font.SysFont("consolas", px(16)))
        desenhar_legenda(self.tela, px, self.fonte_legenda[1], frase, letras)

    def desenhar_culpado(self, area):
        """Quem, onde e como, uma etapa por vez; depois do chute, o resultado de cada parte."""
        x, y = area.topleft
        if self.chute:
            partes = [("Quem", PERSONAGENS[self.chute["quem"]]["nome"], self.chute["quem"] == CULPADO),
                      ("Onde", self.chute["onde"], self.chute["onde"] == ONDE),
                      ("Como", self.chute["como"], self.chute["como"] == COMO)]
            linhas = []
            for titulo, texto, certo in partes:
                linhas.append((f"{titulo}: {texto}", self.fonte_grande, (226, 230, 222)))
                linhas.append(("Certo." if certo else "Errado.", self.fonte,
                               (150, 190, 120) if certo else (220, 110, 100)))
            acertos = sum(certo for _, _, certo in partes)
            linhas.append(("", self.fonte, None))
            if acertos == 3:
                final = ("Você resolveu o caso. Fernando Almeida liberou a Amostra 47.", (150, 190, 120))
            else:
                final = (f"Você acertou {acertos} de 3. A verdade continua enterrada no Helix...", (220, 110, 100))
            linhas.append((final[0], self.fonte_grande, final[1]))
            if acertos < 3:
                linhas.append(("", self.fonte, None))
                if self.pode_tentar_de_novo():
                    linhas.append(("Você já descobriu toda a verdade. Aperte E para acusar de novo.", self.fonte, (150, 190, 120)))
                else:
                    linhas.append(("Descubra 100% da verdade para poder acusar de novo.", self.fonte, (190, 196, 188)))
            for texto, fonte, cor in linhas:
                for linha in quebrar_texto(fonte, texto, area.width) if texto else [""]:
                    rotulo = fonte.render(linha, True, cor or (0, 0, 0))
                    self.tela.blit(rotulo, (x, y))
                    y += rotulo.get_height() + self.px(4)
            return
        if not self.pode_chutar():
            texto = (f"Você ainda não sabe o bastante para acusar alguém. Descubra pelo menos "
                     f"{MINIMO_CHUTE}% da verdade (agora: {self.progresso_verdade()}%).")
            for linha in quebrar_texto(self.fonte_grande, texto, area.width):
                rotulo = self.fonte_grande.render(linha, True, (190, 196, 188))
                self.tela.blit(rotulo, (x, y))
                y += rotulo.get_height() + self.px(4)
            self.botoes_suspeitos = []
            return
        etapa = self.etapa_chute
        # Etapas no topo: as já escolhidas mostram a escolha.
        resumo = []
        for i, (titulo, _, _) in enumerate(ETAPAS_CHUTE):
            if i < etapa:
                resumo.append(f"{titulo}: {self.opcoes_chute(i)[self.respostas_chute[i]]}")
            elif i == etapa:
                resumo.append(f"[{titulo}]")
            else:
                resumo.append(titulo)
        for linha in quebrar_texto(self.fonte, "   ·   ".join(resumo), area.width):
            rotulo = self.fonte.render(linha, True, (150, 190, 120))
            self.tela.blit(rotulo, (x, y))
            y += rotulo.get_height()
        y += self.px(8)
        pergunta = ETAPAS_CHUTE[etapa][1] + (" Só dá para chutar uma vez até 100%." if etapa == 0 else "")
        for linha in quebrar_texto(self.fonte, pergunta, area.width):
            dica = self.fonte.render(linha, True, (190, 196, 188))
            self.tela.blit(dica, (x, y))
            y += dica.get_height()
        y += self.px(12)
        self.botoes_suspeitos = []
        fonte = self.fonte if etapa == 2 else self.fonte_grande  # "como" tem frases longas
        altura_linha = fonte.get_linesize()
        for i, texto in enumerate(self.opcoes_chute(etapa)):
            marcado = i == self.respostas_chute[etapa]
            linhas = quebrar_texto(fonte, ("> " if marcado else "  ") + texto, area.width - self.px(12))
            botao = pygame.Rect(x, y, area.width, len(linhas) * altura_linha + self.px(6))
            if marcado:
                pygame.draw.rect(self.tela, (20, 32, 26), botao)
            for j, linha in enumerate(linhas):
                rotulo = fonte.render(linha, True, (150, 190, 120) if marcado else (200, 206, 198))
                self.tela.blit(rotulo, (x + self.px(6), y + self.px(3) + j * altura_linha))
            self.botoes_suspeitos.append(botao)
            y = botao.bottom + self.px(4)
        if self.confirmando_chute is not None:
            self.desenhar_aviso_chute()

    def desenhar_aviso_chute(self):
        veu = pygame.Surface(self.tela.get_size(), pygame.SRCALPHA)
        veu.fill((0, 0, 0, 170))
        self.tela.blit(veu, (0, 0))
        largura_texto = self.fonte_grande.size("Você só pode fazer a acusação uma vez até 100%.")[0]
        caixa = pygame.Rect(0, 0, largura_texto + self.px(64), self.px(210))
        caixa.center = (self.largura // 2, self.altura // 2)
        pygame.draw.rect(self.tela, (14, 22, 19), caixa)
        pygame.draw.rect(self.tela, (220, 110, 100), caixa, max(1, self.px(2)))
        y = caixa.y + self.px(18)
        titulo = self.fonte_titulo.render("AVISO", True, (220, 110, 100))
        self.tela.blit(titulo, titulo.get_rect(midtop=(caixa.centerx, y)))
        y += titulo.get_height() + self.px(12)
        for texto in ("Você só pode fazer a acusação uma vez até 100%.", "Você tem certeza?"):
            rotulo = self.fonte_grande.render(texto, True, (226, 230, 222))
            self.tela.blit(rotulo, rotulo.get_rect(midtop=(caixa.centerx, y)))
            y += rotulo.get_height() + self.px(4)
        self.botoes_aviso = []
        for i, texto in enumerate(("Sim", "Não")):
            marcado = i == self.confirmando_chute
            rotulo = self.fonte_grande.render(texto, True, (150, 190, 120) if marcado else (170, 176, 168))
            botao = rotulo.get_rect(center=(caixa.centerx + (-1 if i == 0 else 1) * self.px(70),
                                            caixa.bottom - self.px(34))).inflate(self.px(28), self.px(10))
            if marcado:
                pygame.draw.rect(self.tela, (20, 32, 26), botao)
                pygame.draw.rect(self.tela, (88, 112, 92), botao, 1)
            self.tela.blit(rotulo, rotulo.get_rect(center=botao.center))
            self.botoes_aviso.append(botao)

    def tocar_gravacao(self):
        """Gravador: E toca a gravação; E de novo enquanto toca, para."""
        if self.canal_gravacao and self.canal_gravacao.get_busy():
            self.canal_gravacao.stop()
            return
        caminho_audio = self.inspecionando.audio
        if caminho_audio not in self.gravacoes:
            try:
                self.gravacoes[caminho_audio] = pygame.mixer.Sound(caminho(caminho_audio))
            except pygame.error:
                return  # sem áudio (mixer desligado ou arquivo com problema)
        som = self.gravacoes[caminho_audio]
        som.set_volume(self.volume["efeitos"])
        self.canal_gravacao = som.play()

    def fechar_inspecao(self):
        self.inspecionando = None
        if self.canal_gravacao:
            self.canal_gravacao.stop()
            self.canal_gravacao = None

    def tocar(self, nome):
        if nome in self.sons:
            self.sons[nome].play()

    def atualizar_ambiente(self):
        """Zumbido do laboratório em loop durante a partida (não no menu principal nem na cutscene)."""
        if "ambiente" not in self.sons:
            return
        no_menu_principal = self.menu_sistema == "principal" or (
            self.menu_sistema == "volume" and self.volume_origem == "principal")
        jogando = not no_menu_principal and not self.cutscene and not self.final
        # Na trilha e na fachada, som de floresta; dentro do complexo, o zumbido do laboratório.
        som = (("floresta" if self.chave_mapa == FACHADA and "floresta" in self.sons else "ambiente")
               if jogando else None)
        if som != self.ambiente_tocando:
            if self.ambiente_tocando:
                self.sons[self.ambiente_tocando].fadeout(600)
            if som:
                self.sons[som].play(loops=-1, fade_ms=600 if self.ambiente_tocando else 0)
        self.ambiente_tocando = som

    def atualizar(self, dt, teclas):
        if self.aviso and not self.flashback and not self.fade:
            self.aviso["t"] += dt
            if self.aviso["t"] >= AVISO:
                self.aviso = None
        if self.iniciando is not None:
            # "Jogar": depois do fade do menu, começa a cutscene.
            self.iniciando += dt
            if self.iniciando >= INICIO:
                self.iniciando = None
                self.menu_sistema = None
                self.modo_teste = False
                self.pistas = {}
                self.anotacoes = ""
                self.chute = self.confirmando_chute = None
                self.etapa_chute, self.respostas_chute = 0, [0, 0, 0]
                self.flashback_visto = False
                self.energia_ligada = False
                self.pagina_notas = None
                self.sortear_itens()
                self.cutscene = Cutscene(PERSONAGENS[PERSONAGEM_INICIO])
                self.cutscene.ao_escrever = lambda: self.tocar(f"tic-{random.randint(1, 3)}")
                self.cutscene.volume = self.volume["efeitos"]
            return
        self.atualizar_ambiente()
        if self.final:
            self.atualizar_final(dt)
            return
        if self.cutscene:
            self.cutscene.atualizar(dt, teclas)
            if self.cutscene.terminou:
                # Fim da abertura: a Giulia entra na primeira sala, clareando do preto.
                self.cutscene = None
                self.personagem = PERSONAGEM_INICIO
                self.carregar_mapa(FACHADA)
                self.fade = ["clareando", 0.0, None]
                self.tutorial_inicio = True  # controles na tela até apertar E
            return
        if self.indo_flashback is not None:
            self.indo_flashback += dt
            if self.indo_flashback >= ENTRAR_FLASHBACK:
                self.indo_flashback = None
                self.flashback = Flashback()
                self.flashback.ao_escrever = lambda: self.tocar(f"tic-{random.randint(1, 3)}")
            return
        if self.flashback:
            self.flashback.atualizar(dt)
            if self.flashback.terminou:
                self.fim_flashback()
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
        if self.tutorial_inicio:
            return
        if self.dialogo and not self.algum_menu():
            fala = ITENS[self.dialogo["item"].chave]["fala"]
            antes = int(self.dialogo["letras"])
            self.dialogo["letras"] = min(len(fala), self.dialogo["letras"] + 45 * dt)
            if any(not c.isspace() and (antes + i) % 2 == 0 for i, c in enumerate(fala[antes:int(self.dialogo["letras"])])):
                self.tocar(f"tic-{random.randint(1, 3)}")
            return
        if self.conversa and not self.algum_menu():
            texto = self.conversa["falas"][self.conversa["i"]][1]
            antes = int(self.conversa["letras"])
            self.conversa["letras"] = min(len(texto), self.conversa["letras"] + 45 * dt)
            if any(not c.isspace() and (antes + i) % 2 == 0 for i, c in enumerate(texto[antes:int(self.conversa["letras"])])):
                self.tocar(f"tic-{random.randint(1, 3)}")
            return
        if self.obtendo and not self.algum_menu():
            self.obtendo["t"] += dt
            if self.obtendo["t"] >= OBTER:
                chave_obtida = self.obtendo["item"].chave
                contido = ITENS[chave_obtida].get("contem")
                self.obtendo = None
                if chave_obtida == PENDRIVE:
                    self.falar([(self.jogador.nome.split()[0],
                                 "Acho que os computadores da central de segurança ainda funcionam...")])
                if contido and contido not in self.pistas:
                    dados = ITENS[contido]
                    dentro = SimpleNamespace(chave=contido, id=dados["id"], nome=dados["nome"], coletado=False)
                    self.dialogo = {"item": dentro, "letras": 0.0}
            return
        # Segurar Backspace nas anotações apaga várias letras (depois de um instante, em sequência).
        if self.mapa_mental and self.aba_mental == "notas" and not self.inspecionando and teclas[pygame.K_BACKSPACE]:
            self.apagando += dt
            while self.apagando > 0.45 and self.anotacoes:
                self.anotacoes = self.anotacoes[:-1]
                self.pagina_notas = None
                self.apagando -= 0.035
                self.tocar("tecla-1")
        else:
            self.apagando = 0.0
        if self.inspecionando and not self.menu_sistema:
            # Folha ampliada: W/S (ou setas) rolam enquanto seguradas.
            sentido = (teclas[pygame.K_s] or teclas[pygame.K_DOWN]) - (teclas[pygame.K_w] or teclas[pygame.K_UP])
            if sentido and hasattr(self.inspecionando, "rolagem"):
                self.inspecionando.rolagem = max(0.0, min(1.0, self.inspecionando.rolagem + sentido * dt * 0.6 / self.inspecionando.zoom))
            lado = (teclas[pygame.K_d] or teclas[pygame.K_RIGHT]) - (teclas[pygame.K_a] or teclas[pygame.K_LEFT])
            if lado and hasattr(self.inspecionando, "lado") and len(self.inspecionando.paginas) == 1:
                self.inspecionando.lado = max(0.0, min(1.0, self.inspecionando.lado + lado * dt * 0.8 / self.inspecionando.zoom))
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

        if self.chave_mapa == FACHADA and not self.energia_ligada:
            perto = self.gerador_proximo()
            desenhar_brilho(self.tela, pygame.Vector2(GERADOR[0], GERADOR[1] - 20), visao, self.zoom, pygame.time.get_ticks() / 1000, perto)
            if perto and not proximo and not (self.dialogo or self.obtendo or self.conversa):
                x = (GERADOR[0] - visao.x) * self.zoom
                y = (GERADOR[1] - visao.y - 70) * self.zoom
                self.desenhar_caixa("Pressione E para ligar o gerador", self.fonte_grande, (255, 255, 255), (x, y))
        computador = self.computador_disponivel()
        if computador:
            perto = self.computador_proximo() is not None
            desenhar_brilho(self.tela, pygame.Vector2(computador), visao, self.zoom, pygame.time.get_ticks() / 1000, perto)
            if perto and not proximo and not (self.dialogo or self.obtendo or self.conversa):
                x = (computador[0] - visao.x) * self.zoom
                y = (computador[1] - visao.y - 40) * self.zoom
                self.desenhar_caixa("Pressione E para usar o computador", self.fonte_grande, (255, 255, 255), (x, y))
        if proximo and not (self.dialogo or self.obtendo or self.conversa):
            x = (proximo.posicao.x - visao.x) * self.zoom
            y = (proximo.posicao.y - visao.y - 40) * self.zoom
            self.desenhar_caixa("Pressione E para interagir", self.fonte_grande, (255, 255, 255), (x, y))


    def desenhar_menu(self, titulo, opcoes, atual, dica, veu=True, meio=None):
        """Menu sobre o jogo: botões clicáveis, com a opção atual em verde."""
        if veu:
            escuro = pygame.Surface(self.tela.get_size(), pygame.SRCALPHA)
            escuro.fill((0, 0, 0, 170))
            self.tela.blit(escuro, (0, 0))
        meio = self.largura // 2 if meio is None else meio
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
        if isinstance(dica, list):  # teclas desenhadas, com a ação ao lado
            self.desenhar_atalhos(dica, (meio, topo + self.px(80) + len(opcoes) * passo + self.px(22)), centro=True)
        elif dica:
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
        progresso = pygame.Rect(margem, topo + linhas * (lado + legenda + espaco * 2), direita - margem, barra_altura)

        # Abas: pistas ou anotações.
        x = direita + self.px(32)
        largura = self.largura - x - margem
        self.abas_mental = {}
        ax = x
        for aba, texto in (("pistas", f"Pistas ({len(self.pistas)})"), ("notas", "Anotações"), ("culpado", "Culpado")):
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
        elif self.aba_mental == "culpado":
            pass  # desenhada no fim, para o aviso ficar por cima de tudo
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
            premissas = self.premissas(chave)
            if premissas:
                y += self.px(6)
            for premissa in premissas:
                for linha in quebrar_texto(self.fonte, premissa, largura):
                    rotulo = self.fonte.render(linha, True, (150, 190, 120))
                    self.tela.blit(rotulo, (x, y))
                    y += rotulo.get_height()
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
            atalhos = [(["←", "→"], "virar página"), (["Esc"], "pistas"), (["Tab"], "fechar")]
        elif self.aba_mental == "culpado":
            ultima = self.etapa_chute == len(ETAPAS_CHUTE) - 1
            atalhos = ([(["E"], "acusar de novo")] if self.pode_tentar_de_novo() else [] if self.chute or not self.pode_chutar() else [(["W", "S"], "escolher"), (["E"], "chutar" if ultima else "próximo")]
                       + ([(["Backspace"], "voltar")] if self.etapa_chute else [])) \
                + [(["Esc"], "pistas"), (["Tab"], "fechar")]
        else:
            atalhos = ([(["A", "D"], "passar"), (["E"], "ampliar")] if self.pistas else []) \
                + [(["N"], "anotações"), (["C"], "culpado"), (["Tab"], "fechar")]
        inicio_atalhos = self.desenhar_atalhos(atalhos, (self.largura - margem, self.altura - margem))
        # A barra de progresso termina antes das dicas de teclado, para não ficarem uma em cima da outra.
        progresso.width = min(progresso.width, inicio_atalhos - self.px(20) - progresso.x)
        self.desenhar_progresso(progresso)
        if self.aba_mental == "culpado":
            self.desenhar_culpado(pygame.Rect(x, y, largura, self.altura - y - margem))

    def desenhar_tecla(self, texto, x, base):
        """Desenha uma teclinha com o texto, apoiada em `base`; devolve onde ela termina (x)."""
        fonte = self.fonte_pequena
        rotulo = fonte.render(texto, True, (226, 230, 222))
        altura = fonte.get_height() + self.px(4)
        caixa = pygame.Rect(x, base - altura, max(altura, rotulo.get_width() + 2 * self.px(5)), altura)
        pygame.draw.rect(self.tela, (30, 42, 36), caixa, border_radius=self.px(3))
        pygame.draw.rect(self.tela, (120, 140, 122), caixa, 1, border_radius=self.px(3))
        pygame.draw.line(self.tela, (70, 84, 72), (caixa.x + 2, caixa.bottom), (caixa.right - 3, caixa.bottom))
        self.tela.blit(rotulo, rotulo.get_rect(center=caixa.center))
        return caixa.right

    def desenhar_tutorial(self, x0=None, topo=None):
        """Ao lado das opções da pausa: as teclas do jogo e o que cada uma faz."""
        linhas = [
            (["W", "A", "S", "D"], "andar (ou as setas)"),
            (["E"], "interagir, conversar e confirmar"),
            (["Tab"], "mapa mental: salas, pistas e anotações"),
            (["R"], "tocar gravações"),
            (["Esc"], "pausa e voltar"),
            (["F11"], "tela cheia"),
        ]
        if self.modo_teste:
            linhas += [(["Caps Lock"], "antes / depois do incidente"), (["Alt"], "trocar personagem")]
        x0 = round(self.largura * 0.55) if x0 is None else x0
        topo = self.botoes_menu[0].top if topo is None else topo
        passo = self.fonte_pequena.get_height() + self.px(14)
        # Coluna da ação logo depois da fileira de teclas mais larga.
        larguras = [sum(max(self.fonte_pequena.get_height() + self.px(4), self.fonte_pequena.size(t)[0] + 2 * self.px(5))
                        + self.px(3) for t in teclas) for teclas, _ in linhas]
        coluna_acao = x0 + max(larguras) + self.px(12)
        largura = coluna_acao - x0 + max(self.fonte_pequena.size(a)[0] for _, a in linhas) + self.px(12)
        painel = pygame.Rect(x0 - self.px(14), topo - self.px(36), largura + self.px(28), len(linhas) * passo + self.px(50))
        fundo = pygame.Surface(painel.size, pygame.SRCALPHA)
        fundo.fill((14, 22, 19, 200))
        self.tela.blit(fundo, painel)
        pygame.draw.rect(self.tela, (88, 112, 92), painel, 1)
        titulo = self.fonte.render("Controles", True, (150, 190, 120))
        self.tela.blit(titulo, (x0, topo - self.px(28)))
        for n, (teclas, acao) in enumerate(linhas):
            base = topo + self.px(12) + (n + 1) * passo - self.px(10)
            x = x0
            for tecla in teclas:
                x = self.desenhar_tecla(tecla, x, base) + self.px(3)
            texto = self.fonte_pequena.render(acao, True, (200, 206, 198))
            self.tela.blit(texto, (coluna_acao, base - texto.get_height() - self.px(1)))

    def desenhar_atalhos(self, atalhos, canto, centro=False):
        """Dicas de teclado: o desenho de cada tecla e, do lado, o que ela faz (alinhado à direita)."""
        fonte = self.fonte_pequena
        folga, espaco = self.px(5), self.px(14)
        pecas = []  # (superfície, é tecla?)
        for teclas, acao in atalhos:
            for tecla in teclas:
                pecas.append((fonte.render(tecla, True, (226, 230, 222)), True))
            pecas.append((fonte.render(acao, True, (170, 180, 168)), False))
        largura = sum(p.get_width() + (2 * folga + self.px(3) if tecla else espaco) for p, tecla in pecas)
        x, base = canto[0] - (largura // 2 if centro else largura), canto[1]
        inicio = x
        altura = fonte.get_height() + self.px(4)
        for superficie, tecla in pecas:
            if tecla:
                caixa = pygame.Rect(x, base - altura, superficie.get_width() + 2 * folga, altura)
                caixa.width = max(caixa.width, altura)  # teclas de uma letra ficam quadradinhas
                pygame.draw.rect(self.tela, (30, 42, 36), caixa, border_radius=self.px(3))
                pygame.draw.rect(self.tela, (120, 140, 122), caixa, 1, border_radius=self.px(3))
                pygame.draw.line(self.tela, (70, 84, 72), (caixa.x + 2, caixa.bottom), (caixa.right - 3, caixa.bottom))
                self.tela.blit(superficie, superficie.get_rect(center=caixa.center))
                x = caixa.right + self.px(3)
            else:
                self.tela.blit(superficie, (x + self.px(2), base - altura + (altura - superficie.get_height()) // 2))
                x += superficie.get_width() + espaco
        return inicio  # onde as dicas começam (x)

    def desenhar_progresso(self, area):
        """Progressão da verdade: quanto dos itens do caso já foi encontrado."""
        porcentagem = self.progresso_verdade()
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
        # Texto: cada parágrafo quebrado na largura da folha e dividido em páginas;
        # quando a última enche, aparece uma página nova.
        largura_texto = area.right - margem_x - self.px(16)
        # Post-it no topo da 1ª página: o texto dessa página começa depois dele.
        fonte_post = self.fonte_pequena
        largura_post = area.right - margem_x - self.px(24)
        linhas_post = [l for p in POST_IT for l in quebrar_texto(fonte_post, p, largura_post - self.px(16))]
        altura_post = len(linhas_post) * fonte_post.get_linesize() + self.px(16)
        reservadas = altura_post // altura_linha + 1
        todas = [None] * reservadas
        for paragrafo in self.anotacoes.split("\n"):
            todas += quebrar_texto(fonte, paragrafo, largura_texto) or [""]
        cabem = max(1, (area.bottom - topo_texto - self.px(30)) // altura_linha)
        paginas = [todas[i:i + cabem] for i in range(0, len(todas), cabem)] or [[""]]
        self.paginas_notas_total = len(paginas)
        indice = len(paginas) - 1 if self.pagina_notas is None else min(self.pagina_notas, len(paginas) - 1)
        linhas = paginas[indice]
        escrevendo = indice == len(paginas) - 1
        numero = self.fonte_pequena.render(
            ("<  " if indice > 0 else "   ") + f"página {indice + 1} / {len(paginas)}"
            + ("  >" if indice < len(paginas) - 1 else "   "), True, (120, 112, 96))
        self.tela.blit(numero, numero.get_rect(bottomright=(area.right - self.px(10), area.bottom - self.px(6))))
        x_texto = margem_x + self.px(10)
        if indice == 0:
            post = pygame.Rect(margem_x + self.px(8), topo_texto - self.px(4), largura_post, altura_post)
            pygame.draw.rect(self.tela, (0, 0, 0), post.move(self.px(3), self.px(3)))
            pygame.draw.rect(self.tela, (244, 222, 120), post)
            pygame.draw.rect(self.tela, (214, 180, 70), post, 1)
            fita = pygame.Rect(0, 0, self.px(46), self.px(12))
            fita.center = (post.centerx, post.top)
            pygame.draw.rect(self.tela, (220, 216, 200), fita)
            for n, linha in enumerate(linhas_post):
                rotulo = fonte_post.render(linha, True, (70, 56, 30))
                self.tela.blit(rotulo, (post.x + self.px(8), post.y + self.px(8) + n * fonte_post.get_linesize()))
        primeira = reservadas if indice == 0 else 0  # linha onde o texto começa nesta página
        if not self.anotacoes:
            vazio = fonte.render("Escreva aqui o que for importante...", True, (160, 150, 128))
            self.tela.blit(vazio, (x_texto, topo_texto + (primeira + 1) * altura_linha - fonte.get_ascent() - self.px(3)))
        for n, linha in enumerate(linhas):
            if linha is None:
                continue
            texto = fonte.render(linha, True, (34, 52, 110))
            self.tela.blit(texto, (x_texto, topo_texto + (n + 1) * altura_linha - fonte.get_ascent() - self.px(3)))
        if escrevendo and pygame.time.get_ticks() // 500 % 2 == 0:  # cursor piscando no fim do texto
            ultima = linhas[-1] if linhas and self.anotacoes and linhas[-1] is not None else ""
            cx = x_texto + fonte.size(ultima)[0] + self.px(2)
            cy = topo_texto + (len(linhas) if self.anotacoes else primeira + 1) * altura_linha
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
            if len(paginas) == 1 and pagina.get_height() > pagina.get_width() * 1.15:
                self.desenhar_folha(item, pagina)  # documento em pé: folha grande para dar de ler
                self.desenhar_atalhos([(["Roda", "+", "-"], "zoom"), (["W", "A", "S", "D"], "mover"), (["E"], "continuar")],
                                      (meio, self.altura - self.px(16)), centro=True)
                return
            escala = min(self.largura * 0.8 / pagina.get_width(), lado / pagina.get_height())
            arte = pygame.transform.smoothscale(pagina, (round(pagina.get_width() * escala), round(pagina.get_height() * escala)))
            self.tela.blit(arte, arte.get_rect(midtop=(meio, self.px(20))))
            if len(paginas) > 1:
                contador = self.fonte_grande.render(f"<   página {item.pagina + 1} / {len(paginas)}   >", True, (150, 190, 120))
                self.tela.blit(contador, contador.get_rect(midbottom=(meio, self.altura - self.px(40))))
        elif getattr(item, "texto", None):
            self.desenhar_documento(item)
        else:
            arte = pygame.transform.smoothscale(item.imagem, (lado, lado))
            self.tela.blit(arte, arte.get_rect(midtop=(meio, self.px(20))))
        if paginas or not getattr(item, "texto", None):  # documento já traz título e texto ao lado
            self.desenhar_legenda_inspecao(item, meio)
        self.desenhar_dica_inspecao(item, meio)

    def desenhar_documento(self, item):
        """Imagem à esquerda; à direita, nome, o conteúdo (Inspecionar/Ler/Ouvir) e a observação da Giulia."""
        margem = self.px(40)
        lado = min(self.px(240), int(self.largura * 0.3))
        arte = pygame.transform.smoothscale(item.imagem, (lado, lado))
        self.tela.blit(arte, arte.get_rect(midleft=(margem, self.altura // 2 - self.px(10))))
        x = margem + lado + self.px(32)
        largura = self.largura - x - margem
        y = self.px(28)
        for linha in quebrar_texto(self.fonte_grande, f"{item.id} — {item.nome}", largura):
            rotulo = self.fonte_grande.render(linha, True, (150, 190, 120))
            self.tela.blit(rotulo, (x, y))
            y += rotulo.get_height()
        y += self.px(10)
        for paragrafo in item.texto:
            if not paragrafo:
                y += self.px(8)
                continue
            for linha in quebrar_texto(self.fonte, paragrafo, largura):
                rotulo = self.fonte.render(linha, True, (226, 230, 222))
                self.tela.blit(rotulo, (x, y))
                y += rotulo.get_height() + self.px(2)
        y += self.px(12)
        for linha in quebrar_texto(self.fonte, item.mensagem, largura):
            rotulo = self.fonte.render(linha, True, (226, 196, 142))
            self.tela.blit(rotulo, (x, y))
            y += rotulo.get_height()
        self.desenhar_premissas(item, x, y + self.px(6), largura)

    def desenhar_aviso(self):
        """Faixa no topo da tela que aparece e some devagar."""
        t = self.aviso["t"]
        alfa = min(1.0, t / 0.3, (AVISO - t) / 0.6)
        rotulo = self.fonte_grande.render(self.aviso["texto"], True, (150, 190, 120))
        caixa = rotulo.get_rect(midtop=(self.largura // 2, self.px(24))).inflate(self.px(36), self.px(16))
        painel = pygame.Surface(caixa.size, pygame.SRCALPHA)
        pygame.draw.rect(painel, (12, 20, 14, 210), painel.get_rect(), border_radius=self.px(6))
        pygame.draw.rect(painel, (150, 190, 120, 180), painel.get_rect(), 1, border_radius=self.px(6))
        painel.blit(rotulo, rotulo.get_rect(center=painel.get_rect().center))
        painel.set_alpha(round(255 * max(0.0, alfa)))
        self.tela.blit(painel, caixa)

    def desenhar_premissas(self, item, x, y, largura):
        """Premissas do item, em verde, logo abaixo da observação da Giulia."""
        for premissa in getattr(item, "premissas", None) or []:
            for linha in quebrar_texto(self.fonte, premissa, largura):
                rotulo = self.fonte.render(linha, True, (150, 190, 120))
                self.tela.blit(rotulo, (x, y))
                y += rotulo.get_height()

    def ampliar_folha(self, passo):
        item = self.inspecionando
        if hasattr(item, "zoom") and passo:
            item.zoom = max(1.0, min(3.0, item.zoom * (1.25 if passo > 0 else 0.8)))

    def desenhar_folha(self, item, pagina):
        """Folha em pé quase da altura da tela, à esquerda; título e observação à direita.
        Roda do mouse (ou +/-) amplia; W/S rolam para cima e para baixo."""
        margem = self.px(24)
        janela = pygame.Rect(margem, self.px(16), 0, self.altura - self.px(56))
        janela.width = round(pagina.get_width() * janela.height / pagina.get_height())
        altura = round(janela.height * item.zoom)
        largura = round(janela.width * item.zoom)
        arte = pygame.transform.smoothscale(pagina, (largura, altura))
        recorte = pygame.Rect(0, 0, janela.width, janela.height)
        recorte.x = round((largura - janela.width) * item.lado)
        recorte.y = round((altura - janela.height) * item.rolagem)
        self.tela.blit(arte, janela, recorte)
        x = margem * 2 + janela.width
        coluna = self.largura - x - margem
        y = self.altura // 3
        for linha in quebrar_texto(self.fonte_titulo, f"{item.id} — {item.nome}", coluna):
            rotulo = self.fonte_titulo.render(linha, True, (255, 255, 255))
            self.tela.blit(rotulo, (x, y))
            y += rotulo.get_height()
        y += self.px(16)
        for linha in quebrar_texto(self.fonte_grande, item.mensagem, coluna):
            rotulo = self.fonte_grande.render(linha, True, (225, 225, 225))
            self.tela.blit(rotulo, (x, y))
            y += rotulo.get_height() + self.px(4)
        self.desenhar_premissas(item, x, y + self.px(6), coluna)

    def desenhar_legenda_inspecao(self, item, meio):
        titulo = self.fonte_titulo.render(f"{item.id} — {item.nome}" if item.nome else item.id, True, (255, 255, 255))
        self.tela.blit(titulo, titulo.get_rect(midtop=(meio, self.px(315))))
        largura_texto = min(self.largura - self.px(80), self.px(800))
        for i, linha in enumerate(quebrar_texto(self.fonte_grande, item.mensagem, largura_texto)):
            texto = self.fonte_grande.render(linha, True, (225, 225, 225))
            self.tela.blit(texto, texto.get_rect(midtop=(meio, self.px(362 + i * 26))))
        y = self.px(362 + (i + 1) * 26 + 6)
        for premissa in getattr(item, "premissas", None) or []:
            for linha in quebrar_texto(self.fonte, premissa, largura_texto):
                rotulo = self.fonte.render(linha, True, (150, 190, 120))
                self.tela.blit(rotulo, rotulo.get_rect(midtop=(meio, y)))
                y += rotulo.get_height()

    def desenhar_dica_inspecao(self, item, meio):
        if getattr(item, "audio", None):
            tocando = self.canal_gravacao and self.canal_gravacao.get_busy()
            atalhos = [(["R"], "parar gravação" if tocando else "tocar gravação"), (["E"], "voltar")]
        else:
            atalhos = ([(["A", "D"], "folhear")] if len(getattr(item, "paginas", None) or []) > 1 else [])                 + [(["E"], "continuar")]
        self.desenhar_atalhos(atalhos, (meio, self.altura - self.px(16)), centro=True)

    def desenhar(self):
        if self.final:
            self.desenhar_final()
        elif self.flashback:
            self.flashback.desenhar(self.tela, self.px, self.caixa)
        elif self.cutscene:
            self.cutscene.desenhar(self.tela, self.px)
        elif self.menu_sistema == "principal":
            self.tela.fill((0, 0, 0))  # menu principal sem fundo
            self.desenhar_menu("Amostra 47", MENUS_SISTEMA["principal"], None,
                               "Clique ou E para escolher", veu=False)
            if self.iniciando is not None:
                veu = pygame.Surface(self.tela.get_size())
                veu.set_alpha(round(255 * min(1.0, self.iniciando / INICIO)))
                self.tela.blit(veu, (0, 0))
        elif self.menu_sistema == "volume":
            if self.volume_origem == "principal":
                self.tela.fill((0, 0, 0))
            else:
                self.desenhar_jogo()
            # Menu "Opções" (por enquanto só os volumes; outras opções entram aqui depois).
            numero = lambda v: f"<  {round(v * 100):3d}%  >"
            opcoes = [("efeitos", f"Efeitos sonoros   {numero(self.volume['efeitos'])}"),
                      ("musica", f"Música            {numero(self.volume['musica'])}"), ("voltar", "Voltar")]
            self.desenhar_menu("Opções", opcoes, None, [(["A", "D"], "ajustar"), (["Esc"], "voltar")],
                               veu=self.volume_origem != "principal")
        elif self.menu_sistema == "pausa":
            self.desenhar_jogo()
            # Opções à esquerda do centro e, do lado, o tutorial das teclas.
            self.desenhar_menu("Pausa", MENUS_SISTEMA["pausa"], None, "",
                               meio=round(self.largura * 0.3))
            self.desenhar_tutorial()
        elif self.mapa_mental and not self.inspecionando:
            self.desenhar_jogo()
            self.desenhar_mapa_mental()
        elif self.inspecionando:
            self.desenhar_inspecao()
        else:
            self.desenhar_jogo()
            if self.menu_mapas:
                self.desenhar_menu("Ir para", [(c, self.nome_sala(c)) for c in self.destinos],
                                   self.chave_mapa, [(["E"], "escolher"), (["Esc"], "fechar")])
            elif self.menu_personagens:
                self.desenhar_menu("Trocar personagem", [(c, PERSONAGENS[c]["nome"]) for c in PERSONAGENS_MENU],
                                   self.personagem, [(["E"], "escolher"), (["Esc"], "fechar")])
            if self.dialogo:
                fala = ITENS[self.dialogo["item"].chave]["fala"]
                seta = self.dialogo["letras"] >= len(fala) and pygame.time.get_ticks() // 500 % 2 == 0
                self.caixa.desenhar(self.tela, self.px, self.jogador.nome.split()[0], fala, self.dialogo["letras"], seta)
            if self.conversa:
                nome, texto = self.conversa["falas"][self.conversa["i"]]
                seta = self.conversa["letras"] >= len(texto) and pygame.time.get_ticks() // 500 % 2 == 0
                self.caixa.desenhar(self.tela, self.px, nome, texto, self.conversa["letras"], seta)
            if self.obtendo:
                self.desenhar_obtencao()
            if self.aviso and not self.fade:
                self.desenhar_aviso()
            if self.tutorial_inicio and not self.fade:
                self.desenhar_tutorial(round(self.largura * 0.36), round(self.altura * 0.36))
                self.desenhar_atalhos([(["E"], "continuar")], (self.largura // 2, self.altura - self.px(16)), centro=True)
            if self.indo_flashback is not None:
                veu = pygame.Surface(self.tela.get_size())
                veu.set_alpha(round(255 * min(1.0, self.indo_flashback / ENTRAR_FLASHBACK)))
                self.tela.blit(veu, (0, 0))
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
