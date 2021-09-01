from time import sleep
# from math import trunc
# Definindo Funções
def lerNumero():
    while True:
        try:
            l = float(input("\033[0;32mDigite um número:\033[m "))
        except:
            print("\033[0;31m< ERROR > Valor numérico inválido < ERRO >\033[m")
            sleep(0.8)
            print("\033[0;32mTente novamente...\033[m")
            continue
        else:
            break
    return l

def exibir():
    print(f"\033[0;32mO número digitado foi {numero} e sua porção inteira é {numero:.0f}\033[m")
    # print(f"\033[0;32mO número digitado foi {numero} e sua porção inteira é {trunc(numero)}\033[m")


# Programa Principal
numero = lerNumero()
exibir()