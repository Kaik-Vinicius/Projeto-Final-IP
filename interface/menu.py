import pygame
from gerenciamento.constants import LARGURA_TELA, ALTURA_TELA
class MenuInicial:
    def __init__(self, largura_tela, altura_tela):
        self.LARGURA_TELA = largura_tela
        self.ALTURA_TELA = altura_tela

        # Carrega o plano de fundo e garante que ele preencha a tela toda (1920x1080)
        self.fundo = pygame.image.load("assets/menu_inicial/fundo_menu.png")
        self.fundo = pygame.transform.scale(self.fundo, (self.LARGURA_TELA, self.ALTURA_TELA))

        # Sprites do Botão Jogar
        self.botao_jogar_normal = pygame.image.load("assets/menu_inicial/botao_jogar/botao_normal.png").convert_alpha()
        self.botao_jogar_hover = pygame.image.load("assets/menu_inicial/botao_jogar/botao_hover.png").convert_alpha()
        self.botao_jogar_press = pygame.image.load("assets/menu_inicial/botao_jogar/botao_pressed.png").convert_alpha()

        # Sprites do Botão Quit
        self.botao_quit_normal = pygame.image.load("assets/menu_inicial/botao_quit/botao_quit_normal.png").convert_alpha()
        self.botao_quit_hover = pygame.image.load("assets/menu_inicial/botao_quit/botao_quit_hover.png").convert_alpha()
        self.botao_quit_press = pygame.image.load("assets/menu_inicial/botao_quit/botao_quit_pressed.png").convert_alpha()

        # Retângulos de Colisão e Posicionamento (Perfeitamente alinhados na tela)
        self.botao_rect = self.botao_jogar_normal.get_rect(center=(self.LARGURA_TELA // 2, 870))
        self.botao_quit_rect = self.botao_quit_normal.get_rect(topright=(self.LARGURA_TELA - 30, 30))

        self.botao_jogar_pressed = False
        self.botao_quit_pressed = False

    def tratar_eventos(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1 and self.botao_rect.collidepoint(evento.pos):
                self.botao_jogar_pressed = True

            if evento.button == 1 and self.botao_quit_rect.collidepoint(evento.pos):
                self.botao_quit_pressed = True
        
        if evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                if self.botao_jogar_pressed and self.botao_rect.collidepoint(evento.pos):
                    self.botao_jogar_pressed = False
                    return "jogar"
                
                self.botao_jogar_pressed = False

                if self.botao_quit_pressed and self.botao_quit_rect.collidepoint(evento.pos):
                    self.botao_quit_pressed = False
                    return "quit"

                self.botao_quit_pressed = False

        return None
    
    def desenhar(self, tela):
        tela.blit(self.fundo, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        # Renderização do estado visual do botão Jogar
        if self.botao_jogar_pressed and self.botao_rect.collidepoint(mouse_pos):
            tela.blit(self.botao_jogar_press, self.botao_rect)
        elif self.botao_rect.collidepoint(mouse_pos):
            tela.blit(self.botao_jogar_hover, self.botao_rect)
        else:
            tela.blit(self.botao_jogar_normal, self.botao_rect)

        # Renderização do estado visual do botão Quit
        if self.botao_quit_pressed and self.botao_quit_rect.collidepoint(mouse_pos):
            tela.blit(self.botao_quit_press, self.botao_quit_rect)
        elif self.botao_quit_rect.collidepoint(mouse_pos):
            tela.blit(self.botao_quit_hover, self.botao_quit_rect)
        else:
            tela.blit(self.botao_quit_normal, self.botao_quit_rect)

class MenuDificuldade:
    def __init__(self, largura_tela, altura_tela):
        self.LARGURA_TELA = largura_tela
        self.ALTURA_TELA = altura_tela

        # Carrega o plano de fundo e garante que ele preencha a tela toda (1920x1080)
        self.fundo = pygame.image.load("assets/menu_dificuldade/fundo_menu_dificuldade.png")
        self.fundo = pygame.transform.scale(self.fundo, (self.LARGURA_TELA, self.ALTURA_TELA))

        # Sprites dos Botões de Dificuldade
        self.botao_facil_normal = pygame.image.load("assets/menu_dificuldade/botao_facil/botao_facil1.png").convert_alpha()
        self.botao_facil_hover = pygame.image.load("assets/menu_dificuldade/botao_facil/botao_facil2.png").convert_alpha()
        self.botao_facil_press = pygame.image.load("assets/menu_dificuldade/botao_facil/botao_facil3.png").convert_alpha()

        self.botao_medio_normal = pygame.image.load("assets/menu_dificuldade/botao_medio/botao_medio1.png").convert_alpha()
        self.botao_medio_hover = pygame.image.load("assets/menu_dificuldade/botao_medio/botao_medio2.png").convert_alpha()
        self.botao_medio_press = pygame.image.load("assets/menu_dificuldade/botao_medio/botao_medio3.png").convert_alpha()

        self.botao_dificil_normal = pygame.image.load("assets/menu_dificuldade/botao_dificil/botao_dificil1.png").convert_alpha()
        self.botao_dificil_hover = pygame.image.load("assets/menu_dificuldade/botao_dificil/botao_dificil2.png").convert_alpha()
        self.botao_dificil_press = pygame.image.load("assets/menu_dificuldade/botao_dificil/botao_dificil3.png").convert_alpha()

        # Retângulos de Colisão e Posicionamento
        self.botao_facil_rect = self.botao_facil_normal.get_rect(center=(960, 430))
        self.botao_medio_rect = self.botao_medio_normal.get_rect(center=(960, 550))
        self.botao_dificil_rect = self.botao_dificil_normal.get_rect(center=(960, 670))

        # Estados de pressionamento dos botões
        self.botao_facil_pressed = False
        self.botao_medio_pressed = False
        self.botao_dificil_pressed = False

    def tratar_eventos(self, evento):
        pos_mouse = pygame.mouse.get_pos()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if self.botao_facil_rect.collidepoint(pos_mouse):
                    self.botao_facil_pressed = True

                elif self.botao_medio_rect.collidepoint(pos_mouse):
                    self.botao_medio_pressed = True

                elif self.botao_dificil_rect.collidepoint(pos_mouse):
                    self.botao_dificil_pressed = True

        if evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                if self.botao_facil_pressed and self.botao_facil_rect.collidepoint(pos_mouse):
                    self.botao_facil_pressed = False
                    return "facil"

                elif self.botao_medio_pressed and self.botao_medio_rect.collidepoint(pos_mouse):
                    self.botao_medio_pressed = False
                    return "medio"

                elif self.botao_dificil_pressed and self.botao_dificil_rect.collidepoint(pos_mouse):
                    self.botao_dificil_pressed = False
                    return "dificil"

                self.botao_facil_pressed = False
                self.botao_medio_pressed = False
                self.botao_dificil_pressed = False

        return None
        
    def desenhar(self, tela):
        tela.blit(self.fundo, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        # Renderização do estado visual do botão Fácil
        if self.botao_facil_pressed and self.botao_facil_rect.collidepoint(mouse_pos):
            tela.blit(self.botao_facil_press, self.botao_facil_rect)
        elif self.botao_facil_rect.collidepoint(mouse_pos):
            tela.blit(self.botao_facil_hover, self.botao_facil_rect)
        else:
            tela.blit(self.botao_facil_normal, self.botao_facil_rect)

        # Renderização do estado visual do botão Médio
        if self.botao_medio_pressed and self.botao_medio_rect.collidepoint(mouse_pos):
            tela.blit(self.botao_medio_press, self.botao_medio_rect)
        elif self.botao_medio_rect.collidepoint(mouse_pos):
            tela.blit(self.botao_medio_hover, self.botao_medio_rect)
        else:
            tela.blit(self.botao_medio_normal, self.botao_medio_rect)

        # Renderização do estado visual do botão Difícil
        if self.botao_dificil_pressed and self.botao_dificil_rect.collidepoint(mouse_pos):
            tela.blit(self.botao_dificil_press, self.botao_dificil_rect)
        elif self.botao_dificil_rect.collidepoint(mouse_pos):
            tela.blit(self.botao_dificil_hover, self.botao_dificil_rect)
        else:
            tela.blit(self.botao_dificil_normal, self.botao_dificil_rect)