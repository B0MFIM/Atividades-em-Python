# Definindo Funções
from time import sleep
def lerproduto():
    while True:
        try:
            l = float(input("\033[0;32mQual é o preço do produto?\033[m R$"))
        except:
            print("\033[0;31m< ERROR > Falha ao ler valor < ERRO >\033[m")
            sleep(0.5)
            print("\033[0;32mTente Novamente...\033[m")
            continue
        else:
            break
    return l

def lerDesconto():
    while True:
        try:
            l = int(input("\033[0;32mQual é o desconto do produto?\033[m "))
        except:
            print("\033[0;31m< ERROR > Falha ao ler valor < ERRO >\033[m")
            sleep(0.5)
            print("\033[0;32mTente Novamente...\033[m")
            continue
        else:
            break
    return l

def desconto():
    d = pp - (pp * dp / 100)
    return d

def exibir():
    print(f"\033[0;32mO produto de\033[m R${pp:.2f}\033[0;32m, com desconto de \033[m{dp}%\033[0;32m, tem o valor de:\033[m R${desconto():.2f} ")

# Programa principal
pp = lerproduto()
dp = lerDesconto()
exibir()