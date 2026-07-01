# ==========================================
# CONFIGURAÇÕES DE TELA (RESOLUÇÃO TOTAL)
# ==========================================
LARGURA_TELA = 1920
ALTURA_TELA = 1080
FPS = 30

# ==========================================
# PROPORÇÕES DO CAMPO DE JOGO
# ==========================================
LARGURA_CAMPO_JOGAVEL = 1280
ALTURA_CAMPO_JOGAVEL = 1080
LARGURA_ARQUIBANCADA = 320 
ALTURA_ARQUIBANCADA = 1080

# Deslocamento horizontal (Arquibancadas de 320px em cada lado)
OFFSET_X = (LARGURA_TELA - LARGURA_CAMPO_JOGAVEL) // 2  # 320

CAMPO_X = OFFSET_X
CAMPO_Y = 0

# Recuo das linhas de fundo (Linha horizontal onde fica o gol)
RECUO_LINHA_FUNDO = 72 # 72 PQ 8 PIXELS SAO DA LINHA EM SI, AI DÁ PRA O NEYMAR ANDAR POR CIMA DA LINHA


# LIMITES DAS QUATRO LINHAS BRANCAS (TRAVAS)
# LEMBRE-SE QUE ESSAS CONSTANTES DE LIMITES SAO AS COORDENADAS DOS PIXELS DAS
# LINHAS BRANCAS QUE DELIMITAM O CAMPO
LIMITE_ESQUERDO = OFFSET_X                              # 320
LIMITE_DIREITO  = OFFSET_X + LARGURA_CAMPO_JOGAVEL      # 1600
LIMITE_SUPERIOR = RECUO_LINHA_FUNDO                    # 80
LIMITE_INFERIOR = ALTURA_CAMPO_JOGAVEL  # 1080

# CONSTANTES DOS LIMITES QUE PRENDEM O NEY NO CAMPO AJUSTADAS PARA O TAMANHO DA HITBOX DELE
LIMITE_ESQUERDO_CAMPO_NEYMAR = OFFSET_X -10
LIMITE_DIREITO_CAMPO_NEYMAR = OFFSET_X + LARGURA_CAMPO_JOGAVEL +10
LIMITE_SUPERIOR_CAMPO_NEYMAR = 0
LIMITE_INFERIOR_CAMPO_NEYMAR = ALTURA_CAMPO_JOGAVEL + 10

# TUPLA IMPORTANTE PRA DEFINIR OS LIMITES E PRENDER O NEYMAR
TUPLA_LIMITES_CAMPO = (LIMITE_ESQUERDO, LIMITE_SUPERIOR, LIMITE_DIREITO - LIMITE_ESQUERDO, LIMITE_INFERIOR)
ALTURA_REAL_RETANGULO = LIMITE_INFERIOR - LIMITE_SUPERIOR

TUPLA_LIMITES_CAMPO_PRA_NEYMAR = (LIMITE_ESQUERDO_CAMPO_NEYMAR, LIMITE_SUPERIOR_CAMPO_NEYMAR, LIMITE_DIREITO_CAMPO_NEYMAR - LIMITE_ESQUERDO_CAMPO_NEYMAR, LIMITE_INFERIOR_CAMPO_NEYMAR)

# ==========================================
# CONFIGURAÇÕES GEOMÉTRICAS DOS ELEMENTOS
# ==========================================

# CONFIGURAÇÕES PARA O GOL 
LARGURA_GOL = 224 #antes era 120 
ALTURA_GOL = 54 #antes era 40
POS_GOL_X = OFFSET_X + (LARGURA_CAMPO_JOGAVEL // 2) - (LARGURA_GOL // 2)
POS_GOL_Y = LIMITE_SUPERIOR


# ==========================================
# CORES DO JOGO
# ==========================================

COR_GOLEIRO = (0, 255, 100)

# ==========================================
# VELOCIDADES E GAMEPLAY
# ==========================================
VELOCIDADE_NEY = 5
VELOCIDADE_NEY_PRIME = 8
VELOCIDADE_ZAG = 3
FORCA_CHUTE = 15 
FORCA_LANCAMENTO_ALIADO = 16
VELOCIDADE_LANCAMENTO_INICIAL = 12

TAMANHO_ITEM = 32
TEMPO_CHUTEIRA = 4000 
META_ESTRELA = 100

LARGURA_NEYMAR = 80
ALTURA_NEYMAR = 108

DRIBLES_CONFIG = {
    'pedalada': {'ganho': 20, 'chance_inicial': 0.70, 'chance_max': 0.95},
    '360': {'ganho': 30, 'chance_inicial': 0.60, 'chance_max': 0.85}
}

# CONFIGURAÇÃO DE CENÁRIOS TÁTICOS (DIFICULDADE FÁCIL - BOLA EM ESPAÇO VAZIO)

# =========================================================================
# BANCO DE CENÁRIOS TÁTICOS COLETIVOS (TODAS AS DIFICULDADES)
# Limites do campo jogável: X (320 até 1280) | Y (70 até 1080)
# =========================================================================

CENARIOS_TATICOS = {
    "facil": {
        1: {
            "nome": "FÁCIL - Ataque Veloz pela Ponta Esquerda",
            "neymar_pos": (450, 850),       
            "bola_origem": (650, 1050),     
            "bola_destino": (520, 750),     
            "aliados_pos": [(750, 650), (1400, 450), (370, 500)], 
            "zagueiros_pos": [(550, 450), (750, 400), (950, 370), (1200, 330)] 
        },
        2: {
            "nome": "FÁCIL - Contra-Ataque Centralizado",
            "neymar_pos": (800, 900),       
            "bola_origem": (500, 1070),      
            "bola_destino": (700, 750),     
            "aliados_pos": [(1110, 550)], # CONTRA-ATAQUE SO COM UM ALIADO
            "zagueiros_pos": [(1250, 600), (670, 570), (1000, 500)] 
        },
        3: {
            "nome": "FÁCIL - Infiltração pela Direita",
            "neymar_pos": (1550, 850),      
            "bola_origem": (980, 1070),     
            "bola_destino": (1420, 480),    
            "aliados_pos": [(900, 470)],
            "zagueiros_pos": [(1100, 280), (1200, 400), (900, 300)]
        },
        4: {
            "nome": "FÁCIL - Pivô na Entrada da Área",
            "neymar_pos": (960, 1000),       
            "bola_origem": (1400, 1070),     
            "bola_destino": (960, 860),     
            "aliados_pos": [(450, 600), (1250, 420), (800, 850)],
            "zagueiros_pos": [(700, 450), (1000, 580), (550, 650), (1190, 480)] 
        },
        5: {
            "nome": "FÁCIL - Cobrança de Escanteio",
            "neymar_pos": (900, 410),      
            "bola_origem": (1540, 110),      
            "bola_destino": (1450, 420),    
            "aliados_pos": [(1450, 430), (1620, 60)],
            "zagueiros_pos": [(650, 250), (850, 150), (1085, 350), (1120, 200)]
        }
        
    },
    "medio": {
        1: {
            "nome": "MÉDIO - COBRANÇA RECUADA DE LATERAL",
            "neymar_pos": (1100, 1000),       
            "bola_origem": (1590, 700),     
            "bola_destino": (1430, 780), 
            "aliados_pos": [(1530, 370)], 
            "zagueiros_pos": [(1200, 300), (1020, 380), (1380, 220), (1130, 720)] 
        },
        2: {
            "nome": "MÉDIO - Cobrança de Falta com jogada ensaiada",
            "neymar_pos": (1220, 520),       
            "bola_origem": (810, 650),      
            "bola_destino": (815, 620),     
            "aliados_pos": [(815, 620)],
            "zagueiros_pos": [(1030, 210), (1200, 265), (850, 370), (912, 370)]
        },
        3: {
            "nome": "MÉDIO - Ataque Flanco Esquerdo Cercado",
            "neymar_pos": (400, 750),      
            "bola_origem": (800, 1000),     
            "bola_destino": (450, 650),    
            "aliados_pos": [(540, 200), (950, 490)],
            "zagueiros_pos": [(450, 400), (600, 380), (800, 450), (710, 150), (880, 700)]
        },
        4: {
            "nome": "MÉDIO - Funil Tático pela Direita",
            "neymar_pos": (1420, 720),      
            "bola_origem": (1100, 950),     
            "bola_destino": (1400, 740),    
            "aliados_pos": [(1050, 650), (850, 450)],
            "zagueiros_pos": [(1200, 430), (1480, 500), (1100, 400), (900, 350)]
        },
    },
    "dificil": {
        1: {
            "nome": "DIFÍCIL - Transição Rápida com Zaga em Linha",
            "neymar_pos": (600, 750),       
            "bola_origem": (450, 1000),     
            "bola_destino": (480, 650),     
            "aliados_pos": [(850, 720), (1450, 400), (930, 390)], 
            "zagueiros_pos": [(720, 620), (920, 580), (1120, 540), (1300, 500), (450, 170), (620, 230), (750, 340), (490, 410)] 
        },
        2: {
            "nome": "DIFÍCIL - Infiltração Diagonal",
            "neymar_pos": (1500, 900),      
            "bola_origem": (1200, 1000),      
            "bola_destino": (1480, 700),     
            "aliados_pos": [(700, 550), (450, 400), (1330, 220)], 
            "zagueiros_pos": [(1150, 580), (1300, 480), (950, 450), (1100, 320), (920, 690), (1030, 830), (1530, 140), (860, 1000)] 
        },
        3: {
            "nome": "DIFICIL - PENALTI ENSAIADO - A APOSTA MAIS LOUCA!!!!!",
            "neymar_pos": (580, 750),      
            "bola_origem": (960, 270),     
            "bola_destino": (960, 270),    
            "aliados_pos": [(960, 270), (450, 200)],
            "zagueiros_pos": [(1240, 620), (1020, 580), (800, 540), (580, 500), (920, 500), (650, 280), (850, 720)]
        },
    }
}