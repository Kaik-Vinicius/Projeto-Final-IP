import pygame
import math
import random


class Bola(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # ADICIONANDO OS SPRITES DA BOLA
        self.frames_bola = [
            pygame.image.load("assets/bola/bola1.png").convert_alpha(),
            pygame.image.load("assets/bola/bola2.png").convert_alpha(),
            pygame.image.load("assets/bola/bola3.png").convert_alpha(),
            pygame.image.load("assets/bola/bola4.png").convert_alpha()
        ]

        # Ajusta o tamanho da bola
        self.frames_bola = [
            pygame.transform.scale(frame, (16, 16))
            for frame in self.frames_bola
        ]
        
        self.frame_atual = 0
        self.image = self.frames_bola[self.frame_atual]
        self.rect = self.image.get_rect()

        self.tempo_ultima_animacao = 0
        self.intervalo_animacao = 80

        # CONTROLE DO MOVIMENTO
        self.velocidade_x = 0.0
        self.velocidade_y = 0.0

        # ESTADOS DA BOLA
        self.em_movimento = False
        self.no_chao_esperando = False

        # DONO ATUAL DA BOLA (NEYMAR OU ALIADO)
        self.dono = None

        # PRECISÃO DECIMAL
        self.px = 0.0
        self.py = 0.0

        # POSIÇÃO DO FRAME ANTERIOR PARA COLISÃO CONTÍNUA
        self.prev_center = pygame.math.Vector2(self.rect.center)

        # DESTINO EXPLÍCITO
        self.tem_destino = False
        self.destino_x = None
        self.destino_y = None
        
        # ATRIBUTO QUE DIZ O RESULTADO DO CHUTE
        self.resultado_chute = None

        # DICIONARIOS DOS OFFSETS PADRÃO (PARADO)
        self.offsets_posse = {
            "frente":   (32, 80),
            "costas":   (32, 75),
            "esquerda": (10, 75),
            "direita":  (50, 75)   
        }

    def sincronizar_coordenadas_float(self):
        self.px = float(self.rect.x)
        self.py = float(self.rect.y)

    def _registrar_prev_center(self):
        self.prev_center.update(self.rect.centerx, self.rect.centery)

    def _limpar_destino(self):
        self.tem_destino = False
        self.destino_x = None
        self.destino_y = None

    def animar(self):
        centro_atual = self.rect.center
        if not self.em_movimento:
            self.frame_atual = 0
            self.image = self.frames_bola[self.frame_atual]
            self.rect = self.image.get_rect(center=centro_atual)
            return

        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.tempo_ultima_animacao > self.intervalo_animacao:
            self.tempo_ultima_animacao = tempo_atual
            if self.velocidade_x < 0: self.frame_atual -= 1
            else: self.frame_atual += 1
            self.frame_atual %= len(self.frames_bola)
            self.image = self.frames_bola[self.frame_atual]
            self.rect = self.image.get_rect(center=centro_atual)

    def iniciar_lancamento(self, x_inicial, y_inicial, x_destino, y_destino, velocidade_lancamento):
        self.dono = None
        self.rect.centerx = x_inicial
        self.rect.centery = y_inicial
        self.sincronizar_coordenadas_float()
        self._registrar_prev_center()
        self.destino_x = x_destino
        self.destino_y = y_destino
        self.tem_destino = True
        self.em_movimento = True
        self.no_chao_esperando = False
        dx = x_destino - x_inicial
        dy = y_destino - y_inicial
        angulo = math.atan2(dy, dx)
        self.velocidade_x = math.cos(angulo) * velocidade_lancamento
        self.velocidade_y = math.sin(angulo) * velocidade_lancamento

    def _colar_no_pe_do_dono(self):
        if self.dono is not None:
            direcao = getattr(self.dono, 'olhando_para', 'frente')
            
            # Pega o offset base (parado)
            offset_x, offset_y = self.offsets_posse.get(direcao, self.offsets_posse['frente'])

            # Aplica a posição
            self.rect.x = self.dono.rect.x + offset_x
            self.rect.y = self.dono.rect.y + offset_y

    def atualizar_posicao(self, neymar=None):
        if self.dono is not None:
            self._colar_no_pe_do_dono()
            self.sincronizar_coordenadas_float()
            self._registrar_prev_center()
            self.animar()
            return

        if self.em_movimento:
            self._registrar_prev_center()
            self.px += self.velocidade_x
            self.py += self.velocidade_y
            self.rect.x = int(self.px)
            self.rect.y = int(self.py)
            if self.tem_destino and self.destino_x is not None and self.destino_y is not None:
                distancia = math.hypot(self.destino_x - self.rect.centerx, self.destino_y - self.rect.centery)
                if distancia < 12: self.ficar_no_chao()
            if self.rect.bottom < 0: self.resetar(neymar)
        elif neymar is not None and neymar.tem_bola:
            self.dono = neymar
            self._colar_no_pe_do_dono()
            self.sincronizar_coordenadas_float()
            self._registrar_prev_center()
        self.animar()

    def ficar_no_chao(self):
        self.velocidade_x = 0.0
        self.velocidade_y = 0.0
        self.em_movimento = False
        self.no_chao_esperando = True
        self.dono = None
        self._limpar_destino()

    def dominar(self, jogador):
        self.no_chao_esperando = False
        self.em_movimento = False
        self.velocidade_x = 0.0
        self.velocidade_y = 0.0
        self.dono = jogador
        self._limpar_destino()
        self._colar_no_pe_do_dono()
        self.sincronizar_coordenadas_float()
        self._registrar_prev_center()
        if hasattr(jogador, "tem_bola"): jogador.tem_bola = True
        if hasattr(jogador, "tempo_recebeu_bola"): jogador.tempo_recebeu_bola = pygame.time.get_ticks()

    def chutar(self, origem_x, origem_y, FORCA_CHUTE, resultado='gol'):
        self.dono = None
        self._limpar_destino()
        self.rect.centerx = origem_x
        self.rect.centery = origem_y
        self.no_chao_esperando = False
        self.em_movimento = True
        self._registrar_prev_center()
        self.resultado_chute = resultado 
        alvo_y = 70
        if resultado == 'gol': alvo_x = random.randint(880, 1040)
        elif resultado == 'defesa': alvo_x = random.randint(930, 990)
        else: 
            if random.random() < 0.5: alvo_x = random.randint(730, 840)
            else: alvo_x = random.randint(1080, 1190)
        dx = alvo_x - origem_x
        dy = alvo_y - origem_y
        distancia_alvo = math.hypot(dx, dy)
        if distancia_alvo > 0:
            self.velocidade_x = (dx / distancia_alvo) * FORCA_CHUTE
            self.velocidade_y = (dy / distancia_alvo) * FORCA_CHUTE
        else: self.velocidade_x = 0.0; self.velocidade_y = -FORCA_CHUTE

    def passar(self, origem_x, origem_y, destino_x, destino_y, velocidade_passe):
        self.dono = None
        self.em_movimento = True
        self.no_chao_esperando = False
        self.rect.centerx = origem_x
        self.rect.centery = origem_y
        self.sincronizar_coordenadas_float()
        self._registrar_prev_center()
        self.destino_x = destino_x
        self.destino_y = destino_y
        self.tem_destino = True
        dx = destino_x - origem_x
        dy = destino_y - origem_y
        angulo = math.atan2(dy, dx)
        self.velocidade_x = math.cos(angulo) * velocidade_passe
        self.velocidade_y = math.sin(angulo) * velocidade_passe

    def lancar_em_profundidade(self, origem_x, origem_y, destino_x, destino_y, velocidade_passe):
        self.dono = None
        self.em_movimento = True
        self.no_chao_esperando = False
        self.rect.centerx = origem_x
        self.rect.centery = origem_y
        self.sincronizar_coordenadas_float()
        self._registrar_prev_center()
        self.destino_x = destino_x
        self.destino_y = destino_y
        self.tem_destino = True
        dx = destino_x - origem_x
        dy = destino_y - origem_y
        angulo = math.atan2(dy, dx)
        self.velocidade_x = math.cos(angulo) * velocidade_passe
        self.velocidade_y = math.sin(angulo) * velocidade_passe
        
    def resetar(self, neymar=None):
        self.ficar_no_chao()
        if neymar:
            self.rect.center = neymar.rect.center
            self.sincronizar_coordenadas_float()