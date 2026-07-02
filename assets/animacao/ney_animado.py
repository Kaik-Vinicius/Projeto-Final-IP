import pygame
import random

class NeymarAnimacao:
    def __init__(self):
        
        # =====================
        # FRAMES DELE PARADO
        # ====================
        
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
        
        # ============================
        # FRAMES ANIMADOS DELE CORRENDO 
        # ============================
        self.frames_correndo_frente = [
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
        ]
        
        # ==================
        # FRAMES DOS DRIBLES DELE
        # ===================
        
        # FRAMES DA PEDALADA
        self.frames_pedalada_direita = [
            pygame.image.load('assets/jogadores/ney/ney_driblando/pedalada/pedalada_direita/pedaladadireita1.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_driblando/pedalada/pedalada_direita/pedaladadireita2.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_driblando/pedalada/pedalada_direita/pedaladadireita3.png').convert_alpha(),
        ]
        
        self.frames_pedalada_esquerda = [
            pygame.image.load('assets/jogadores/ney/ney_driblando/pedalada/pedalada_esquerda/pedaladaesquerda1.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_driblando/pedalada/pedalada_esquerda/pedaladaesquerda2.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_driblando/pedalada/pedalada_esquerda/pedaladaesquerda3.png').convert_alpha(),
        ]
        
        # GIRO 360
        self.giro_360 = [
            pygame.image.load('assets/jogadores/ney/ney_driblando/360/360_1.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_driblando/360/360_2.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_driblando/360/360_3.png').convert_alpha(),
            pygame.image.load('assets/jogadores/ney/ney_driblando/360/360_4.png').convert_alpha(),
        ]
        
        # ===============
        # FRAMES DA COROA 
        # ===============
        self.frames_coroa = [
            pygame.image.load("assets/jogadores/ney/prime/coroa_prime1.png").convert_alpha(),
            pygame.image.load("assets/jogadores/ney/prime/coroa_prime2.png").convert_alpha(),
            pygame.image.load("assets/jogadores/ney/prime/coroa_prime3.png").convert_alpha(),
        ]

        self.frame_coroa_atual = 0
        self.ultimo_update_coroa = pygame.time.get_ticks()
        self.velocidade_coroa = 150 # Velocidade do "brilho" da coroa em ms
        
        # CARREGA O SPRITE DA SOMBRA
        self.sombra_horizontal = pygame.image.load("assets/jogadores/sombra_jogador_horizontal.png").convert_alpha()
        self.sombra_vertical = pygame.image.load("assets/jogadores/sombra_jogador_vertical.png").convert_alpha()
        
        
        # ATRIBUTOS DOS DRIBLES
        self.em_drible = False
        self.drible_encerrado = False
        
        # ESSA É A SOMBRA QUE INICIA
        self.sombra_atual = self.sombra_horizontal
        
        # VAI ANDAR PELA LISTA ATUAL
        self.lista_atual = self.frames_parado_frente
        self.frame_atual = 0
        self.velocidade_animacao = 0 # ms
        self.ultimo_update = pygame.time.get_ticks()
    
    def iniciar_animacao_pedalada(self, olhando_para):
        """ATIVA A ANIMAÇÃO DA PEDALADA"""
        self.em_drible = True
        self.drible_encerrado = False
        self.frame_atual = 0
        self.ultimo_update = pygame.time.get_ticks()
        self.velocidade_animacao = 80

        if olhando_para in ['direita', 'esquerda']:
            direcao_final = olhando_para
        else:
            # SE NAO ESTIVER OLHANDO PRA OS LADOS ESCOLHE ALEATORIAMENTE
            direcao_final = random.choice(['direita', 'esquerda'])

        if direcao_final == 'direita':
            self.lista_atual = self.frames_pedalada_direita
            self.sombra_atual = self.sombra_vertical
        else:
            self.lista_atual = self.frames_pedalada_esquerda
            self.sombra_atual = self.sombra_vertical
    
    def iniciar_animacao_360(self):
        """ATIVA OS FRAMES DA ANIMAÇÃO DO 360"""
        self.em_drible = True
        self.drible_encerrado = False
        self.frame_atual = 0
        self.ultimo_update = pygame.time.get_ticks()
        self.velocidade_animacao = 80 
        
        self.lista_atual = self.giro_360
        self.sombra_atual = self.sombra_vertical 
        
    def atualizar_animacao_coroa(self):
        """ATUALIZA A ANIMAÇÃO DA COROA"""
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.ultimo_update_coroa > self.velocidade_coroa:
            self.ultimo_update_coroa = tempo_atual
            self.frame_coroa_atual = (self.frame_coroa_atual + 1) % len(self.frames_coroa)
        
        return self.frames_coroa[self.frame_coroa_atual]
    
    
    def obter_imagem_inicial(self):
        """RETORNA O PRIMEIRO FRAME PRA O SETUP DA ANIMAÇÃO"""
        return self.lista_atual[self.frame_atual]

    def atualizar_animacao(self, em_movimento, olhando_para):
        """
        RECEBE O ESTADO ATUAL DO NEYMAR MONITORANDO SUA MOVIMENTAÇÃO
        """
        tempo_atual = pygame.time.get_ticks()
        
        # SE ESTIVER EM DRIBLE, IGNORA A MOVIMENTAÇÃO PADRÃO ATÉ ACABAR OS FRAMES
        if self.em_drible:
            if tempo_atual - self.ultimo_update > self.velocidade_animacao:
                self.ultimo_update = tempo_atual
                self.frame_atual += 1
                
                # SE PASSOU DO ULTIMO FRAME ENCERRA A PEDALADA
                if self.frame_atual >= len(self.lista_atual):
                    self.frame_atual = 0
                    self.em_drible = False
                    self.drible_encerrado = True
            
            return self.lista_atual[self.frame_atual]
        
        # DEFINE QUAL LISTA VAI USAR DEPENDENDO DO MONITORAMENTO DO MOVIMENTO
        if not em_movimento:
            if olhando_para == "frente":
                self.lista_atual = self.frames_parado_frente
                self.sombra_atual = self.sombra_horizontal
            if olhando_para == "costas":
                self.lista_atual = self.frames_parado_costas
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
            elif olhando_para == "costas":
                self.lista_atual = self.frames_correndo_costas
                self.sombra_atual = self.sombra_horizontal
            elif olhando_para == "direita":
                self.lista_atual = self.frames_correndo_direita
                self.sombra_atual = self.sombra_vertical
            elif olhando_para == "esquerda":
                self.lista_atual = self.frames_correndo_esquerda
                self.sombra_atual = self.sombra_vertical


        # LOGICA DO RELOGIO QUE ATUALIZA OS FRAMES
        
        # SE FOR CORRENDO TEM QUE ATUALIZAR MAIS RAPIDO
        if self.lista_atual == self.frames_correndo_costas or self.lista_atual == self.frames_correndo_frente or self.lista_atual == self.frames_correndo_direita or self.lista_atual == self.frames_correndo_esquerda:
            
            self.velocidade_animacao = 50
        
        # SE FOR PARADO É MAIS DEVAGAR
        else: 
            self.velocidade_animacao = 200
        
        if tempo_atual - self.ultimo_update > self.velocidade_animacao:
            self.ultimo_update = tempo_atual
            self.frame_atual += 1
            
            if self.frame_atual >= len(self.lista_atual):
                self.frame_atual = 0
                
        # RETORNA A IMAGEM QUE DEVE SER DESENHADA NESSE FRAME
        return self.lista_atual[self.frame_atual]