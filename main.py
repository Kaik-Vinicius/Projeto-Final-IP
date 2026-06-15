# =-=-=-=-= ARQUIVO MAIN TEMPORARIO =-=-=-=-=
import pygame
import sys
import math
import ctypes 
from gerenciamento.constants import *
from entidades.neymar import Neymar  
from entidades.zagueiro import Zagueiro
from entidades.aliado import Aliado
from entidades.bola import Bola
from gerenciamento.funcoes_importantes import *
import random
from entidades.coletaveis import Coletavel
from interface.menu import MenuInicial, MenuDificuldade
from interface.pause import BotaoPause, MenuPause

def main():
    # ISSO DAQUI TIRA O ZOOM DO SISTEMA NOS PC's com proporcao 16:10, MAS AINDA ASSIM NAO FICA TAO BOM
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except:
        pass
  
    # =-=-=-=-=-=-=-=-=-=-=
    # INICIAÇÃO DO JOGO
    pygame.init()
    
    # CRIA A TELA UTILIZANDO A FLAG 'pygame.SCALED'
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA), pygame.SCALED)
    pygame.display.set_caption("Neymar Jr: The Last Dance")

    # ADICIONANDO OS MENUS E INTERFACES
    menu_inicial = MenuInicial(LARGURA_TELA, ALTURA_TELA)
    menu_dificuldade = MenuDificuldade(LARGURA_TELA, ALTURA_TELA)
    botao_pause = BotaoPause(LARGURA_TELA, ALTURA_TELA)
    menu_pause = MenuPause(LARGURA_TELA, ALTURA_TELA)


    # CONTROLE DE ESCALA DO SPRITE DO CAMPO
    campo_original = pygame.image.load("assets/campo/campo_1280x1080.png").convert()
    campo_jogo = pygame.transform.smoothscale(campo_original, (LARGURA_CAMPO_JOGAVEL, ALTURA_CAMPO_JOGAVEL))
  
    CAMPO_X = OFFSET_X
    CAMPO_Y = 0


    # ESTADO INICIAL DO JOGO
    estado = "menu"


    #ESTADO DA DIFICULDADE INICIAL DO JOGO
    dificuldade = None
  
    # RELOGIO DO FPS DO JOGO
    relogio = pygame.time.Clock()
    
    neymar = Neymar() # CRIA O NEYMAR COMO OBJETO
    zagueiro1 = Zagueiro(400, 300)
    
    rodando = True
    while rodando:
      
        # REGISTRA EVENTO POR EVENTO DO JOGO
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
        
        # DESENHA A COR DO GRAMADO
        tela.fill(COR_GRAMADO)
        
        # DESENHANDO AS LINHAS DO CAMPO
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
        
        # AQUI ATUALIZA O JOGO COM TUDO QUE ESTÁ DESENHADO NAQUELE MOMENTO
        pygame.display.flip()
        relogio.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()