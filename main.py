# =-=-=-=-= ARQUIVO MAIN COM BUG DO 'GROUP' CORRIGIDO =-=-=-=-=
import pygame
import sys
import math
import ctypes  
from constants import *
from neymar import Neymar   
from zagueiro import Zagueiro
from aliado import Aliado
from bola import Bola
import random
from coletaveis import Coletavel
from interface.menu import MenuInicial
from interface.pause import BotaoPause, MenuPause

def evitar_zoom_do_sistema():
    """ Evita que o Windows aplique escala de 125% ou 150% e corte o jogo """
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except:
        pass 

def main():
    evitar_zoom_do_sistema()
    
    pygame.init()
    
    # CRIA A TELA UTILIZANDO A FLAG 'pygame.SCALED'
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA), pygame.SCALED)
    pygame.display.set_caption("Neymar Jr: The Last Dance")

    # ADICIONANDO OS MENUS E INTERFACES
    menu_inicial = MenuInicial(LARGURA_TELA, ALTURA_TELA)
    botao_pause = BotaoPause(LARGURA_TELA, ALTURA_TELA)
    menu_pause = MenuPause(LARGURA_TELA, ALTURA_TELA)

    # CONTROLE DE ESCALA DO SPRITE DO CAMPO
    campo_original = pygame.image.load("assets/campo/campo_1280x1080.png").convert()
    campo_jogo = pygame.transform.smoothscale(campo_original, (LARGURA_CAMPO_JOGAVEL, ALTURA_CAMPO_JOGAVEL))
    
    CAMPO_X = OFFSET_X
    CAMPO_Y = 0

    # ESTADO INICIAL DO JOGO
    estado = "menu"
    
    # RELOGIO DO FPS DO JOGO
    relogio = pygame.time.Clock()
    
    # INSTANCIANDO JOGADORES
    neymar = Neymar() 
    zagueiro1 = Zagueiro(OFFSET_X + 400, 300)
    
    aliado_1 = Aliado(OFFSET_X + 300, 500)
    grupo_aliados = pygame.sprite.Group()
    grupo_aliados.add(aliado_1)
    
    # INSTANCIA A BOLA
    bola = Bola()
    
    pos_x_inicial_bola = OFFSET_X + (LARGURA_CAMPO_JOGAVEL // 2)
    bola.iniciar_lancamento(pos_x_inicial_bola, ALTURA_CAMPO_JOGAVEL, pos_x_inicial_bola, ALTURA_CAMPO_JOGAVEL - 250, velocidade_lancamento=6)
    
    grupo_coletaveis = pygame.sprite.Group() 
    tempo_ultima_chuteira = 0
    
    rodando = True
    while rodando:
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                
            if estado == "menu":
                acao = menu_inicial.tratar_eventos(evento)
                if acao == "jogar":
                    estado = "jogando"
                elif acao == "quit":
                    rodando = False

            elif estado == "jogando":
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE: 
                        neymar.chutar_pro_gol(bola)
                    elif evento.key == pygame.K_f: 
                        neymar.dar_passe(bola, grupo_aliados)

                acao_pause = botao_pause.tratar_eventos(evento)
                if acao_pause == "pause":
                    estado = "pause"
        
        if estado == "jogando":
            teclas = pygame.key.get_pressed()
            neymar.mover(teclas)
            bola.atualizar_posicao(neymar)
            
            for aliado in grupo_aliados:
                aliado.atualizar_cronometro(neymar, bola)
                tempo_atual = pygame.time.get_ticks()
                
                if bola.em_movimento and not neymar.tem_bola and not aliado.tem_bola:
                    if tempo_atual - aliado.tempo_ultimo_passe > 500:
                        if bola.rect.colliderect(aliado.rect):
                            aliado.receber_bola()
                            bola.velocidade_x = 0
                            bola.velocidade_y = 0
                    
            # CORREÇÃO AQUI: Linha limpa e corrigida sem o "group" fantasma
            if neymar.rect.colliderect(bola.rect):
                if not neymar.tem_bola and not any(aliado.tem_bola for aliado in grupo_aliados):
                    tempo_atual = pygame.time.get_ticks()
                    if tempo_atual - neymar.tempo_ultimo_passe > 500:
                        if bola.no_chao_esperando or (bola.em_movimento and hasattr(bola, 'destino_x')):
                            if hasattr(bola, 'destino_x'):
                                del bola.destino_x
                                del bola.destino_y
                            bola.dominar(neymar)

            pos_neymar = pygame.math.Vector2(neymar.rect.center)
            pos_zagueiro = pygame.math.Vector2(zagueiro1.rect.center)
            distancia = pos_zagueiro.distance_to(pos_neymar)

            if distancia < 250:
                zagueiro1.perseguir(neymar)
            else:
                zagueiro1.idle()
            
            grupo_coletaveis.update()
            itens_tocados = pygame.sprite.spritecollide(neymar, grupo_coletaveis, False)
            for item in itens_tocados:
                if item.tipo == 'chuteira':
                    item.kill()
                    tempo_ultima_chuteira = pygame.time.get_ticks()
                elif item.tipo == 'estrela':
                    item.kill() 
            
            if pygame.time.get_ticks() - tempo_ultima_chuteira > 2000:
                if not any(i.tipo == 'chuteira' for i in grupo_coletaveis):
                    pos_atual_neymar = neymar.rect.center
                    grupo_coletaveis.add(Coletavel('chuteira', pos_atual_neymar))
                    
                    if random.random() < 0.3:
                        grupo_coletaveis.add(Coletavel('estrela', pos_atual_neymar))

        elif estado == "pause":
            acao_menu_pause = menu_pause.tratar_eventos(evento)
            if acao_menu_pause == "retomar":
                estado = "jogando"
            elif acao_menu_pause == "menu_inicial":
                estado = "menu"
        
        # RENDERIZAÇÃO
        if estado == "menu":
            menu_inicial.desenhar(tela)
        
        elif estado == "jogando":
            tela.fill((20, 20, 20))
            tela.blit(campo_jogo, (CAMPO_X, CAMPO_Y))

            grupo_coletaveis.draw(tela)
            grupo_aliados.draw(tela)
            
            tela.blit(zagueiro1.image, zagueiro1.rect)
            tela.blit(neymar.image, neymar.rect)
            tela.blit(bola.image, bola.rect)

            botao_pause.desenhar(tela)

        elif estado == "pause":
            menu_pause.desenhar(tela)
        
        pygame.display.flip()
        relogio.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()