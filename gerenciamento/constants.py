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

# Deslocamento horizontal (Arquibancadas de 320px em cada lado)
OFFSET_X = (LARGURA_TELA - LARGURA_CAMPO_JOGAVEL) // 2  # 320

# Recuo das linhas de fundo (Linha horizontal onde fica o gol)
RECUO_LINHA_FUNDO = 72 # 72 PQ 8 PIXELS SAO DA LINHA EM SI, AI DÁ PRA O NEYMAR ANDAR POR CIMA DA LINHA

# ==========================================
# LIMITES DAS QUATRO LINHAS BRANCAS (TRAVAS)
# ==========================================
# Use estas constantes para prender o Neymar dentro do retângulo de cal
# LEMBRE-SE QUE ESSAS CONSTANTES DE LIMITES SAO AS COORDENADAS DOS PIXELS DAS
# LINHAS BRANCAS QUE DELIMITAM O CAMPO
LIMITE_ESQUERDO = OFFSET_X                              # 320
LIMITE_DIREITO  = OFFSET_X + LARGURA_CAMPO_JOGAVEL      # 1600
LIMITE_SUPERIOR = RECUO_LINHA_FUNDO                    # 80
LIMITE_INFERIOR = ALTURA_CAMPO_JOGAVEL - RECUO_LINHA_FUNDO  # 1008

# TUPLA IMPORTANTE PRA DEFINIR OS LIMITES E PRENDER O NEYMAR
TUPLA_LIMITES_CAMPO = (LIMITE_ESQUERDO, LIMITE_SUPERIOR, LIMITE_DIREITO - LIMITE_ESQUERDO, LIMITE_INFERIOR)

# Altura real do retângulo de cal (1080 - 40 - 40 = 1000)
ALTURA_REAL_RETANGULO = LIMITE_INFERIOR - LIMITE_SUPERIOR

# ==========================================
# CONFIGURAÇÕES GEOMÉTRICAS DOS ELEMENTOS
# ==========================================

# CONFIGURAÇÕES PARA O GOL (Centralizado no topo sobre a linha dos 40px)
LARGURA_GOL = 120
ALTURA_GOL = 40
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
COR_BOLA = (255, 255, 255)  
COR_ESTRELA = (255, 255, 0)   
COR_CHUTEIRA = (255, 128, 0)  

# ==========================================
# VELOCIDADES E GAMEPLAY
# ==========================================
VELOCIDADE_NEY = 5
VELOCIDADE_ZAG = 3
FORCA_CHUTE = 15 
FORCA_LANCAMENTO_ALIADO = 16

TAMANHO_ITEM = 20 
TEMPO_CHUTEIRA = 4000 
META_ESTRELA = 100

CONFIANCA_POR_DIFICULDADE = {
    'FACIL': 30,
    'MEDIO': 20,
    'DIFICIL': 10
}

DRIBLES_CONFIG = {
    'pedalada': {'ganho': 15, 'chance_inicial': 0.70, 'chance_max': 0.90},
    '360': {'ganho': 25, 'chance_inicial': 0.50, 'chance_max': 0.80},
    'lambreta': {'ganho': 40, 'chance_inicial': 0.25, 'chance_max': 0.75}
}