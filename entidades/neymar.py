import pygame
import math
import random
from gerenciamento.funcoes_importantes import prender_neymar_campo
from entidades.bola import Bola
from entidades.coletaveis import Coletavel
from gerenciamento.constants import (LARGURA_TELA, ALTURA_TELA, VELOCIDADE_NEY, COR_NEYMAR, FORCA_CHUTE, TUPLA_LIMITES_CAMPO, DRIBLES_CONFIG)
from animacao.ney_animado import NeymarAnimacao

class Neymar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # 🌟 INSTANCIA O MONITOR DE ANIMAÇÃO EXTERNO
        self.animador = NeymarAnimacao()

        # Define a imagem inicial baseada no primeiro frame do animador
        if hasattr(self.animador, 'obter_imagem_inicial'):
            self.image = self.animador.obter_imagem_inicial()
        else:
            self.image = pygame.Surface((45, 40))
            self.image.fill(COR_NEYMAR)
            
        # Retângulo expandido (Hitbox controlada de 45x70)
        LARGURA_HITBOX = 45
        ALTURA_HITBOX = 70
        self.rect = pygame.Rect(0, 0, LARGURA_HITBOX, ALTURA_HITBOX)

        # Posicionamento inicial na tela
        self.rect.centerx = LARGURA_TELA // 2
        self.rect.centery = ALTURA_TELA - 100

        # 🌟 CAMADA INICIAL PADRÃO (Usando o underline para a propriedade)
        self._layer = 5

        self.velocidade = VELOCIDADE_NEY
        self.barra_estrela = 0
        self.tem_bola = False
        self.tempo_ultimo_passe = 0
        self.tempo_ultimo_chute = 0

        # Controle de drible e especial
        self.bola_em_drible = False
        self.tempo_inicio_drible = 0
        self.drible_efetivo = False
        self.ney_prime = False 
        self.tempo_prime = 0
        self.confianca = 0
        self.ultimo_tipo_drible = 'manual'

        # Variáveis de estado para animação e direção
        self.em_movimento = False
        self.olhando_para = "frente" # Pode ser "frente" ou "costas"

    # 🌟 PROPERTY PARA GERENCIAR AS CAMADAS DE FORMA SEGURA NO PYGAME
    @property
    def layer(self):
        return self._layer

    @layer.setter
    def layer(self, nova_camada):
        self._layer = nova_camada
        if self.groups():
            for grupo in self.groups():
                if hasattr(grupo, 'change_layer'):
                    grupo.change_layer(self, nova_camada)

    def mover(self, teclas, bola, grupo_zagueiros):
        """
        Controla a movimentação física do Neymar e atualiza dinamicamente 
        as camadas (Z-order) para o correto desenho da bola.
        """
        self.em_movimento = False

        # Vetor de movimento para o frame atual
        dx = 0
        dy = 0

        if teclas[pygame.K_a]:
            dx = -self.velocidade
            self.em_movimento = True
            # Se você implementar esquerda futuramente: self.olhando_para = "esquerda"
        if teclas[pygame.K_d]:
            dx = self.velocidade
            self.em_movimento = True
            # Se você implementar direita futuramente: self.olhando_para = "direita"
            
        if teclas[pygame.K_w]:
            dy = -self.velocidade
            self.em_movimento = True
            self.olhando_para = "costas"
        if teclas[pygame.K_s]:
            dy = self.velocidade
            self.em_movimento = True
            self.olhando_para = "frente"

        # Aplica o movimento ao rect (adicione suas colisões com zagueiros aqui se houver)
        self.rect.x += dx
        self.rect.y += dy

        # 🌟 O PULO DO GATO: ATUALIZAÇÃO DE CAMADAS DINÂMICAS 🌟
        if self.tem_bola:
            if self.olhando_para == "costas":
                # Quando anda para trás, o Neymar vai para a camada de baixo (4)
                # Como a bola na condução de costas assume camada 7, ela fica na FRENTE das pernas.
                self.layer = 4
            else:
                # Padrão normal correndo para frente ou lados
                self.layer = 5

    def update(self):
        """
        Atualiza os frames da animação baseando-se no estado atual do jogador.
        """
        # Chama a lógica do seu script de animações externo
        if hasattr(self.animador, 'atualizar_frames'):
            self.image = self.animador.atualizar_frames(self.em_movimento, self.olhando_para)
    
            
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
        
        # SE FOR O MODO NEY PRIME ELE FICA COM 95% DE CHANCE DE FAZER O GOL
        if self.ney_prime:
            probabilidade_gol = 0.95
        
        # SE NAO FOR O MODO NEY PRIME AI ELE ENTRA NESSE CALCULO DA DISTANCIA E TUDO MAIS
        else:
            # CÁLCULO DA DISTÂNCIA
            distancia = math.hypot(centro_gol_x - self.rect.centerx, centro_gol_y - self.rect.centery)
            
            # QUANTO MAIS PERTO, MAIOR A CHANCE COM MAXIMO DE 0.95 E MINIMO DE 0.05
            fator_distancia = max(0.05, min(0.95, 1.0 - (distancia / 1000.0)))

            # CÁLCULO DA CONFIANÇA O MINIMO É ZERO E O MAXIMO É 100
            fator_confianca = max(0.0, min(1.0, self.confianca / 100.0))

            # PROBABILIDADE FINAL == UM PESO DE 60% PRA DISTANCIA E UM PESO DE 40% PRA CONFIANCA (talvez possamos mudar isso daqui)
            probabilidade_gol = (fator_distancia * 0.65) + (fator_confianca * 0.35)

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
        
        # SO ATUALIZA SE TIVER NO MODO NEY PRIME PRA NAO FICAR MUITA APELAÇÃO
        if not self.ney_prime:
            self.confianca += valor
        
        # Garante que a confiança não fique negativa
        if self.confianca < 0:
            self.confianca = 0
        
        if self.confianca >= 100:
            self.confianca = 0
            
    def calcular_chance_drible(self, tipo_drible):
        """APLICA A FORMULA PRA CALCULAR SE DRIBLOU OU NAO"""
        
        # SE ELE TIVER NO PRIME, ELE NUNCA ERRA DRIBLE
        if self.ney_prime:
            return 1.0
        
        c_ini = DRIBLES_CONFIG[tipo_drible]['chance_inicial']
        c_max = DRIBLES_CONFIG[tipo_drible]['chance_max']
        
        chance = c_ini + ((self.confianca / 100.0) * (c_max - c_ini))
        
        if getattr(self, 'ney_prime', False):
            return 1.0
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
            if zagueiro.preparo_pro_bote and not zagueiro.driblado and not zagueiro.atordoado_por_drible:
                dx = zagueiro.rect.centerx - bola.rect.centerx
                dy = zagueiro.rect.centery - bola.rect.centery
                
                distancia_bola_zagueiro = math.hypot(dx, dy)
            
               # ESSA CONDICIONAL VERIFICA SE ESTA NA DISTANCIA IDEAL PRA APLICAR O DRIBLE
                if 95 <= distancia_bola_zagueiro <= 140:
                    
                    if self.drible_efetivo:
                        break
                    
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
                        zagueiro_mais_proximo.ficar_atordoado_por_drible(tempo=1500) # ATORDOAMENTO DE 1.5s
                        self.bola_em_drible = True
                        self.drible_efetivo = True
                        self.tempo_inicio_drible = pygame.time.get_ticks()
                        self.ultimo_tipo_drible = tipo_drible
                    else:
                        print('errou o drible')


