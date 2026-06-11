# =-=-=-=-= ARQUIVO MAIN TEMPORARIO PARA TESTES =-=-=-=-=
import pygame
import sys
import math
from constants import *
from neymar import Neymar
from zagueiro import Zagueiro

def main():
    pygame.init()
    
    # CRIA A TELA DO JOGO 
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Neymar Jr - Rumo ao Hexa 2026")
    
    # RELOGIO DO FPS DO JOGO
    relogio = pygame.time.Clock()
    
    neymar = Neymar() # CRIA O NEYMAR COMO OBJETO
    zagueiro1 = Zagueiro()
    
    rodando = True
    while rodando:
        
        # VERIFICA SE EU NAO FECHEI A JANELA
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
        
        # MOVE O NEYMAR DENTRO DO JOGO
        teclas = pygame.key.get_pressed()
        neymar.mover(teclas)

        # CALCULA A DISTANCIA ENTRE O NEYMAR E O ZAGUEIRO, EPOIS VOU ACESSAR PARA DECIDIR AS ESCOLHAS DOS ZAGUEIROS
        pos_neymar = pygame.math.Vector2(neymar.rect.center)
        pos_zagueiro = pygame.math.Vector2(zagueiro1.rect.center)

        distancia = pos_zagueiro.distance_to(pos_neymar)

        # MOVE O ZAGUEIRO NA DIRECAO DO NEYMAR
        if(distancia < 250):
            zagueiro1.perseguir(neymar)
        
        # DESENHA A COR DO GRAMADO
        tela.fill(COR_GRAMADO)
        
        # DESENHANDO AS LINHAS DO CAMPO
        
        #LINHA DO MEIO DE CAMPO
        posicao_y_meio_campo = ALTURA_TELA - 5
        pygame.draw.line(tela, COR_LINHA, (0, posicao_y_meio_campo), (LARGURA_TELA, posicao_y_meio_campo), 3)
        
        # ARCO DO MEIO DE CAMPO (A MEIA LUA)
        pygame.draw.arc(tela, COR_LINHA, (ARCO_X, ARCO_Y, LARGURA_ARCO, ALTURA_ARCO), 0, math.pi, 3)
        
        # LINHA DE FUNDO
        pygame.draw.line(tela, COR_LINHA, (0, POS_GOL_Y), (LARGURA_TELA, POS_GOL_Y), 3)
        
        # DESENHANDO A GRANDE AREA
        pygame.draw.rect(tela, COR_LINHA, (POSICAO_X_AREA, POS_GOL_Y, LARGURA_AREA, ALTURA_AREA), 3)
        
        # DESENHANDO O GOL, NO CASO AS SUAS TRAVES
        pygame.draw.rect(tela, COR_TRAVE, (POS_GOL_X, POS_GOL_Y - ALTURA_GOL, LARGURA_GOL, ALTURA_GOL), 4)
        
        # O NEYMAR AQUI AGORA É DESENHADO POR CIMA DO GRAMADO
        tela.blit(zagueiro1.image, zagueiro1.rect)
        tela.blit(neymar.image, neymar.rect)
        
        # AQUI ATUALIZA O JOGO COM TUDO QUE ESTÁ DESENHADO NAQUELE MOMENTO
        pygame.display.flip()
        
        # JOGO RODANDO A 30 FPS
        relogio.tick(FPS)

    # FECHA O JOGO
    pygame.quit()
    sys.exit()

# começa o jogo aqui
if __name__ == '__main__':
    main()
            
        
        
        