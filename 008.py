# Definindo Funções
def tabuada(v):
    linha()
    for c in range(1, 10+1):
        print(f"\033[0;32m{v}\033[m x \033[0;32m{c}\033[m = \033[0;33m{v * c}\033[m")
    linha()

def lerValor():
    l = int(input("\033[0;32mDigite um valor inteiro: \033[m"))
    return l

def linha():
    print("\033[0;32m~\033[m"*28)


# Programa Principal
n = lerValor()
tabuada(n)