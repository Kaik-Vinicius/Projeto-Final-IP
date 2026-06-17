import pygame
import math
import random
from gerenciamento.funcoes_importantes import prender_neymar_campo
from entidades.bola import Bola
from gerenciamento.constants import (LARGURA_TELA, ALTURA_TELA, VELOCIDADE_NEY, 
            COR_NEYMAR, FORCA_CHUTE, TUPLA_LIMITES_CAMPO, DRIBLES_CONFIG)


class Neymar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((45, 40))
        self.image.fill(COR_NEYMAR)
        self.rect = self.image.get_rect()

        self.rect.centerx = LARGURA_TELA // 2
        self.rect.centery = ALTURA_TELA - 100

        self.velocidade = VELOCIDADE_NEY
        self.barra_estrela = 0
        self.tem_bola = False
        self.tempo_ultimo_passe = 0

        # ISSO DAQUI É A PARTE QUE VAI ENTRAR O DRIBLE DO NEY
        self.bola_em_drible = False
        self.tempo_inicio_drible = 0

    def mover(self, teclas):
        dx = 0
        dy = 0

        if teclas[pygame.K_a]:
            dx += -self.velocidade
        if teclas[pygame.K_d]:
            dx += self.velocidade
        if teclas[pygame.K_w]:
            dy += -self.velocidade
        if teclas[pygame.K_s]:
            dy += self.velocidade
        
        self.rect.x += dx
        self.rect.y += dy
        
        # chama a funcao que prende o ney no campo
        prender_neymar_campo(self, TUPLA_LIMITES_CAMPO)
    
    # metodo pra o ney dar passe
    def dar_passe(self, bola, grupo_aliados):
        """PROCURA O ALIADO MAIS PROXIMO PRA DAR O PASSE"""
        if self.tem_bola and len(grupo_aliados) > 0:
            aliado_mais_proximo = None
            distancia_minima = float('inf')

            for aliado in grupo_aliados:
                dx = aliado.rect.centerx - self.rect.centerx
                dy = aliado.rect.centery - self.rect.centery
                distancia = math.hypot(dx, dy)

                if distancia < distancia_minima:
                    distancia_minima = distancia
                    aliado_mais_proximo = aliado

            if aliado_mais_proximo:
                self.tempo_ultimo_passe = pygame.time.get_ticks()
                self.tem_bola = False
                
                # SE TIVER ALIADO PROXIMO O NEYMAR DÁ O PASSE
                bola.passar(self.rect.centerx, self.rect.centery, aliado_mais_proximo.rect.centerx, aliado_mais_proximo.rect.centery, 12)

    # metodo pra chutar pra o gol
    def chutar_pro_gol(self, bola):
        """FAZ O NEYMAR CHUTAR A BOLA"""
        if self.tem_bola:
            self.tempo_ultimo_passe = pygame.time.get_ticks()
            bola.chutar(FORCA_CHUTE)
            self.tem_bola = False

    def driblar(self, tipo_drible, grupo_zagueiros):
        """
        RECEBE COMO PARAMETRO O TIPO DE DRIBLE QUE O NEY EXECUTOU E O GRUPO DE ZAGUEIROS QUE VAI SER PERCORRIDO
        """
        if not self.tem_bola:
            return
        
        tipo_drible = tipo_drible.lower()

        # VERIFICA SE TODOS ESTAO EM IDLE PRA PODER EXECUTAR ALGUM DRIBLE
        todos_em_idle = all(zagueiro.esta_em_idle() for zagueiro in grupo_zagueiros)

        #if todos_em_idle:
            ####################################


