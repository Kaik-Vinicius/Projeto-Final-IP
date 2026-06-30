import pygame

class NeymarAnimacao:
    def __init__(self):
        # 1. Carrega os frames de frente
        self.frames_parado_frente = [
            pygame.image.load("assets/jogadores/ney/ney_idle/idle frente/idle frente1.png").convert_alpha(),
            pygame.image.load("assets/jogadores/ney/ney_idle/idle frente/idle frente2.png").convert_alpha(),
            pygame.image.load("assets/jogadores/ney/ney_idle/idle frente/idle frente3.png").convert_alpha(),
            pygame.image.load("assets/jogadores/ney/ney_idle/idle frente/idle frente4.png").convert_alpha(),
        ]
        
        # 2. Carrega os frames de costas
        self.frames_parado_costas = [
           pygame.image.load("assets/jogadores/ney/ney_idle/idle costas/idle costas1.png").convert_alpha(),
           pygame.image.load("assets/jogadores/ney/ney_idle/idle costas/idle costas2.png").convert_alpha(),
           pygame.image.load("assets/jogadores/ney/ney_idle/idle costas/idle costas3.png").convert_alpha(),
           pygame.image.load("assets/jogadores/ney/ney_idle/idle costas/idle costas4.png").convert_alpha(),
        ]
        
        # Estado Inicial
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
        tempo_actual = pygame.time.get_ticks()
        
        # Define qual lista usar baseada no monitoramento de movimento
        if not em_movimento:
            if olhando_para == "frente":
                self.lista_atual = self.frames_parado_frente
            if olhando_para == "costas":
                self.lista_atual = self.frames_parado_costas
        else:
            # Se futuramente tiver animação de corrida, a troca de listas entra aqui!
            pass

        # Lógica do relógio para mudar o frame
        if tempo_actual - self.ultimo_update > self.velocidade_animacao:
            self.ultimo_update = tempo_actual
            self.frame_atual += 1
            
            if self.frame_atual >= len(self.lista_atual):
                self.frame_atual = 0
                
        # Retorna a imagem exata que deve ser desenhada nesse milissegundo
        return self.lista_atual[self.frame_atual]