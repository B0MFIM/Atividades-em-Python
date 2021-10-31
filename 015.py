from time import sleep
from Biblioteca import leitura
# from math import trunc


# Definindo Funções
def exibir():
    print(f"\033[0;32mO número digitado foi {numero} e sua porção inteira é {numero:.0f}\033[m")
    # print(f"\033[0;32mO número digitado foi {numero} e sua porção inteira é {trunc(numero)}\033[m")


# Programa Principal
numero = leitura.lerNúmReal()
exibir()