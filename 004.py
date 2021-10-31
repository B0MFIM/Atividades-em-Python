from Biblioteca import leitura

# Definindo Métodos
def sucessor(v):
    s = v+1
    return s

def antecessor(v):
    a = v-1
    return a

def exibir():
    print(f"\033[0;32mO sucessor de {n} é:\033[m \033[0;34m{sucessor(n)}\033[m")
    print(f"\033[0;32mO antecessor de {n} é:\033[m \033[0;34m{antecessor(n)}\033[m")


# Programa Principal
n = leitura.lerNúmInteiro()
exibir()