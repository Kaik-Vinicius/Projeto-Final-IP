import pygame
import math
import random
from gerenciamento.funcoes_importantes import prender_neymar_campo
from entidades.bola import Bola
from entidades.coletaveis import Coletavel
from gerenciamento.constants import (LARGURA_TELA, ALTURA_TELA, VELOCIDADE_NEY, COR_NEYMAR, FORCA_CHUTE, TUPLA_LIMITES_CAMPO, DRIBLES_CONFIG)


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
        self.tempo_ultimo_chute = 0

        # ISSO DAQUI É A PARTE QUE VAI ENTRAR O DRIBLE DO NEY
        self.bola_em_drible = False
        self.tempo_inicio_drible = 0
        self.drible_efetivo = False
        
        # ATRIBUINDO A CONFIANCA DO NEYMAR
        self.confianca = 0
        self.ultimo_tipo_drible = 'manual'
<<<<<<< HEAD

=======
>>>>>>> jogador-e-chute


    def mover(self, teclas, bola, grupo_zagueiros=None):
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
        
        # AQUI O NEYMAR VAI TENTAR DESVIAR MANUALMENTE SEM DRIBLES
        if grupo_zagueiros and self.tem_bola and (dx != 0 or dy != 0):
            self.checar_desvio_manual(bola, grupo_zagueiros)
    
            
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
        """
        CALCULA A PROBABILIDADE DE GOL BASEADO NA DISTÂNCIA E CONFIANÇA DO NEYMAR,
        E DISPARA A BOLA COM O DESTINO CORRETO.
        """
        if not self.tem_bola:
            return
        
        # NEYMAR PERDE A POSSE DA BOLA
        self.tem_bola = False
        
        # COORDENADAS QUE VAO GUIAR OS CHUTES PRA O GOL
        centro_gol_x = 960
        centro_gol_y = 70

        # CÁLCULO DA DISTÂNCIA
        distancia = math.hypot(centro_gol_x - self.rect.centerx, centro_gol_y - self.rect.centery)
        
        # QUANTO MAIS PERTO, MAIOR A CHANCE COM MAXIMO DE 0.95 E MINIMO DE 0.05
        fator_distancia = max(0.05, min(0.95, 1.0 - (distancia / 1000.0)))

        # CÁLCULO DA CONFIANÇA O MINIMO É ZERO E O MAXIMO É 100
        fator_confianca = max(0.0, min(1.0, self.confianca / 100.0))

        # PROBABILIDADE FINAL == UM PESO DE 60% PRA DISTANCIA E UM PESO DE 40% PRA CONFIANCA (talvez possamos mudar isso daqui)
        probabilidade_gol = (fator_distancia * 0.6) + (fator_confianca * 0.4)

        # DEFINIÇÃO DO RESULTADO DO CHUTE
        # AQUI ENTRA A ALEATORIEDADE DE SE VAI SER GOL OU NAO
        if random.random() <= probabilidade_gol: 
            resultado = 'gol'
        else:
            # SE ELE ERRAR O GOL, AI É DEFINIDO 50/50 SE VAI PRA FORA OU SE O GOLEIRO PEGA
            if random.random() < 0.5:
                resultado = 'defesa'
                
            else:
                resultado = 'fora'
                
        self.tempo_ultimo_chute = pygame.time.get_ticks() # REGISTRA O TEMPO DO ULTIMO CHUTE
        
        # CHAMA O METODO DE CHUTAR PRA BOLA SER CHUTADA
        bola.chutar(self.rect.centerx, self.rect.centery, FORCA_CHUTE, resultado)
    
    def atualizar_confianca(self, valor):
        """
        ATUALIZA A CONFIANÇA SEMPRE QUE ALGO ACONTECE
        """
        self.confianca += valor
        
        # Garante que a confiança não fique negativa
        if self.confianca < 0:
            self.confianca = 0
            
    def calcular_chance_drible(self, tipo_drible):
        """APLICA A FORMULA PRA CALCULAR SE DRIBLOU OU NAO"""
        
        c_ini = DRIBLES_CONFIG[tipo_drible]['chance_inicial']
        c_max = DRIBLES_CONFIG[tipo_drible]['chance_max']
        
        chance = c_ini + ((self.confianca / 100.0) * (c_max - c_ini))
<<<<<<< HEAD
            
        if getattr(self, 'ney_prime', False):
            return 1.0

=======
        
        if getattr(self, 'ney_prime', False):
            return 1.0
>>>>>>> jogador-e-chute
        return min(chance, c_max)
        

    def checar_desvio_manual(self, bola, grupo_zagueiros):
        """
        VERIFICA SE O NEYMAR SE AFASTOU DO ZAGUEIRO ENQUANTO ELE ARMAVA O BOTE USANDO AS TECLAS 'WASD'
        """
        
        tempo_atual = pygame.time.get_ticks()
        
        # SE PASSOU 1.5s DO ULTIMO DRIBLE, AI LIBERA A FLAG PRA PODER DRIBLAR DE NOVO
        if self.drible_efetivo and tempo_atual - self.tempo_inicio_drible >= 1500:
            self.drible_efetivo = False
            
        # ITERA SOBRE CADA ZAGUEIRO
        for zagueiro in grupo_zagueiros:
            preparo = getattr(zagueiro, 'preparo_pro_bote', False)
            driblado = getattr(zagueiro, 'driblado', False)
            atordoado = getattr(zagueiro, 'atordoado_por_drible', False)
            
            if preparo and not driblado and not atordoado:
                dx = zagueiro.rect.centerx - bola.rect.centerx
                dy = zagueiro.rect.centery - bola.rect.centery
                
                distancia_bola_zagueiro = math.hypot(dx, dy)
            
               # ESSA CONDICIONAL VERIFICA SE ESTA NA DISTANCIA IDEAL PRA APLICAR O DRIBLE
                if 95 <= distancia_bola_zagueiro <= 140:
                    
                    if self.drible_efetivo:
                        break
                    
                    if hasattr(zagueiro, 'ficar_atordoado_por_drible'):
                        zagueiro.ficar_atordoado_por_drible(tempo=1000)
                    self.bola_em_drible = True
                    self.drible_efetivo = True
                    self.tempo_inicio_drible = pygame.time.get_ticks()
                    self.ultimo_tipo_drible = 'manual'

                    
    def driblar(self, tipo_drible, bola, grupo_zagueiros, grupo_coletaveis=None):
        """
        RECEBE COMO PARAMETRO O TIPO DE DRIBLE QUE O NEY EXECUTOU E O GRUPO DE ZAGUEIROS QUE VAI SER PERCORRIDO
        """
        # SE NAO TIVER A BOLA OU SE JA TIVER EM UM DRIBLE EFETIVO, ELE BLOQUEIA
        if not self.tem_bola or self.drible_efetivo:
            return
        
        tipo_drible = tipo_drible.lower()
        
        ganho_confianca = DRIBLES_CONFIG[tipo_drible]['ganho']
        
        # VERIFICA SE TODOS ESTAO EM IDLE PRA PODER EXECUTAR ALGUM DRIBLE
        todos_em_idle = all(zagueiro.esta_em_idle() for zagueiro in grupo_zagueiros)
        
        # DEFINE O ZAGUEIRO PROXIMO
        zagueiro_mais_proximo = None
        dist_min = float('inf')
        
        # FOR QUE IRA BUSCAR O ZAGUEIRO MAIS PROXIMO
        for zagueiro in grupo_zagueiros:
            dx = zagueiro.rect.centerx - bola.rect.centerx
            dy = zagueiro.rect.centery - bola.rect.centery
            distancia = math.hypot(dx, dy)
            
            if distancia < dist_min:
                dist_min = distancia
                zagueiro_mais_proximo = zagueiro
        
        # AQUI O NEY SO FAZ FIRULA
        if todos_em_idle and dist_min > 120:
            self.bola_em_drible = True 
            self.drible_efetivo = False # A FIRULA NAO É CONSIDERADA UM DRIBLE EFETIVO
            self.tempo_inicio_drible = pygame.time.get_ticks()
            self.ultimo_tipo_drible = 'firula'
            return
        
        # AQUI ELE VAI TENTAR DRIBLAR O ZAGUEIRO CASO ELE ESTEJA PREPARADO PRA UMM BOTE
        elif zagueiro_mais_proximo and dist_min <= 110:
                if zagueiro_mais_proximo.preparo_pro_bote: # SO FAZ O DRIBLE SE O ZAGUEIRO MAIS PROXIMO TIVER PREPARADO PRO BOTE
                    chance_final = self.calcular_chance_drible(tipo_drible)
                    
                    if random.random() <= chance_final: # ISSO DAQUI RANDOMIZA A CHANCE DE DAR CERTO
                        if hasattr(zagueiro_mais_proximo, 'ficar_atordoado_por_drible'):
                            zagueiro_mais_proximo.ficar_atordoado_por_drible(tempo=1500) # ATORDOAMENTO DE 1.5s
                        self.bola_em_drible = True
                        self.drible_efetivo = True
                        self.tempo_inicio_drible = pygame.time.get_ticks()
                        self.ultimo_tipo_drible = tipo_drible
<<<<<<< HEAD
=======
                        
            


>>>>>>> jogador-e-chute
