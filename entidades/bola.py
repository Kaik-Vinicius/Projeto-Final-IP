import pygame
import math
from gerenciamento.constants import COR_BOLA


class Bola(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(COR_BOLA)
        self.rect = self.image.get_rect()

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

        # DESTINO EXPLÍCITO (SEM USAR hasattr)
        self.tem_destino = False
        self.destino_x = None
        self.destino_y = None

    def sincronizar_coordenadas_float(self):
        """
        TRANSFORMA AS COORDENADAS DA BOLA EM FLOAT
        """
        self.px = float(self.rect.x)
        self.py = float(self.rect.y)

    def _registrar_prev_center(self):
        self.prev_center.update(self.rect.centerx, self.rect.centery)

    def _limpar_destino(self):
        self.tem_destino = False
        self.destino_x = None
        self.destino_y = None

    def iniciar_lancamento(self, x_inicial, y_inicial, x_destino, y_destino, velocidade_lancamento):
        """
        LANÇAMENTO INICIAL DA BOLA
        """
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

    def atualizar_posicao(self, neymar=None):
        """
        GERENCIA A FISICA DA BOLA A CADA FRAME
        """
        # Se a bola estiver com alguém, ela segue o dono e não "voa"
        if self.dono is not None:
            self.rect.center = self.dono.rect.center
            self.sincronizar_coordenadas_float()
            self._registrar_prev_center()
            return

        if self.em_movimento:
            # guarda a posição anterior antes de mover
            self._registrar_prev_center()

            self.px += self.velocidade_x
            self.py += self.velocidade_y

            self.rect.x = int(self.px)
            self.rect.y = int(self.py)

            # Se houver destino, checa chegada
            if self.tem_destino and self.destino_x is not None and self.destino_y is not None:
                distancia = math.hypot(self.destino_x - self.rect.centerx, self.destino_y - self.rect.centery)
                if distancia < 12:
                    self.ficar_no_chao()

            # Segurança para sair do mapa
            if self.rect.bottom < 0:
                self.resetar(neymar)

        elif neymar is not None and neymar.tem_bola:
            # fallback de compatibilidade
            self.rect.center = neymar.rect.center
            self.sincronizar_coordenadas_float()
            self._registrar_prev_center()

    def ficar_no_chao(self):
        """
        INTERROMPE O LANÇAMENTO E DEIXA A BOLA PARADA
        """
        self.velocidade_x = 0.0
        self.velocidade_y = 0.0
        self.em_movimento = False
        self.no_chao_esperando = True
        self.dono = None
        self._limpar_destino()

    def dominar(self, jogador):
        """
        FAZ A BOLA FICAR DOMINADA NO PÉ DO JOGADOR
        FUNCIONA PARA NEYMAR E PARA O ALIADO
        """
        self.no_chao_esperando = False
        self.em_movimento = False
        self.velocidade_x = 0.0
        self.velocidade_y = 0.0
        self.dono = jogador
        self._limpar_destino()

        self.rect.center = jogador.rect.center
        self.sincronizar_coordenadas_float()
        self._registrar_prev_center()

        if hasattr(jogador, "tem_bola"):
            jogador.tem_bola = True

        if hasattr(jogador, "tempo_recebeu_bola"):
            jogador.tempo_recebeu_bola = pygame.time.get_ticks()

    def chutar(self, forca_chute):
        """
        FAZ O NEYMAR CHUTAR A BOLA
        """
        self.dono = None
        self._limpar_destino()
        self.no_chao_esperando = False
        self.em_movimento = True
        self.velocidade_x = 0.0
        self.velocidade_y = -forca_chute
        self._registrar_prev_center()

    def passar(self, origem_x, origem_y, destino_x, destino_y, velocidade_passe):
        """
        PASSE NORMAL PARA O ALIADO
        """
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
        """
        PASSE EM PROFUNDIDADE DO ALIADO DE VOLTA AO NEYMAR
        """
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
    
    # PROVAVELMENTE VOU TIRAR ESSE METODO DEPOIS
    def resetar(self, neymar):
        """SEGURANÇA PRA EVITAR DA BOLA SAIR DO MAPA"""
        self.velocidade_x = 0.0
        self.velocidade_y = 0.0
        self.em_movimento = False
        self.no_chao_esperando = False
        self.dono = neymar
        self._limpar_destino()
        neymar.tem_bola = True
        self.rect.center = neymar.rect.center
        self.sincronizar_coordenadas_float()
        self._registrar_prev_center()

        