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
        
        # ESTADOS DA BOLA
        self.em_movimento = False
        self.no_chao_esperando = False
        
        # PRECISÃO DECIMAL
        self.px = 0.0
        self.py = 0.0
        
    def sincronizar_coordenadas_float(self):
        """
        TRANSFORMA AS COORDENADAS DA BOLA EM FLOAT
        """
        self.px = float(self.rect.x)
        self.py = float(self.rect.y)
        
    def iniciar_lancamento(self, x_inicial, y_inicial, x_destino, y_destino, velocidade_lancamento):
        """
        VAI SER O QUE VAI LANÇAR A BOLA PRA O NEYMAR NO CAMPO DE ATAQUE A CADA OPORTUNIDADE
        """
        
        # DE ONDE A BOLA VAI VIM
        self.rect.centerx = x_inicial
        self.rect.centery = y_inicial
        self.sincronizar_coordenadas_float() # FAZ A SINCRONIZAÇÃO
        
        # AONDE A BOLA VAI PARAR
        self.destino_x = x_destino
        self.destino_y = y_destino
        
        # VARIAVEIS DE ESTADO DA BOLA NO MOMENTO QUE SEU LANÇAMENTO É INICIADO
        self.em_movimento = True
        self.no_chao_esperando = False
        
        # CALCULO TRIGONOMETRICO PRA DESCOBRIR O ANGULO DO LANÇAMENTO
        dx = x_destino - x_inicial
        dy = y_destino - y_inicial
        angulo = math.atan2(dy, dx)
        
        # APLICAÇÃO DA VELOCIDADE NOS DOIS EIXOS DE ACORDO COM O ANGULO
        self.velocidade_x = math.cos(angulo) * velocidade_lancamento
        self.velocidade_y = math.sin(angulo) * velocidade_lancamento
        
    def atualizar_posicao(self, neymar):
        """
        VAI GERENCIAR A FISICA DA MOVIMENTAÇÃO DA BOLA A CADA FRAME DO JOGO
        """
        # VAI ATUALIZAR O MOVIMENTO DA BOLA
        if self.em_movimento:
            self.px += self.velocidade_x
            self.py += self.velocidade_y
        
            # REPASSA OS VALORES PRA INTEIRO
            self.rect.x = int(self.px)
            self.rect.y = int(self.py)
            
            # CHECA SE A BOLA AINDA TA VOANDO E SE ALCANÇOU O DESTINO
            if hasattr(self, 'destino_x'):
                distancia = math.hypot(self.destino_x - self.rect.centerx, self.destino_y - self.rect.centery)
                if distancia < 12:  # Chegou perto o suficiente do destino (raio de 10 pixels)
                    self.ficar_no_chao()
                    
            # =================================================================
            # COLOCANDO ESSA MARGEM DE SEGURANÇA POR ENQUANTO, DEPOIS VAI MUDAR
            # PQ PRECISA DEFINIR EXATAMENTE O TAMANHO DO CAMPO, NO CASO DENTRO DAS 4 LINHAS QUE O DELIMITAM
            if self.rect.bottom < 0:
                self.resetar(neymar)
            # =================================================================
            
            
        # SE ESTIVER CONDUZIDA, OU SEJA NO PE DO NEYMAR
        elif neymar.tem_bola:
            self.rect.centerx = neymar.rect.centerx
            self.rect.centery = neymar.rect.centery
            self.sincronizar_coordenadas_float() #sincroniza
            
    def ficar_no_chao(self):
        """
        INTERROMPE O LANÇAMENTO DA BOLA E ELA FICA PARADA
        """
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.em_movimento = False
        self.no_chao_esperando = True
        
        if hasattr(self, 'destino_x'):
            del self.destino_x
            del self.destino_y
            
    def dominar(self, neymar):
        """
        FAZ O NEYMAR DOMINAR A BOLA NO SEU PÉ
        """
        self.no_chao_esperando = False
        self.em_movimento = False
        self.velocidade_x = 0  # ZERA A VELOCIDADE DA BOLA PQ O NEY DOMINOU ELA
        self.velocidade_y = 0  
        neymar.tem_bola = True
        
    def chutar(self, forca_chute):
        """
        FAZ O NEYMAR CHUTAR A BOLA
        
        =-=-=-=-=-=-=
        OBS.: VAI TER QUE SER MUDADO DEPOIS PARA A BOLA IR SEMPRE NA DIREÇÃO DO GOL
        INDEPENDENTE DE ONDE O NEYMAR ESTEJA, E NAO PRA CIMA COMO ESTA AGORA
        """
        if not self.em_movimento and not self.no_chao_esperando:
            self.velocidade_x = 0
            self.velocidade_y = -forca_chute # negativo pra poder subir na direção do eixo Y
            self.em_movimento = True
            
    
    def passar(self, origem_x, origem_y, destino_x, destino_y, velocidade_passe):
        """
        CALCULA O VETOR E A TRAJETORIA DA BOLA ATE O ALIADO MAIS PROXIMO PRA PODER PASSÁ-LA
        """
        self.em_movimento = True
        self.no_chao_esperando = False
        
        # GUARDA AGORA OS NOVOS DESTINO DA BOLA
        self.destino_x = destino_x
        self.destino_y = destino_y
        
        dx = destino_x - origem_x
                                    # FAZ ISSO DAQUI BASEADO NA POSICAO DO ALIADO MAIS PROXIMO
        dy = destino_y - origem_y
        angulo = math.atan2(dy, dx)
        
        self.velocidade_x = math.cos(angulo) * velocidade_passe
        self.velocidade_y = math.sin(angulo) * velocidade_passe

    def lancar_em_profundidade(self, origem_x, origem_y, destino_x, destino_y, velocidade_passe):
        """
        CALCULA O VETOR E A TRAJETORIA DA BOLA ATE O ALIADO MAIS PROXIMO PRA PODER PASSÁ-LA
        """
        self.em_movimento = True
        self.no_chao_esperando = False
        
        # GUARDA AGORA OS NOVOS DESTINO DA BOLA
        self.destino_x = destino_x
        self.destino_y = destino_y
        
        dx = destino_x - origem_x
                                    # FAZ ISSO DAQUI BASEADO NA POSICAO DO ALIADO MAIS PROXIMO
        dy = destino_y - origem_y
        angulo = math.atan2(dy, dx)
        
        self.velocidade_x = math.cos(angulo) * velocidade_passe
        self.velocidade_y = math.sin(angulo) * velocidade_passe
        self.sincronizar_coordenadas_float() # SINCRONIZA
        
        
    def resetar(self, neymar):
        """SEGURANÇA PRA EVITAR DA BOLA SAIR DO MAPA"""
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.em_movimento = False
        self.no_chao_esperando = False
        neymar.tem_bola = True
            
            
        
            
        