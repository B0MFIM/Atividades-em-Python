from Biblioteca import continuar

# Definindo Funções
def lendoValor():
    print("=-" * 25)
    while True:
        try:
            for contador in range(0, 5):
                lista.append(int(input(f"\033[0;33mDigite um valor na posição {contador + 1}:\033[m ")))
        except:
            lista.clear()
            print("\033[0;31m< ERRO > valores inseridos inválidados < ERRO >\033[m")
            continue
        else:
            break

def exibição():
    print("=-" * 25)
    print(f"\033[0;32mVocê digitou os valores:\033[m", end=" ")
    for numero in lista:
        print(numero, end=" ")
    print(f"\n\033[0;32mO Maior valor digitado foi:\033[m {max(lista)} \033[0;32m-> Na(s) posição(ôes):\033[m ", end="")
    for i, v in enumerate(lista):
        if v == max(lista):
            print(f"{i + 1}.. ", end="")
    print(f"\n\033[0;32mO Menor valor digitado foi:\033[m {min(lista)} \033[0;32m-> Na(s) posição(ôes):\033[m ", end="")
    for i, v in enumerate(lista):
        if v == min(lista):
            print(f"{i + 1}.. ", end="")
    print("\n")


# Programa Principal
lista = list()
while True:
    lendoValor()
    exibição()
    c = continuar.continuar()
    if c == True:
        lista.clear()
        continue
    else:
        print("\033[0;32mAté...\033[m")
        break