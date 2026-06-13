# =-=-=-=-= ARQUIVO MAIN TEMPORARIO PARA TESTES =-=-=-=-=
import pygame
import sys
import math
from constants import *
from neymar import Neymar   
from zagueiro import Zagueiro
from aliado import Aliado
from bola import Bola
import random
from coletaveis import Coletavel
from interface.menu import MenuInicial
from interface.pause import BotaoPause, MenuPause

def main():
    
    pygame.init()
    
    # CRIA A TELA DO JOGO 
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Neymar Jr: The Last Dance")

    #ADICIONANDO O MENU INICIAL
    menu_inicial = MenuInicial(LARGURA_TELA, ALTURA_TELA)

    #ADICIONANDO O BOTAO DE PAUSE
    botao_pause = BotaoPause(LARGURA_TELA, ALTURA_TELA)

    #ADICIONANDO O MENU DE PAUSE
    menu_pause = MenuPause(LARGURA_TELA, ALTURA_TELA)

    #ADICIONANDO O CAMPO:
    campo_jogo=pygame.image.load("assets/campo/campo_1280x1080.png").convert()
    CAMPO_X = (LARGURA_TELA - 1280) // 2
    CAMPO_Y = 0

    #ADICIONANDO O ESTADO DO JOGO, INICIALMENTE ELE VAI COMEÇAR NO MENU
    estado = "menu"
    
    # RELOGIO DO FPS DO JOGO
    relogio = pygame.time.Clock()
    
    neymar = Neymar() # CRIA O NEYMAR COMO OBJETO
    zagueiro1 = Zagueiro(720, 300)#AUMENTEI EM 320 O X PARA NAO SPAWNAR FORA DO CAMPO
    
    # COLOCANDO CADA ALIADO EM UM GRUPO
    aliado_1 = Aliado(620, 500)#AUMENTEI EM 320 O X PARA NAO SPAWNAR FORA DO CAMPO
    grupo_aliados = pygame.sprite.Group()
    grupo_aliados.add(aliado_1)
    
    # INSTANCIA A BOLA
    bola = Bola()
    
    # DE ONDE A BOLA VEM E DE ONDE INICIA SEU LANÇAMENTO
    bola.iniciar_lancamento(LARGURA_TELA // 2, ALTURA_TELA, LARGURA_TELA // 2, ALTURA_TELA - 250, velocidade_lancamento=6)
    
    grupo_coletaveis = pygame.sprite.Group() # REMOVI A BOLA DO GRUPOS DOS COLETAVEIS QUE NICHOLAS FEZ, SO VAI TER A CHUTEIRA E A ESTRELA
    tempo_ultima_chuteira = 0
    zagueiro1 = Zagueiro(720, 300)#AUMENTEI EM 320 O X PARA NAO SPAWNAR FORA DO CAMPO
    
    rodando = True
    while rodando:
        
        # VERIFICA SE EU NAO FECHEI A JANELA
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                
            #VERIFICA SE O ESTADO DO JOGO FOR MENU    
            if estado == "menu":
                acao= menu_inicial.tratar_eventos(evento)

                #SE A AÇÃO FOR JOGAR, ENTÃO O ESTADO DO JOGO MUDA PARA JOGANDO
                if acao == "jogar":
                    estado = "jogando"

                #ADICIONANDO A AÇÃO DE QUITAR O JOGO
                elif acao == "quit":
                    rodando = False

            #SE ESTADO FOR JOGANDO, VERIFICA OS EVENTOS
            elif estado == "jogando":
                # SE O EVENTO FOR ALGUMA TECLA PRESSIONADA
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE: # SE FOR PRA ELE CHUTAR
                        neymar.chutar_pro_gol(bola)
                    
                    elif evento.key == pygame.K_f: # SE FOR PRA ELE DAR O PASSE
                        neymar.dar_passe(bola, grupo_aliados)

                # VERIFICA SE O EVENTO FOI DE CLICAR NO BOTAO DE PAUSE
                acao_pause = botao_pause.tratar_eventos(evento)
                if acao_pause == "pause":
                    estado = "pause"
        
        #SE O ESTADO DO JOGO FOR JOGANDO, ENTÃO ELE VAI ATUALIZAR AS LÓGICAS DE JOGO
        if estado == "jogando":

            # MOVE O NEYMAR DENTRO DO JOGO
            teclas = pygame.key.get_pressed()
            neymar.mover(teclas)
            
            # ATUALIZA A POSIÇÃO DA BOLA DENTRO DO JOGO
            bola.atualizar_posicao(neymar)
            
            # ATUALIZA SEMPRE O RELÓGIO DOS ALIADOS
            for aliado in grupo_aliados:
                aliado.atualizar_cronometro(neymar, bola)
                
                # PEGA O TEMPO ATUAL DO JOGO PRA FAZER UMA COMPARAÇÃO
                # ISSO VAI EVITAR O RE-DOMINIO DO ALIADO
                tempo_atual = pygame.time.get_ticks()
                
                # ELE SO PEGA A BOLA SE ELA TIVER EM MOVIMENTO E SE NEM ELE E NEM O NEYMAR TIVER A BOLA
                if bola.em_movimento and not neymar.tem_bola and not aliado.tem_bola:
                    if tempo_atual - aliado.tempo_ultimo_passe > 500:
                        if bola.rect.colliderect(aliado.rect):
                            aliado.receber_bola()
                            # ZERA A VELOCIDADE DA BOLA PRA MOSTRAR QUE ELE DOMINOU A BOLA
                            bola.velocidade_x = 0
                            bola.velocidade_y = 0
                    
            # SE A BOLA COLIDIR COM O NEYMAR
            if neymar.rect.colliderect(bola.rect):
                # ELE SO DOMINA A BOLA SE ELE JA NAO TIVER COM A BOLA E SE NENHUM ALIADO A RETEM MAIS
                if not neymar.tem_bola and not any(aliado.tem_bola for aliado in grupo_aliados):
                    
                    # TEMPO ATUAL DO JOGO
                    tempo_atual = pygame.time.get_ticks()
                    
                    # ELE SO VAI PODER RE-DOMINAR
                    if tempo_atual - neymar.tempo_ultimo_passe > 500:
                        
                        # O NEY SO PODE DOMINAR A BOLA SE ELA JA PAROU OU SE TA VINDO DE UM PASSE (DOMINAR ELA NO AR)
                        if bola.no_chao_esperando or (bola.em_movimento and hasattr(bola, 'destino_x')):
                            
                        # DELETA OS DESTINOS ANTIGOS
                            if hasattr(bola, 'destino_x'):
                                del bola.destino_x
                                del bola.destino_y
                                
                            bola.dominar(neymar)

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
                if item.tipo == 'chuteira':
                    item.kill()
                    tempo_ultima_chuteira = pygame.time.get_ticks()
                elif item.tipo == 'estrela':
                    item.kill() # ******IMPLEMENTAR LOGICA DE PONTOS DA ESTRELA FUTURAMENTE
            
            # SPAWN DOS ITENS PERTO DO JOGADOR (FUTURAMENTE VAMOS PRECISAR REFORMULAR ESSA LOGICA PRA OS DRIBLES)
            if pygame.time.get_ticks() - tempo_ultima_chuteira > 2000:
                if not any(i.tipo == 'chuteira' for i in grupo_coletaveis):
                    
                    # Pega a posição exata do Neymar
                    pos_atual_neymar = neymar.rect.center
                    
                    # item nasce no raio proximo dele
                    grupo_coletaveis.add(Coletavel('chuteira', pos_atual_neymar))
                    
                    if random.random() < 0.3:
                        grupo_coletaveis.add(Coletavel('estrela', pos_atual_neymar))

        #VERIFICA SE APERTOU EM RETOMAR OU MENU INICIAL NO MENU DE PAUSE
        elif estado == "pause":
            acao_menu_pause = menu_pause.tratar_eventos(evento)
            if acao_menu_pause == "retomar":
                estado = "jogando"
            elif acao_menu_pause == "menu_inicial":
                estado = "menu"
        
        if estado == "menu":
            menu_inicial.desenhar(tela)
        
        #DESENHANDO O CAMPO
        elif estado == "jogando":
            tela.fill((0, 0, 0))
            tela.blit(campo_jogo, (CAMPO_X, CAMPO_Y))

            # DESENHO DOS ITENS
            grupo_coletaveis.draw(tela)
            
            # DESENHANDO AS LINHAS DO CAMPO
            #posicao_y_meio_campo = ALTURA_TELA - 5
            #pygame.draw.line(tela, COR_LINHA, (0, posicao_y_meio_campo), (LARGURA_TELA, posicao_y_meio_campo), 3) #LINHA DO MEIO DE CAMPO
            #pygame.draw.arc(tela, COR_LINHA, (ARCO_X, ARCO_Y, LARGURA_ARCO, ALTURA_ARCO), 0, math.pi, 3) # ARCO DO MEIO DE CAMPO (A MEIA LUA)
            #pygame.draw.line(tela, COR_LINHA, (0, POS_GOL_Y), (LARGURA_TELA, POS_GOL_Y), 3) # LINHA DE FUNDO
            #pygame.draw.rect(tela, COR_LINHA, (POSICAO_X_AREA, POS_GOL_Y, LARGURA_AREA, ALTURA_AREA), 3) # DESENHANDO A GRANDE AREA
            #pygame.draw.rect(tela, COR_TRAVE, (POS_GOL_X, POS_GOL_Y - ALTURA_GOL, LARGURA_GOL, ALTURA_GOL), 4) # DESENHANDO O GOL, NO CASO AS SUAS TRAVES
            
            # DESENHA O GRUPO DE ALIADOS NA TELA
            grupo_aliados.draw(tela)
            
            # O NEYMAR AQUI AGORA É DESENHADO POR CIMA DO GRAMADO
            tela.blit(zagueiro1.image, zagueiro1.rect)
            tela.blit(neymar.image, neymar.rect)
            
            # DESENHA A BOLA POR CIMA DO NEYMAR
            tela.blit(bola.image, bola.rect)

            # DESENHA O BOTAO DE PAUSE POR CIMA DE TUDO
            botao_pause.desenhar(tela)

        #DESENHANDO MENU DE PAUSE
        elif estado == "pause":
            menu_pause.desenhar(tela)
        
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
            
        
        
        