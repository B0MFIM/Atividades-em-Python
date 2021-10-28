from random import randint
from time import sleep

# Definindo Funções
def lerJogo():
    while True:
        try:
            while True:
                l = int(input("\033[0;32mEm que número estou pensando?\033[m "))
                if l > 5 or l < 0:
                    print("AMIGO, É UM NÚMERO ENTRE 0 e 5!!")
                    sleep(1)
                    print("TENTA DE NOVO AÍ")
                    sleep(1)
                    continue
                else:
                    break
        except:
            print("É PRA VOCÊ DIGITAR UM NÚMERO DE 0 A 5 AMIGO!")
            sleep(1.5)
            print("TENTA DE NOVO AÍ")
            sleep(1)
            continue
        else:
            break
    return l

def linha():
    print("\033[0;34m-=-\033[m" * 20)

def exibir():
    linha()
    print("VOU PENSAR EM UM NÚMERO DE 0 A 5, TENTE ADIVINHAR!!".center(60))
    linha()

    sleep(1)
    jogo = lerJogo()
    sleep(0.5)

    linha()
    print("PROCESSANDO...".center(60))
    linha()

    sleep(1)

    if jogo == computador:
        print("PARABÉNS! ACERTOU!!".center(60))
        linha()
    else:
        print("OPA! VOCÊ ERROU!!".center(60))
        linha()


# Programa Principal
computador = randint(0, 5)
exibir()