import pygame
import random
from gerenciamento.constants import (LIMITE_ESQUERDO, LIMITE_DIREITO, 
                                     LIMITE_SUPERIOR, LIMITE_INFERIOR, 
                                     TAMANHO_ITEM, COR_ESTRELA, 
                                     COR_CHUTEIRA, TEMPO_CHUTEIRA)

class Coletavel(pygame.sprite.Sprite):
    def __init__(self, tipo, pos_jogador=None): 
        super().__init__()
        self.tipo = tipo 
        self.image = pygame.Surface((TAMANHO_ITEM, TAMANHO_ITEM)) 
        
        # Pinta a cor do quadrado dependendo do tipo 
        if self.tipo == 'estrela':
            self.image.fill(COR_ESTRELA)
        elif self.tipo == 'chuteira':
            self.image.fill(COR_CHUTEIRA)
            
        self.rect = self.image.get_rect()
        
        # ---(LIMITES DO CAMPO) ---
        self.rect.x = random.randint(LIMITE_ESQUERDO, LIMITE_DIREITO - TAMANHO_ITEM)
        self.rect.y = random.randint(LIMITE_SUPERIOR, LIMITE_INFERIOR - TAMANHO_ITEM)
            
        self.tempo_nascimento = pygame.time.get_ticks()

    def update(self):
        # O cronômetro de desaparecimento da chuteira
        if self.tipo == 'chuteira':
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.tempo_nascimento > TEMPO_CHUTEIRA:
                self.kill()