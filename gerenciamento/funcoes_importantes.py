import math
import pygame
import random
from entidades.zagueiro import Zagueiro
from entidades.aliado import Aliado
from gerenciamento.constants import *

def prender_neymar_campo(neymar, campo_jogavel):
    """
    PRENDE O NEYMAR NO CAMPO BASEADO APENAS NOS PÉS
    """
    x_campo, y_campo, largura_campo, altura_campo = campo_jogavel

    # CALCULA OS LIMITES DO CAMPO
    x_min = x_campo
    x_max = x_campo + largura_campo
    y_min = y_campo
    y_max = altura_campo

    # PEGA A POSICAO ATUAL DOS PES DO NEYMAR
    pes_x, pes_y = neymar.rect.midbottom

    # TRAVA NO EIXO X
    if pes_x < x_min:
        pes_x = x_min
    elif pes_x > x_max:
        pes_x = x_max

    # TRAVA NO EIXO Y
    if pes_y < y_min:
        pes_y = y_min
    elif pes_y > y_max:
        pes_y = y_max

    # APLICA A NOVA POSICAO TRAVADA NOS PES
    neymar.rect.midbottom = (pes_x, pes_y)

def limpar_campo(neymar, grupo_aliados, grupo_zagueiros, grupo_coletaveis):
    """
    RESETA TUDO E LIMPA O CAMPO PRA EVITAR QUE O JOGO FIQUE PUXANDO INFORMAÇÕES DE OUTRAS PARTIDAS ANTERIORES
    """
    grupo_aliados.empty()
    grupo_coletaveis.empty()
    grupo_zagueiros.empty()
    
    # RESET TOTAL DO OBJETO NEYMAR 
    neymar.tem_bola = False
    neymar.confianca = 0
    neymar.ney_prime = False
    neymar.velocidade = VELOCIDADE_NEY
    neymar.bola_em_drible = False
    neymar.drible_efetivo = False
    neymar.ultimo_tipo_drible = 'manual'
    
    return 0,0,0,0,0 # RETORNO DAS CHUTEIRAS, ESTRELAS, GOLS DO BRASIL E ARGENTINA E TEMPO DO ULTIMO DRIBLE

def colisao_coletavel_customizada(jogador, coletavel):
    """
    CRIA UMA HITBOX MENOR PRA O NEYMAR COLIDIR COM OS ITENS DE FORMA MAIS NORMAL
    """
    hitbox_menor = jogador.rect.inflate(-30, -40)
    
    return hitbox_menor.colliderect(coletavel.rect)


def bola_tocou_jogador_continua(bola, jogador):
    """
    CHECA A COLISÃO DA BOLA COM O JOGADOR.
    SE A BOLA ESTIVER PARADA, A HITBOX FICA NORMAL OU REDUZIDA.
    SE ESTIVER EM MOVIMENTO, USA A EXPANÇÃO CONTÍNUA PARA EVITAR GLITCHES.
    """
    # 1. CASO A BOLA ESTEJA PARADA NO CHÃO ESPERANDO
    if getattr(bola, 'no_chao_esperando', False) or (bola.velocidade_x == 0 and bola.velocidade_y == 0):
        # Reduzimos um pouco o retângulo da bola (ex: tira 4 pixels de cada lado) para ficar bem justa
        hitbox_bola_parada = bola.rect.inflate(-30, -30)
        return hitbox_bola_parada.colliderect(jogador.rect)

    # 2. CASO A BOLA ESTEJA EM MOVIMENTO (Mantém a lógica contínua original)
    bola_expandida = bola.rect.inflate(bola.rect.width, bola.rect.height)
    if bola_expandida.colliderect(jogador.rect):
        return True

    jogador_expandido = jogador.rect.inflate(bola.rect.width, bola.rect.height)
    return bool(
        jogador_expandido.clipline(
            (int(bola.prev_center.x), int(bola.prev_center.y)),
            bola.rect.center
        )
    )

def atualizar_ia_zagueiros(grupo_zagueiros, neymar, bola, grupo_aliados):
    """
    CALCULA A DISTANCIA A ATUALIZA O COMPORTAMENTO DE TODOS OS ZAGUEIROS DO GRUPO
    """
    pos_neymar = pygame.math.Vector2(neymar.rect.center)
    pos_bola = pygame.math.Vector2(bola.rect.center)
    alguem_com_aliado = any(aliado.tem_bola for aliado in grupo_aliados)

    for zag in grupo_zagueiros:
        pos_zagueiro = pygame.math.Vector2(zag.rect.center)
        distancia_neymar = pos_zagueiro.distance_to(pos_neymar)
        distancia_bola = pos_zagueiro.distance_to(pos_bola)
        
        zag.atualizar(neymar, bola, distancia_neymar, distancia_bola, alguem_com_aliado)


def verificar_desarme_zagueiros(grupo_zagueiros, bola, bola_tocou_jogador_continua):
    """
    VERIFICA SE ALGUM ZAGUEIRO EM CARRINHO CONSEGUIU DESARMAR A BOLA
    """
    for zag in grupo_zagueiros:
        # SE O ZAGUEIRO ESTA EM CARRINHO E SE A COLISAO DELE ESTA ATIVA
        if zag.frames_do_dash > 0 and zag.colisao_ativa():
            # SE COLIDIU COM A BOLA
            if bola_tocou_jogador_continua(bola, zag) or bola.rect.colliderect(zag.rect):
                print("TRAVOU! Um dos zagueiros desarmou o Neymar com um carrinho perfeito!")
                return True
                
    return False


def checar_conclusao_jogada(bola, neymar):
    """
    VERIFICA SE A BOLA PASSOU DA LINHA DE FUNDO, SE FOI GOL OU NAO
    """
    
    if (bola.rect.centerx < 280 or
        bola.rect.centerx > 1640 or
        bola.rect.centery > 1090 or
        (bola.rect.centery < 65 and getattr(bola, 'resultado_chute', None) is None)):

        bola.resultado_chute = 'fora'
        return True
        

    if bola.em_movimento and getattr(bola, 'resultado_chute', None) is not None:
        
        # DEFINE O LIMITE DA PARADA DA BOLA CONFORME OS PIXELS
        if bola.resultado_chute == 'gol': # se foi gol ela bola vai um pouco mais pra dentro
            limite_parada_y = 35
        else:
            limite_parada_y = 50
            
        if bola.rect.centery <= limite_parada_y:
            
            if bola.resultado_chute == 'gol':
                # GANHA +20 DE CONFIANCA SE FIZER UM GOL
                neymar.atualizar_confianca(20)
                print("GOOOOOL DO NEYMAR!!!") 
            elif bola.resultado_chute == 'defesa':
                print("MILAGRE DO GOLEIRO! CHANCE PERDIDA!")
            elif bola.resultado_chute == 'fora':
                print("PRA FOOOOOORA! MANDOU LONGE!")
                
            return True 
            
    return False 


def preparar_nova_oportunidade(dificuldade, indice_lance, neymar, bola, grupo_zagueiros, grupo_aliados):
    """
    FUNÇÃO QUE PREPARA NOVA OPORTUNIDADE, LIMPA O CAMPO E POSICIONA TUDO AONDE DEVE ESTAR
    """
    # SEGURANÇA PRA EVITAR ERROS SE A STRING VIER NULA
    if dificuldade not in CENARIOS_TATICOS:
        dificuldade = "facil"
        
    cenarios_do_nivel = CENARIOS_TATICOS[dificuldade]
    
    # DEFININDO OS LANCES POR INDICE A COMECAR DO 1 PRA FACILITAR NA COMPARAÇÃO
    if indice_lance not in cenarios_do_nivel:
        indice_lance = 1
        
    cenario = cenarios_do_nivel[indice_lance]
    print(f"\n--- INICIANDO LANCE {indice_lance}: {cenario['nome']} ---")

    # REPOSICIONA O NEYMAR NO PROXIMO CENARIO DE JOGADA
    neymar.rect.center = cenario["neymar_pos"]
    neymar.tem_bola = False

    # JOGA A BOLA DA ORIGEM ATE O DESTINO DELA
    origem_x, origem_y = cenario["bola_origem"]
    destino_x, destino_y = cenario["bola_destino"]
    
    bola.iniciar_lancamento(origem_x, origem_y, destino_x, destino_y, VELOCIDADE_LANCAMENTO_INICIAL)

    # RECRIA OS ZAGUEIROS NA NOVA OPORTUNIDADE
    grupo_zagueiros.empty()
    for pos in cenario["zagueiros_pos"]:
        novo_zag = Zagueiro(pos[0], pos[1])
        grupo_zagueiros.add(novo_zag)

    # RECRIA OS ALIADOS NA NOVA OPORTUNIDADE
    grupo_aliados.empty()
    for pos in cenario["aliados_pos"]:
        novo_aliado = Aliado(pos[0], pos[1])
        grupo_aliados.add(novo_aliado)