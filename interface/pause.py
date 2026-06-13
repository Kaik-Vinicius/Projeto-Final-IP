import pygame

from constants import LARGURA_TELA
from constants import ALTURA_TELA

class BotaoPause:
    def __init__(self, LARGURA_TELA, ALTURA_TELA):
        self.LARGURA_TELA = LARGURA_TELA
        self.ALTURA_TELA = ALTURA_TELA

        self.botao_pause_normal = pygame.image.load("assets/menu_pause/botao_pause/botao_pause_n.png").convert_alpha()
        self.botao_pause_hover = pygame.image.load("assets/menu_pause/botao_pause/botao_pause_h.png").convert_alpha()
        self.botao_pause_press = pygame.image.load("assets/menu_pause/botao_pause/botao_pause_p.png").convert_alpha()

        self.botao_rect= self.botao_pause_normal.get_rect(topright=(self.LARGURA_TELA - 30, 30))

        self.botao_pause_pressed = False

    def tratar_eventos(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            
            if evento.button == 1 and self.botao_rect.collidepoint(evento.pos):
                self.botao_pause_pressed = True
        
        if evento.type == pygame.MOUSEBUTTONUP:
            if evento.button==1:
                if self.botao_pause_pressed and self.botao_rect.collidepoint(evento.pos):
                    self.botao_pause_pressed = False
                    return "pause"
                
                self.botao_pause_pressed = False

        return None
    
    def desenhar(self, tela):
        mouse_pos = pygame.mouse.get_pos()

        if self.botao_pause_pressed and self.botao_rect.collidepoint(mouse_pos):
            tela.blit(self.botao_pause_press, self.botao_rect)
        elif self.botao_rect.collidepoint(mouse_pos):
            tela.blit(self.botao_pause_hover, self.botao_rect)
        else:
            tela.blit(self.botao_pause_normal, self.botao_rect)

class MenuPause:
    def __init__(self, LARGURA_TELA, ALTURA_TELA):
        self.LARGURA_TELA = LARGURA_TELA
        self.ALTURA_TELA = ALTURA_TELA

        # IMAGENS DOS BOTÕES DO MENU DE PAUSE

        self.botao_retomar_normal = pygame.image.load("assets/menu_pause/botao_retomar/botao_retomar_n.png").convert_alpha()
        self.botao_retomar_hover = pygame.image.load("assets/menu_pause/botao_retomar/botao_retomar_h.png").convert_alpha()
        self.botao_retomar_press = pygame.image.load("assets/menu_pause/botao_retomar/botao_retomar_p.png").convert_alpha()

        self.botao_retomar_rect = self.botao_retomar_normal.get_rect(center=(self.LARGURA_TELA // 2, 450))
        self.botao_retomar_pressed = False


        self.botao_inicio_normal = pygame.image.load("assets/menu_pause/botao_menu_inicial/botao_inicio_n.png").convert_alpha()
        self.botao_inicio_hover = pygame.image.load("assets/menu_pause/botao_menu_inicial/botao_inicio_h.png").convert_alpha()
        self.botao_inicio_press = pygame.image.load("assets/menu_pause/botao_menu_inicial/botao_inicio_p.png").convert_alpha()

        self.botao_inicio_rect = self.botao_inicio_normal.get_rect(center=(self.LARGURA_TELA // 2, 590))
        self.botao_inicio_pressed = False

    def tratar_eventos(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if self.botao_retomar_rect.collidepoint(evento.pos):
                    self.botao_retomar_pressed = True
                elif self.botao_inicio_rect.collidepoint(evento.pos):
                    self.botao_inicio_pressed = True
        
        if evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                if self.botao_retomar_pressed and self.botao_retomar_rect.collidepoint(evento.pos):
                    self.botao_retomar_pressed = False
                    return "retomar"
                elif self.botao_inicio_pressed and self.botao_inicio_rect.collidepoint(evento.pos):
                    self.botao_inicio_pressed = False
                    return "menu_inicial"
                
                self.botao_retomar_pressed = False
                self.botao_inicio_pressed = False

        return None

    def desenhar(self, tela):
        # DESENHA O FUNDO DE TRANSPARÊNCIA
        fundo_transparente = pygame.Surface((self.LARGURA_TELA, self.ALTURA_TELA), pygame.SRCALPHA)
        fundo_transparente.fill((0, 0, 0, 180))
        tela.blit(fundo_transparente, (0, 0))

        #DESENHA OS BOTÕES DE RETOMAR E INÍCIO
        mouse_pos = pygame.mouse.get_pos()

        if self.botao_retomar_pressed and self.botao_retomar_rect.collidepoint(mouse_pos):
            tela.blit(self.botao_retomar_press, self.botao_retomar_rect)
        elif self.botao_retomar_rect.collidepoint(mouse_pos):
            tela.blit(self.botao_retomar_hover, self.botao_retomar_rect)
        else:
            tela.blit(self.botao_retomar_normal, self.botao_retomar_rect)

        if self.botao_inicio_pressed and self.botao_inicio_rect.collidepoint(mouse_pos):
            tela.blit(self.botao_inicio_press, self.botao_inicio_rect)
        elif self.botao_inicio_rect.collidepoint(mouse_pos):
            tela.blit(self.botao_inicio_hover, self.botao_inicio_rect)
        else:
            tela.blit(self.botao_inicio_normal, self.botao_inicio_rect)