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

# CONFIGURAÇÕES PARA O GOL (Centralizado no topo sobre a linha dos 40px)
LARGURA_GOL = 224 #antes era 120 
ALTURA_GOL = 54 #antes era 40
POS_GOL_X = OFFSET_X + (LARGURA_CAMPO_JOGAVEL // 2) - (LARGURA_GOL // 2)
POS_GOL_Y = LIMITE_SUPERIOR

# CONFIGURAÇÕES DA GRANDE ÁREA (Baseada na linha superior de fundo)
LARGURA_AREA = 806
ALTURA_AREA = 330
POSICAO_X_AREA = OFFSET_X + (LARGURA_CAMPO_JOGAVEL // 2) - (LARGURA_AREA // 2)
POSICAO_Y_AREA = LIMITE_SUPERIOR

# MEIA LUA E LINHA DO MEIO CAMPO
POS_MEIO_CAMPO_Y = LIMITE_SUPERIOR + (ALTURA_REAL_RETANGULO // 2) # 540

LARGURA_ARCO = 180
ALTURA_ARCO = 140
ARCO_X = OFFSET_X + (LARGURA_CAMPO_JOGAVEL // 2) - (LARGURA_ARCO // 2)
ARCO_Y = POS_MEIO_CAMPO_Y - (ALTURA_ARCO // 2)

# ==========================================
# CORES DO JOGO
# ==========================================
COR_GRAMADO = (55, 111, 50) 
COR_LINHA = (255, 255, 255) 
COR_TRAVE = (255, 255, 255) 
COR_NEYMAR = (255, 255, 0)  
COR_ZAGUEIRO = (255, 0, 0)
COR_GOLEIRO = (0, 255, 100)
COR_BOLA = (255, 255, 255)  
COR_ESTRELA = (255, 255, 0)   
COR_CHUTEIRA = (255, 128, 0)  

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

CONFIANCA_POR_DIFICULDADE = {
    'FACIL': 30,
    'MEDIO': 20,
    'DIFICIL': 10 
}

DRIBLES_CONFIG = {
    'pedalada': {'ganho': 15, 'chance_inicial': 0.70, 'chance_max': 0.95},
    '360': {'ganho': 25, 'chance_inicial': 0.65, 'chance_max': 0.85},
    'lambreta': {'ganho': 40, 'chance_inicial': 0.60, 'chance_max': 0.75}
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
            "nome": "FÁCIL - Inversão de Jogada",
            "neymar_pos": (900, 410),      
            "bola_origem": (1580, 100),      
            "bola_destino": (1450, 420),    
            "aliados_pos": [(1450, 430), (1620, 120)],
            "zagueiros_pos": [(650, 250), (850, 150), (1085, 350), (1120, 200)]
        }
        
    },
    "medio": {
        1: {
            "nome": "MÉDIO - COBRANÇA RECUADA DE LATERAL",
            "neymar_pos": (750, 800),       
            "bola_origem": (500, 1050),     
            "bola_destino": (700, 700), # Ponto futuro mais curto, zaga mais compacta     
            "aliados_pos": [(400, 800), (1100, 800)], 
            "zagueiros_pos": [(680, 450), (820, 450), (550, 550), (950, 550)] 
        },
        2: {
            "nome": "MÉDIO - Linha de Fundo Direita",
            "neymar_pos": (1100, 750),       
            "bola_origem": (700, 950),      
            "bola_destino": (1050, 650),     
            "aliados_pos": [(600, 700), (800, 850)],
            "zagueiros_pos": [(950, 380), (1100, 420), (750, 450), (500, 500)]
        },
        3: {
            "nome": "MÉDIO - Ataque Flanco Esquerdo",
            "neymar_pos": (400, 750),      
            "bola_origem": (800, 1000),     
            "bola_destino": (450, 650),    
            "aliados_pos": [(700, 700), (950, 800)],
            "zagueiros_pos": [(450, 400), (600, 380), (800, 450), (1050, 480)]
        },
        4: {
            "nome": "MÉDIO - Bola Dividida no Meio",
            "neymar_pos": (800, 700),       
            "bola_origem": (800, 1050),     
            "bola_destino": (800, 580), # Bola para perigosamente mais perto dos zagueiros     
            "aliados_pos": [(500, 750), (1100, 750)],
            "zagueiros_pos": [(740, 380), (860, 380), (620, 440), (980, 440)] 
        }
    },
    "dificil": {
        1: {
            "nome": "DIFÍCIL - Pressão Total na Intermediária",
            "neymar_pos": (700, 750),       
            "bola_origem": (900, 1000),     
            "bola_destino": (750, 640), # Pouquíssimo espaço para pensar antes do bote     
            "aliados_pos": [(450, 800)], 
            "zagueiros_pos": [(680, 480), (820, 480), (720, 580), (880, 580)] # Bloco defensivo ultra-fechado
        },
        2: {
            "nome": "DIFÍCIL - Corredor Polonês na Ponta",
            "neymar_pos": (400, 700),       
            "bola_origem": (350, 950),      
            "bola_destino": (420, 600),     
            "aliados_pos": [(800, 750)],
            "zagueiros_pos": [(420, 420), (550, 450), (400, 520), (680, 500)] # Dois zagueiros cercando o seu lado
        },
        3: {
            "nome": "DIFÍCIL - Transição Rápida Abafada",
            "neymar_pos": (1100, 700),      
            "bola_origem": (750, 950),     
            "bola_destino": (1050, 600),    
            "aliados_pos": [(700, 750)],
            "zagueiros_pos": [(1020, 420), (900, 450), (1080, 520), (800, 500)]
        }
    }
}