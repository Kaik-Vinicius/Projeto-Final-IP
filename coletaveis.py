import pygame
import random
from constants import (LARGURA_TELA, ALTURA_TELA, COR_BOLA, 
                       COR_ESTRELA, COR_CHUTEIRA, TAMANHO_ITEM, TEMPO_CHUTEIRA)

class Coletavel(pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()
        self.tipo = tipo 
        self.image = pygame.Surface((TAMANHO_ITEM, TAMANHO_ITEM)) 
        
        # Define cor baseado no tipo
        if self.tipo == 'bola':
            self.image.fill(COR_BOLA)
        elif self.tipo == 'estrela':
            self.image.fill(COR_ESTRELA)
        elif self.tipo == 'chuteira':
            self.image.fill(COR_CHUTEIRA)
            
        self.rect = self.image.get_rect()
        margem = 50
        self.rect.x = random.randint(margem, LARGURA_TELA - margem)
        self.rect.y = random.randint(margem, ALTURA_TELA - margem)
        self.tempo_nascimento = pygame.time.get_ticks()

    def update(self):
        # A chuteira some depois de X tempo
        if self.tipo == 'chuteira':
            if pygame.time.get_ticks() - self.tempo_nascimento > TEMPO_CHUTEIRA:
                self.kill()