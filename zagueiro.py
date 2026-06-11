import pygame
from constants import (LARGURA_TELA, ALTURA_TELA, VELOCIDADE_ZAG, COR_ZAGUEIRO, CONFIANCA_POR_DIFICULDADE, DRIBLES_CONFIG, META_ESTRELA, FORCA_CHUTE, POS_GOL_X, POS_GOL_Y)

class Zagueiro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # DEFININDO O RETANGULO DO ZAGUEIRO
        self.image = pygame.Surface((45,40))
        self.image.fill(COR_ZAGUEIRO)
        self.rect = self.image.get_rect()
        
        # ONDE ELE VAI SPAWNAR - VOU MUDAR ISSO DEPOIS PARAS ISSO SER DEFINIDO NA MAIN
        self.rect.centerx = LARGURA_TELA // 2
        self.rect.centery = ALTURA_TELA - 500
        
        self.velocidade = VELOCIDADE_ZAG # A VELOCIDADE QUE ELE VAI ANDAR

    def perseguir(self, neymar):
        # RECEBE A POSICAO X E Y DO NEYMAR
        neymar_x = neymar.rect.x
        neymar_y = neymar.rect.y

        # CALCULA A DISTANCIA DO ZAGUEIRO PARA O NEYMAR
        dist_x = self.rect.x - neymar_x
        dist_y = self.rect.y - neymar_y

        dist_total = ((dist_x ** 2) + (dist_y ** 2)) ** 0.5

        # NORMATIZA A DISTANCIA PARA UMA PERSGUICAO MAIS FLUIDA, EU ACHO
        norma_x = dist_x / dist_total
        norma_y = dist_y / dist_total

        # MOVE O ZAGUEIRO
        self.rect.x -= (norma_x * self.velocidade)
        self.rect.y -= (norma_y * self.velocidade)

        # MANTER DENTRO DA TELA
        self.rect.clamp_ip(pygame.Rect(0, 0, LARGURA_TELA, ALTURA_TELA)) 

        
        
            