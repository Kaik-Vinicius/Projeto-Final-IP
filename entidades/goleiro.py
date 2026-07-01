import pygame
from gerenciamento.constants import (COR_GOLEIRO)

class Goleiro (pygame.sprite.Sprite):
    def __init__(self, pos_inicial_x, pos_inicial_y):
        super().__init__()
      
        # DEFININDO O RETANGULO DO ZAGUEIRO
        self.image = pygame.Surface((45,40))
        self.image.fill(COR_GOLEIRO)
        self.rect = self.image.get_rect()
      
        # ONDE ELE VAI SPAWNAR
        self.rect.centerx = pos_inicial_x
        self.rect.centery = pos_inicial_y

        # AQUI CADA ZAGUEIRO GUARDA SUA POSICAO INICIAL INDEPENDENTEMENTE
        self.spawn_x = pos_inicial_x
        self.spawn_y = pos_inicial_y
      
        self.velocidade = 2 # A VELOCIDADE QUE ELE VAI ANDAR

    def perseguir_neymar(self, neymar):
        neymar_x = neymar.rect.centerx

        # CALCULA A DISTANCIA E DIREÇÃO NO EIXO X
        dist_x = self.rect.centerx - neymar_x

        # 2 PARA NAO FICAR TREMENDO
        if abs(dist_x) > 2:
            # NORMTIZA O VETOR NO EIXO X
            norma_x = dist_x / abs(dist_x)

            # MOVE O GOLEIRO APENAS NO EIXO X
            self.rect.x -= (norma_x * self.velocidade)

        # MANTER DENTRO DA ÁREA DO GOL
        self.rect.clamp_ip(pygame.Rect(900, 80, 120, 0))

    def pular_na_bola(self, bola, distancia_bola):
        alvo = bola.alvo_x

        if alvo > 1060:
            alvo = 1060
        elif alvo < 860:
            alvo = 860

        # CALCULA A DISTANCIA E DIREÇÃO NO EIXO X
        dist_x = self.rect.centerx - alvo

        velocidade = abs(8 - (min(distancia_bola, 200) / 200) * 10)

        # 2 PARA NAO FICAR TREMENDO
        if abs(dist_x) > 2:
            # NORMTIZA O VETOR NO EIXO X
            norma_x = dist_x / abs(dist_x)

            # MOVE O GOLEIRO APENAS NO EIXO X
            if bola.resultado_chute == 'gol':
                self.rect.x -= (norma_x * velocidade) * 0.75
            else:
                self.rect.x -= norma_x * velocidade

        # MANTER DENTRO DA ÁREA DO GOL
        self.rect.clamp_ip(pygame.Rect(860, 80, 200, 0))
         
    def att_gol(self, neymar, bola):
        pos_goleiro = pygame.math.Vector2(self.rect.center)
        pos_neymar = pygame.math.Vector2(neymar.rect.center)
        pos_bola = pygame.math.Vector2(bola.rect.center)
        distancia_neymar = pos_goleiro.distance_to(pos_neymar)
        distancia_bola = pos_goleiro.distance_to(pos_bola)

        # SE O NEYMAR TIVER 
        if bola.foi_chutada:
            if distancia_bola <= 200:
                self.pular_na_bola(bola, distancia_bola)

        if 30 < distancia_neymar < 250:
            self.perseguir_neymar(neymar)