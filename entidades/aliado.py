import pygame
from gerenciamento.constants import FORCA_LANCAMENTO_ALIADO

class Aliado(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.image = pygame.Surface((45, 40))
        self.image.fill((100, 149, 237))
        self.rect = self.image.get_rect()

        self.rect.centerx = pos_x
        self.rect.centery = pos_y

        self.tem_bola = False
        self.tempo_recebeu_bola = 0
        self.tempo_reacao = 1000

        self.tempo_ultimo_passe = 0

    def receber_bola(self):
        """
        ATIVA QUANDO A BOLA ENCOSTA NO ALIADO
        """
        if not self.tem_bola:
            self.tem_bola = True
            self.tempo_recebeu_bola = pygame.time.get_ticks()

    def atualizar_cronometro(self, neymar, bola):
        """
        CHECA O TEMPO PARA DEVOLVER A BOLA
        """
        if self.tem_bola:
            tempo_atual = pygame.time.get_ticks()

            if tempo_atual - self.tempo_recebeu_bola >= self.tempo_reacao:
                self.tem_bola = False
                self.tempo_ultimo_passe = tempo_atual

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
                
                # LANÇA A BOLA DE VOLTA PRA O NEYMAR
                bola.lancar_em_profundidade(self.rect.centerx, self.rect.centery, destino_x, destino_y, FORCA_LANCAMENTO_ALIADO)