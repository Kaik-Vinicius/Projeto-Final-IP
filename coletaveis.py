import pygame
import random
import math
from constants import (LARGURA_TELA, ALTURA_TELA, COR_BOLA, 
                       COR_ESTRELA, COR_CHUTEIRA, TAMANHO_ITEM, TEMPO_CHUTEIRA)

class Coletavel(pygame.sprite.Sprite):
    def __init__(self, tipo, pos_jogador=None): 
        super().__init__()
        self.tipo = tipo 
        self.image = pygame.Surface((TAMANHO_ITEM, TAMANHO_ITEM)) 
        
        if self.tipo == 'bola':
            self.image.fill(COR_BOLA)
        elif self.tipo == 'estrela':
            self.image.fill(COR_ESTRELA)
        elif self.tipo == 'chuteira':
            self.image.fill(COR_CHUTEIRA)
            
        self.rect = self.image.get_rect()
        margem = 50
        
        # --- LÓGICA DE SPAWN FRONTAL E PRÓXIMO ---
        if pos_jogador and self.tipo in ['chuteira', 'estrela']:
            
            #  
            distancia_min = 80  
            distancia_max = 200 
            distancia = random.randint(distancia_min, distancia_max)
            
            angulo = random.uniform(math.pi * 1.25, math.pi * 1.75) 
            
            novo_x = pos_jogador[0] + int(math.cos(angulo) * distancia)
            novo_y = pos_jogador[1] + int(math.sin(angulo) * distancia)
            
            # Garante que não nasça fora do campo
            self.rect.x = max(margem, min(LARGURA_TELA - margem, novo_x))
            self.rect.y = max(margem, min(ALTURA_TELA - margem, novo_y))
        else:
            
            self.rect.x = random.randint(margem, LARGURA_TELA - margem)
            self.rect.y = random.randint(margem, ALTURA_TELA - margem)
            
        self.tempo_nascimento = pygame.time.get_ticks()

    def update(self):
        if self.tipo == 'chuteira':
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.tempo_nascimento > TEMPO_CHUTEIRA:
                self.kill()