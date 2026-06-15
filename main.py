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
      
        # REGISTRA EVENTO POR EVENTO DO JOGO
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
          
            # SE APERTAR EM MENU ELE ABRE O MENU DO JOGO
            if estado == "menu":
                acao = menu_inicial.tratar_eventos(evento)
                if acao == "jogar":
                    estado = "dificuldade"
                elif acao == "quit":
                    rodando = False
          
            #SELECIONANDO AS DIFICULDADES DO JOGO
            elif estado == "dificuldade":
                acao = menu_dificuldade.tratar_eventos(evento)

                if acao == "facil":
                    dificuldade = "facil"
                    estado = "jogando"

                elif acao == "medio":
                    dificuldade = "medio"
                    estado = "jogando"

                elif acao == "dificil":
                    dificuldade = "dificil"
                    estado = "jogando"

            elif estado == "jogando":
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        neymar.chutar_pro_gol(bola)
                    elif evento.key == pygame.K_f:
                        neymar.dar_passe(bola, grupo_aliados)

                acao_pause = botao_pause.tratar_eventos(evento)
                if acao_pause == "pause":
                    estado = "pause"

        # SE O ESTADO FOR JOGANDO, VAI SEGUIR O FLUXO NORMALMENTE DO JOGO
        if estado == "jogando":
            teclas = pygame.key.get_pressed()
            neymar.mover(teclas)
            bola.atualizar_posicao(neymar)
            tempo_atual = pygame.time.get_ticks()
          
            # CHECA A SITUAÇÃO DE CADA ALIADO SEMPRE
            for aliado in grupo_aliados:
                aliado.atualizar_cronometro(neymar, bola)

            tempo_atual = pygame.time.get_ticks()

            # RECEBIMENTO DA BOLA PELOS ALIADOS COM COLISÃO CONTÍNUA
            for aliado in grupo_aliados:

                # SE ELE JA TIVR COM A BOLA NAO PODE DOMINAR ELA
                if aliado.tem_bola:
                    continue

                # SE O NEY TEM BOLA O ZAGUEIRO NAO PODE DOMINAR A BOLA
                if neymar.tem_bola:
                    continue

                # EVITA QUE A BOLA FIQUE PRESA NELE
                if tempo_atual - aliado.tempo_ultimo_passe <= 500:
                    continue

                # bola parada ou em movimento
                if bola.no_chao_esperando or bola.em_movimento:

                    if bola_tocou_jogador_continua(bola, aliado):

                        aliado.receber_bola()

                        bola.em_movimento = False
                        bola.no_chao_esperando = False

                        bola.velocidade_x = 0
                        bola.velocidade_y = 0

                        # VAI DEIXAR A BOLA EXATAMENTE NO CENTRO DO ALIADO
                        bola.rect.center = aliado.rect.center

                        break
                  
            # COLISÃO CONTÍNUA COM O NEYMAR
            if bola_tocou_jogador_continua(bola, neymar):

                # SO DOMINA SE NENHUM ALIADO TIVER SEGURANDO A BOLA
                if not neymar.tem_bola and not any(aliado.tem_bola for aliado in grupo_aliados):

                    tempo_atual = pygame.time.get_ticks()

                    # TRAVA O RE-DOMINIO DA BOLA
                    if tempo_atual - neymar.tempo_ultimo_passe > 500:

                        if bola.no_chao_esperando or bola.em_movimento:

                            if hasattr(bola, 'destino_x'):
                                del bola.destino_x

                            if hasattr(bola, 'destino_y'):
                                del bola.destino_y

                            bola.dominar(neymar)
                          
            # ISSO DAQUI É O SISTEMA PRA O ZAGUEIRO MEIO QUE PERSEGUIR O NEYMAR
            pos_neymar = pygame.math.Vector2(neymar.rect.center)
            pos_bola = pygame.math.Vector2(bola.rect.center)
            pos_zagueiro = pygame.math.Vector2(zagueiro1.rect.center)
            distancia_neymar = pos_zagueiro.distance_to(pos_neymar)
            distancia_bola = pos_zagueiro.distance_to(pos_bola)
          
            # CONDICIONAL QUE FAZ O ZAGUEIRO PERSEGUIR O NEYMAR
            zagueiro1.atualizar(neymar, bola, distancia_neymar, distancia_bola, any(aliado.tem_bola for aliado in grupo_aliados))

            # ========================
            # DEFINE AQUI O GRUPO DOS COLETAVEIS
            # ========================
            #OBS.: TIREI A "bola" PQ ELA PRECISOU SER PROGRAMADA A PARTE
          
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

        elif estado == "dificuldade":
            menu_dificuldade.desenhar(tela)
      
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
