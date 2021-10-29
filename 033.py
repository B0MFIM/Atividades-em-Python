# Definindo Funções
def lerNúmero():
    while True:
        try:
            for c in range(1, 3+1):
                l = int(input(f"\033[0;33mDigite o {c}º Número:\033[m "))
                lista.append(l)
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            print("\033[0;32mTente novamente...\033[m")
            lista.clear()
            continue
        else:
            break

def maiorNúmero():
    if lista[1] < lista[0] > lista[2]:
        print(f"\033[0;32mO maior número foi:\033[m {lista[0]}")
    if lista[0] < lista[1] > lista[2]:
        print(f"\033[0;32mO maior número foi:\033[m {lista[1]}")
    if lista[1] < lista[2] > lista[0]:
        print(f"\033[0;32mO maior número foi:\033[m {lista[2]}")

def menorNúmero():
    if lista[1] > lista[0] < lista[2]:
        print(f"\033[0;32mO menor número foi:\033[m {lista[0]}")
    if lista[0] > lista[1] < lista[2]:
        print(f"\033[0;32mO menor número foi:\033[m {lista[1]}")
    if lista[1] > lista[2] < lista[0]:
        print(f"\033[0;32mO menor número foi:\033[m {lista[2]}")


# Programa Principal
lista = list()
n = lerNúmero()
maiorNúmero()
menorNúmero()
