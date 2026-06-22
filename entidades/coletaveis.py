import pygame
import random
import math
from gerenciamento.constants import (LIMITE_ESQUERDO, LIMITE_DIREITO, 
                                     LIMITE_SUPERIOR, LIMITE_INFERIOR, 
                                     TAMANHO_ITEM, COR_ESTRELA, 
                                     COR_CHUTEIRA, TEMPO_CHUTEIRA)

class Coletavel(pygame.sprite.Sprite):
    def __init__(self, tipo, pos_jogador=None): 
        super().__init__()
        self.tipo = tipo 
        self.image = pygame.Surface((TAMANHO_ITEM, TAMANHO_ITEM)) 
        
        if self.tipo == 'estrela':
            self.image.fill(COR_ESTRELA)
        elif self.tipo == 'chuteira':
            self.image.fill(COR_CHUTEIRA)
            
        self.rect = self.image.get_rect()
        
        # --- LÓGICA DE SPAWN (NA FRENTE DO JOGADOR) ---
        if pos_jogador is not None:
            if self.tipo == 'chuteira':
                distancia_min = 60  
                distancia_max = 120 
                angulo = random.uniform(math.pi * 1.25, math.pi * 1.75) 
            elif self.tipo == 'estrela':
                distancia_min = 80 
                distancia_max = 120 
                angulo = random.uniform(math.pi * 1.35, math.pi * 1.65) # Bem na frente
            
            distancia = random.randint(distancia_min, distancia_max)
            novo_x = pos_jogador[0] + int(math.cos(angulo) * distancia)
            novo_y = pos_jogador[1] + int(math.sin(angulo) * distancia)
            
            # TRAVA NO CAMPO (Não deixa nascer fora da linha)
            self.rect.x = max(LIMITE_ESQUERDO, min(LIMITE_DIREITO - TAMANHO_ITEM, novo_x))
            self.rect.y = max(LIMITE_SUPERIOR, min(LIMITE_INFERIOR - TAMANHO_ITEM, novo_y))
            
        else:
            self.rect.x = random.randint(LIMITE_ESQUERDO, LIMITE_DIREITO - TAMANHO_ITEM)
            self.rect.y = random.randint(LIMITE_SUPERIOR, LIMITE_INFERIOR - TAMANHO_ITEM)
            
        self.tempo_nascimento = pygame.time.get_ticks()

    def update(self):
        if self.tipo == 'chuteira':
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.tempo_nascimento > TEMPO_CHUTEIRA:
                self.kill()