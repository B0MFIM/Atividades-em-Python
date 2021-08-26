from math import sqrt

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

def leiaInt():
    while True:
        try: 
            l = int(input("\033[0;32mDigite um número: \033[m"))
        except:
            print("\033[0;31m< ERRO > Indique um número inteiro válido < ERRO >\033[m")
            continue
        else:
            break
    return l

def linha():
    print("\033[0;35m~\033[m"*40)

# Programa Pricipal
linha()
n = leiaInt()
linha()
exibir()
linha()