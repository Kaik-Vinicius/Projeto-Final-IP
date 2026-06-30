import pygame

class NeymarAnimacao:
    def __init__(self):
        # CARREGA OS FRAMES DE FRENTE
        self.frames_parado_frente = [
            pygame.image.load("assets/jogadores/ney/ney_idle/idle_frente/idle_frente1.png").convert_alpha(),
            pygame.image.load("assets/jogadores/ney/ney_idle/idle_frente/idle_frente2.png").convert_alpha(),
            pygame.image.load("assets/jogadores/ney/ney_idle/idle_frente/idle_frente3.png").convert_alpha(),
            pygame.image.load("assets/jogadores/ney/ney_idle/idle_frente/idle_frente4.png").convert_alpha(),
            
        ]
        
        # CARREGA OS FRAMES DE COSTAS
        self.frames_parado_costas = [
           pygame.image.load("assets/jogadores/ney/ney_idle/idle_costas/idle_costas1.png").convert_alpha(),
           pygame.image.load("assets/jogadores/ney/ney_idle/idle_costas/idle_costas2.png").convert_alpha(),
           pygame.image.load("assets/jogadores/ney/ney_idle/idle_costas/idle_costas3.png").convert_alpha(),
           pygame.image.load("assets/jogadores/ney/ney_idle/idle_costas/idle_costas4.png").convert_alpha(),
        ]

        self.frames_parado_direita = [
            pygame.image.load("assets/jogadores/ney/ney_idle/idle_direita/idle_direita1.png").convert_alpha(),
            pygame.image.load("assets/jogadores/ney/ney_idle/idle_direita/idle_direita2.png").convert_alpha(),
            pygame.image.load("assets/jogadores/ney/ney_idle/idle_direita/idle_direita3.png").convert_alpha(),
            pygame.image.load("assets/jogadores/ney/ney_idle/idle_direita/idle_direita4.png").convert_alpha(),
        ]

        self.frames_parado_esquerda = [
            pygame.image.load("assets/jogadores/ney/ney_idle/idle_esquerda/idle_esquerda1.png").convert_alpha(),
            pygame.image.load("assets/jogadores/ney/ney_idle/idle_esquerda/idle_esquerda2.png").convert_alpha(),
            pygame.image.load("assets/jogadores/ney/ney_idle/idle_esquerda/idle_esquerda3.png").convert_alpha(),
            pygame.image.load("assets/jogadores/ney/ney_idle/idle_esquerda/idle_esquerda4.png").convert_alpha(),

        ]

        self.lista_atual = self.frames_parado_frente
        self.frame_atual = 0
        self.velocidade_animacao = 200 # ms
        self.ultimo_update = pygame.time.get_ticks()

    def obter_imagem_inicial(self):
        """Retorna o primeiro frame para o setup do sprite"""
        return self.lista_atual[self.frame_atual]

    def atualizar_animacao(self, em_movimento, olhando_para):
        """
        Recebe o estado atual do Neymar monitorado na movimentação 
        e atualiza a imagem correspondente.
        """
        tempo_atual = pygame.time.get_ticks()
        
        # Define qual lista usar baseada no monitoramento de movimento
        if not em_movimento:
            if olhando_para == "frente":
                self.lista_atual = self.frames_parado_frente
            if olhando_para == "costas":
                self.lista_atual = self.frames_parado_costas
            if olhando_para == 'direita':
                self.lista_atual = self.frames_parado_direita
            if olhando_para == 'esquerda':
                self.lista_atual = self.frames_parado_esquerda
        else:
            # DEPOIS IMPLEMENTAR OS SPRITES CORRENDO AQUI
            pass

        # LOGICA DO RELOGIO QUE ATUALIZA OS FRAMES
        if tempo_atual - self.ultimo_update > self.velocidade_animacao:
            self.ultimo_update = tempo_atual
            self.frame_atual += 1
            
            if self.frame_atual >= len(self.lista_atual):
                self.frame_atual = 0
                
        # RETORNA A IMAGEM QUE DEVE SER DESENHADA NESSE FRAME
        return self.lista_atual[self.frame_atual]