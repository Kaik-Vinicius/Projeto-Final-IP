# =-=-=-=-= ARQUIVO MAIN TEMPORARIO PARA TESTES =-=-=-=-=
import pygame
import sys
from constants import LARGURA_TELA, ALTURA_TELA, COR_GRAMADO, FPS
from neymar import Neymar

def main():
    pygame.init()
    
    # CRIA A TELA DO JOGO 
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Neymar Simulator - Teste de Movimentação")
    
    # RELOGIO DO FPS DO JOGO
    relogio = pygame.time.Clock()
    
    neymar = Neymar() # CRIA O NEYMAR COMO OBJETO
    
    rodando = True
    while rodando:
        
        # VERIFICA SE EU NAO FECHEI A JANELA
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
        
        # MOVE O NEYMAR DENTRO DO JOGO
        teclas = pygame.key.get_pressed()
        neymar.mover(teclas)
        
        # DESENHA A COR DO GRAMADO
        tela.fill(COR_GRAMADO)
        
        # O NEYMAR AQUI AGORA É DESENHADO POR CIMA DO GRAMADO
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
            
        
        
        