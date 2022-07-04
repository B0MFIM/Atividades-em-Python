from time import sleep
from random import randint


# Definindo Funções
def linha():
    print("\033[0;35m-=-\033[m" * 15)

def computador():
    print("\033[0;33mVAMOS JOGAR JO-KEN-PO\033[m".center(55))
    linha()
    c = randint(0, 2)
    return c

def opções():
    print("\033[0;33mVamos, Escolha!!\033[m".center(55))
    print("\033[0;34m[ 0 ]  -  Pedra\033[m".center(55))
    print("\033[0;34m[ 1 ]  -  Papel\033[m".center(55))
    print("\033[0;34m[ 2 ] - Tesoura\033[m".center(55))
    linha()
    o = int(input("\033[0;32mQual a sua jogada?\033[m "))
    linha()
    return o

def jogando():
    if c == 0:
        print("\033[0;33mJO!!\033[m".center(55))
        sleep(1)
        print("\033[0;33mKEN!\033[m".center(55))
        sleep(1)
        print("\033[0;33mPO!!\033[m".center(55))
        linha()
        if jogador == 0:
            print("\033[0;33mOPA! EMPATOU :/\033[m".center(55))
        elif jogador == 1:
            print("\033[0;33mOPA! VOCÊ GANHOU :(\033[m".center(55))
        elif jogador == 2:
            print("\033[0;33mOPA! VOCÊ PERDEU :)\033[m".center(55))
        else:
            print("\033[0;33mAmigo, essa opção não existe no jogo :)\033[m".center(55))
        linha()
    elif c == 1:
        print("\033[0;33mJO!!\033[m".center(55))
        sleep(1)
        print("\033[0;33mKEN!\033[m".center(55))
        sleep(1)
        print("\033[0;33mPO!!\033[m".center(55))
        linha()
        if jogador == 0:
            print("\033[0;33mOPA! VOCÊ PERDEU :)\033[m".center(55))
        elif jogador == 1:
            print("\033[0;33mOPA! EMPATOU :/\033[m".center(55))
        elif jogador == 2:
            print("\033[0;33mOPA! VOCÊ GANHOU :(\033[m".center(55))
        else:
            print("\033[0;33mAmigo, essa opção não existe no jogo :)\033[m".center(55))
    elif c == 2:
        print("\033[0;33mJO!!\033[m".center(55))
        sleep(1)
        print("\033[0;33mKEN!\033[m".center(55))
        sleep(1)
        print("\033[0;33mPO!!\033[m".center(55))
        linha()
        if jogador == 0:
            print("\033[0;33mOPA! VOCÊ GANHOU :(\033[m".center(55))
        elif jogador == 1:
            print("\033[0;33mOPA! VOCÊ PERDEU :)\033[m".center(55))
        elif jogador == 2:
            print("\033[0;33mOPA! EMPATOU :/\033[m".center(55))
        else:
            print("\033[0;33mAmigo, essa opção não existe no jogo :/\033[m".center(55))
        linha()

def novamente():
    while True:
        c = str(input("\033[0;32mJogar Novamente? [S/N]\033[m ")).upper().strip()
        if c == "S":
            c = True
            break
        elif c == "N":
            c = False
            break
        else:
            print("\033[0;33m< ERRO > valor inserido inválido < ERRO >\033[m")
            print("\033[0;32mTente novamente...\033[m")
            continue
    return c


# Programa Principal
while True:
    linha()
    c = computador()
    sleep(1.5)
    jogador = opções()
    jogando()
    n = novamente()
    if n == True:
        continue
    else:
        print("\033[0;33mAté a próxima :P\033[m".center(55))
        break