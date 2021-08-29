# Definindo Funções
from time import sleep
def lerSalario():
    while True:
        try:
            l = float(input("\033[0;32mQual é o salário do funcionário?\033[m R$"))
        except:
            print("\033[0;31m< ERROR > Falha ao ler salário < ERRO >\033[m")
            sleep(0.5)
            print("\033[0;32mTente Novamente...\033[m")
            continue
        else:
            break
    return l

def aumento():
    d = s + (s * 15 / 100)
    return d

def novoSalario():
    linha()
    print(f"\033[0;32mO salario de\033[m R${s:.2f}\033[0;32m, do funcionário, teve aumento de\033[m 15%")
    sleep(1)
    print(f"\033[0;32mO salário atual do funcionário é de:\033[m R${aumento():.2f}")
    linha()

def linha():
    print("\033[0;32m~\033[m"*60)


# Programa principal
s = lerSalario()
novoSalario()