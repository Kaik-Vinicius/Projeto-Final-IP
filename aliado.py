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
        
        self.tem_bola = False # INICIALMENTE ELE NAO VAI TER BOLA
        self.tempo_recebeu_bola = 0 # O TEMPO QUE ELE VAI RECEBER A BOLA
        self.tempo_reacao = 1000 # O TEMPO ED REAÇÃO DELE PRA FAZER A TABELA COM O NEYMAR
        
        # TEMPO DE CONTROLE PRA EVITAR RE-DOMINIO DA BOLA PELO ALIADO
        self.tempo_ultimo_passe = 0
        
        
    def receber_bola(self):
        """
       ATIVA SOMENTE QUANDO A BOLA ENCOSTA NO ALIADO
        """
        
        if not self.tem_bola:
            self.tem_bola = True
            # SALVA O EXATO MOMENTO QUE O ALIADO RECEBE A BOLA
            self.tempo_recebeu_bola = pygame.time.get_ticks()
        
    def atualizar_cronometro(self, neymar, bola):
        """
        CHECA O RELOGIO VARIAS VEZES ATE ULTRAPASSSAR O MINIMO QUE SEJA O TEMPO DE REAÇÃO
        """
        if self.tem_bola:
            tempo_atual = pygame.time.get_ticks()
            
            # SE A DIFERENÇA PASSAR DE UM SEGUNDO ELE VAI DEVOLVER A BOLA PRA O NEYMAR
            if tempo_atual - self.tempo_recebeu_bola >= self.tempo_reacao:
                self.tem_bola = False  # TIRA A BOLA DELE
                
                # TEMPO QUE VAI SER SUFICIENTE PRA BOLA SAIR DO PE DELE E ELE NAO PEGA-LA DE VOLTA
                # ISSO VAI DAR TEMPO DE SAIR DO RANGE DELE E CHEGAR ATE O NEYMAR
                self.tempo_ultimo_passe = pygame.time.get_ticks()
                
                # SISTEMA PRA VER QUAIS TECLAS ESTAO ATIVAS PRA PODER ANTECIPAR UM POUCO MAIS O PASSE
                teclas = pygame.key.get_pressed()
                
                # SE O NEYMAR TIVER ATRAS DO JOGADOR, ELE FAZ UM PASSE RECUADO, NAO JOGA EXATAMENTE NA FRENTE DELE
                if neymar.rect.centery >= self.rect.centery - 20:
                    destino_x = neymar.rect.centerx
                    destino_y = neymar.rect.centery
                
                
                # se ele ja tiver andando pra frente, antecipa um pouco mais
                else:
                    antecipacao = 120
                    if teclas[pygame.K_w]:
                        antecipacao = 200
                
                    # ATE A ONDE A BOLA TEM QUE IR EM PROFUNDIDADE PRA O NEYMAR
                    destino_x = neymar.rect.centerx
                    destino_y = neymar.rect.centery - antecipacao
                
                bola.lancar_em_profundidade(self.rect.centerx, self.rect.centery, 
                            destino_x, destino_y, 12)
               
        
        
        
    
        