import pygame
from gerenciamento.constants import (LARGURA_TELA, ALTURA_TELA, VELOCIDADE_ZAG, COR_ZAGUEIRO, CONFIANCA_POR_DIFICULDADE, DRIBLES_CONFIG, META_ESTRELA, FORCA_CHUTE, POS_GOL_X, POS_GOL_Y)

# FIZ ALGUMAS MUDANÇAS NA CLASSE DO ZAGUEIRO, PRINCIPALMENTE PRA NAO BUGAR A POSICAO DE SPAWN DE CADA UM

class Zagueiro(pygame.sprite.Sprite):
    def __init__(self, pos_inicial_x, pos_inicial_y):
        super().__init__()
      
        # DEFININDO O RETANGULO DO ZAGUEIRO
        self.image = pygame.Surface((45,40))
        self.image.fill(COR_ZAGUEIRO)
        self.rect = self.image.get_rect()
      
        # ONDE ELE VAI SPAWNAR
        self.rect.centerx = pos_inicial_x
        self.rect.centery = pos_inicial_y

        # AQUI CADA ZAGUEIRO GUARDA SUA POSICAO INICIAL INDEPENDENTEMENTE
        self.spawn_x = pos_inicial_x
        self.spawn_y = pos_inicial_y
      
        self.velocidade = VELOCIDADE_ZAG # A VELOCIDADE QUE ELE VAI ANDAR

        #VARIAVEIS PARA O CARRINHO
        self.pausa = False
        self.tempo_pausa = 0
        self.preparo_pro_bote = False
        self.atordoamento_bote = False

        # ATRIBUTOS DE ATORDOAMENTO DO ZAGUEIRO
        self.atordoado_por_drible = False
        self.tempo_atordoado_drible = 0

        # VARIÁVEIS PARA O DIVIDIDO POR FRAMES PRA FICAR MAIS ORGANICO
        self.frames_do_dash = 0
        self.direcao_dash = pygame.math.Vector2(0, 0)
        self.forca_total_dash = 100

    def perseguir_bola(self, bola):
        # RECEBE A POSICAO X E Y DA BOLA
        bola_x = bola.rect.centerx
        bola_y = bola.rect.centery

        # CALCULA A DISTANCIA DO ZAGUEIRO PARA A BOLA
        dist_x = self.rect.centerx - bola_x
        dist_y = self.rect.centery - bola_y

        dist_total = ((dist_x ** 2) + (dist_y ** 2)) ** 0.5

        # NORMATIZA A DISTANCIA PARA UMA PERSGUICAO MAIS FLUIDA, EU ACHO
        norma_x = dist_x / dist_total
        norma_y = dist_y / dist_total

        # MOVE O ZAGUEIRO
        self.rect.x -= (norma_x * self.velocidade)
        self.rect.y -= (norma_y * self.velocidade)

        # MANTER DENTRO DA TELA
        self.rect.clamp_ip(pygame.Rect(0, 0, LARGURA_TELA, ALTURA_TELA))


    def perseguir_neymar(self, neymar):
        # RECEBE A POSICAO X E Y DO NEYMAR
        neymar_x = neymar.rect.centerx
        neymar_y = neymar.rect.centery

        # CALCULA A DISTANCIA DO ZAGUEIRO PARA O NEYMAR
        dist_x = self.rect.centerx - neymar_x
        dist_y = self.rect.centery - neymar_y

        dist_total = ((dist_x ** 2) + (dist_y ** 2)) ** 0.5


        # NORMATIZA A DISTANCIA PARA UMA PERSGUICAO MAIS FLUIDA, EU ACHO
        norma_x = dist_x / dist_total
        norma_y = dist_y / dist_total

        # MOVE O ZAGUEIRO
        self.rect.x -= (norma_x * self.velocidade)
        self.rect.y -= (norma_y * self.velocidade)

        # MANTER DENTRO DA TELA
        self.rect.clamp_ip(pygame.Rect(0, 0, LARGURA_TELA, ALTURA_TELA))

    def idle(self):
        # MUDANÇA FEITA PRA ATUALIZAR AS VARIAVEIS DE SPAWN DE CADA ZAGUEIRO INDIVIDUALMENTE
        if(self.rect.centerx != self.spawn_x and self.rect.centery != self.spawn_y):
            # RECUPERANDO A POSIÇÂO INICIAL DO ZAGUEIRO
            pos_inicial_x = self.spawn_x
            pos_inicial_y = self.spawn_y

            # CALCULA A DISTANCIA DO ZAGUEIRO PARA SUA POSIÇÃO INICIAL
            dist_x = self.rect.centerx - pos_inicial_x
            dist_y = self.rect.centery - pos_inicial_y

            dist_total = ((dist_x ** 2) + (dist_y ** 2)) ** 0.5

            # NORMATIZA A DISTANCIA PARA VOLTAR PARA A POSIÇÃO INICIAL
            norma_x = dist_x / dist_total
            norma_y = dist_y / dist_total

            # MOVE O ZAGUEIRO
            self.rect.x -= (norma_x * self.velocidade) / 1.5
            self.rect.y -= (norma_y * self.velocidade) / 1.5

    def iniciar_carrinho(self, bola):
        #CRIANDO UM VETOR DO ZAGUEIRO PARA A BOLA
        pos_zag = pygame.math.Vector2(self.rect.centerx, self.rect.centery)
        pos_bola = pygame.math.Vector2(bola.rect.centerx, bola.rect.centery)
        direcao = pos_bola - pos_zag

        #NORMATIZA O VETOR E PREPARA O CARRINHO/DASH
        if direcao.length() > 0: #PRA NAO CRASHR SE O VETOR FOR 0
            self.direcao_dash = direcao.normalize()
            self.frames_do_dash = 3  # O dash vai durar exatamente 3 frames
        else:
           self.frames_do_dash = 0

    # NOVO MÉTODO PRA O ZAGUEIRO FICAR ATORDOADO POR CAUSA DO DRIBLE
    def ficar_atordoado_por_drible(self, tempo):
        """METODO CHAMADO PELO NEYMAR PARA CONGELAR O MARCADOR APOS UM DRIBLE OU DESVIO"""
        self.atordoado_por_drible = True
        self.preparo_pro_bote = False
        self.pausa = False
        self.frames_do_dash = 0
        self.tempo_atordoado_drible = pygame.time.get_ticks() + tempo

    def atualizar(self, neymar, bola, distancia_neymar, distancia_bola, alguem_com_bola):
        tempo_atual = pygame.time.get_ticks()
        
        # 
        if self.atordoado_por_drible:
            if tempo_atual >= self.tempo_atordoado_drible:
                self.atordoado_por_drible = False
            return

        if self.frames_do_dash > 0:
            # DIVIDE O COMPRIMENTO DO DASH PELA QUANTIDADE FIXA DE FRAMES (3)
            passo = self.forca_total_dash / 3
          
            # MOVE 1/3 DA DISTANCIA DO DASH EM CADA FRAME
            self.rect.centerx += int(self.direcao_dash.x * passo)
            self.rect.centery += int(self.direcao_dash.y * passo)
            self.rect.clamp_ip(pygame.Rect(0, 0, LARGURA_TELA, ALTURA_TELA))
          
            self.frames_do_dash -= 1 #CONTABILIZANDO OS FRAMES
          
            # ACABOU O DASH, GUARDA O TEMPO EM QUE O DASH ACABOU
            if self.frames_do_dash == 0:
                self.atordoamento_bote = True
                self.tempo_pausa = pygame.time.get_ticks()
            return #GARANTIR QUE NADA MAIS ACONTEÇA


        # FICA PARADO POR 1 SEGUNDO DEPOIS DO DASH
        if self.atordoamento_bote:
            if tempo_atual - self.tempo_pausa >= 1000:
                self.atordoamento_bote = False
            return #GARANTIR QUE NADA MAIS ACONTEÇA


        # PREPARO DO DASH, 1 SEGUNDO PARADO PRA COMEÇAR
        if self.preparo_pro_bote:
            if not self.pausa:
                self.pausa = True
                self.tempo_pausa = tempo_atual
            else:
                if tempo_atual - self.tempo_pausa >= 500:
                    self.pausa = False
                    self.preparo_pro_bote = False
                  
                    #CHAMA O INÍCIO DO DASH/CARRINHO
                    self.iniciar_carrinho(bola)
            return


        # CONTROLE MOVIMENTAÇÃO BÁSICA DO ZAGUEIRO
        if distancia_bola < 80 and not bola.em_movimento:
            self.preparo_pro_bote = True
        elif distancia_bola < 80 and neymar.tem_bola:
            self.preparo_pro_bote = True
        elif distancia_bola < 150 and not neymar.tem_bola and not alguem_com_bola:
            self.perseguir_bola(bola)
        elif distancia_neymar < 300 or alguem_com_bola:
            self.perseguir_neymar(neymar)
        else:
            self.idle()
    
    def esta_em_idle(self):
        # RETORNA TRUE SE O ZAGUEIRO ESTIVER EM IDLE, SE ESTIVER FAZENDO QUALQUER OUTRA COISA ELE RETORNA FALSE
        # ALTERAÇÃO PRA CHECAR TAMBEM SE NAO ESTA EM DRIBLE
        if not self.preparo_pro_bote and not self.atordoamento_bote and self.frames_do_dash == 0 and not self.atordoado_por_drible:
            return True
        return False