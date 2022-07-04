from Biblioteca.continuar import continuar

# Definindo Funções
def exibição():
    for linha in range(0, 3):
        for coluna in range(0, 3):
            while True:
                try:
                    matriz[linha][coluna] = int(input(f"\033[0;32mDigite um valor para [{linha}, {coluna}]:\033[m "))
                except:
                    print("\033[0;31m< ERRO > valores inseridos inválidados < ERRO >\033[m")
                    continue
                else:
                    break

    print("-=-" * 10)

    for linha in range(0, 3):
        for coluna in range(0, 3):
            print(f"\033[0;34m[{matriz[linha][coluna]:^5}]\033[m", end="")
        print()


# Programa Principal
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
while True:
    exibição()
    c = continuar()
    if c == True:
        continue
    else:
        break