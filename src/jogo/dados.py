"""Definições de conteúdo da beta: personagens, mapas e itens.

Para adicionar um novo personagem, mapa ou item, basta criar uma nova entrada
nos dicionários abaixo e escolher qual usar em ``amostra47.py``.
Coordenadas em pixels da tela (o mapa é desenhado em 720 x 720).
"""

PERSONAGENS = {
    # Sprites gerados no PixelLab: 8 direções com 8 quadros de caminhada cada.
    "otavio-ferraz": {
        "nome": "Otávio Ferraz",
        "pasta_sprites": "sprites/otavio-ferraz-pixellab",
        "velocidade": 105,  # pixels por segundo
        "fps_andando": 10,
        "balanco": False,
    },
    # Sprites gerados no PixelLab (clara_costa (1).zip): 8 direções.
    "clara-costa": {
        "nome": "Clara Costa",
        "pasta_sprites": "sprites/clara-costa-pixellab",
        "velocidade": 105,  # pixels por segundo
        "fps_andando": 10,
        "balanco": False,
    },
    # Sprites gerados no PixelLab (Giulia_Pistori_21-year-old_young_woman_casual_ur.zip): 8 direções.
    "giulia-pistori": {
        "nome": "Giulia Pistori",
        "pasta_sprites": "sprites/giulia-pistori-pixellab",
        "velocidade": 105,  # pixels por segundo
        "fps_andando": 10,
        "balanco": False,
    },
    # Sprites gerados no PixelLab: 8 direções.
    "amie-lin": {
        "nome": "Amie Lin",
        "pasta_sprites": "sprites/amie-lin-pixellab",
        "velocidade": 105,  # pixels por segundo
        "fps_andando": 10,
        "balanco": False,
    },
    "angela-torres": {
        "nome": "Angela Torres",
        "pasta_sprites": "sprites/angela-torres-pixellab",
        "velocidade": 105,
        "fps_andando": 10,
        "balanco": False,
    },
    # Sprites gerados no PixelLab: 8 direções; na caminhada de frente, o quadro 6
    # usa a cabeça do quadro 5 (a original saiu deformada).
    "beatrice-salles": {
        "nome": "Beatrice Salles",
        "pasta_sprites": "sprites/beatrice-salles-pixellab",
        "velocidade": 105,  # pixels por segundo
        "fps_andando": 10,
        "balanco": False,
    },
    # Sprites gerados no PixelLab (Giovani_Pistori_adult_male_head.zip): 8 direções.
    "giovani-pistori": {
        "nome": "Giovani Pistori",
        "pasta_sprites": "sprites/giovani-pistori-pixellab",
        "velocidade": 105,
        "fps_andando": 10,
        "balanco": False,
    },
    # Sprites gerados no PixelLab (Dr._Fernando_Almeida_middle-aged_male_scientific.zip).
    "fernando-almeida": {
        "nome": "Fernando Almeida",
        "pasta_sprites": "sprites/fernando-almeida-pixellab",
        "velocidade": 105,
        "fps_andando": 10,
        "balanco": False,
    },
}

MAPAS = {
    "camara-de-contencao": {
        "nome": "Câmara de contenção",
        # Imagem em resolução original; o jogo a escala para "tamanho" x zoom.
        # Mapa sem objetos; os objetos vêm separados em "objetos" (abaixo).
        "imagem": "mapas/camara-de-contencao-vazia.png",
        "tamanho": (720, 720),
        # Área de piso onde o personagem pode andar (x, y, largura, altura).
        "area_andavel": (138, 138, 445, 413),
        # Retângulos bloqueados dentro da área andável (o tanque central).
        "obstaculos": [(212, 161, 293, 298)],
        # Piso andável (branco) só com as paredes, a partir do contorno vermelho em
        # Downloads/camara-de-contencao-colisoes.png; substitui os retângulos acima.
        "mascara": "mapas/camara-de-contencao-paredes.png",
        # Objetos desenhados por cima do mapa, na ordem da altura (base) com o personagem.
        # retangulo = (x, y, largura, altura) no mapa; pe = fração de baixo que colide (com 80% da largura);
        # bases/linha (opcionais) = colisão e linha de profundidade em frações da imagem.
        "pasta_objetos": "mapas/objetos/camara-de-contencao",
        # Resolução dos objetos em pixels por unidade do mapa (menor = mais pixelado).
        "pixels_por_unidade_objetos": 2,
        "objetos": [
            {"imagem": "tanque.png", "retangulo": (294.4, 161.5, 132.3, 244.7),
             # base larga do tubo e o console da frente; atrás dela dá para passar.
             "bases": [(0, 0.75, 1, 0.17), (0.36, 0.9, 0.28, 0.1)], "linha": 0.92},
            {"imagem": "console-esquerdo.png", "retangulo": (52.1, 31.7, 105.5, 121.1), "pe": 0.3},
            {"imagem": "console-direito.png", "retangulo": (562.6, 31.7, 102.2, 121.1), "pe": 0.3},
            {"imagem": "armario-esquerdo.png", "retangulo": (89.6, 180.8, 47.4, 219.9), "pe": 0.3},
            {"imagem": "armario-direito.png", "retangulo": (582.6, 180.8, 44.2, 219.9), "pe": 0.3},
            {"imagem": "terminal.png", "retangulo": (545.0, 425.0, 33.6, 55.0), "pe": 0.3},
            {"imagem": "armario-terminal.png", "retangulo": (97.0, 420.0, 30.0, 75.0), "pe": 0.3},
            {"imagem": "mesa-esquerda.png", "retangulo": (130.0, 437.0, 54.5, 59.6), "pe": 0.3},
            {"imagem": "carrinho.png", "retangulo": (474.1, 403.2, 50.7, 59.0), "pe": 0.3},
            {"imagem": "cilindros.png", "retangulo": (580.7, 432.7, 41.0, 46.2), "pe": 0.3},
        ],
        "inicio": (360, 520),
    },
    "sala-de-servidores": {
        "nome": "Sala de servidores",
        # Base vazia e objetos do kit sala_servidores.zip (CENA_MONTAGEM.json, escala 2160 / 3).
        "imagem": "mapas/sala-de-servidores-vazia.png",
        "tamanho": (720, 720),
        "area_andavel": (84, 138, 552, 421),
        "obstaculos": [],
        # Piso andável aproximado (branco), desenhado à mão sobre a base vazia.
        "mascara": "mapas/sala-de-servidores-paredes.png",
        "pasta_objetos": "mapas/objetos/sala-de-servidores",
        "pixels_por_unidade_objetos": 2,
        # Lista no JSON da pasta: mesmo formato da Câmara; decalques têm "bases": [].
        "objetos": "objetos.json",
        "inicio": (360, 540),
    },
    "sala-de-evacuacao": {
        "nome": "Sala de evacuação",
        # Mapa vazio; objetos posicionados como em docs/locais/sala-de-evacuacao/mapa-limpo.webp.
        "imagem": "mapas/sala-de-evacuacao-vazia.png",
        "tamanho": (720, 720),
        "area_andavel": (89, 116, 544, 435),
        "obstaculos": [],
        "mascara": "mapas/sala-de-evacuacao-paredes.png",
        "pasta_objetos": "mapas/objetos/sala-de-evacuacao",
        "pixels_por_unidade_objetos": 2,
        "objetos": "objetos.json",
        "inicio": (360, 500),
    },
    "laboratorio-de-analises": {
        "nome": "Laboratório de análises",
        # Mapa vazio (ampliado no Upscayl) e objetos de LABORATORIO_ANALISES_OBJETOS_SEPARADOS_2160.zip,
        # nas posições do POSICOES_MAPA_2160.csv do pacote.
        "imagem": "mapas/laboratorio-de-analises-vazia.png",
        "tamanho": (720, 720),
        "area_andavel": (89, 116, 544, 435),
        "obstaculos": [],
        "mascara": "mapas/laboratorio-de-analises-paredes.png",
        "pasta_objetos": "mapas/objetos/laboratorio-de-analises",
        "pixels_por_unidade_objetos": 2,
        "objetos": "objetos.json",
        "inicio": (360, 530),
    },
    "tunel-de-ventilacao": {
        "nome": "Túnel de ventilação",
        # Base e peças de Downloads/objetos/dutos ventilacao, montadas numa imagem só
        # nas posições de docs/locais/tunel-de-ventilacao/mapa-limpo.webp.
        "imagem": "mapas/tunel-de-ventilacao.png",
        "tamanho": (720, 720),
        "area_andavel": (0, 0, 720, 720),
        "obstaculos": [],
        # Corredores andáveis (branco), desenhados à mão sobre a referência.
        "mascara": "mapas/tunel-de-ventilacao-paredes.png",
        "inicio": (382, 520),
    },
    "central-de-seguranca": {
        "nome": "Central de segurança",
        # Mapa vazio (ampliado no Upscayl) e objetos de Downloads/objetos/central seguranca,
        # nas posições de docs/locais/central-de-seguranca/mapa-limpo.webp.
        "imagem": "mapas/central-de-seguranca-vazia.png",
        "tamanho": (720, 720),
        "area_andavel": (0, 0, 720, 720),
        "obstaculos": [],
        "mascara": "mapas/central-de-seguranca-paredes.png",
        "pasta_objetos": "mapas/objetos/central-de-seguranca",
        "pixels_por_unidade_objetos": 2,
        "objetos": "objetos.json",
        "inicio": (360, 565),
    },
    "central-de-seguranca-pos-incidente": {
        "nome": "Central de segurança (pós-incidente)",
        # Mapa vazio e objetos de Downloads/objetos/central seguranca quebrada,
        # nas mesmas posições e com a mesma máscara da central limpa.
        "imagem": "mapas/central-de-seguranca-pos-incidente-vazia.png",
        "tamanho": (720, 720),
        "area_andavel": (0, 0, 720, 720),
        "obstaculos": [],
        "mascara": "mapas/central-de-seguranca-paredes.png",
        "pasta_objetos": "mapas/objetos/central-de-seguranca-pos-incidente",
        "pixels_por_unidade_objetos": 2,
        "objetos": "objetos.json",
        "inicio": (360, 565),
    },
    "camara-de-contencao-pos-incidente": {
        "nome": "Câmara de contenção (pós-incidente)",
        # Mapa vazio (ampliado no Upscayl) e objetos de Downloads/objetos/sala contencao quebrada,
        # nas posições de docs/locais/camara-de-contencao/mapa.webp.
        "imagem": "mapas/camara-de-contencao-pos-incidente-vazia.png",
        "tamanho": (720, 720),
        "area_andavel": (0, 0, 720, 720),
        "obstaculos": [],
        "mascara": "mapas/camara-de-contencao-paredes.png",
        "pasta_objetos": "mapas/objetos/camara-de-contencao-pos-incidente",
        "pixels_por_unidade_objetos": 2,
        "objetos": "objetos.json",
        "inicio": (360, 560),
    },
    "sala-de-servidores-pos-incidente": {
        "nome": "Sala de servidores (pós-incidente)",
        # Mapa vazio (ampliado no Upscayl) e objetos de Downloads/objetos/sala servidores quebrada,
        # nas posições de docs/locais/sala-de-servidores/mapa.webp; paredes iguais às da sala de servidores.
        "imagem": "mapas/sala-de-servidores-pos-incidente-vazia.png",
        "tamanho": (720, 720),
        "area_andavel": (0, 0, 720, 720),
        "obstaculos": [],
        "mascara": "mapas/sala-de-servidores-paredes.png",
        "pasta_objetos": "mapas/objetos/sala-de-servidores-pos-incidente",
        "pixels_por_unidade_objetos": 2,
        "objetos": "objetos.json",
        "inicio": (360, 540),
    },
    "sala-de-evacuacao-pos-incidente": {
        "nome": "Sala de evacuação (pós-incidente)",
        # Mapa vazio (ampliado no Upscayl) e objetos de Downloads/objetos/sala evacuacao quebrada,
        # nas posições da sala de evacuação; paredes iguais às dela.
        "imagem": "mapas/sala-de-evacuacao-pos-incidente-vazia.png",
        "tamanho": (720, 720),
        "area_andavel": (0, 0, 720, 720),
        "obstaculos": [],
        "mascara": "mapas/sala-de-evacuacao-paredes.png",
        "pasta_objetos": "mapas/objetos/sala-de-evacuacao-pos-incidente",
        "pixels_por_unidade_objetos": 2,
        "objetos": "objetos.json",
        "inicio": (360, 500),
    },
    "laboratorio-de-analises-pos-incidente": {
        "nome": "Laboratório de análises (pós-incidente)",
        # Mapa vazio (ampliado no Upscayl) e objetos de Downloads/objetos/laboratorio analises quebrado,
        # nas posições de docs/locais/laboratorio-de-analises/mapa.webp; paredes iguais às do laboratório.
        "imagem": "mapas/laboratorio-de-analises-pos-incidente-vazia.png",
        "tamanho": (720, 720),
        "area_andavel": (0, 0, 720, 720),
        "obstaculos": [],
        "mascara": "mapas/laboratorio-de-analises-paredes.png",
        "pasta_objetos": "mapas/objetos/laboratorio-de-analises-pos-incidente",
        "pixels_por_unidade_objetos": 2,
        "objetos": "objetos.json",
        "inicio": (360, 530),
    },
    "tunel-de-ventilacao-pos-incidente": {
        "nome": "Túnel de ventilação (pós-incidente)",
        # Mapa completo (já com as peças), versão enviada na conversa;
        # paredes do túnel de ventilação, com ajustes desta versão.
        "imagem": "mapas/tunel-de-ventilacao-pos-incidente.png",
        "tamanho": (720, 720),
        "area_andavel": (0, 0, 720, 720),
        "obstaculos": [],
        "mascara": "mapas/tunel-de-ventilacao-pos-incidente-paredes.png",
        "inicio": (382, 520),
    },
}

# Itens investigativos. "mensagem" é o que o item revela de fato (para a investigação);
# "fala" é o que a personagem diz ao encontrar, sem saber o que é; "palpite" é o que
# ela acha que é, em poucas palavras, e aparece no mapa mental.
# Onde cada item aparece é sorteado a cada partida (ver mapas/locais-itens.json).
ITENS = {
    "cracha-de-acesso": {
        "id": "OBJ-01",
        "nome": "Crachá de acesso",
        "imagem": "itens/cracha-de-acesso.png",
        "mensagem": "Permite reconstruir quem entrou nos setores restritos e em quais horários.",
        "fala": "Um crachá do complexo... Espera. Essa foto. É o meu pai.",
        "palpite": "O crachá do meu pai.",
    },
    "pendrive-criptografado": {
        "id": "OBJ-02",
        "nome": "Pendrive criptografado",
        "imagem": "itens/pendrive-criptografado.png",
        "mensagem": "Cópia parcial dos registros do experimento, com a autorização feita pela conta da direção.",
        "fala": "Um pendrive. Tem um cadeado gravado nele... alguém quis muito esconder o que tem aqui dentro.",
        "palpite": "Um pendrive trancado. Segredos?",
    },
    "gravador-de-audio": {
        "id": "OBJ-03",
        "nome": "Gravador de áudio",
        "imagem": "itens/gravador-de-audio.png",
        "mensagem": "Gravações de Amie Lin sobre inconsistências e o pedido de antecipação do experimento.",
        "fala": "Tem um compartimento por dentro... um gravadorzinho de voz, preso numa alça. Quem será que falava aqui?",
        "dentro_de": "bolsa-de-campo",
        "palpite": "Um gravador. Vozes de alguém.",
    },
    "frasco-de-contencao": {
        "id": "OBJ-04",
        "nome": "Frasco de contenção",
        "imagem": "itens/frasco-de-contencao.png",
        "mensagem": "Ajuda a verificar se houve retirada manual da amostra. O frasco está vazio.",
        "fala": "Um frasco lacrado... e vazio. O que quer que estivesse aqui dentro, saiu.",
        "palpite": "Um frasco vazio. Vazio demais.",
    },
    "relatorio-de-acesso": {
        "id": "OBJ-05",
        "nome": "Relatório de acesso",
        "imagem": "itens/relatorio-de-acesso.png",
        "mensagem": "Horários, setores visitados e tentativas de entrada.",
        "fala": "Folhas cheias de horários e nomes de setores. Parece um controle de quem entrava e saía.",
        "palpite": "Uma lista de quem entrou e saiu.",
    },
    "sensor-de-pressao": {
        "id": "OBJ-06",
        "nome": "Sensor de pressão",
        "imagem": "itens/sensor-de-pressao.png",
        "mensagem": (
            "Sensor de pressão encontrado na maleta de Clara Costa: "
            "registra uma alteração MANUAL dos parâmetros de contenção."
        ),
        "fala": "As travas cederam. Encaixado na espuma, um mostrador de metal... o ponteiro travou no vermelho.",
        "dentro_de": "maleta-de-amostras",
        "palpite": "Um medidor travado no vermelho.",
    },
    "ordem-de-manutencao": {
        "id": "OBJ-07",
        "nome": "Ordem de manutenção da ventilação",
        "imagem": "itens/ordem-de-manutencao.png",
        "mensagem": "Ordem de serviço da ventilação com inconsistências; o aval de Beatrice foi manipulado.",
        "fala": "Um papel de serviço da ventilação, assinado... mas essa assinatura parece meio torta.",
        "palpite": "Papel da ventilação. Assinatura esquisita.",
    },
    # Itens pessoais dos funcionários (docs/itens/pessoais). Também sorteados, exceto a
    # foto da família, que fica fixa,
    # e os que vêm dentro de outros ("dentro_de"/"contem") ("fixo": sala -> posição do brilho, em cada fase).
    "bolsa-de-campo": {
        "id": "PES-01",
        "nome": "Bolsa de campo de Amie Lin",
        "imagem": "itens/bolsa-de-campo.png",
        "mensagem": "Bolsa de campo de Amie Lin. Guardava o gravador de áudio dela.",
        "fala": "Uma bolsa preta com o símbolo de risco biológico. Pesada... tem alguma coisa aqui dentro.",
        "contem": "gravador-de-audio",
        "palpite": "Bolsa de risco biológico. Tem algo dentro.",
    },
    "caderno-de-simbolos": {
        "id": "PES-02",
        "nome": "Caderno de anotações de Angela Torres",
        "imagem": "itens/caderno-de-simbolos.png",
        "mensagem": "Caderno de Angela com o dicionário dos símbolos lógicos usados na investigação.",
        "fala": "Um caderno cheio de setinhas e sinais... ~, v, ^. Eu conheço isso. Alguém me ensinou essas setas.",
        "palpite": "O caderno das setinhas. Eu conheço.",
        "paginas": ["itens/caderno-de-simbolos-aberto.png"],  # ao ampliar, abre na página dos símbolos
    },
    "gravata": {
        "id": "PES-03",
        "nome": "Gravata de Otávio Ferraz",
        "imagem": "itens/gravata.png",
        "mensagem": "A gravata de Otávio, que morreu perto de uma das portas tentando fugir.",
        "fala": "Uma gravata vermelha, ainda com o nó feito. Rasgada... quem usava não teve tempo de tirar.",
        "palpite": "Gravata de alguém que tentou fugir.",
    },
    "maleta-de-amostras": {
        "id": "PES-04",
        "nome": "Maleta de amostras de Clara Costa",
        "imagem": "itens/maleta-de-amostras.png",
        "mensagem": "Maleta de Clara Costa. Guardava o sensor de pressão.",
        "fala": "Uma maleta rígida, travada nas laterais. Risco biológico de novo... o que eles guardavam aqui?",
        "contem": "sensor-de-pressao",
        "palpite": "Maleta trancada de amostras.",
    },
    "oculos-de-protecao": {
        "id": "PES-05",
        "nome": "Óculos de proteção de Beatrice Salles",
        "imagem": "itens/oculos-de-protecao.png",
        "mensagem": "Os óculos de Beatrice, que voltou para ajudar e morreu nos dutos.",
        "fala": "Óculos de proteção redondos, de bronze. Uma das lentes está estilhaçada.",
        "palpite": "Óculos de bronze, uma lente quebrada.",
    },
    "foto-da-familia": {
        "id": "PES-06",
        "nome": "Foto da família do Helix",
        "imagem": "itens/foto-da-familia.png",
        "mensagem": "Foto da festinha de sete anos de Giulia, com toda a equipe. Destrava um flashback.",
        "fala": "Um porta-retrato... sou eu? Com sete anos, enrolada no cardigã do meu pai. E todos eles em volta de mim.",
        "palpite": "Minha festa de sete anos. Todos eles.",
        # Sobre a mesa de monitores do fundo, à esquerda do teclado.
        "fixo": {"central-de-seguranca": (300, 145), "central-de-seguranca-pos-incidente": (300, 140)},
    },
    "caderno-do-fernando": {
        "id": "PES-07",
        "nome": "Caderno de Fernando Almeida",
        "imagem": "itens/caderno-do-fernando.png",
        "mensagem": "Caderno de Fernando com anotações suspeitas: negócios, cronograma, equipe, o pai e fragmentos.",
        "fala": "Um caderno de capa escura, cheio de páginas arrancadas e enfiadas de volta. Anotações de alguém importante.",
        "palpite": "Caderno de alguém, cheio de páginas soltas.",
        # Páginas que dá para folhear (setas ou A/D) ao ampliar. A página 6, quase uma
        # confissão, fica de fora até o fim da história.
        "paginas": [f"itens/caderno-do-fernando-pagina-{n}.png" for n in range(1, 6)],
    },
}


# Portas de cada sala: ponto no piso em frente (x, y, em unidades) e o meio da porta
# desenhada, onde aparece o brilho. Perto de uma delas, E abre o menu de destinos;
# quem chega numa sala aparece na primeira porta.
PORTAS = {
    "central-de-seguranca": [((360, 565), (362, 607))],
    "sala-de-servidores": [((356, 125), (358, 62)), ((346, 565), (358, 630))],
    "laboratorio-de-analises": [((361, 125), (367, 68)), ((343, 555), (367, 622))],
    "camara-de-contencao": [((365, 125), (367, 62)), ((363, 565), (367, 630))],
    "sala-de-evacuacao": [((361, 125), (367, 62)), ((368, 555), (367, 630))],
    "tunel-de-ventilacao": [((375, 150), (375, 45)), ((375, 690), (375, 690))],
}
for _sala, _portas in PORTAS.items():
    for _chave, _par in ((_sala, _sala + "-pos-incidente"), (_sala + "-pos-incidente", _sala)):
        MAPAS[_chave]["portas"] = [piso for piso, _ in _portas]
        MAPAS[_chave]["brilho_portas"] = [meio for _, meio in _portas]
        MAPAS[_chave]["par"] = _par  # Tab alterna antes/depois do incidente
