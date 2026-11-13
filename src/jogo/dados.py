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
        "escala": 0.9,  # um pouco menor que os outros
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
    # Textos de amostra47_textos_itens.md:
    # "fala" = Descrição (aparece ao coletar); "palpite" = Observação de Giulia (mapa mental);
    # "texto" = Inspecionar / Ler / Ouvir (tela de inspeção; uma linha por item da lista).
    "cracha-de-acesso": {
        "id": "OBJ-01",
        "nome": "Crachá de acesso de Giovani Pistori",
        "imagem": "itens/cracha-de-acesso.png",
        "paginas": ["itens/cracha-de-acesso.png", "itens/cracha-de-acesso-verso.png"],  # frente e verso (foto)
        "fala": "Um crachá antigo do Complexo Helix, preso a um suporte de plástico rígido. O cartão está desgastado, "
                "com manchas escuras próximas às bordas. A foto funcional ainda é reconhecível.",
        "palpite": "Ele carregava essa foto para o trabalho... o tempo todo? Talvez eu possa usar para acessar as câmeras.",
        "texto": [
            "COMPLEXO HELIX — IDENTIFICAÇÃO FUNCIONAL",
            "GIOVANI PISTORI",
            "Setor: Segurança",
            "Função: Chefe de Segurança",
            "Credencial: Acesso interno de segurança",
            "Código de identificação: [parcialmente ilegível]",
            "",
            "Verso: uma pequena fotografia mostra Giovani abraçando Giulia ainda criança. Os dois sorriem. "
            "A imagem foi colocada no verso do crachá, onde não deveria haver nada além da identificação técnica.",
        ],
    },
    "pendrive-criptografado": {
        "id": "OBJ-02",
        "nome": "Pendrive criptografado de Angela Torres",
        "imagem": "itens/pendrive-criptografado.png",
        "fala": "Um pendrive industrial protegido por uma carcaça de metal. O lacre de segurança está gasto, mas o "
                "dispositivo parece intacto. Não é possível ler seus arquivos sem um terminal compatível.",
        "palpite": "Isso registra uma autorização. Mas quem estava usando a conta?",
        # "premissas" aparecem abaixo da observação; "premissas_cameras" as substituem depois de ver as câmeras.
        "premissas_cameras": [
            "X = A liberação da Amostra 47 foi autorizada pela direção.",
            "R = O sistema registrou uma autorização administrativa para alterar a contenção.",
            "Z = O pendrive contém o registro decisivo da autorização administrativa.",
        ],
        "texto": [
            "UNIDADE DE ARMAZENAMENTO EXTERNO",
            "Conteúdo: CRIPTOGRAFADO",
            "Última verificação: [indisponível]",
            "Acesso aos registros: NEGADO",
        ],
    },
    "gravador-de-audio": {
        "id": "OBJ-03",
        "nome": "Gravador de áudio de Amie Lin",
        "imagem": "itens/gravador-de-audio.png",
        "fala": "Um gravador portátil encontrado dentro da bolsa de campo de Amie. Os botões estão gastos e a carcaça "
                "apresenta riscos. Uma gravação anterior ao alarme geral ainda pode ser reproduzida.",
        "dentro_de": "bolsa-de-campo",
        "palpite": "Amie avisou. Mas Fernando decidiu continuar mesmo assim.",
        "premissas": [
            "P = Amie Lin alertou sobre o risco de acelerar o experimento.",
            "Q = Fernando Almeida solicitou a antecipação do experimento.",
        ],
        "audio": "sons/gravador-amie-lin.mp3",  # E na inspeção toca a gravação
        "texto": [
            "[Ruído de equipamento ao fundo. Passos no corredor.]",
            "AMIE: “Os resultados ainda precisam ser revisados. Não terminamos as verificações de segurança.”",
            "VOZ MASCULINA: “O cronograma foi antecipado. A direção quer a próxima etapa preparada.”",
            "AMIE: “Eu já registrei os riscos. Antecipar o experimento nessas condições não é seguro.”",
            "VOZ MASCULINA: “A solicitação veio do doutor Fernando.”",
            "AMIE: “Então quero essa orientação documentada.”",
            "[Clique. Fim da gravação.]",
        ],
    },
    "frasco-de-contencao": {
        "id": "OBJ-04",
        "nome": "Frasco de contenção",
        "imagem": "itens/frasco-de-contencao.png",
        "fala": "Um pequeno recipiente de vidro técnico, com tampa metálica e rótulo de risco biológico parcialmente "
                "rasgado. Há marcas de manuseio na superfície. O frasco está vazio.",
        "palpite": "Não parece quebrado. Alguém pode ter retirado o conteúdo.",
        "texto": [
            "COMPLEXO HELIX — MATERIAL SOB CONTENÇÃO",
            "Identificação: AMOSTRA 47",
            "Manuseio: somente por pessoal autorizado",
            "Condição atual: RECIPIENTE VAZIO",
            "Registro de retirada: [não localizado no recipiente]",
        ],
    },
    "relatorio-de-acesso": {
        "id": "OBJ-05",
        "nome": "Relatório de acesso",
        "imagem": "itens/relatorio-de-acesso.png",
        "paginas": ["itens/relatorio-de-acesso-documento.png"],  # ao ampliar, mostra o relatório preenchido
        "fala": "Uma prancheta com folhas de controle de entrada e saída. Parte da tinta desapareceu e algumas linhas "
                "foram assinaladas à mão. Ainda é possível reconstruir a sequência de movimentações.",
        "palpite": "Otávio saiu do laboratório antes da liberação. Então por que ainda havia suspeitas sobre ele?",
        "premissas": ["W = Otávio Ferraz deixou o laboratório de análises antes da liberação da amostra."],
        "texto": [
            "COMPLEXO HELIX — CENTRAL DE SEGURANÇA",
            "RELATÓRIO DE ACESSOS E OCORRÊNCIAS",
            "Período: horas anteriores ao alarme geral",
            "",
            "• Credencial de Otávio Ferraz — Laboratório de análises — Saída registrada antes da liberação",
            "• Credencial de segurança — Áreas de monitoramento — Movimentação interna registrada",
            "• Conta da direção — Sistema de contenção — Autorização administrativa indicada em registro complementar",
            "• Evento não identificado — Acesso restrito — Origem a verificar",
            "",
            "NOTA DE CONFERÊNCIA: Os registros de circulação física e os comandos administrativos devem ser "
            "analisados separadamente. A presença de um nome no controle de portas não identifica, por si só, "
            "o autor de um comando de sistema.",
        ],
    },
    "sensor-de-pressao": {
        "id": "OBJ-06",
        "nome": "Sensor de pressão de Clara Costa",
        "imagem": "itens/sensor-de-pressao.png",
        "fala": "Um manômetro metálico, retirado de um equipamento de contenção e guardado na maleta de Clara. "
                "O ponteiro vermelho permanece próximo da faixa de alerta.",
        "dentro_de": "maleta-de-amostras",
        "palpite": "A mudança foi manual... e o registro aponta para a câmara.",
        "premissas": [
            "K = O setor associado à alteração manual foi a Câmara de Contenção.",
            "~A = Não houve arrombamento da câmara de contenção.",
        ],
        "texto": [
            "CONTROLE DE CONTENÇÃO — INSPEÇÃO TÉCNICA",
            "Setor: CÂMARA DE CONTENÇÃO",
            "Responsável pelo registro: CLARA COSTA",
            "Ocorrência: variação de pressão incompatível com a condição prevista",
            "Histórico do controle: PARÂMETROS ALTERADOS MANUALMENTE",
            "Procedimento recomendado: suspender a operação até verificação técnica",
            "Valores numéricos: [não recuperados]",
        ],
    },
    "ordem-de-manutencao": {
        "id": "OBJ-07",
        "nome": "Ordem de manutenção da ventilação",
        "imagem": "itens/ordem-de-manutencao.png",
        "paginas": ["itens/ordem-de-manutencao-documento.jpg"],  # ao ampliar, mostra o documento preenchido
        "fala": "Uma ordem de serviço presa a uma prancheta de metal envelhecido. O formulário indica uma intervenção "
                "no sistema de ventilação, mas os campos de solicitação e aprovação apresentam sinais de inconsistência.",
        "palpite": "O nome de Beatrice Salles está aqui. Mas isso não prova que ela fez o pedido.",
        "premissas": ["V = A ordem de manutenção da ventilação partiu de Beatrice Salles."],
        "premissas_cameras": [
            "~V = A ordem de manutenção da ventilação não partiu de Beatrice Salles.",
            "S = Angela Torres identificou que o comando foi executado com uma conta da direção.",
        ],
        "texto": [
            "COMPLEXO HELIX — MANUTENÇÃO OPERACIONAL",
            "ORDEM DE SERVIÇO — SISTEMA DE VENTILAÇÃO",
            "Setor: Túneis e dutos de ventilação",
            "Tipo de serviço: revisão / ajuste operacional",
            "Solicitante declarado: setor de manutenção",
            "Responsável técnico indicado: BEATRICE SALLES",
            "Assinatura de autorização: [não verificável]",
            "Origem eletrônica do pedido: [divergente do setor informado]",
            "Estado da validação: PENDENTE DE CONFERÊNCIA",
            "",
            "OBSERVAÇÃO DE AUDITORIA: A origem da solicitação e o aval técnico não apresentam "
            "correspondência verificável nos registros recuperados.",
        ],
    },
    "bolsa-de-campo": {
        "id": "PES-01",
        "nome": "Bolsa de campo de Amie Lin",
        "imagem": "itens/bolsa-de-campo.png",
        "fala": "Bolsa de trabalho escura com o símbolo de risco biológico. Os zíperes estão endurecidos e há marcas "
                "de uso nas alças. Era usada para transportar instrumentos pessoais de pesquisa.",
        "contem": "gravador-de-audio",
        "palpite": "Amie guardou isso com cuidado. Talvez tenha gravado algo importante.",
        "texto": ["No compartimento central, preso por uma pequena alça, está um gravador de áudio."],
    },
    "caderno-de-simbolos": {
        "id": "PES-02",
        "nome": "Caderno de símbolos de Angela Torres",
        "imagem": "itens/caderno-de-simbolos.png",
        "fala": "Caderno espiral de capa preta, com abas coloridas e anotações feitas à mão. Algumas páginas "
                "apresentam pequenos exemplos de lógica.",
        "palpite": "Angela me mostrava essas setinhas quando eu era pequena... Eu achava que era um jogo.",
        "paginas": ["itens/caderno-de-simbolos-aberto.png"],  # ao ampliar, abre na página dos símbolos
    },
    "caderno-do-fernando": {
        "id": "PES-03",
        "nome": "Caderno de Fernando Almeida",
        "imagem": "itens/caderno-do-fernando.png",
        "fala": "Caderno de anotações pessoais, com a lombada danificada e várias folhas arrancadas. As páginas "
                "remanescentes não seguem uma ordem clara.",
        "palpite": "Se ele arrancou essas páginas, o que estava tentando esconder?",
        "paginas": [f"itens/caderno-do-fernando-pagina-{n}.png" for n in range(1, 6)],
    },
    "foto-da-familia": {
        "id": "PES-04",
        "nome": "Fotografia da família do Helix",
        "imagem": "itens/foto-da-familia.png",
        "fala": "Um porta-retrato enferrujado com o vidro trincado. A fotografia desbotada mostra uma pequena festa "
                "de aniversário no Complexo Helix. Ao centro está uma menina loira, cercada por seis adultos... sou eu.",
        "palpite": "Sou eu... Eu não lembrava que todos estavam lá.",
        "fixo": {"central-de-seguranca": (300, 145), "central-de-seguranca-pos-incidente": (300, 140)},
        "texto": [
            "Giulia, sete anos. Giovani, Angela, Amie, Beatrice, Clara e Otávio. Sete velinhas no bolo. "
            "A menina usa um cardigã marrom grande demais para ela. Fernando não aparece na fotografia.",
        ],
    },
    "gravata": {
        "id": "PES-05",
        "nome": "Gravata de Otávio Ferraz",
        "imagem": "itens/gravata.png",
        "fala": "Uma gravata estreita vermelho-terracota, ainda com o nó formado. O tecido está sujo e rasgado "
                "nas laterais.",
        "palpite": "Ele esteve aqui, perto das saídas. O que aconteceu quando as portas fecharam?",
        "texto": [
            "O nó permanece intacto, como se a gravata tivesse sido arrancada ou retirada às pressas. "
            "Não há bilhete nem identificação escrita.",
        ],
    },
    "maleta-de-amostras": {
        "id": "PES-06",
        "nome": "Maleta de amostras de Clara Costa",
        "imagem": "itens/maleta-de-amostras.png",
        "fala": "Maleta rígida de inspeção, com travas metálicas e marca de risco biológico. A superfície está "
                "arranhada, mas o interior permanece organizado.",
        "contem": "sensor-de-pressao",
        "palpite": "Clara estava verificando a contenção. Talvez o sensor guarde o que ela encontrou.",
        "premissas": ["U = Clara Costa registrou a alteração manual dos parâmetros de contenção."],
        "texto": [
            "Duas divisórias de espuma. À esquerda está encaixado um sensor de pressão. À direita, um módulo "
            "retangular sem identificação recuperável.",
        ],
    },
    "oculos-de-protecao": {
        "id": "PES-07",
        "nome": "Óculos de proteção de Beatrice Salles",
        "imagem": "itens/oculos-de-protecao.png",
        "fala": "Óculos de proteção de armação metálica, com a lente direita estilhaçada e correia de couro bastante "
                "gasta. Foram encontrados nos dutos de manutenção.",
        "palpite": "Beatrice voltou para os dutos enquanto os outros procuravam as saídas... Talvez estivesse tentando ajudar alguém.",
        "texto": ["A lente esquerda ainda está inteira. Não há inscrição nem documento preso aos óculos."],
    },
}

MAPAS["fachada-do-complexo"] = {
    "nome": "Fachada do Complexo Helix",
    # Área externa depois da abertura; a porta principal leva para dentro do complexo.
    # Imagem 1122x1402 em 640 unidades de largura, para preencher a tela.
    "imagem": "mapas/fachada-do-complexo.png",
    "tamanho": (640, 800),  # fachada em cima e a trilha da floresta embaixo
    "area_andavel": (0, 0, 640, 800),
    "obstaculos": [],
    "mascara": "mapas/fachada-do-complexo-paredes.png",
    "inicio": (325, 787),  # começo da trilha, embaixo
    "escala_personagens": 0.58,  "velocidade_personagens": 0.75,  # Giulia menor, proporcional ao carro
    # Gerador: começa desligado; a Giulia liga para a porta do complexo funcionar.
    "pasta_objetos": "mapas/objetos/fachada-do-complexo",
    "pixels_por_unidade_objetos": 1.75,
    "objetos": [
        {"id": "gerador", "imagem": "gerador-desligado.png", "imagem_ligado": "gerador-ligado.png",
         "retangulo": (205, 234, 57, 34), "pe": 0.35},
    ],
    "portas": [(327, 222)],
    "brilho_portas": [(327, 194)],
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
