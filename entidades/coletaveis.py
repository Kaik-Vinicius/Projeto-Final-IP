import pygame
import random
import math
from gerenciamento.constants import (LIMITE_ESQUERDO, LIMITE_DIREITO, 
                                     LIMITE_SUPERIOR, LIMITE_INFERIOR, 
                                     TAMANHO_ITEM, TEMPO_CHUTEIRA)

class Coletavel(pygame.sprite.Sprite):
    def __init__(self, tipo, pos_jogador=None): 
        super().__init__()
        self.tipo = tipo 
        
        # CARREGAMENTO DOS FRAMES DA ANIMAÇÃO DOS COLETAVEIS
        
        # SE FOR CHUTEIRA
        if self.tipo == 'chuteira':
            self.frames = [
                pygame.image.load("assets/chuteira/chuteira1.png").convert_alpha(),
                pygame.image.load("assets/chuteira/chuteira2.png").convert_alpha(),
                pygame.image.load("assets/chuteira/chuteira3.png").convert_alpha(),
                pygame.image.load("assets/chuteira/chuteira4.png").convert_alpha(),
            ]
            self.velocidade_animacao = 150 # VELOCIDADE DE ANIMAÇÃO DA CHUTEIRA

        # SE FOR ESTRELA
        elif self.tipo == 'estrela':
            
            self.frames = [
                pygame.image.load("assets/estrela/estrela1.png").convert_alpha(),
                pygame.image.load("assets/estrela/estrela2.png").convert_alpha(),
                pygame.image.load("assets/estrela/estrela3.png").convert_alpha(),
                pygame.image.load("assets/estrela/estrela4.png").convert_alpha(),
                pygame.image.load("assets/estrela/estrela5.png").convert_alpha(),
                pygame.image.load("assets/estrela/estrela6.png").convert_alpha(),
            ]
            
            self.velocidade_animacao = 120 
            
        # COLOCA OS FRAMES DEPENDENDO DO TAMANHO DO ITEM
        self.frames = [pygame.transform.smoothscale(f, (TAMANHO_ITEM, TAMANHO_ITEM)) for f in self.frames]
        
        # DEFINE O ESTADO INICIAL DO SPRITE
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect = self.image.get_rect()
        
        # VARIAVEIS DE CONTROLE DE TEMPO
        self.ultimo_update_animacao = pygame.time.get_ticks()
        self.tempo_nascimento = pygame.time.get_ticks()

        # LOGICA DE SPAWN NA FRENTE DO JOGADOR
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

    def update(self):
        tempo_atual = pygame.time.get_ticks()
        
        # TEMPO QUE A CHUTEIRA FICA NO MAPA
        if self.tipo == 'chuteira':
            if tempo_atual - self.tempo_nascimento > TEMPO_CHUTEIRA:
                self.kill()
                return

        # ATUALIZACAO DOS FRAMES
        if tempo_atual - self.ultimo_update_animacao > self.velocidade_animacao:
            self.ultimo_update_animacao = tempo_atual
            self.frame_atual += 1
            
            if self.frame_atual >= len(self.frames):
                self.frame_atual = 0
                
            self.image = self.frames[self.frame_atual]