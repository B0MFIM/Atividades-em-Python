from math import sqrt
from Biblioteca import leitura

# Definindo Métodos
def dobro(v):
    d = v * 2
    return d

def triplo(v):
    t = v * 3
    return t

def raizQuadrada(v):
    r = sqrt(v)
    return r

def exibir():
    print(f"O dobro de \033[0;33m{n}\033[m é \033[0;34m{dobro(n)}\033[m")
    print(f"O triplo de \033[0;33m{n}\033[m é \033[0;34m{triplo(n)}\033[m")
    print(f"A raiz quadrada de \033[0;33m{n}\033[m é \033[0;34m{raizQuadrada(n)}\033[m")

def linha():
    print("\033[0;35m~\033[m"*40)

# Programa Pricipal
linha()
n = leitura.lerNúmInteiro()
linha()
exibir()
linha()