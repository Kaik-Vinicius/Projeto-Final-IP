import pygame

class AliadoAnimado:
    def __init__(self):
        # CARREGA OS FRAMES DE FRENTE
        self.frames_idle = [
            pygame.image.load("assets/jogadores/aliado_brasil/idle_frente1.png").convert_alpha(),
            pygame.image.load("assets/jogadores/aliado_brasil/idle_frente2.png").convert_alpha(),
            pygame.image.load("assets/jogadores/aliado_brasil/idle_frente3.png").convert_alpha(),
            pygame.image.load("assets/jogadores/aliado_brasil/idle_frente4.png").convert_alpha(),
        ]
        
        # CARREGA O SPRITE DA SOMBRA
        self.sombra_horizontal = pygame.image.load("assets/jogadores/sombra_jogador_horizontal.png").convert_alpha()
        
        # CONTROLES DO LOOP DE ANIMAÇÃO
        self.lista_atual = self.frames_idle
        self.frame_atual = 0
        self.velocidade_animacao = 180  # ms
        self.ultimo_update = pygame.time.get_ticks()

    def obter_imagem_inicial(self):
        """Retorna o primeiro frame para o setup do sprite"""
        return self.lista_atual[self.frame_atual]

    def atualizar_animacao(self):
        """Atualiza o relógio interno e retorna o frame correto do jogador"""
        tempo_atual = pygame.time.get_ticks()
        
        # Mantém parado de frente e com a sombra horizontal ativa
        self.lista_atual = self.frames_idle
        
        if tempo_atual - self.ultimo_update > self.velocidade_animacao:
            self.ultimo_update = tempo_atual
            self.frame_atual += 1
            
            if self.frame_atual >= len(self.lista_atual):
                self.frame_atual = 0
                
        return self.lista_atual[self.frame_atual]