# Jogo do Projeto Final de IP
https://docs.google.com/document/d/1SNAlg9n5pRUbYihomY0YJYzg-TBxjXq7mLdqfHWCqBc/edit?usp=sharing

Descrição Inicial:

Interface -> Possivelmente 2 pessoas (sugestão de divisão: pessoa 1 - Menu Inicial e Pause / pessoa 2 - Modo Espera e Criação de lances de gol) - dificuldade facil-medio
 - Menu Inicial:
  - 1ª tela do jogo, onde se escolhe a dificuldade
 - Menu Pause:
  - Abrir aba sobre o jogo, pausando o tempo
 - Modo Espera:
  - Tela onde os minutos passam esperando aparecer uma oportunidade de gol

Funcoes neymar - passe, drible, chute -> 2 pessoas muito provável (sem sugestão de divisão) - dificuldade medio-alto

 - Passe
  - Identificar seta de movimentação ou identificar jogador mais próximo?
  - Passe lento para o jogador que devolve com um passe rápido em direção à posição do neymar na hora do passe
 - Drible
  - Quando o aparecer uma exclamação no zagueiro, o usuario deve apertar um botão de drible, ativando temporariamente um estado de drible para a bola, impedindo ela de ser desarmada
 - Chute
  - Quando o usuario chutar, identificamos:
   - confiança
   - distância do gol
   - aleatoriedade
  - a partir do calculo, aparece um vídeo em pixel para cada caso de chute:
   - gol (dois angulos)
   - goleiro defende
   - bola na trave (duas traves)
   - bola pra fora (pros dois lados)

Zagueiro -> 1 pessoa - dificuldade medio-alto

 - Zagueiro sempre recebe a distância dele para a bola, estados:
  - Idle, nenhum dos casos, volta lentamente à posição base dele (lateral, zagueiro, volante)
  - Próximo à bola, anda em direção à bola
  - Muito próximo, aparece uma exclamação por 1 seg avisando que ele vai dar carrinho
  - Carrinho, dá um carrinho na direção da bola, vendo se driblou o não
  - Atordoamento, fica 1,5 seg parado em carrinho para voltar ao idle

Coletaveis - status do neymar -> 1 pessoa - dificuldade medio

 - bola, bola começa no lance como um passe, devendo ser buscada pelo neymar
 - estrela (ney prime), aparece raramente nos lances, ao pegar, neymar não perde a bola por 15 seg e os chutes ficam muito mais precisos (ex: 90% dos chutes são gol)
 - chuteira (energia), aparece com base no drible escolhido, ficando disponível para coleta por 0,5 seg, conta para o calculo do chute
