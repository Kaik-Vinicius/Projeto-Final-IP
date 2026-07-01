import pygame

class ZagueiroAnimacao:
    def __init__(self):
        
        # =====================
        # FRAMES DELE PARADO
        # ====================
        
        # CARREGA OS FRAMES DE FRENTE
        self.frames_parado_frente = [
            pygame.image.load("assets/jogadores/zagueiro_arg/idle/frente/frente1.png").convert_alpha(),
            pygame.image.load("assets/jogadores/zagueiro_arg/idle/frente/frente2.png").convert_alpha(),
            pygame.image.load("assets/jogadores/zagueiro_arg/idle/frente/frente3.png").convert_alpha(),
            pygame.image.load("assets/jogadores/zagueiro_arg/idle/frente/frente4.png").convert_alpha(),
        ]
        
        # CARREGA OS FRAMES DE COSTAS
        self.frames_parado_esquerda = [
            pygame.image.load("assets/jogadores/zagueiro_arg/idle/esquerda/esquerda1.png").convert_alpha(),
            pygame.image.load("assets/jogadores/zagueiro_arg/idle/esquerda/esquerda2.png").convert_alpha(),
            pygame.image.load("assets/jogadores/zagueiro_arg/idle/esquerda/esquerda3.png").convert_alpha(),
            pygame.image.load("assets/jogadores/zagueiro_arg/idle/esquerda/esquerda4.png").convert_alpha(),
        ]

        self.frames_parado_direita = [
            pygame.image.load("assets/jogadores/zagueiro_arg/idle/direita/direita1.png").convert_alpha(),
            pygame.image.load("assets/jogadores/zagueiro_arg/idle/direita/direita2.png").convert_alpha(),
            pygame.image.load("assets/jogadores/zagueiro_arg/idle/direita/direita3.png").convert_alpha(),
            pygame.image.load("assets/jogadores/zagueiro_arg/idle/direita/direita4.png").convert_alpha(),
        ]

        # ============================
        # FRAMES ANIMADOS DELE CORRENDO 
        # ============================
        """self.frames_correndo_frente = [
            pygame.image.load('assets/jogadores/ney/ney_correndo/correndo_frente/correndo_frente1.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_correndo/correndo_frente/correndo_frente2.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_correndo/correndo_frente/correndo_frente3.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_correndo/correndo_frente/correndo_frente4.png').convert_alpha(),
        ]
        
        self.frames_correndo_costas = [
            pygame.image.load('assets/jogadores/ney/ney_correndo/correndo_costas/correndo_costas1.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_correndo/correndo_costas/correndo_costas2.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_correndo/correndo_costas/correndo_costas3.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_correndo/correndo_costas/correndo_costas4.png').convert_alpha(),
        ]
        
        self.frames_correndo_esquerda = [
            pygame.image.load('assets/jogadores/ney/ney_correndo/correndo_esquerda/correndo_esquerda1.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_correndo/correndo_esquerda/correndo_esquerda2.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_correndo/correndo_esquerda/correndo_esquerda3.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_correndo/correndo_esquerda/correndo_esquerda4.png').convert_alpha(),
        ]
        
        self.frames_correndo_direita = [
            pygame.image.load('assets/jogadores/ney/ney_correndo/correndo_direita/correndo_direita1.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_correndo/correndo_direita/correndo_direita2.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_correndo/correndo_direita/correndo_direita3.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_correndo/correndo_direita/correndo_direita4.png').convert_alpha(),
        ]"""
        
        # CARREGA O SPRITE DA SOMBRA
        self.sombra_horizontal = pygame.image.load("assets/jogadores/sombra_jogador_horizontal.png").convert_alpha()
        self.sombra_vertical = pygame.image.load("assets/jogadores/sombra_jogador_vertical.png").convert_alpha()
        
        # ESSA É A SOMBRA QUE INICIA
        self.sombra_atual = self.sombra_horizontal
        
        # VAI ANDAR PELA LISTA ATUAL
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
        
        # DEFINE QUAL LISTA VAI USAR DEPENDENDO DO MONITORAMENTO DO MOVIMENTO
        if not em_movimento:
            if olhando_para == "frente":
                self.lista_atual = self.frames_parado_frente
                self.sombra_atual = self.sombra_horizontal
            if olhando_para == 'direita':
                self.lista_atual = self.frames_parado_direita
                self.sombra_atual = self.sombra_vertical
            if olhando_para == 'esquerda':
                self.lista_atual = self.frames_parado_esquerda
                self.sombra_atual = self.sombra_vertical
        else:
            # ATIVA A ANIMAÇÃO DE CORRENDO PRA FRENTE
            if olhando_para == "frente":
                self.lista_atual = self.frames_correndo_frente
                self.sombra_atual = self.sombra_horizontal
            elif olhando_para == "direita":
                self.lista_atual = self.frames_correndo_direita
                self.sombra_atual = self.sombra_vertical
            elif olhando_para == "esquerda":
                self.lista_atual = self.frames_correndo_esquerda
                self.sombra_atual = self.sombra_vertical

        # LOGICA DO RELOGIO QUE ATUALIZA OS FRAMES
        if tempo_atual - self.ultimo_update > self.velocidade_animacao:
            self.ultimo_update = tempo_atual
            self.frame_atual += 1
            
            if self.frame_atual >= len(self.lista_atual):
                self.frame_atual = 0
                
        # RETORNA A IMAGEM QUE DEVE SER DESENHADA NESSE FRAME
        return self.lista_atual[self.frame_atual]