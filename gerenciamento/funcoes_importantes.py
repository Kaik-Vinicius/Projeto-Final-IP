import math
# =-=-=-=-=--=-= FUNCAO QUE PRENDE O NEY NO CAMPO =-=-=-=-=-=-=-=-=-=
def prender_neymar_campo(neymar, campo_jogavel):
    neymar.rect.clamp_ip(campo_jogavel)
    

# =-=-=-=-=--=-= FUNCAO QUE VAI RETONAR SE A BOLA COLIDIU COM O JOGADOR =-=-=-=-=-=-=-=-=-=
def bola_tocou_jogador_continua(bola, jogador):
    """
    EXPANDE BEM A HITBOX DA BOLA E DO JOGADOR E EVITA QUE O JOGAGOR ACABE NAO DOMINANDO A BOLA
    """
    bola_expandida = bola.rect.inflate(bola.rect.width, bola.rect.height)
    if bola_expandida.colliderect(jogador.rect):
        return True

    jogador_expandidado = jogador.rect.inflate(bola.rect.width, bola.rect.height)
    return bool(
        jogador_expandidado.clipline(
            (int(bola.prev_center.x), int(bola.prev_center.y)),
            bola.rect.center))
        
def direcao_bola(origem_x, origem_y):
    esquerdax = 870 - origem_x
    esquerday = 70 - origem_y
    direitax= 1050 - origem_x
    direitay= 70 - origem_y
    distancia_esquerda = math.hypot(esquerdax, esquerday)
    distancia_direita = math.hypot(direitax, direitay)
    if distancia_esquerda > distancia_direita:        
        direcaox = direitax / distancia_direita
        direcaoy = direitay / distancia_direita
        return direcaox, direcaoy
    elif distancia_direita > distancia_esquerda:
        direcaox = esquerdax / distancia_esquerda
        direcaoy = esquerday / distancia_esquerda
        return direcaox, direcaoy
    else:
        return 0.0, -1.0