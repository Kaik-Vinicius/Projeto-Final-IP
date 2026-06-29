import pygame

def desenhar_placar_superior(tela, fonte_pequena, chuteiras, estrelas, chances, gols_brasil=0, gols_argentina=0):
    """
    Desenha a barra preta do topo e as informações de itens coletados, lances e o Placar Real.
    Compartilhada entre a tela de espera e a tela de jogo ativo.
    """
    # Cria e desenha a barra superior escura semi-transparente
    barra_superior = pygame.Surface((tela.get_width(), 50), pygame.SRCALPHA)
    barra_superior.fill((0, 0, 0, 160)) 
    tela.blit(barra_superior, (0, 0))
    
    # Renderiza os textos com os valores atuais
    txt_chuteiras = fonte_pequena.render(f"  Chuteiras: {chuteiras}", True, (255, 255, 255))
    txt_estrelas = fonte_pequena.render(f"  Estrelas: {estrelas}", True, (255, 255, 255))
    txt_chances = fonte_pequena.render(f"  Chances Restantes: {chances}", True, (255, 215, 0))
    
    # --- NOVO: PLACAR CENTRALIZADO ---
    # Renderiza o placar clássico BRA x ARG
    texto_placar = f"BRA {gols_brasil} x {gols_argentina} ARG"
    txt_placar = fonte_pequena.render(texto_placar, True, (255, 255, 255))
    
    # Calcula o X centralizado exato na tela
    pos_x_placar = (tela.get_width() // 2) - (txt_placar.get_width() // 2)
    # ---------------------------------

    # Desenha os textos nas posições corretas
    tela.blit(txt_chuteiras, (20, 15))
    tela.blit(txt_estrelas, (200, 15))
    tela.blit(txt_placar, (pos_x_placar, 15)) # Placar bem no centro
    tela.blit(txt_chances, (tela.get_width() - 380, 15))

def desenhar_tela_espera(tela, campo_jogo, pos_campo, fonte_jogo, fonte_pequena, 
                         chuteiras, estrelas, chances, minuto_atual, tempo_atual, botao_pause,
                         gols_brasil=0, gols_argentina=0): # === ADICIONADO OS PARÂMETROS DE GOLS ===
    """
    Função responsável por renderizar todo o visual da Tela de Espera Passiva.
    Isola o código para manter o arquivo main.py limpo.
    """
    # Desenha o gramado de fundo
    tela.fill((20, 20, 20))
    tela.blit(campo_jogo, pos_campo) 
    
    # Reaproveita a função modificada para desenhar o placar completo na tela de espera também!
    desenhar_placar_superior(tela, fonte_pequena, chuteiras, estrelas, chances, gols_brasil, gols_argentina)
    
    # Barra inferior translúcida do Cronômetro
    barra_inferior = pygame.Surface((tela.get_width(), 60), pygame.SRCALPHA)
    barra_inferior.fill((0, 0, 0, 180))
    tela.blit(barra_inferior, (0, tela.get_height() - 60))
    
    # Renderiza o relógio
    txt_relogio = fonte_jogo.render(f"  {minuto_atual}' MIN", True, (255, 255, 255))
    tela.blit(txt_relogio, (20, tela.get_height() - 45))
    
    # Efeito piscante inteligente da mensagem inferior
    if (tempo_atual // 500) % 2 == 0:
        if chances <= 0:
            txt_aguardando = fonte_pequena.render("SINALIZANDO FIM DE JOGO... AGUARDANDO APITO FINAL!", True, (255, 100, 100))
        else:
            txt_aguardando = fonte_pequena.render("AGUARDANDO OPORTUNIDADE DE ATAQUE...", True, (255, 255, 0))
        
        pos_x_texto = (tela.get_width() // 2) - (txt_aguardando.get_width() // 2)
        tela.blit(txt_aguardando, (pos_x_texto, tela.get_height() - 40))
    
    # Desenha o botão de pause por cima da barra superior
    botao_pause.desenhar(tela)

def atualizar_logica_espera(tempo_atual, ultimo_tick_relogio, minuto_atual, 
                            minuto_proximo_ataque, oportunidades_restantes, intervalo_minuto_ms):
    """
    Processa toda a lógica do relógio e transição de turnos da tela de espera.
    Retorna uma tupla com: (novo_estado, novo_minuto, novo_ultimo_tick)
    """
    estado_atual = "espera"
    
    # Se passou de 90 minutos, encerra a partida
    if minuto_atual >= 90:
        print("Fim do jogo!")
        return "menu", minuto_atual, ultimo_tick_relogio
        
    # AQUI ACELERA O RELOGIO
    if oportunidades_restantes > 0:
        intervalo_dinamico = intervalo_minuto_ms
    else:
        intervalo_dinamico = 200 # Passa mais rápido se não houver chances
        
    # Atualiza o ponteiro dos minutos
    if tempo_atual - ultimo_tick_relogio >= intervalo_dinamico:
        minuto_atual += 1
        ultimo_tick_relogio = tempo_atual
        
    # Gatilho para iniciar o ataque
    if minuto_atual >= minuto_proximo_ataque and oportunidades_restantes > 0:
        estado_atual = "jogando"
        
    return estado_atual, minuto_atual, ultimo_tick_relogio