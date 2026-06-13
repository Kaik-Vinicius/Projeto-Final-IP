import pygame
import math
from bola import Bola
from constants import (LARGURA_TELA, ALTURA_TELA, VELOCIDADE_NEY, COR_NEYMAR, CONFIANCA_POR_DIFICULDADE, DRIBLES_CONFIG, META_ESTRELA, FORCA_CHUTE, POS_GOL_X, POS_GOL_Y)


class Neymar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # DEFININDO O RETANGULO DO NEYMAR
        self.image = pygame.Surface((45,40))
        self.image.fill(COR_NEYMAR)
        self.rect = self.image.get_rect()
        
        # ONDE ELE VAI SPAWNAR INICIALMENTE PRA TESTES
        self.rect.centerx = LARGURA_TELA // 2
        self.rect.centery = ALTURA_TELA - 100
        
        self.velocidade = VELOCIDADE_NEY # A VELOCIDADE QUE ELE VAI ANDAR
        
        # OBS.: AINDA FALTA IMPLEMENTAR AQUI DEPOIS O SISTEMA PRA QUANDO O USUARIO ESCOLHER A
        # DIFICULDADE, QUE, A DEPENDER DELA, VAI TER CONFIANÇAS DIFERENTES
        
        
        # isso daqui por enquanto nao vai servir muito
        # por enquanto eu so quero ver o neymar andando no campo
        self.barra_estrela = 0
        self.tem_bola = False
        
        # ATRIBUTO DE SEGURANÇA PRA O PASSE
        self.tempo_ultimo_passe = 0
        
    def mover(self, teclas):
        """
        MOVE O NEYMAR COM AS TECLAS W-A-S-D
        """
        
        dx = 0
        dy = 0
        
        # TECLAS DE MOVIMENTO SÃO: W-A-S-D
        
        # PRA OS LADOS:
        if teclas[pygame.K_a]:
            dx += -self.velocidade
        if teclas[pygame.K_d]:
            dx += self.velocidade
        
        # PRA CIMA E PRA BAIXO:
        if teclas[pygame.K_w]:
            dy += -self.velocidade 
        if teclas[pygame.K_s]:
            dy += self.velocidade    
            
        # MOVENDO O OBJETO DEPOIS DE APERTAR UMA TECLA
        self.rect.x += dx
        self.rect.y += dy   
        
        # NAO VAI DEIXAR O NEY SAIR DA TELA
        self.rect.clamp_ip(pygame.Rect(0, 0, LARGURA_TELA, ALTURA_TELA)) 
    
    def dar_passe(self, bola, grupo_aliados):
        """ PROCURA O ALIADO MAIS PROXIMO PRA DAR O PASSE """
        
        if self.tem_bola == True and len(grupo_aliados) > 0:
            aliado_mais_proximo = None
            distancia_minima = float('inf')  # coloca um valor infinito logo de cara pra fazer a comparacao
            
            # ESSE FOR VAI "VARRER" TODOS OS ALIADOS DO GRUPO DE ALIADOS
            # E VER QUAL É O QUE ESTÁ MAIS PRÓXIMO
            for aliado in grupo_aliados:
                
                dx = aliado.rect.centerx - self.rect.centerx
                dy = aliado.rect.centery - self.rect.centery
                distancia = math.hypot(dx, dy)
                
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    aliado_mais_proximo = aliado
                    
            if aliado_mais_proximo:
                
                # REGISTRA O TEMPO DO PASSE DO NEYMAR
                self.tempo_ultimo_passe = pygame.time.get_ticks()
                
                self.tem_bola = False # NEYMAR DEPOIS QUE PASSA A BOLA, ELE PERDE A POSSE DELA
                
                # ESSE 12 É A VELOCIDADE DO PASSE, MAS DEPOIS É SO MUDAR O VALOR OU ATRIBUIR UMA VARIAVEL NAS CONSTANTES
                bola.passar(self.rect.centerx, self.rect.centery, aliado_mais_proximo.rect.centerx, aliado_mais_proximo.rect.centery, 12)
                
                
    def chutar_pro_gol(self, bola):
        """ FAZ O NEYMAR MANDAR UMA BOMBA DIRETO EM DIREÇÃO AO GOL """
        if self.tem_bola:
            # CHAMA O METODO DA BOLA PRA CHUTAR
            bola.chutar(FORCA_CHUTE)
            
            #NEYMAR PERDE A POSSE DA BOLA
            self.tem_bola = False
        
            