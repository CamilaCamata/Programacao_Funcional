#################################################
# Programção I / Programação Funcional (2023/1) #
# EP2 - Jogo da Velha                           #
# Nome: Camila Camata Crespo                    #
# Matrícula: 2023100465                         #
#################################################

from os import system, name #import ultilizado para limpar tela do terminal.
import random #import utilizado para sortear quem inicia a partida.
def limpaTela():
    """Reponsável por limpar a tela do terminal.
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def getMatricula():
    """Retorna a matrícula do aluno como string.
    """
    return "2023100465"

def getNome():
    """Retorna o nome do aluno como string 
    """
    return "Camila Camata Crespo"

def Cor(cor):
    """Função responsável por colorir.
    Parâmetro:
    -> cor: referente a cor desejada.
    Retorna a cor escolhida.
    """
    if cor == "br/br":
        return "\033[1;30;40m"
    if cor == "mg/br":
        return "\033[1;35;40m"
    if cor == "mg/cin":
        return "\033[1;35;47m"
    if cor == "amar":
        return "\033[1;36;46m"
    if cor == "azul":
        return "\033[1;35;44m"
    if cor == "amarelo":
        return "\033[1;35;43m"
    if cor == "red":
        return "\033[1;35;41m"
    if cor == "br/mag":
        return "\033[1;37;45m"

def apresentacao():
    """Responsável por exibir mensagem de apresentação do jogo na tela inicial.
    """

    corbr = Cor("br/br")
    mgbr= Cor("mg/br")
    mgcin = Cor("mg/cin")
    amr = Cor("amar")
    input(
          f"{corbr}o                                             x\033[m\n"
          f"\033[1;33;40mo     BEM-VINDO(A) AO JOGO DA VELHA RABBIT    x\033[m\n"
          f"{corbr}o                                             x\033[m\n"
          f"{corbr}o                                             x\033[m\n"
          f"{corbr}o      \033[m\033[1;37;45m | \033[m{corbr}  \033[m\033[1;37;45m | \033[m{corbr}                               x\033[m\n"
          f"{corbr}o      \033[m\033[1;37;45m | \033[m{corbr}  \033[m\033[1;37;45m | \033[m{corbr}                               x\033[m\n"
          f"{corbr}o     \033[m\033[1;30;45m  _    _  \033[m{corbr}       {getMatricula()}             x\033[m\n"
          f"{corbr}o     \033[m{mgcin} .6 .  6. \033[m{corbr}       {getNome()}   x\033[m\n"
          f"{corbr}o     \033[m{mgcin}     7    \033[m{corbr}                              x\033[m\n"
          f"{corbr}o                                             x\033[m\n"
          f"\033[1;31;40mo       Pressione ENTER para continuar...     x\033[m\n"
          f"{corbr}o                                             x\033[m\n")

def escolheNivel():
    """Responsável por exibir os níveis disponíveis para jogar, sendo eles, Fácil, Normal e Hard.
    Retorna o nível escolhido pelo jogador.
    """
    cor = Cor("br/br")
    limpaTela()
    try:
        nivel = int(input(f"{cor}  \033[m\033[1;30;47m DESEJA JOGAR EM QUAL NÍVEL? \033[m\033[1;30;40m                o\033[m\n"
            f"{cor}                                               x\033[m\n"
            f"{cor}           [1] \033[m\033[7;34;40m NÍVEL: FÁCIL \033[m\033[1;30;40m                  x\033[m\n"
            f"{cor}                                               o\033[m\n"
            f"{cor}           [2] \033[m\033[7;33;40m NÌVEL: NORMAL \030\033[1;30;40m                 x\033[m\n"
            f"{cor}                                               o\033[m\n"
            f"{cor}           [3]  \033[m\033[7;31;40m NÍVEL: HARD \033[m\033[1;33;40m                  x\033[m\n"
            f"{cor}                                               o\033[m\n"
            f"{cor}       \033[m\033[1;35;47m V \033[m\033[1;30;40m  \033[m\033[1;35;47m V \033[m\033[1;30;40m                                x\033[m\n"
            f"{cor}      \033[1;35;47m  ~    ~  \033[m\033[1;35;40m                               o\033[m\n"
            f"{cor}      \033[1;35;47m .\033[m\033[1;35;47ma\033[m\033[1;35;47m .  \033[m\033[1;35;47ma\033[m\033[1;35;47m. \033[m\033[1;35;40m                               x\033[m\n"
            f"{cor}      \033[1;35;47m    w     \033[m\033[1;35;40m                               o\033[m\n"
            f"{cor}                                               x\033[m\n\033[1;30;40mNível: \033[m"))
        if nivel != 1 and nivel != 2 and nivel != 3:
            input("Digite um dos níveis disponíveis!\nPressione uma tecla...")
            return escolheNivel()
        return nivel
    except:
        input("Digite um dos níveis disponíveis!\n Pressione Enter para continuar!")
        return escolheNivel()
    
def confereVitoria(simbolo,tabuleiro):
    """Confere se o jogador ganhou a partida.
    Recebe com parâmetro:
    -> simbolo: letra do jogador ou da maquina ('X'ou'O').
    -> tabuleiro: lista de tamanho 10 representando as posições do jogo, sendo a posição 0 descartada.
    Retorna True caso o jogador ou a máquina tenha ganhado e False caso contrário.
    """
    if tabuleiro[1]==tabuleiro[4]==tabuleiro[7]==simbolo:
        return True
    elif tabuleiro[2]==tabuleiro[5]==tabuleiro[8]==simbolo:
        return True
    elif tabuleiro[3]==tabuleiro[6]==tabuleiro[9]==simbolo:
        return True
    elif tabuleiro[7]==tabuleiro[8]==tabuleiro[9]==simbolo:
        return True
    elif tabuleiro[4]==tabuleiro[5]==tabuleiro[6]==simbolo:
        return True
    elif tabuleiro[1]==tabuleiro[2]==tabuleiro[3]==simbolo:
        return True
    elif tabuleiro[3]==tabuleiro[5]==tabuleiro[7]==simbolo:
        return True
    elif tabuleiro[1]==tabuleiro[5]==tabuleiro[9]==simbolo:
        return True
    else:
        return False


def desenhofinal(tabuleiro,nivel=3,computadorganhou=False,jogadorganhou=False,empate=False):
    """Responsável por exibir desenho final, informando quem ganhou a partida ou se houve um empate.
    Recebe:
    -> nivel: nivel da partida.
    -> computadorganhou: True caso o computador tenha ganho, False caso contrário.
    -> jogadorganhou: True caso o adversário tenha ganho a partida, false caso contrário.
    -> empate: responsável por falar se houve empate (True) ou não (False).
    """
    
    fundo = Cor("br/br")
    pele=Cor("mg/cin")
    tab=Cor("mg/br")
    if jogadorganhou == True:
        msg = "VOCÊ GANHOU!!"
        if nivel == 1:
            cor = Cor("azul")
        if nivel ==2:
            cor = Cor("amarelo")
        if nivel ==3:
            cor = Cor("red")
    if computadorganhou == True:
        msg = "COMPUTADOR RABBIT GANHOU!!"
        cor = Cor("br/mag")
    if empate == True:
        msg = "EMPATOU!"
        cor = Cor("br/mag")
   
    print(f"{fundo}o  x o x o x o x o x o x o x o x o x o x o x o\033[m\n"
            f"{fundo}x        \033[m{cor} | \033[m{fundo}  \033[m{cor} | \033[m{tab}            |       |        \033[m\n"
            f"{fundo}o        \033[m{cor} | \033[m{fundo}  \033[m{cor} | \033[m{tab}        {tabuleiro[7]}   |   {tabuleiro[8]}   |   {tabuleiro[9]}    \033[m\n"
            f"{fundo}x       \033[m{cor}          \033[m{tab}      -----|-------|-----   \033[m\n"
            f"{fundo}o       \033[m{pele}  â  . â  \033[m{tab}       {tabuleiro[4]}   |   {tabuleiro[5]}   |   {tabuleiro[6]}    \033[m\n"
            f"{fundo}x       \033[m{pele}     7    \033[m{tab}      -----|-------|-----   \033[m\n"
            f"{fundo}o    \033[m{cor}  \033[m{fundo}     \033[m{pele}  \033[m{fundo}     \033[m{cor}  \033[m{tab}    {tabuleiro[1]}   |   {tabuleiro[2]}   |   {tabuleiro[3]}    \033[m\n"
            f"{fundo}x    \033[m{cor}   \033[m{pele} |      | \033[m{cor}   \033[m{tab}        |       |        \033[m\n"
            f"{fundo}o       \033[m{pele} \033[m{cor}        \033[m{pele} \033[m{fundo}                            \033[m\n"
            f"     {fundo} {msg} \033[m")


def XouO(nivel, possivelX = ['x','X'], possivelO =['o','O'],i=0): 
    """Responsável por pedir ao jogador escolher se irá querer ser o jogador 'X' ou 'O'
    Parâmetros:
    -> nivel: nível da partida
    -> possivelX: lista com as possibilidades,'x' minusculo ou 'X' maiúsculo, que aceita de entrada.
    -> possivelO: lista com as possibilidades,'o' minúsculo ou 'O' maiúsculo, que aceita de entrada.
    -> i: auxilia para que só exiba as opções na primeira tentativa.
    Retorna a letra escolhida.
    """
      
    if nivel == 1:
        cor = "\033[1;35;44m"
    elif nivel == 2:
        cor = "\033[1;35;43m"
    else:
        cor = "\033[1;35;41m"
    if i == 0:
        print("\033[1;35;40m                                                \033[m\n"
            f"\033[1;35;40m      {cor} | \033[m\033[1;35;40m                                       \033[m\n"
            f"\033[1;35;40m      \033[m{cor} | \033[m\033[1;35;40m  \033[m{cor} V \033[m\033[1;35;40m                                  \033[m\n"
            f"\033[1;35;40m     \033[m{cor}  \    /  \033[m\033[1;35;40m                                 \033[m")
        print(f"\033[1;35;40m     \033[m\033[1;35;47m .\033[m{cor}>\033[m\033[1;35;47m .  \033[m{cor}<\033[m\033[1;35;47m. \033[m\033[1;35;40m  \033[m\033[1;35;40m                               \033[m\n"
            "\033[1;35;40m     \033[m\033[1;35;47m    ^     \033[m\033[1;35;40m                                 \033[m\n"
            "\033[1;35;40m                                                \033[m")
    xOUo = input("\033[1;30;40m                                                \033[m\n"
                  "\033[1;30;40m  \033[m\033[1;30;47m Deseja ser o jogador 'X' ou 'O'?\033[m\033[1;30;40m             \033[m\n\033[1;30;40mSou: \033[m")
    if xOUo in possivelX:
        return 'X'
    if xOUo in possivelO:
        return 'O'
    print("Simbolo inválido!")
    return XouO(nivel,possivelX,possivelO,i+1)


def imprimetabuleiro(nivel,l_jogadas = [" "," "," "," "," "," "," "," "," "," "]):
     """Responsável por imprimir o tabuleiro do jogo.
     Parâmetros:
     -> nivel: nível de jogo escolhido pelo jogador (Fácil, Normal, Hard)
     -> Tabuleiro: lista de tamanho 10 representando as posições do tabuleiro do jogo, sendo a posiçção 0 descartada
    """
     limpaTela()
     if nivel == 1:
         cor = "\033[1;35;44m" 
     if nivel == 2:
         cor = "\033[1;35;43m"
     if nivel == 3:
         cor = "\033[1;35;41m"  
     print("\033[1;35;40m                                                         \033[m\n"
           f"\033[1;35;40m                       |       |                         \033[m\n"
           f"\033[1;35;40m  \033[m\033[1;35;40m    {cor} | \033[m\033[1;35;40m\033[1;35;40m          {l_jogadas[7]}   |   {l_jogadas[8]}   |   {l_jogadas[9]} \033[m\033[1;35;40m       \033[1;37;45m | \033[m\033[1;35;40m          \033[m\n"    #     7 | 8 | 9
           f"\033[1;35;40m      \033[m{cor} | \033[m\033[1;35;40m  \033[m{cor} V \033[m\033[1;35;40m  -------|-------|-------\033[1;35;40m     \033[m\033[1;37;45m | \033[m\033[1;35;40m  \033[m\033[1;37;45m V \033[m\033[1;35;40m     \033[m\n"                                           #     4 | 5 | 6
           f"\033[1;35;40m     \033[m{cor}  \    /  \033[m\033[1;35;40m    {l_jogadas[4]}   |   {l_jogadas[5]}   |   {l_jogadas[6]} \033[m\033[1;35;40m      \033[m\033[1;35;45m  \    /  \033[m\033[1;35;40m    \033[m\n"    #     1 | 2 | 3
           f"\033[1;35;40m     \033[m\033[1;35;47m .\033[m{cor}a\033[m\033[1;35;47m .  \033[m{cor}a\033[m\033[1;35;47m. \033[m\033[1;35;40m -------|-------|------- \033[m\033[1;35;40m   \033[m\033[1;35;47m .\033[m\033[1;35;47m6\033[m\033[1;35;47m .  \033[m\033[1;35;47m6\033[m\033[1;35;47m. \033[m\033[1;35;40m    \033[m\n"                                           #     Tabuleiro exibido correspondente aos numeros do teclado
           f"\033[1;35;40m     \033[m\033[1;35;47m    ^     \033[m\033[1;35;40m    {l_jogadas[1]}   |   {l_jogadas[2]}   |   {l_jogadas[3]}   \033[m\033[1;35;40m    \033[m\033[1;35;47m    ^     \033[m\033[1;35;40m    \033[m\n"    #     descartando o zero.
            "\033[1;35;40m                       |       |                         \033[m\n"
          "\033[1;35;40m                                                         \033[m\n")


def travaVitoria(tabuleiro,simbolo):
    """Função responsável por verificar se o adversário ou o computador está prestes a ganhar, caso o adversário esteja prestes a
    ganhar o computador escolhe a posição que irá parar a vitória, se for o computador que estiver prestes a ganhar ele escolhe a posição
    que garantirá a vitória.
    Parâmetros:
    -> tabuleiro: lista de tamanho 10, reresentando as posições do tabuleiro, sendo a poisição 0 descartada.
    -> simbolo: letra do computador ou do adversário.("X" ou "O")
    Retorna a posição de jogada.
    """
    
    if (tabuleiro[1]==tabuleiro[4] == simbolo and tabuleiro[7] ==" ")or(tabuleiro[8]==tabuleiro[9]==simbolo and tabuleiro[7]==" ")or(tabuleiro[3]==tabuleiro[5]==simbolo and tabuleiro[7]==" "):
        return 7       

    if (tabuleiro[4]==tabuleiro[7]==simbolo and tabuleiro[1]==" ")or(tabuleiro[2]==tabuleiro[3]==simbolo and tabuleiro[1]==" ") or (tabuleiro[9]==tabuleiro[5]==simbolo and tabuleiro[1]==" "):
        return 1    

    if (tabuleiro[1]==tabuleiro[7]==simbolo and tabuleiro[4]==" ")or(tabuleiro[5]==tabuleiro[6]==simbolo and tabuleiro[4]==" "):
        return 4    

    if (tabuleiro[2]==tabuleiro[5]==simbolo and tabuleiro[8]==" ")or(tabuleiro[7]==tabuleiro[9]==simbolo and tabuleiro[8]==" "):
        return 8    

    if (tabuleiro[2]==tabuleiro[8]==simbolo and tabuleiro[5]==" ")or(tabuleiro[4]==tabuleiro[6]==simbolo and tabuleiro[5]==" ")or(tabuleiro[3]==tabuleiro[7]==simbolo and tabuleiro[5]==" ")or(tabuleiro[1]==tabuleiro[9]==simbolo and tabuleiro[5]==" "):
        return 5    

    if (tabuleiro[5]==tabuleiro[8]==simbolo and tabuleiro[2]==" ")or(tabuleiro[1]==tabuleiro[3]==simbolo and tabuleiro[2]==" "):
        return 2

    if (tabuleiro[3]==tabuleiro[6]==simbolo and tabuleiro[9]==" ")or(tabuleiro[7]==tabuleiro[8]==simbolo and tabuleiro[9]==" ")or(tabuleiro[1]==tabuleiro[5]==simbolo and tabuleiro[9]==" "):
        return 9       

    if (tabuleiro[3]==tabuleiro[9]==simbolo and tabuleiro[6]==" ")or(tabuleiro[4]==tabuleiro[5]==simbolo and tabuleiro[6]==" "):
        return 6    

    if (tabuleiro[6]==tabuleiro[9]==simbolo and tabuleiro[3]==" ")or(tabuleiro[1]==tabuleiro[2]==simbolo and tabuleiro[3]==" ")or(tabuleiro[5]==tabuleiro[7]==simbolo and tabuleiro[3]==" "):
        return 3
    else:#Caso ninguém esteja prestes a ganhar, retorna 0.
        return 0


def Posicao(tabuleiro):
    """Responsável por verificar quais posições estão disponíveis para jogada, dando preferência as melhores
    posições de jogada.
    Parâmetro:
    -> tabuleiro: lista de tamanho 10, representando o tabuleiro do jogo, sendo a posição 0 descartada.
    Retorna: Uma posição disponível.
    """
    if tabuleiro[9]==" ":
        return 9
    if tabuleiro[3]==" ":
        return 3
    if tabuleiro[5]==" ":
        return 5
    if tabuleiro[2]==" ":
        return 2
    if tabuleiro[8]==" ":
        return 8
    if tabuleiro[4]==" ":
        return 4
    if tabuleiro[1]==" ":
        return 1
    if tabuleiro[6]==" ":
        return 6
    if tabuleiro[7]==" ":
        return 7

def jogadaComputador(tabuleiro,simboloComputador,qJogador = 1,nivel=3):
    """
    Recebe o tabuleiro e o simbolo do computador e determina onde o jogador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas
    sendo a posição 0 do tabuleiro descartada.
    
    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro.
    simboloComputador: letra do computador
    qJogador: 1 caso o computador comece jogando primeiro; 2 caso o compuutador comece sendo o jogador 2.
    nivel: nivel de dificuldade da jogada.
    
    Retorno: 
    Posição (entre 1 e 9) da jogada do computador
    
    Estratégia:

    -> Nível fácil: somente chama a função que analisa as melhores posições disponíveis de jogada e retorna uma delas.

    -> Nível normal: O computador sempre incicia sua jogada  pelas quinas (posições:1,3,7,9) tentando formar uma jogada 
    que deixará o adversário sem alternativas. Tentando prever algumas possibilidades de jogadas e a partir da terceira rodada
    as posições são escolhidas pela função Posicao, sempre contando com o auxílio da função travaVitória apenas para 
    tentar ganhar o jogo.

    -> Nível hard: Divide sua estratégia em duas, uma para quando o computador inicia a partida, começando pelas
    quinas [1,3,7,9] tentando forma uma encrusilhada para o adversário; e outra para quando o adversário inicia a partida, 
    caso o adversário inicie na posição [5] o computador joga nas posições do laterais[2,4,8,6], sendo mais uma partida
    defensiva, caso contrário tenta usar da primeira estratégia, em ambos os casos sempre tentando prêver possíveis jogadas e 
    com o auxilio da função 'travaVitoria', toda vez que o adversário estiver prestes a fazer alguma jogada que garantiria a 
    vitória a ele, o computador também tenta parar ele escolhendo a posição que não deixará de forma alguma o adversário ganhar, 
    tendo assim uma garantia caso ocorra uma alternativa não prevista.O mesmo valhe para jogadas em que o computador está prestes a 
    ganhar, sempre passando a posição que garantirá a vitória ou irá parar a jogada vitoriosa do adversário como preferência.
    
    """
    if simboloComputador =="X":
        simboloJogador ="O"
    elif simboloComputador=="O":
        simboloJogador ="X"
    if nivel == 1:#Nível Fácil
        tabuleiro1=tabuleiro[:]
        posicao = Posicao(tabuleiro1)
        return posicao
    if nivel == 2:#Nível Normal
        tabuleiro2=tabuleiro[:]
        if travaVitoria(tabuleiro2,simboloComputador)!=0:
            posicao = travaVitoria(tabuleiro2,simboloComputador)
            return posicao
        if tabuleiro[7]==" ":
            return 7
        if (tabuleiro[2]!=simboloComputador or tabuleiro[4]!=simboloComputador or tabuleiro[6]!=" ") and tabuleiro[9]==" ":
            return 9
        if tabuleiro[9]== simboloComputador:
            if tabuleiro[8]==" ":
                return 8
            elif tabuleiro[8]!=simboloComputador and tabuleiro[5]==" ":
                return 5
        if tabuleiro[1]==" ":
            return 1
        else:
            tabuleiro3=tabuleiro[:]
            posicao = Posicao(tabuleiro3)
            return posicao

    if nivel == 3: #Nível Hard
        tabuleiro4=tabuleiro[:]
        if travaVitoria(tabuleiro4,simboloComputador)!=0:
            posicao = travaVitoria(tabuleiro4,simboloComputador)
            return posicao
        tabuleiro5 = tabuleiro[:]    
        if travaVitoria(tabuleiro5,simboloJogador)!=0:
            posicao = travaVitoria(tabuleiro5,simboloJogador)
            return posicao

        if qJogador == 1:#Caso o computador comece a primeira partida.
            if tabuleiro[1]==" ":
                return 1
            if tabuleiro[1]==simboloComputador:
                if tabuleiro[7]==" ":
                    return 7
                elif tabuleiro[9]==" " and tabuleiro[7] != simboloComputador:
                    return 9
                elif tabuleiro[3]==" " and tabuleiro[7] != simboloComputador and tabuleiro[9]!= simboloComputador:
                    return 3
            tabuleiro6=tabuleiro[:]
            posicao = Posicao(tabuleiro6)
            return posicao
        
        if qJogador == 2:#Caso o adversário comece a primeira partida.
            
            if (tabuleiro[1]==tabuleiro[3]==tabuleiro[8]==simboloJogador)or(tabuleiro[9]==tabuleiro[7]==tabuleiro[2]==simboloJogador):
                if tabuleiro[4]==" ":
                    return 4
                else:
                    tabcop = tabuleiro[:]
                    posicao = Posicao(tabcop)
                    return posicao                     
            if tabuleiro[1]==tabuleiro[7]==tabuleiro[6]==simboloJogador:
                if tabuleiro[2]==" ":
                    return 2
                else:
                    tabcop1=tabuleiro[:]
                    posicao = Posicao(tabcop1)
                    return posicao          
            if (tabuleiro[1]!=" " or tabuleiro[3]!=" " or tabuleiro[7]!=" " or tabuleiro[9]!=" "):
                if  tabuleiro[5]==" ":
                    return 5
                else:
                    tabcop2 = tabuleiro[:]
                    posicao = Posicao(tabcop2)
                    return posicao
            
            if tabuleiro[5]!= simboloComputador and tabuleiro[1]==" ":
                return 1
            
            if tabuleiro[5]==simboloComputador:
                if (tabuleiro[1]!=" " and tabuleiro[3]!=" ") or (tabuleiro[1]!=" " and tabuleiro[9]!=" ") and tabuleiro[2]==" ":
                    return 2
                if (tabuleiro[1]!=" " and tabuleiro[7]!=" ") or (tabuleiro[7]!=" " and tabuleiro[3]!=" ") and tabuleiro[4]==" ":
                    return 4
                if (tabuleiro[3] !=" " and tabuleiro[9]!=" ") and tabuleiro[6]==" ":
                        return 6
                if (tabuleiro[7] !=" " and tabuleiro[9] !=" ") and tabuleiro[8]==" ":
                    return 8
                
                if (tabuleiro[4] !=" " and tabuleiro[7] !=" ") or (tabuleiro[2] !=" " and tabuleiro[3] !=" ") and tabuleiro[1]==" ":
                    return 1                
                elif (tabuleiro[9] !=" " and tabuleiro[8] !=" ") or (tabuleiro[1] !=" " and tabuleiro[4] !=" ") and tabuleiro[7]==" ":
                    return 7
                elif (tabuleiro[8] !=" " and tabuleiro[7] !=" ") or (tabuleiro[6] !=" " and tabuleiro[3] !=" ") and tabuleiro[9]==" ":
                    return 9
                elif (tabuleiro[1] !=" " and tabuleiro[2] !=" ") or (tabuleiro[9] !=" " and tabuleiro[6] !=" ") and tabuleiro[3]==" ":
                    return 3
                else:
                    tabuleiro9=tabuleiro[:]
                    posicao = Posicao(tabuleiro9)
                    return posicao
                
            if tabuleiro[1]==simboloComputador:
                if tabuleiro[8]!=" " and tabuleiro[2]==" ":
                    return 2
                if tabuleiro[7]!=" " and tabuleiro[3]==" ":
                    return 3
                if tabuleiro[4]!=" " and tabuleiro[6]==" ":
                    return 6
                if tabuleiro[6]!=" " and tabuleiro[4]==" ":
                    return 4
                if tabuleiro[2]!=" " and tabuleiro[8]==" ":
                    return 8
                if tabuleiro[3]!=" " and tabuleiro[7]==" ":
                    return 7
                else:
                    tabuleiro10=tabuleiro[:]
                    posicao = Posicao(tabuleiro10)
                    return posicao
            tabuleiro11=tabuleiro[:]
            posicao = Posicao(tabuleiro11)
            return posicao


def pedeJogada(nivel,tabuleiro,i=0):
    """Responsável por pedir uma posição de jogada ao adversário.
    Parâmetro:
    -> nivel: nivel de dificuldade da partida.
    -> tabuleiro: lista de tamanho 10 representando as posições disponíveis do tabuleiro.
    -> i: variável contadora que permite o tabuleiro só ser impresso na primeira tentativa de obter a
    posição do adversário.
    Retorna a posição escolhida (de 1-9) no tabuleiro.
    """
    tabuleiro1=tabuleiro[:]
    try:
        if i == 0:
            limpaTela()
            imprimetabuleiro(nivel,tabuleiro1)
        posicao = int(input("Qual posição deseja marcar(1-9): "))
        if posicao >= 1 and posicao <=9:
            if tabuleiro1[posicao]==" ":
                return posicao                   
            else:
                return pedeJogada(nivel,tabuleiro1,i+1)
        else:
            print("Valor inválido. Você deve digitar um número inteiro entre 1 e 9.")
            return pedeJogada(nivel,tabuleiro1,i+1)
    except:
        print("Valor inválido. Você deve digitar um número inteiro entre 1 e 9.")
        return pedeJogada(nivel,tabuleiro1,i+1)                


def primeiro_Jogador():
    """Responsável por sortear quem iniciará a partida, caso for sorteado o n° 1, o computador começa, caso for o n°2 o 
    adversário começa.
    Retorna: numéro (1 ou 2) que decedirá quem iniciará a partida.
    """
    p_jogador = random.choice([1,2])
    return p_jogador


def Jogadas(tabuleiro,simboloComputador="X",simboloJogador="O",qJogador=2,i=1,nivel=3):
    """Responsável por controlar as jogadas.
    ParÂmetros:
    -> tabuleiro: lista de tamanho 10 representando as posições do tabuleiro.
    -> simboloComputador: letra do computador.
    -> simboloJogador: simbolo do adversário.
    -> qJogador: quem começa primeiro a jogada, caso for '1' quem começa é o computador.
    -> i: representa o nḿero de partidas, sendo encerrado o jogo quando o tabuleiro completa todas as posições.
    Retorna:
     -> 0: caso alguém ganhe a partida ou empate, afim de encerrar o programa
     -> a própria função caso o jogo prossiga.
    """
    if i == 1:
        apresentacao()
        nivel = escolheNivel()
        limpaTela()
        simboloJogador = XouO(nivel)

        if simboloJogador == "X":
            simboloComputador = "O"

        elif simboloJogador == "O":
            simboloComputador = "X"
        qJogador = primeiro_Jogador()

    if qJogador==1:#Computador começa

        if i== 1:
            print("O computador começa!")
            input("Pressione uma tecla.")

        if i <=5:
            tabuleiro1 = tabuleiro[:]
            posicao_computador = jogadaComputador(tabuleiro1, simboloComputador,qJogador,nivel)
            tabuleiro1[posicao_computador]=simboloComputador
            tabuleiro2 = tabuleiro1[:]
            
            tabuleiro3 = tabuleiro2[:]
            if confereVitoria(simboloComputador,tabuleiro3) == True:
                limpaTela()
                tabuleiro4 = tabuleiro2[:]
                desenhofinal(tabuleiro4,nivel,True)
                return 0
            
            if i<5:         
                limpaTela()
                posicao_jogador = pedeJogada(nivel,tabuleiro2)
                tabuleiro2[posicao_jogador] = simboloJogador
                
                tabuleiro5 =tabuleiro2[:]
                if confereVitoria(simboloJogador,tabuleiro5)== True:
                    limpaTela()
                    tabuleiro6 =tabuleiro2[:]
                    desenhofinal(tabuleiro6,nivel,computadorganhou=False,jogadorganhou=True)
                    return 0
                
            if i == 5:
                tabuleiro7 = tabuleiro2[:]
                if confereVitoria(simboloComputador,tabuleiro7)==False and confereVitoria(simboloJogador,tabuleiro7)==False:
                    limpaTela()
                    tabuleiro8 = tabuleiro2[:]
                    desenhofinal(tabuleiro8,nivel,computadorganhou=False,jogadorganhou=False,empate=True)
                    return 0
            return Jogadas(tabuleiro2,simboloComputador,simboloJogador,qJogador,i+1,nivel)
        
    if qJogador ==2:#Adversário começa a partida

        if i==1:
            print("Você começa!")
            input("Pressione uma tecla.")

        if i <=5:
            tabuleiro1 = tabuleiro[:]
            posicao_jogador = pedeJogada(nivel,tabuleiro1)
            tabuleiro1[posicao_jogador]=simboloJogador
            tabuleiro2 = tabuleiro1[:]
    
            tabuleiro3 =tabuleiro2[:]
            if confereVitoria(simboloJogador,tabuleiro3)==True:
                limpaTela()
                tabuleiro4=tabuleiro2[:]
                desenhofinal(tabuleiro4,nivel,computadorganhou=False,jogadorganhou=True)
                return 0
            
            if i < 5:
                posicao_computador = jogadaComputador(tabuleiro2,simboloComputador,qJogador,nivel)
                tabuleiro2[posicao_computador]=simboloComputador
                tabuleiro5=tabuleiro2[:]
                imprimetabuleiro(nivel,tabuleiro5)
                tabuleiro6=tabuleiro2[:]

                if confereVitoria(simboloComputador,tabuleiro6) == True:
                    limpaTela()
                    tabuleiro7=tabuleiro2[:]
                    desenhofinal(tabuleiro7,nivel,computadorganhou=True)
                    return 0
                
            if i == 5:
                tabuleiro8 = tabuleiro2[:]
                if confereVitoria(simboloComputador,tabuleiro8) == False and confereVitoria(simboloJogador,tabuleiro8)==False:
                    limpaTela()
                    tabuleiro9 = tabuleiro2[:]
                    desenhofinal(tabuleiro9,nivel,computadorganhou=False,jogadorganhou=False, empate=True)
                    return 0
            return Jogadas(tabuleiro2,simboloComputador,simboloJogador,qJogador,i+1,nivel) 
   
def main():
    limpaTela()
    tabuleiro=[" "," "," "," "," "," "," "," "," "," "]
    Jogadas(tabuleiro[:])
    print()
    

################################
## NÃO ALTERE O CÓDIGO ABAIXO ##
################################
if __name__ == "__main__":
    main()
