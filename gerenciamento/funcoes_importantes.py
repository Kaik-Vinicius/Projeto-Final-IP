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
        
    
    