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
        self.frames_correndo_frente = [
            pygame.image.load('assets/jogadores/zagueiro_arg/correndo/frente/frente1.png').convert_alpha(),
            pygame.image.load('assets/jogadores/zagueiro_arg/correndo/frente/frente2.png').convert_alpha(),
            pygame.image.load('assets/jogadores/zagueiro_arg/correndo/frente/frente3.png').convert_alpha(),
        ]
        
        self.frames_correndo_esquerda = [
            pygame.image.load('assets/jogadores/zagueiro_arg/correndo/esquerda/esquerda1.png').convert_alpha(),
            pygame.image.load('assets/jogadores/zagueiro_arg/correndo/esquerda/esquerda2.png').convert_alpha(),
            pygame.image.load('assets/jogadores/zagueiro_arg/correndo/esquerda/esquerda3.png').convert_alpha(),
        ]
        
        self.frames_correndo_direita = [
            pygame.image.load('assets/jogadores/zagueiro_arg/correndo/direita/direita1.png').convert_alpha(),
            pygame.image.load('assets/jogadores/zagueiro_arg/correndo/direita/direita2.png').convert_alpha(),
            pygame.image.load('assets/jogadores/zagueiro_arg/correndo/direita/direita3.png').convert_alpha(),
        ]

        self.frames_bote_esquerda = [
            pygame.image.load('assets/jogadores/zagueiro_arg/bote/bote_esquerda/bote_esquerda1.png').convert_alpha(),
            pygame.image.load('assets/jogadores/zagueiro_arg/bote/bote_esquerda/bote_esquerda2.png').convert_alpha(),
            pygame.image.load('assets/jogadores/zagueiro_arg/bote/bote_esquerda/bote_esquerda3.png').convert_alpha(),
        ]

        self.frames_bote_direita = [
            pygame.image.load('assets/jogadores/zagueiro_arg/bote/bote_direita/bote1.png').convert_alpha(),
            pygame.image.load('assets/jogadores/zagueiro_arg/bote/bote_direita/bote2.png').convert_alpha(),
            pygame.image.load('assets/jogadores/zagueiro_arg/bote/bote_direita/bote3.png').convert_alpha(),
        ]
        
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

    def atualizar_animacao(self, em_movimento, olhando_para, em_preparo=False, em_dash=False, atordoado=False):
        tempo_atual = pygame.time.get_ticks()
        lista_anterior = self.lista_atual

        # 1. ESTADOS DE BOTE (PREPARO, DASH OU ATORDOADO)
        if em_preparo or em_dash or atordoado:
            # Força a lista de bote baseada na direção (se for frente, escolhe direita como padrão)
            if olhando_para == 'esquerda':
                self.lista_atual = self.frames_bote_esquerda
            else:
                self.lista_atual = self.frames_bote_direita
                
            self.sombra_atual = self.sombra_vertical

            # Se for PREPARO, roda a animação dos 3 sprites
            if em_preparo:
                if self.lista_atual != lista_anterior:
                    self.frame_atual = 0
                    self.ultimo_update = tempo_atual

                if tempo_atual - self.ultimo_update > 166:
                    self.ultimo_update = tempo_atual
                    self.frame_atual += 1
                
                if self.frame_atual > 2:
                    self.frame_atual = 2
            
            # Se for DASH ou ATORDOADO, trava estritamente no último frame (2)
            else:
                self.frame_atual = 2

        # 2. MOVIMENTAÇÃO PADRÃO (CORRIDA / IDLE)
        else:
            if not em_movimento:
                if olhando_para == "frente":
                    self.lista_atual = self.frames_parado_frente
                    self.sombra_atual = self.sombra_horizontal
                elif olhando_para == 'direita':
                    self.lista_atual = self.frames_parado_direita
                    self.sombra_atual = self.sombra_vertical
                elif olhando_para == 'esquerda':
                    self.lista_atual = self.frames_parado_esquerda
                    self.sombra_atual = self.sombra_vertical
            else:
                if olhando_para == "frente":
                    self.lista_atual = self.frames_correndo_frente
                    self.sombra_atual = self.sombra_horizontal
                elif olhando_para == "direita":
                    self.lista_atual = self.frames_correndo_direita
                    self.sombra_atual = self.sombra_vertical
                elif olhando_para == "esquerda":
                    self.lista_atual = self.frames_correndo_esquerda
                    self.sombra_atual = self.sombra_vertical

            if self.lista_atual != lista_anterior:
                self.frame_atual = 0

            if tempo_atual - self.ultimo_update > self.velocidade_animacao:
                self.ultimo_update = tempo_atual
                self.frame_atual += 1

        # Validação final de segurança para o índice
        if self.frame_atual >= len(self.lista_atual) or self.frame_atual < 0:
            if em_dash or atordoado:
                self.frame_atual = 2
            else:
                self.frame_atual = 0
                
        try:
            return self.lista_atual[self.frame_atual]
        except IndexError:
            self.frame_atual = 0
            return self.lista_atual[0]