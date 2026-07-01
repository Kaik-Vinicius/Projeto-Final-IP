import pygame
from gerenciamento.constants import FORCA_LANCAMENTO_ALIADO
from assets.animacao.aliado_animado import AliadoAnimado

class Aliado(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.animador = AliadoAnimado()
        
        # DEFINE O RETANGULO COMO O TAMANHO DO SPRITE
        self.image = self.animador.obter_imagem_inicial()
        self.rect = self.image.get_rect()

        self.rect.centerx = pos_x
        self.rect.centery = pos_y

        self.tem_bola = False
        self.tempo_recebeu_bola = 0
        self.tempo_reacao = 1000
        self.tempo_ultimo_passe = 0

        # OFFSETS DA BOLA PRA MANTER ALINHADO COM O PÉ
        self.offset_bola_x = 0   
        self.offset_bola_y = 49

    def receber_bola(self):
        if not self.tem_bola:
            self.tem_bola = True
            self.tempo_recebeu_bola = pygame.time.get_ticks()

    def atualizar_cronometro(self, neymar, bola):
        if self.tem_bola:
            bola.rect.centerx = self.rect.centerx + self.offset_bola_x
            bola.rect.centery = self.rect.centery + self.offset_bola_y
            bola.dono = self 

            tempo_atual = pygame.time.get_ticks()

            if tempo_atual - self.tempo_recebeu_bola >= self.tempo_reacao:
                self.tem_bola = False
                self.tempo_ultimo_passe = tempo_atual
                bola.dono = None  

                teclas = pygame.key.get_pressed()

                if neymar.rect.centery >= self.rect.centery - 20:
                    destino_x = neymar.rect.centerx
                    destino_y = neymar.rect.centery
                else:
                    antecipacao = 120
                    if teclas[pygame.K_w]:
                        antecipacao = 200

                    destino_x = neymar.rect.centerx
                    destino_y = neymar.rect.centery - antecipacao
                
                bola.lancar_em_profundidade(self.rect.centerx, self.rect.centery, destino_x, destino_y, FORCA_LANCAMENTO_ALIADO)

    def desenhar_aliado_com_sombra(self, tela):
        """MÉTODO PARA DESENHAR O ALIADO POR CIMA DA SOMBRA DA FORMA CORRETA"""
        
        # PEGA A SOMBRA CONFIGURADA NO ANIMADOR
        sombra = self.animador.sombra_horizontal
        sombra_rect = sombra.get_rect()
        
        # ALINHA COM OS PES
        sombra_rect.center = self.rect.midbottom
        
        # AJUSTE PRA ENCAIXAR DEBAIXO DO SPRITE
        sombra_rect.centery -= 10
        
        # DESENHA PRIMEIRO A SOMBRA
        tela.blit(sombra, sombra_rect)
        
        # DEPOIS DESENHA O ALIADO
        tela.blit(self.image, self.rect)

    def update(self):
        # ATUALIZA A IMAGEM
        self.image = self.animador.atualizar_animacao()