# PROPORÇÕES DA TELA
LARGURA_TELA = 1024
ALTURA_TELA = 600

# PROPORÇÕES DO JOGADOR
LARGURA_JOGADOR = 50   
ALTURA_JOGADOR = 75    

# PROPORÇÕES DO ZAGUEIRO
LARGURA_ZAGUEIRO = 55  
ALTURA_ZAGUEIRO = 80   

RAIO_BOLA = 12         

# DEFINIÇÃO NO PADRAO RGB
# Por enquanto vai ser somente cores apenas para diferenciar os objetos
COR_GRAMADO = (34, 139, 34)       
COR_TEXTO = (255, 255, 255)       
COR_LINHA = (255, 255, 255)       
COR_NEYMAR = (255, 215, 0)       
COR_ARGENTINA = (30, 144, 255)   
COR_BOLA = (255, 255, 255)        
COR_CHUTEIRA = (50, 205, 50)      
COR_ESTRELA = (255, 165, 0)       

# DICIONARIO COM AS DIFICULDADES E QUE ESTABELECE AS REGRAS DO JOGO
DIFICULDADES = {
    "FACIL": {"chances": 5, "velocidade_rival": 2},
    "MEDIO": {"chances": 3, "velocidade_rival": 2.5},
    "DIFICIL": {"chances": 1, "velocidade_rival": 3}
}