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
        # RECEBE A POSICAO X E Y DO NEYMAR
        neymar_x = neymar.rect.centerx
        neymar_y = neymar.rect.centery

        # CALCULA A DISTANCIA DO ZAGUEIRO PARA O NEYMAR
        dist_x = self.rect.centerx - neymar_x
        dist_y = self.rect.centery - neymar_y

        dist_total = ((dist_x ** 2) + (dist_y ** 2)) ** 0.5


        # NORMATIZA A DISTANCIA PARA UMA PERSGUICAO MAIS FLUIDA, EU ACHO
        norma_x = dist_x / dist_total
        norma_y = dist_y / dist_total

        # MOVE O ZAGUEIRO
        self.rect.x -= (norma_x * self.velocidade)
        self.rect.y -= (norma_y * self.velocidade)

        # MANTER DENTRO DA TELA
        self.rect.clamp_ip(pygame.Rect(848, 75, 224, 50))
         
    def att_gol(self, neymar):
        pos_goleiro = pygame.math.Vector2(self.rect.center)
        pos_neymar = pygame.math.Vector2(neymar.rect.center)
        distancia_neymar = pos_goleiro.distance_to(pos_neymar)

        if(distancia_neymar > 30 and distancia_neymar < 250):
            self.perseguir_neymar(neymar)