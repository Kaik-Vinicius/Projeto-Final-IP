# =-=-=-=-= ARQUIVO MAIN TEMPORARIO PARA TESTES =-=-=-=-=
import pygame
import sys
import math
from constants import *
from neymar import Neymar   
from zagueiro import Zagueiro
from aliado import Aliado
import random
from coletaveis import Coletavel

def main():
    pygame.init()
    
    # CRIA A TELA DO JOGO 
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Neymar Jr - Rumo ao Hexa 2026")
    
    # RELOGIO DO FPS DO JOGO
    relogio = pygame.time.Clock()
    
    neymar = Neymar() # CRIA O NEYMAR COMO OBJETO
    aliado1 = Aliado(300, 500) # POSICIONA O ALIADO APENAS PRA VER ELE NA TELA
    zagueiro1 = Zagueiro()
    
    grupo_coletaveis = pygame.sprite.Group()
    grupo_coletaveis.add(Coletavel('bola'))
    tempo_ultima_chuteira = 0
    zagueiro1 = Zagueiro(400, 300)
    
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
        else:
            zagueiro1.idle()

        #logica dos itens coletaveis
        grupo_coletaveis.update()
        itens_tocados = pygame.sprite.spritecollide(neymar, grupo_coletaveis, False)
        for item in itens_tocados:
            if item.tipo == 'bola':
                neymar.tem_bola = True
                item.kill()
            elif item.tipo == 'chuteira':
                item.kill()
                tempo_ultima_chuteira = pygame.time.get_ticks()
            elif item.tipo == 'estrela':
                item.kill()
        
        
        if pygame.time.get_ticks() - tempo_ultima_chuteira > 2000:
            if not any(i.tipo == 'chuteira' for i in grupo_coletaveis):
                
                # Pega a posição exata do Neymar
                pos_atual_neymar = neymar.rect.center
                
                # item nasce no raio proximo dele
                grupo_coletaveis.add(Coletavel('chuteira', pos_atual_neymar))
                
                if random.random() < 0.3:
                    grupo_coletaveis.add(Coletavel('estrela', pos_atual_neymar))
        
        # DESENHA A COR DO GRAMADO
        tela.fill(COR_GRAMADO)

        # DESENHO DOS ITENS
        grupo_coletaveis.draw(tela)
        
        # DESENHANDO AS LINHAS DO CAMPO
        #LINHA DO MEIO DE CAMPO
        posicao_y_meio_campo = ALTURA_TELA - 5
        pygame.draw.line(tela, COR_LINHA, (0, posicao_y_meio_campo), (LARGURA_TELA, posicao_y_meio_campo), 3)
        
        # ARCO DO MEIO DE CAMPO (A MEIA LUA)
        pygame.draw.arc(tela, COR_LINHA, (ARCO_X, ARCO_Y, LARGURA_ARCO, ALTURA_ARCO), 0, math.pi, 3)
        
        # LINHA DE FUNDO
        pygame.draw.line(tela, COR_LINHA, (0, POS_GOL_Y), (LARGURA_TELA, POS_GOL_Y), 3)
        pygame.draw.line(tela, COR_LINHA, (60, POS_GOL_Y), (60, ALTURA_TELA), 3)
        pygame.draw.line(tela, COR_LINHA, (1300, POS_GOL_Y), (1300, ALTURA_TELA), 3)
        
        # DESENHANDO A GRANDE AREA
        pygame.draw.rect(tela, COR_LINHA, (POSICAO_X_AREA, POS_GOL_Y, LARGURA_AREA, ALTURA_AREA), 3)
        
        # DESENHANDO O GOL, NO CASO AS SUAS TRAVES
        pygame.draw.rect(tela, COR_TRAVE, (POS_GOL_X, POS_GOL_Y - ALTURA_GOL, LARGURA_GOL, ALTURA_GOL), 4)
        
        # O NEYMAR AQUI AGORA É DESENHADO POR CIMA DO GRAMADO
        tela.blit(zagueiro1.image, zagueiro1.rect)
        tela.blit(neymar.image, neymar.rect)
        tela.blit(aliado1.image, aliado1.rect)
        
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
            
        
        
        