# ⚽ Neymar Jr: The Last Dance

## 👥 Membros da Equipe
* **Darllan Wallace - < dwsf >**
* **Ivan Nicholas - < inss >**
* **Kaik Vinícius - < kvss >**
* **Luiz Apolinário - < lam8 >**
* **Pedro Henrique França - < phfs4 >**
* **Rafael Gonçalves - < rglc >**

---

## 📝 Sinopse do Jogo | Projeto de Introdução a Programação - CIn/UFPE

**Neymar Jr: The Last Dance** é um jogo de ação e estratégia esportiva em 2D desenvolvido em Pygame. No controle de um dos maiores camisas 10 da história do futebol, o seu objetivo é cruzar o campo, encarar zagueiros implacáveis e balançar as redes. 

Mas vencer não é apenas uma questão de correr: você precisará gerenciar a **Confiança** do craque em tempo real. Execute dribles manuais cirúrgicos ou firulas ousadas para deixar os defensores atordoados no gramado. À medida que seus dribles funcionam, sua barra de estrela se acumula até ativar o modo **Ney Prime** — um estado de genialidade pura onde a sua velocidade se torna devastadora e seus chutes ao gol alcançam 95% de precisão.

Trabalhe em equipe fazendo passes rápidos para seus aliados, desvie de botes agressivos da inteligência artificial e calcule a distância ideal para soltar a bomba contra o goleiro. Você tem o necessário para alcançar o topo do futebol arte?

---

# 📸 Capturas de Tela - Imagens do Software em Funcionamento

<img width="1905" height="1067" alt="image" src="https://github.com/user-attachments/assets/f179d27d-e3ff-422c-b74b-a847e4250efc" />
⚔️ Imagem inicial de abertura do jogo

---

<img width="1907" height="1062" alt="image" src="https://github.com/user-attachments/assets/1dd0dd19-020b-42df-a1c7-24f57a80159c" />
⚔️ Imagem do menu de dificuldade

---

<img width="1901" height="1062" alt="image" src="https://github.com/user-attachments/assets/735765a6-33a7-420b-9be4-8a7f65c8d775" />
⚔️ Imagem da tela de espera aguardando oportunidade de gol



## 🏗️ Arquitetura do Projeto e Organização do Código
O projeto foi estruturado utilizando o padrão de arquitetura orientada a objetos (POO) e divisão de responsabilidades em componentes, garantindo que a lógica de renderização, física e estados dos personagens ficassem isoladas.

### 📁 Estrutura de Assets do Projeto

Para garantir melhor organização da identidade visual do projeto, a pasta `assets/` foi dividida em subpastas que contêm os elementos gráficos do jogo separadamente:

```text
assets/
├── animacao/             # Sprites gerais do sistema de animação
├── arquibancada/         # Elementos gráficos do cenário e torcida
├── bola/                 # Frames da bola
├── campo/                # Texturas e linhas do gramado do jogo
├── chuteira/             # Sprites de itens colecionáveis/chuteiras
├── estrela/              # Sprite da estrela
├── fontes/               # Arquivos .ttf de tipografia do jogo
├── icones/               # Ícones de interface e HUD
├── jogadores/            # Sprites do Neymar (ney_idle, ney_run) e zagueiros
├── menu_dificuldade/     # Botões e layouts da tela de seleção de dificuldade
└── menu_inicial/         # Telas de fundo, botões e logos do menu principal
```

### 👾 Estrutura de Entidades do Jogo

Os personagens, objetos interativos e lógicas físicas estão concentrados no módulo `entidades/`. Cada arquivo representa uma classe independente que herda ou gerencia as propriedades de sprites do Pygame:

```text
entidades/
├── aliado.py        # Classe Aliado: Jogadores do mesmo time para dinâmica de passes
├── bola.py          # Classe Bola: Gerencia posse, offsets de movimento, chutes e física
├── coletaveis.py    # Classe Coletaveis: Itens que o Neymar coleta (ex: energéticos, estrelas)
├── goleiro.py       # Classe Goleiro: IA de defesa com comportamento baseado no resultado do chute
├── neymar.py        # Classe Neymar: Entidade principal controlada pelo jogador (inputs, velocidade)
└── zagueiro.py      # Classe Zagueiro: IA inimiga que arma o bote e pode ficar atordoada por dribles
```

### ⚙️ Módulo de Gerenciamento do Sistema

Contém as configurações globais indispensáveis e as funções utilitárias que servem de suporte para o funcionamento de todas as outras entidades do jogo:

```text
gerenciamento/
├── constants.py           # Constantes Globais: Guarda dimensões da tela, velocidades padrão, limites e presets
└── funcoes_importantes.py # Utilitários de Jogo: Funções genéricas cruciais (ex: conter personagens dentro do campo)
```

### 🖥️ Módulo de Interface do Usuário

Gerencia as telas de navegação, estados de transição e fluxos visuais que conectam o jogador ao loop principal do jogo:

```text
interface/
├── menu.py          # Classe Menu: Controla a tela inicial, seleção de dificuldade e botões
├── pause.py         # Classe BotaoPause: Interrompe o loop do jogo e exibe opções de retomada/menu inicial
└── tela_espera.py   # Funções que desempenham papéis visuais e interativos dentro do HUD do jogo e da tela de espera pra outras oportunidades
```
### 🚀 Arquivo Principal do Sistema

O arquivo `main.py` fica localizado diretamente na raiz do repositório e atua como o principal arquivo do jogo, unindo todas as peças que desenvolvemos:

```text
main.py              # Game Loop Principal: Inicializa o Pygame, gerencia eventos e renderiza as telas/entidades
```

## 🛠️ Ferramentas, Bibliotecas e Justificativas de Uso

O desenvolvimento do projeto priorizou o uso de tecnologias nativas do ecossistema Python aliadas a uma biblioteca especializada em jogos bidimensionais, garantindo alta performance na renderização de sprites e precisão matemática.

### 1. Python 3
* **Justificativa:** Linguagem de programação base do projeto. Foi escolhida devido à sua sintaxe limpa e legível, velocidade para prototipagem e pelo forte suporte ao paradigma de **Programação Orientada a Objetos (POO)**, permitindo modularizar o jogo em entidades independentes (Neymar, Bola, Zagueiros, Interfaces).

### 2. Pygame
* **Justificativa:** Biblioteca de código aberto e padrão da indústria para o desenvolvimento de jogos 2D em Python. Suas principais atribuições no projeto são:
    * **`pygame.sprite.Sprite` e `Group`:** Utilizados para gerenciar o ciclo de vida, renderização e atualização em lote de múltiplos elementos idênticos na tela (como o grupo de zagueiros e os coletáveis).
    * **`pygame.Rect`:** Manipulação das caixas delimitadoras (*hitboxes*) para posicionamento exato de textos, botões de menu e para o controle fino dos *offsets* de posse de bola.
    * **`pygame.time.Clock` (Game Loop):** Essencial para travar a taxa de quadros por segundo (FPS), garantindo que a velocidade da bola e dos jogadores seja idêntica em qualquer computador.
    * **Sistema de Eventos:** Captura em tempo real dos inputs do teclado (teclas `W`, `A`, `S`, `D` para movimentação; comandos de chute e passe) e cliques do mouse nos menus.

### 3. Math (Biblioteca Nativa)
* **Justificativa:** Utilizada para resolver a física e a geometria analítica do jogo:
    * **`math.atan2`:** Responsável por calcular o ângulo exato em radianos entre a posição atual da bola e o destino escolhido (seja o pé de um aliado no passe ou o ângulo das redes no chute ao gol).
    * **`math.cos` e `math.sin`:** Usados para decompor o vetor de força resultante em velocidades separadas para os eixos X e Y (`velocidade_x` e `velocidade_y`), gerando trajetórias lineares perfeitas e suaves para a bola.
    * **`math.hypot`:** Utilizado para calcular a distância exata entre duas entidades. É a função que detecta se a bola chegou perto o suficiente do destino para parar no chão (`distancia < 12`) ou se o zagueiro está perto o suficiente do Neymar para tentar um bote.

### 4. Random (Biblioteca Nativa)
* **Justificativa:** Responsável por introduzir o fator de imprevisibilidade e aleatoriedade necessário para tornar o jogo desafiador:
    * **Sucesso do Chute:** Quando o jogador chuta, a função `random.randint` define as coordenadas exatas do alvo nas traves (se o resultado for gol, define um pixel dentro da rede; se for defesa, mira no alcance do goleiro; se for para fora, joga para as linhas de fundo).
    * **IA de Bote:** Define probabilisticamente se os zagueiros vão conseguir desarmar o Neymar ou se vão cair no drible e ficar atordoados.
 
### 5. sys (Biblioteca Nativa)
* **Justificativa:** Utilizada para interagir diretamente com o sistema operacional de forma limpa. No contexto do `main.py`, ela é indispensável para realizar o encerramento completo do processo do jogo (`sys.exit()`) quando o jogador clica no botão "Sair" do menu ou fecha a janela do Pygame. Isso impede que o jogo continue rodando em segundo plano e consumindo memória RAM após ser fechado.

### 6. ctypes (Biblioteca Nativa)
* **Justificativa:** É uma biblioteca de funções avançadas que permite ao Python conversar direto com arquivos de sistema do Windows (DLLs). No projeto, o comando `ctypes.windll.user32.SetProcessDPIAware()` foi utilizado para **resolver problemas de escala e resolução de tela**. 
    * Muitos notebooks modernos possuem telas com proporções de 16:10 ou telas pequenas com alto DPI (onde o Windows aplica um zoom de 125% ou 150% por padrão). Esse zoom do Windows costuma esticar a janela do Pygame, deixando os sprites borrados e cortando as linhas do campo. A chamada do `ctypes` força o sistema operacional a renderizar o jogo na resolução nativa exata definida no arquivo `constants.py`, sem distorções visuais.


## 👥 Divisão de Trabalho dentro do Grupo

O projeto foi desenvolvido de forma modular, onde cada integrante ficou responsável por núcleos específicos do jogo, garantindo a integração dos sistemas por meio do repositório no GitHub.

| Integrante | Responsabilidade Principal | Tarefas Desenvolvidas |
| :--- | :--- | :--- |
| **Darllan Wallace** | **Desenvolvimento da Tela de Espera e da Lógica das Oportunidades** | • Foi responsável por implementar a tela de espera no jogo, permitindo alcançar uma dinamicidade maior ao software. Também fez a barra de carregamento da estrela à medida que acumula confiança. |
| **Ivan Nicholas** | **Desenvolvimento dos Coletáveis e da Lógica de Colisão** | • Criou os itens coletáveis e integrou eles ao sistema de dribles quando eram bem-sucedidos, fazendo eles aparecerem e acumular confiança ao coletar a chuteira. |
| **Kaik Vinícius** | **Desenvolvimento do Neymar, Lógica de Dribles e Gerenciamento do Jogo no Geral** | • Desenvolveu a classe do Neymar, implementou os dribles dele, a lógica de chute e de colisão com o zagueiro. Também definiu as principais constantes responsáveis por gerenciar o jogo, atuando na correção de bugs e inconsistências, além de implementar os sprites e animações do Neymar parado, correndo e no seu modo Ney Prime. Fez também toda a lógica de cálculo probabilístico do gol, tomando como base a confiança acumulada e a distância do gol, mudando o estado da bola e definindo a partir disso o rumo das próximas oportunidades. |
| **Luiz Apolinário** | **Desenvolvimento do Zagueiro, Goleiro e Lógica de Preparo pro Bote, Carrinho e Idle** | • Implementou a classe do zagueiro e desenvolveu mecanismos de perseguir o Neymar dando um bote quando perto o suficiente. Integrou essa parte à main do projeto com checagens de colisões que monitoravam o estado do zagueiro. Fez o mesmo com o Goleiro já que suas funções eram parecidas, deixando ele executar ações diferentes embaixo do gol. Também participou da correção de bugs do sistema. |
| **Rafael Gonçalves** | **Reponsável por toda Identidade Visual do Jogo** | • Desenvolveu todos os assets e animações do jogo, além de integrar no código o sistema do menu inicial, da dificuldade e o menu de pause. Produziu cada frame de animação das entidades do jogo, além dos ícones dos coletáveis também animados, sendo responsável pelos sprites do Neymar, Zagueiro, Goleiro, Coletáveis e Interface. |
| **Pedro Henrique França** | **Desenvolveu a Lógica da Bola Teleguiada ao Gol** | • Responsável por fazer a bola sair do pé do jogador e ir até o gol com variação de angulação a depender de onde se executa o chute, tomando como base a distancia e posicionamento em relação ao centro do gol. |

---

### 🔄 Metodologia de Integração
* **Controle de Versão:** Utilizamos o Git e o GitHub para centralizar o código.
* **Comunicação:** Reuniões rápidas para definir os tomadas de decisões acerca do melhor funcionamento do jogo e viabilidade de produção.

## 🎓 Conceitos da Disciplina Aplicados no Projeto

Abaixo estão listados os conceitos de programação e estrutura de dados que utilizamos para construir a lógica do jogo e onde eles estão aplicados no código:

### 1. Classes e Objetos
* **O Conceito:** Definição de moldes (classes) para instanciar elementos independentes (objetos) que possuem características (atributos) e ações (métodos) próprias.
* **Onde foi usado:** Todo o projeto é baseado nisso. A classe `Neymar` (em `neymar.py`) serve como molde para criar o herói do jogo, enquanto a classe `Zagueiro` permite instanciar múltiplos inimigos de forma independente no campo, cada um controlando sua própria inteligência artificial e posição.

### 2. Encapsulamento e Organização Modular
* **O Conceito:** Ocultar dados internos de uma classe e expor apenas o necessário através de métodos públicos, além de isolar regras de negócio para evitar o acoplamento do código.
* **Onde foi usado:** * No arquivo `main.py`, o loop principal não precisa saber como o Neymar calcula sua velocidade ou altera seus sprites; ele apenas chama o método público `ney.mover()`.
    * No isolamento do módulo `gerenciamento/constants.py`, que encapsula todas as variáveis estáticas do sistema (resolução, velocidades, taxas de atualização), impedindo que valores fiquem "soltos" (*magic numbers*) dentro do código físico.

### 3. Herança (Polimorfismo de Inclusão)
* **O Conceito:** Criação de uma classe nova (filha) a partir de uma classe existente (mãe), herdando seus atributos e métodos, o que evita a duplicidade de código.
* **Onde foi usado:** Todas as nossas entidades (`Neymar`, `Bola`, `Zagueiro`, `Goleiro`, `Coletavel`) herdam diretamente da classe mãe **`pygame.sprite.Sprite`**. Graças a isso, todas elas ganham nativamente os atributos `self.image` e `self.rect`, permitindo que o Pygame as gerencie e desenhe na tela automaticamente.

### 4. Associação de Objetos e Comunicação por Mensagens
* **O Conceito:** A capacidade de um objeto conter uma referência direta a outro objeto para interagir com ele e ler seus estados.
* **Onde foi usado:** * **Física da Bola (`bola.py`):** A classe `Bola` possui o atributo `self.dono`. Quando o Neymar está conduzindo a bola, `self.dono` aponta diretamente para o objeto do `Neymar`.
    * **Animação da Bola:** Dentro do método `animar()` da bola, ela faz uma verificação por mensagem: `getattr(self.dono, 'em_movimento', False)`. A bola lê o estado de movimento do Neymar em tempo real para decidir se deve continuar girando seus sprites enquanto está colada na chuteira dele.
  
 ### 5. Estruturas de Dados: Listas (`lists`)
* **O Conceito:** Coleções ordenadas de elementos mutáveis que permitem o armazenamento e o acesso sequencial de dados por meio de índices.
* **Onde foi usado:** É a base do nosso sistema de animação. No arquivo `ney_animado.py` (e na animação da bola), usamos **listas** para armazenar as sequências de imagens do Pygame, como `self.frames_correndo_direita` e `self.frames_correndo_esquerda`. O jogo percorre essas listas frame por frame usando um contador (`self.frame_atual += 1`) para criar o efeito visual de movimento.

### 6. Estruturas de Dados: Dicionários (`dicts`)
* **O Conceito:** Estruturas de dados que armazenam dados no formato de Chave-Valor (`key: value`), permitindo buscas rápidas e mapeamento direto de estados.
* **Onde foi usado:** Utilizado no gerenciamento de configurações globais e estados visuais. Mapeamos dicionários no arquivo de `constants.py` ou dentro dos gerenciadores de interface para associar opções de menu aos seus respectivos destinos (ex: ligar a string `'facil'` ou `'dificil'` a multiplicadores numéricos de velocidade dos zagueiros).

### 7. Máquina de Estados
* **O Conceito:** Gerenciamento do comportamento de um sistema com base no seu estado atual, alterando o fluxo da aplicação de forma limpa.
* **Onde foi usado:** * **Controle de Telas (`interface/`):** O jogo transiciona entre os estados de `MenuInicial`, `MenuDificuldade`, `JogoAtivo` e `MenuPause`, alterando completamente quais eventos do teclado e renderizações estão ativos.
    * **Animação Lateral Dinâmica:** No método `mover` de `neymar.py`, o jogo usa a variável `self.olhando_para` ("frente", "costas", "esquerda", "direita") como uma máquina de estados de direção. Quando o jogador corre na diagonal (apertando **W + D**), o estado "direita" sobrepõe o vertical, atualizando instantaneamente a lista de animação correta.
 
 ## ⚠️ Desafios, Erros Enfrentados e Lições Aprendidas

### Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?

O maior erro cometido durante o projeto foi basicamente o **acoplamento excessivo da lógica de animação dentro das classes de física dos personagens**, misturado com caminhos de arquivos (*hardcoded*) espalhados por todo o código.

No início do desenvolvimento, colocamos o carregamento de imagens (`pygame.image.load`) e o controle do relógio de animação diretamente dentro dos métodos de movimentação do Neymar e da bola. Quando tentamos adicionar os 4 sprites da corrida para a direita, esquerda e diagonal, o código virou um emaranhado de estruturas condicionais (`if/else`) confusas. Além disso, a bola travava e parava de rodar sempre que o Neymar estava conduzindo ela, pois a física da bola dizia que ela estava "parada" (sem velocidade própria), mas visualmente ela precisava continuar girando junto com os pés do craque.
Além de que não tivemos problemas somente com a animção do Neymar, e sim da maior parte das entidades e as interações animadas que elas tinham umas com as outras.

**Como lidamos com isso:**
Para resolver o problema, precisamos dar um passo atrás e aplicar uma refatoração severa baseada em boas práticas de POO:
1. **Isolamento de Responsabilidades:** Separamos o cérebro físico do corpo visual. Criamos um sistema de animação dedicado (`ney_animado.py`) e modificamos o método `animar()` da bola.
2. **Comunicação por Mensagens:** Em vez de fundir as duas lógicas, fizemos a bola ler o estado do Neymar (`dono.em_movimento`) em tempo real. Se o Neymar estiver correndo, a bola ignora o fato de estar sem velocidade própria e continua girando seus frames.
3. **Módulo de Gerenciamento:** Criamos o `constants.py` e centralizamos os caminhos das pastas de sprites, limpando o código principal.

---

### Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?

O maior desafio técnico do projeto foi **sincronizar a física da bola com a movimentação diagonal do Neymar e a IA dos zagueiros**. 

Fazer a bola se mover em linha reta era simples, mas calcular os passes e chutes em qualquer direção do campo exigiu uma matemática complexa. Quando o Neymar corria na diagonal (apertando **W + D**), a velocidade dele aumentava incorretamente por conta da soma dos eixos, fazendo com que ele andasse mais rápido que a própria bola e "atropelasse" o objeto. Além disso, os zagueiros precisavam perseguir o Neymar de forma inteligente, calculando a menor distância para o bote sem criar movimentos travados ou artificiais.
Sem contar que quando haviam passes devolutivos dos aliados pra o Neymar, muitas vezes a bola não parava à frente dele e fazia com que ela passasse direto e se isolasse do mapa, quebrando completamente a mecânica.

**Como lidamos com isso:**
Contornamos esse desafio aplicando conceitos puros de **geometria analítica e trigonometria** através da biblioteca `math`:
1. **Normalização Vetorial:** No método `mover` do Neymar, aplicamos um fator diagonal ($0.7071$) quando duas teclas de direção são pressionadas juntas. Isso limitou a velocidade máxima nas diagonais, mantendo o movimento uniforme.
2. **Decomposição de Forças:** Implementamos as funções `math.atan2`, `math.cos` e `math.sin` para calcular o ângulo exato do chute ou passe. A força aplicada foi decomposta perfeitamente nos eixos X e Y, fazendo a bola viajar de forma suave e realista até o alvo (seja o gol ou o pé de um aliado).
3. **Cálculo de Proximidade:** Usamos a distância (`math.hypot`) para ditar o comportamento da IA do zagueiro, definindo o raio exato em que ele sai do estado de patrulha e entra em estado de perseguição/bote.
4.  **Cálculo de Previsão da Posição da Bola para Corrigir o Bug do Passe do Aliado:** Utilizamos um mecanismo que previa o centro da bola nos frames seguintes para interromper a trajetória dela e fazer com que ela não passasse direto e sim parasse na frente do Neymar quando ele estivesse em uma jogada de ataque.

---

### Quais as lições aprendidas durante o projeto?

* **Controle de Versão (Git/GitHub):** Integrar módulos feitos separadamente (como interfaces e entidades) sem uma política de *branches* gera conflitos de código. Aprendemos a importância de commits pequenos e focados para evitar a perda de progresso.
* **Modularização e Refatoração:** Código perfeito não nasce na primeira tentativa. Aprendemos a quebrar funções gigantes em métodos de responsabilidade única (como separar a troca de sprites da física de movimento), o que facilitou a depuração de bugs.
* **Uso de Constantes:** Centralizar variáveis de configuração (resoluções, velocidades e caminhos de arquivos) em um arquivo único (`constants.py`) poupa tempo e evita o uso de *magic numbers* (valores soltos no meio do código).
* **Trigonometria Aplicada a Jogos:** Na prática, vetores de movimento e colisões dependem diretamente de conceitos matemáticos como decomposição de eixos (seno/cosseno) e distância Euclidiana. Sem essa base, a movimentação fica travada e artificial.

---

# 🚀 Como Executar o Jogo (Instalação e Execução)
Siga os passos abaixo para clonar o repositório, configurar o ambiente virtual do Python e iniciar o jogo.

Pré-requisitos
Certifique-se de ter o Python 3.10 ou superior instalado no seu computador.

## **Passo a Passo**
## 1. Clonar o Repositório
Abra o seu terminal (Prompt de Comando, PowerShell ou Terminal do Linux/Mac) e execute o comando para clonar o projeto:

```text
git clone https://github.com/Kaik-Vinicius/Projeto-Final-IP.git
cd Projeto-Final-IP
```

---

## 2. Criar o Ambiente Virtual (`venv`)
É altamente recomendável utilizar um ambiente virtual para não misturar as dependências do jogo com as do seu sistema operacional:

### Windows:
```text
python -m venv .venv
```

---

### Linux/macOS:
```text
python3 -m venv .venv
```

## 3. Ativar o Ambiente Virtual
Ative o ambiente virtual para que as instalações fiquem isoladas dentro da pasta .venv:

### Windows (PowerShell):
```text
.venv\Scripts\Activate.ps1
```

---

### Windows (Prompt de Comando - CMD):
```text
.venv\Scripts\activate.bat
```

---

### Linux/macOS:
```text
source .venv/bin/activate
```

---

## 4. Instalar o Pygame
Com a venv ativada, instale a biblioteca do Pygame utilizando o gerenciador de pacotes do Python:

```text
pip install pygame
```

---

## 5. Iniciar o Jogo
Agora basta executar o arquivo principal (`main.py`) localizado na raiz do projeto para abrir a tela do menu inicial:

```text
python main.py
```

