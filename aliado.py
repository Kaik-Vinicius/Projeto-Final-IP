import pygame


# =-=-=-= CLASSE APENAS PRA COLOCAR O ALIADO NO CMAPO =-=-=-=
class Aliado(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        
        # VISUAL DO ALIADO 
        self.image = pygame.Surface((45,40))
        self.image.fill((100, 149, 237)) # UMA COR MEIO AZUL
        self.rect = self.image.get_rect()
        
        # DEFININDO A POSICAO QUE ELE VAI FICAR
        self.rect.centerx = pos_x
        self.rect.centery = pos_y
        
        
        
        
    
        