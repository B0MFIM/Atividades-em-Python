from Biblioteca import leitura

# Definindo Métodos
def soma(a=0, b=0):
    s = a + b
    return s

def linha():
    print("\033[0;33m~\033[m"*20)

def exibir():
    print(f"\033[0;33mA Soma de {n1} + {n2} é {soma(n1, n2)}\033[m")

# Programa Principal
n1 = leitura.lerNúmInteiro()
n2 = leitura.lerNúmInteiro()
linha()
exibir()
linha()