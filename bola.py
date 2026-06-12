# VOU CONTINUAR DEFININDO ESSA CLASSE DA BOLA DEPOIS 
# DE CONVERSAR COM MEU GRUPO SOBRE ISSO

import pygame
import math
from constants import COR_BOLA

class Bola(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(COR_BOLA)
        self.rect = self.image.get_rect()
        
        # CONTROLE DO MOVIMENTO
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.em_movimento = False
        
    def atualizar_posicao(self, neymar):
        """
        
        
        """
        
        