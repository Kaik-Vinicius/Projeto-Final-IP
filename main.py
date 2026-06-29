# =-=-=-=-= ARQUIVO MAIN INTEGRADO =-=-=-=-=
import pygame
import sys
import math
import ctypes 
from gerenciamento.constants import *
from entidades.neymar import Neymar  
from entidades.zagueiro import Zagueiro
from entidades.goleiro import Goleiro
from entidades.aliado import Aliado
from entidades.bola import Bola
from gerenciamento.funcoes_importantes import *
import random
from entidades.coletaveis import Coletavel
from interface.menu import MenuInicial, MenuDificuldade
from interface.pause import BotaoPause, MenuPause
from interface.tela_espera import desenhar_tela_espera, desenhar_placar_superior, atualizar_logica_espera

def main():
    # ISSO DAQUI TIRA O ZOOM DO SISTEMA NOS PC's com proporcao 16:10, MAS AINDA ASSIM NAO FICA TAO BOM
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except:
        pass
  
    # =-=-=-=-=-=-=-=-=-=-=
    # INICIAÇÃO DO JOGO
    pygame.init()
    #Fonte para o placar e cronometro
    fonte_pequena = pygame.font.SysFont("Arial", 20, bold=True)
    fonte_jogo = pygame.font.SysFont("Arial", 30, bold=True)
    
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
    estado_anterior = "menu"

    #ESTADO DA DIFICULDADE INICIAL DO JOGO
    dificuldade = None
  
    # RELOGIO DO FPS DO JOGO
    relogio = pygame.time.Clock()

    # Crônometro para a tela de espera
    minuto_atual, minuto_proximo_ataque, ultimo_tick_relogio, intervalo_minuto_ms = 0, 0, 0, 300
    #Oportunidades totais e restantes para cada dificuldade
    oportunidades_totais, oportunidades_restantes, tamanho_bloco, bloco_atual = 0, 0, 0, 0
    #Contadores para o placar
    chuteiras_coletadas, estrelas_coletadas = 0, 0
    
    gols_brasil = 0
    gols_argentina = 0

    # INSTANCIANDO JOGADORES
    neymar = Neymar()
    
    # GRUPOS DOS JOGADORES TÁTICOS
    grupo_zagueiros = pygame.sprite.Group()
    goleiro = Goleiro(960, 75)
    grupo_aliados = pygame.sprite.Group()
  
    # INSTANCIA A BOLA
    bola = Bola()
  
    grupo_coletaveis = pygame.sprite.Group()
    tempo_ultimo_drible_registrado = 0 
  
    rodando = True
    while rodando:

        tempo_atual = pygame.time.get_ticks()

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
                    oportunidades_totais = 5
                    gols_brasil = 0
                    gols_argentina = 0
                    
                elif acao == "medio":
                    dificuldade = "medio"
                    oportunidades_totais = 4
                    gols_brasil = 0
                    gols_argentina = 1

                elif acao == "dificil":
                    dificuldade = "dificil"
                    oportunidades_totais = 3
                    gols_brasil = 0
                    gols_argentina = 2

                if acao in ["facil", "medio", "dificil"]:
                    tamanho_bloco = 90 // oportunidades_totais
                    oportunidades_restantes = oportunidades_totais
                    bloco_atual = 0

                    #Sorteio da minutagem das oportunidades de gols
                    minuto_proximo_ataque = random.randint(2, tamanho_bloco - 2)

                    minuto_atual = 0
                    ultimo_tick_relogio = pygame.time.get_ticks()
                    estado = "espera"

            elif estado == "jogando":
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        neymar.chutar_pro_gol(bola)
                    elif evento.key == pygame.K_f:
                        neymar.dar_passe(bola, grupo_aliados)
                    
                    # MAPEANDO OS BOTOES DOS DRIBLES DO NEYMAR
                    elif evento.key == pygame.K_j:
                        neymar.driblar("pedalada", bola, grupo_zagueiros) 
                    elif evento.key == pygame.K_k:
                        neymar.driblar("360", bola, grupo_zagueiros)
                    elif evento.key == pygame.K_l:
                        neymar.driblar("lambreta", bola, grupo_zagueiros)

                acao_pause = botao_pause.tratar_eventos(evento)
                if acao_pause == "pause":
                    estado_anterior = estado
                    estado = "pause"

            elif estado == "espera":
                acao_pause = botao_pause.tratar_eventos(evento)
                if acao_pause == "pause":
                    estado_anterior = estado
                    estado = "pause"

        # LÓGICA PASSA DA TELA DE ESPERA
        if estado == "espera":
            proximo_estado, minuto_atual, ultimo_tick_relogio = atualizar_logica_espera(
                tempo_atual, ultimo_tick_relogio, minuto_atual, 
                minuto_proximo_ataque, oportunidades_restantes, intervalo_minuto_ms
            )
            
            # SE O JOGO ACABAR ELE FINALIZA E VOLTA PRA O MENU
            if minuto_atual >= 90:

                grupo_aliados.empty()
                grupo_coletaveis.empty()
                grupo_zagueiros.empty()
                neymar.tem_bola = False
                
                # ZERA OS GOLS =
                gols_brasil = 0
                gols_argentina = 0

                estado = 'menu'
                continue
            
            # INICIA A NOVA OPORTUNIDADE DE ATAQUE
            if proximo_estado == "jogando" and oportunidades_restantes > 0:
        
                lance_atual = (oportunidades_totais - oportunidades_restantes) + 1
                # SPAWNA OS NOVOS ALIADOS E ZAGUEIROS E LANÇA A BOLA DE LONGE
                preparar_nova_oportunidade(dificuldade, lance_atual, neymar, bola, grupo_zagueiros, grupo_aliados)
                estado = "jogando"
            
        # ATUALIZAÇÃO E FÍSICA ATIVA (JOGANDO)
        if estado == "jogando":
            teclas = pygame.key.get_pressed()
            neymar.mover(teclas, bola, grupo_zagueiros)
            bola.atualizar_posicao(neymar)
            
            # TIRA A BOLA DO ESTADO TRAVADO DE EM DRIBLE
            if neymar.bola_em_drible:
                if tempo_atual - neymar.tempo_inicio_drible > 400:
                    neymar.bola_em_drible = False
          
            # CHECA A SITUAÇÃO DE CADA ALIADO SEMPRE
            for aliado in grupo_aliados:
                aliado.atualizar_cronometro(neymar, bola)

            # RECEBIMENTO DA BOLA PELOS ALIADOS COM COLISÃO CONTÍNUA
            for aliado in grupo_aliados:
                if aliado.tem_bola or neymar.tem_bola:
                    continue

                if tempo_atual - aliado.tempo_ultimo_passe <= 500:
                    continue

                if bola.no_chao_esperando or bola.em_movimento:
                    if bola_tocou_jogador_continua(bola, aliado):
                        aliado.receber_bola()
                        bola.em_movimento = False
                        bola.no_chao_esperando = False
                        bola.velocidade_x = 0
                        bola.velocidade_y = 0
                        bola.rect.center = aliado.rect.center
                        break
                  
            # COLISÃO CONTÍNUA COM O NEYMAR
            if bola_tocou_jogador_continua(bola, neymar):
                if not neymar.tem_bola and not any(aliado.tem_bola for aliado in grupo_aliados):
                    if tempo_atual - neymar.tempo_ultimo_chute > 350: 
                        if tempo_atual - neymar.tempo_ultimo_passe > 500: 
                            if bola.no_chao_esperando or bola.em_movimento:
                                if hasattr(bola, 'destino_x'): del bola.destino_x
                                if hasattr(bola, 'destino_y'): del bola.destino_y
                                bola.dominar(neymar)
            
            # ATUALIZA TODOS OS ZAGUEIROS DE UMA VEZ SÓ
            atualizar_ia_zagueiros(grupo_zagueiros, neymar, bola, grupo_aliados) 
            goleiro.att_gol(neymar)

            # CHECA SE O NEYMAR TOMOU O CARRINHO OU NAO
            if verificar_desarme_zagueiros(grupo_zagueiros, bola, bola_tocou_jogador_continua):
                neymar.tem_bola = False
                bola.resultado_chute = None

                oportunidades_restantes -= 1
                bloco_atual += 1
                estado = "espera"
                ultimo_tick_relogio = tempo_atual

                if oportunidades_restantes > 0:
                    minuto_inicio_bloco = bloco_atual * tamanho_bloco
                    minuto_fim_bloco = minuto_inicio_bloco + tamanho_bloco
                    minuto_proximo_ataque = random.randint(minuto_inicio_bloco + 2, minuto_fim_bloco - 2)
            
            # DETECTA O DRIBLE E GERA A CHUTEIRA
            if getattr(neymar, 'drible_efetivo', False):
                if neymar.tempo_inicio_drible != tempo_ultimo_drible_registrado:
                    ultimo_drible = getattr(neymar, 'ultimo_tipo_drible', 'manual')
                    
                    if ultimo_drible == 'manual':
                        ganho_futuro = 5
                    elif ultimo_drible == 'pedalada':
                        ganho_futuro = 15
                    elif ultimo_drible == '360':
                        ganho_futuro = 25
                    elif ultimo_drible == 'lambreta':
                        ganho_futuro = 40
                    else:
                        ganho_futuro = 10 

                    confianca_atual = getattr(neymar, 'confianca', 0)
                    
                    if confianca_atual + ganho_futuro >= META_ESTRELA and not getattr(neymar, 'ney_prime', False):
                        if not any(i.tipo == 'estrela' for i in grupo_coletaveis):
                            grupo_coletaveis.add(Coletavel('estrela', pos_jogador=neymar.rect.center))
                    else:
                        nova_chuteira = Coletavel('chuteira', pos_jogador=neymar.rect.center)
                        nova_chuteira.valor_recompensa = ganho_futuro 
                        grupo_coletaveis.add(nova_chuteira)
                        
                    tempo_ultimo_drible_registrado = neymar.tempo_inicio_drible
            
            # ISSO DAQUI VAI TIRAR A BOLA DO ESTADO TRAVADO DE EM DRIBLE
            if neymar.bola_em_drible:
                if tempo_atual - neymar.tempo_inicio_drible > 400:
                    neymar.bola_em_drible = False
                    neymar.drible_efetivo = False

            # DETECTA A CONFIANÇA 100% E GERA A ESTRELA (SISTEMA TEMPORÁRIO QUE DEPOIS VAI SER MUDADO)
            if getattr(neymar, 'confianca', 0) >= META_ESTRELA:
                if not any(i.tipo == 'estrela' for i in grupo_coletaveis) and not getattr(neymar, 'ney_prime', False):
                    grupo_coletaveis.add(Coletavel('estrela', pos_jogador=neymar.rect.center))

            # LÓGICA DE PEGAR OS ITENS
            grupo_coletaveis.update()
            itens_tocados = pygame.sprite.spritecollide(neymar, grupo_coletaveis, False)
            
            for item in itens_tocados:
                if item.tipo == 'chuteira':
                    item.kill()
                    neymar.atualizar_confianca(item.valor_recompensa) 
                    chuteiras_coletadas += 1 
                elif item.tipo == 'estrela':
                    item.kill() 
                    estrelas_coletadas += 1 
                    neymar.ney_prime = True
                    neymar.tempo_prime = pygame.time.get_ticks()
                    neymar.confianca = 0 

            if getattr(neymar, 'ney_prime', False):
                if pygame.time.get_ticks() - getattr(neymar, 'tempo_prime', 0) > 7000:
                    neymar.ney_prime = False

            # DETECTA SE FOI GOL OU JOGADA PERDIDA NA LINHA DE FUNDO
            if checar_conclusao_jogada(bola):
                if bola.resultado_chute == 'gol':
                    gols_brasil += 1

                bola.resultado_chute = None

                oportunidades_restantes -= 1
                bloco_atual += 1
                estado = "espera"
                ultimo_tick_relogio = tempo_atual

                if oportunidades_restantes > 0:
                    minuto_inicio_bloco = bloco_atual * tamanho_bloco
                    minuto_fim_bloco = minuto_inicio_bloco + tamanho_bloco
                    minuto_proximo_ataque = random.randint(minuto_inicio_bloco + 2, minuto_fim_bloco - 2)
                    
        elif estado == "pause":
            acao_menu_pause = menu_pause.tratar_eventos(evento)
            if acao_menu_pause == "retomar":
                estado = estado_anterior
            elif acao_menu_pause == "menu_inicial":
                estado = "menu"

        # RENDERIZAÇÃO (DESENHO DOS ELEMENTOS GRÁFICOS)
        if estado == "menu":
            menu_inicial.desenhar(tela)

        elif estado == "dificuldade":
            menu_dificuldade.desenhar(tela)

        elif estado == "espera":
            desenhar_tela_espera(
                tela, campo_jogo, (CAMPO_X, CAMPO_Y), fonte_jogo, fonte_pequena,
                chuteiras_coletadas, estrelas_coletadas, oportunidades_restantes,
                minuto_atual, tempo_atual, botao_pause, gols_brasil, gols_argentina
            )

        elif estado == "jogando":
           
            tela.fill((20, 20, 20))
            tela.blit(campo_jogo, (CAMPO_X, CAMPO_Y))

            grupo_coletaveis.draw(tela)
            grupo_aliados.draw(tela)
            grupo_zagueiros.draw(tela) 
            
            tela.blit(neymar.image, neymar.rect)
            tela.blit(goleiro.image, goleiro.rect)
            tela.blit(bola.image, bola.rect)
            desenhar_placar_superior(tela, fonte_pequena, chuteiras_coletadas, estrelas_coletadas, oportunidades_restantes, gols_brasil, gols_argentina)
            
            # HUD DE TESTES VISUALIZADOR DE CONFIANÇA 
            confianca_atual = int(getattr(neymar, 'confianca', 0)) 
            texto_confianca = fonte_pequena.render(f"Confiança: {confianca_atual}/100", True, (255, 255, 255)) 
            tela.blit(texto_confianca, (CAMPO_X + 20, 100))

            botao_pause.desenhar(tela)

        elif estado == "pause":
            menu_pause.desenhar(tela)
      
        pygame.display.flip()
        relogio.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()