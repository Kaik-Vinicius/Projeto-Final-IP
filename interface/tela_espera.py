import pygame
from gerenciamento.constants import *

def desenhar_placar_superior(tela, fonte_pequena, chuteiras, estrelas, chances, confianca, asset_chuteira, asset_estrela, asset_brasil, asset_argentina, gols_brasil=0, gols_argentina=0):
    """
    DESENHA A BARRA TRANSLUCIDA COM AS INFORMAÇÕES DOS COLETAVEIS E DA CONFIANCA
    """
    
    # RENDERIZA COM OS VALORES ATUAIS
    txt_chuteiras = fonte_pequena.render(f"x{chuteiras}", True, (255, 255, 255))
    txt_estrelas = fonte_pequena.render(f"x{estrelas}", True, (255, 255, 255))
    txt_confianca = fonte_pequena.render(f"Confiança: {confianca}/100", True, (255, 255, 255))
    
    # DESENHA OS ICONES E OS TEXTOS NA POSICAO CORRETA
    inicial_x_chuteira = 220
    tela.blit(asset_chuteira, (inicial_x_chuteira, 10)) # POSICIONA O ICONE DA CHTEIRA
    
    # NUMERO DA CONTAGEM AO LADO DO ICONE
    pos_x_count_chuteira = inicial_x_chuteira + asset_chuteira.get_width() + 10
    tela.blit(txt_chuteiras, (pos_x_count_chuteira, 34))
    
    # DESENHA A ESTRELA NA POSICAO CORRETA
    inicial_x_estrela = pos_x_count_chuteira + txt_chuteiras.get_width() + 55
    tela.blit(asset_estrela, (inicial_x_estrela, 15)) 
    
    # NUMERO DA CONTAGEM
    pos_x_count_estrela = inicial_x_estrela + asset_estrela.get_width() + 3
    tela.blit(txt_estrelas, (pos_x_count_estrela, 34))
    
    pos_x_confianca = pos_x_count_estrela + txt_estrelas.get_width() + 45
    tela.blit(txt_confianca, (pos_x_confianca, 15))

    # BARRA DE CONFIANÇA ESTILIZADA

    barra_x = 500  
    barra_y = 40   
    largura_maxima = 160  
    altura_barra = 15     
    raio_borda = altura_barra // 2 
    
    # Borda Externa Preta e Fundo Cinza
    pygame.draw.rect(tela, (0, 0, 0), (barra_x - 2, barra_y - 2, largura_maxima + 4, altura_barra + 4), border_radius=raio_borda + 2)
    pygame.draw.rect(tela, (112, 128, 144), (barra_x, barra_y, largura_maxima, altura_barra), border_radius=raio_borda)
    
    # Cálculo do preenchimento da barra com base na confiança
    META_ESTRELA = 100 
    proporcao = min(confianca / META_ESTRELA, 1.0)
    largura_atual = int(largura_maxima * proporcao)
    
    if largura_atual > 0:
        tempo = pygame.time.get_ticks()
        
        deslocamento_fluxo = int(tempo * 0.03) % 16  

        # Definição das Cores
        if proporcao >= 1.0:
            cor_base = (218, 165, 32); cor_fluxo = (255, 235, 100); cor_brilho = (255, 255, 180)
        else:
            cor_base = (39, 174, 96); cor_fluxo = (46, 204, 113); cor_brilho = (163, 243, 191)
            
        # Superfície temporária para o miolo da barra
        surf_interna = pygame.Surface((largura_atual, altura_barra), pygame.SRCALPHA)
        
        # Evita que o conteúdo da barra vaze para fora da borda arredondada
        pygame.draw.rect(surf_interna, cor_base, (0, 0, largura_atual, altura_barra), border_radius=raio_borda)
        
        inicio_reto = raio_borda
        fim_reto = largura_atual - raio_borda
        
        if fim_reto > inicio_reto:
            for x_listra in range(inicio_reto - 16, fim_reto + 16, 16):
                x_animado = x_listra + deslocamento_fluxo
                
                # Só desenha a listra se ela estiver estritamente dentro do miolo reto da barra
                if x_animado >= inicio_reto and x_animado <= fim_reto:
                    pontos_fatia = [
                        (x_animado, 0), 
                        (x_animado + 4, 0),             
                        (x_animado + 1, altura_barra), 
                        (x_animado - 3, altura_barra)
                    ]
                    pygame.draw.polygon(surf_interna, cor_fluxo, pontos_fatia)
            
        tela.blit(surf_interna, (barra_x, barra_y))
        
        if largura_atual > 8:
            pygame.draw.rect(tela, cor_brilho, (barra_x + 4, barra_y + 2, largura_atual - 8, 3), border_radius=2)
    
    # ==== LADO DO PLACAR ====
    
    # RENDERIZA O TEXTO DOS GOLS INDIVIDUAIS
    txt_gols_br = fonte_pequena.render(f"{gols_brasil}", True, (255, 255, 255))
    txt_vs = fonte_pequena.render("x", True, (150, 150, 150)) # Um 'x' cinza discreto
    txt_gols_arg = fonte_pequena.render(f"{gols_argentina}", True, (255, 255, 255))
    
    # RECUAMOS 650 PIXELS PRA DESENHAR O PLACAR
    inicio_x_placar = tela.get_width() - 650
       
    # DESENHA O ESCUDO DO BRASIL
    tela.blit(asset_brasil, (inicio_x_placar, -5))
    
    # DESENHA OS GOLS DO BRASIL
    pos_x_gols_br = inicio_x_placar + asset_brasil.get_width() - 10
    tela.blit(txt_gols_br, (pos_x_gols_br, 30))
    
    # DESENHA O x QUE SEPARA OS GOLS
    pos_x_vs = pos_x_gols_br + txt_gols_br.get_width() + 15
    tela.blit(txt_vs, (pos_x_vs, 30))
    
    # DESENHA OS GOLS DA ARGENTINA
    pos_x_gols_arg = pos_x_vs + txt_vs.get_width() + 15
    tela.blit(txt_gols_arg, (pos_x_gols_arg, 30))
    
    # DESENHA O ESCUDO DA ARGENTINA
    pos_x_escudo_arg = pos_x_gols_arg + txt_gols_arg.get_width() 
    tela.blit(asset_argentina, (pos_x_escudo_arg, -6))

def desenhar_tela_espera(tela, campo_jogo, pos_campo, arquibancada_esquerda, arquibancada_direita, fonte_jogo, fonte_pequena, asset_chuteira, asset_estrela, asset_brasil, asset_argentina, chuteiras, estrelas, chances, confianca, minuto_atual, tempo_atual, botao_pause, gols_brasil=0, gols_argentina=0):
    """
    FUNCAO QUE DESENHA TODA A TELA DE ESPERA
    """
    # DESENHA O GRAMADO DE FUNDO
    tela.fill((20, 20, 20))
    tela.blit(campo_jogo, pos_campo) 
    
    # DESENHA AS ARQUIBANCADAS NA TELA
    tela.blit(arquibancada_esquerda,(CAMPO_X - LARGURA_ARQUIBANCADA, CAMPO_Y))
    tela.blit(arquibancada_direita, (CAMPO_X + LARGURA_CAMPO_JOGAVEL, CAMPO_Y))
            
    desenhar_placar_superior(tela, fonte_pequena, chuteiras, estrelas, chances, confianca, asset_chuteira, asset_estrela,asset_brasil, asset_argentina, gols_brasil, gols_argentina)
    
    # BARRA INFERIOR TRANSLLUCIDA DO TEMPO CONTANDO
    barra_inferior = pygame.Surface((tela.get_width(), 60), pygame.SRCALPHA)
    barra_inferior.fill((0, 0, 0, 180))
    tela.blit(barra_inferior, (0, tela.get_height() - 60))
    
    # BARRA DE CONFIANÇA ESTILIZADA

    barra_x = 500  
    barra_y = 40   
    largura_maxima = 160  
    altura_barra = 15     
    raio_borda = altura_barra // 2  # Cria o formato perfeito de cápsula/pílula
    
    # Borda Externa Preta e Fundo Cinza
    pygame.draw.rect(tela, (0, 0, 0), (barra_x - 2, barra_y - 2, largura_maxima + 4, altura_barra + 4), border_radius=raio_borda + 2)
    pygame.draw.rect(tela, (112, 128, 144), (barra_x, barra_y, largura_maxima, altura_barra), border_radius=raio_borda)
    
    # Cálculo do preenchimento da barra com base na confiança
    META_ESTRELA = 100 
    proporcao = min(confianca / META_ESTRELA, 1.0)
    largura_atual = int(largura_maxima * proporcao)
    
    if largura_atual > 0:
        tempo = pygame.time.get_ticks()
        
        deslocamento_fluxo = int(tempo * 0.03) % 16  

        # Definição das Cores
        if proporcao >= 1.0:
            cor_base = (218, 165, 32); cor_fluxo = (255, 235, 100); cor_brilho = (255, 255, 180)
        else:
            cor_base = (39, 174, 96); cor_fluxo = (46, 204, 113); cor_brilho = (163, 243, 191)
            
        # Superfície temporária para o miolo da barra
        surf_interna = pygame.Surface((largura_atual, altura_barra), pygame.SRCALPHA)
        
        # Evita que o conteúdo da barra vaze para fora da borda arredondada
        pygame.draw.rect(surf_interna, cor_base, (0, 0, largura_atual, altura_barra), border_radius=raio_borda)
        
        inicio_reto = raio_borda
        fim_reto = largura_atual - raio_borda
        
        if fim_reto > inicio_reto:
            for x_listra in range(inicio_reto - 16, fim_reto + 16, 16):
                x_animado = x_listra + deslocamento_fluxo
                
                # Só desenha a listra se ela estiver estritamente dentro do miolo reto da barra
                if x_animado >= inicio_reto and x_animado <= fim_reto:
                    pontos_fatia = [
                        (x_animado, 0), 
                        (x_animado + 4, 0),             
                        (x_animado + 1, altura_barra), 
                        (x_animado - 3, altura_barra)
                    ]
                    pygame.draw.polygon(surf_interna, cor_fluxo, pontos_fatia)
            
        tela.blit(surf_interna, (barra_x, barra_y))
        
        if largura_atual > 8:
            pygame.draw.rect(tela, cor_brilho, (barra_x + 4, barra_y + 2, largura_atual - 8, 3), border_radius=2)

    # RENDERIZA O RELOGIO CONTANDO
    txt_relogio = fonte_jogo.render(f"  {minuto_atual}' MIN", True, (255, 255, 255))
    tela.blit(txt_relogio, (20, tela.get_height() - 45))
    
    # EFEITO PISCANTE DA IMAGEM NA TELA
    if (tempo_atual // 500) % 2 == 0:
        if chances <= 0:
            txt_aguardando = fonte_pequena.render("SINALIZANDO FIM DE JOGO... AGUARDANDO APITO FINAL!", True, (255, 100, 100))
        else:
            txt_aguardando = fonte_pequena.render("AGUARDANDO OPORTUNIDADE DE ATAQUE...", True, (255, 255, 0))
        
        pos_x_texto = (tela.get_width() // 2) - (txt_aguardando.get_width() // 2)
        tela.blit(txt_aguardando, (pos_x_texto, tela.get_height() - 40))
    
    # DESENHA O BOTAO DE PAUSE POR CIMA 
    botao_pause.desenhar(tela)

def atualizar_logica_espera(tempo_atual, ultimo_tick_relogio, minuto_atual, 
                            minuto_proximo_ataque, oportunidades_restantes, intervalo_minuto_ms):
    """
    ATUALIZA TUDO DA TELA DE ESPERA
    """
    estado_atual = "espera"
    
    # SE PASSAR 90 MINUTOS O JOGO ACABA
    if minuto_atual >= 90:
        return "menu", minuto_atual, ultimo_tick_relogio
        
    # AQUI ACELERA O RELOGIO
    if oportunidades_restantes > 0:
        intervalo_dinamico = intervalo_minuto_ms
    else:
        intervalo_dinamico = 200 # PASSA MAIS RAPIDO SE NAO HOUVER CHANCES
        
    # ATUALIZA O PONTEIRO DOS MINUTOS
    if tempo_atual - ultimo_tick_relogio >= intervalo_dinamico:
        minuto_atual += 1
        ultimo_tick_relogio = tempo_atual
        
    # INICIACAO DO ATAQUE
    if minuto_atual >= minuto_proximo_ataque and oportunidades_restantes > 0:
        estado_atual = "jogando"
        
    return estado_atual, minuto_atual, ultimo_tick_relogio