from Biblioteca.continuar import continuar

# Definindo Funções
def exibição():
    somaPares = somaColuna = maior = 0

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
            if matriz[linha][coluna] % 2 == 0:
                somaPares += matriz[linha][coluna]
        print()
    print("-=-" * 10)
    print(f"\033[0;32mA soma dos valores pares é:\033[m {somaPares}")

    for linha in range(0, 3):
        somaColuna += matriz[linha][2]
    print(f"\033[0;32mA soma dos valores da terceira coluna é:\033[m {somaColuna}")
    for coluna in range(0, 3):
        if coluna == 0:
            maior = matriz[1][coluna]
        elif matriz[1][coluna] > maior:
            maior = matriz[1][coluna]
    print(f"\033[0;32mO maior valor da segunda linha é:\033[m {maior}")


# Programa Principal
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
while True:
    exibição()
    c = continuar()
    if c == True:
        continue
    else:
        break