# Definindo Métodos
def sucessor(v):
    s = v+1
    return s

def antecessor(v):
    a = v-1
    return a

def leiaInt():
    while True:
        try:
            l = int(input("\033[0;32mDigite um valor inteiro: \033[m"))
        except:
            print("\033[0;31m< ERRO > Indique um valor inteiro válido < ERRO >\033[m")
            continue
        else:
            break
    return l

def exibir():
    print(f"\033[0;32mO sucessor de {n} é:\033[m \033[0;34m{sucessor(n)}\033[m")
    print(f"\033[0;32mO antecessor de {n} é:\033[m \033[0;34m{antecessor(n)}\033[m")


# Programa Principal
n = leiaInt()
exibir()