from Biblioteca.continuar import continuar

# Definindo Funções
def exibição():
    for contador in range(1, 7+1):
        while True:
            try:
                valor = int(input(f"\033[0;32mDigite o {contador}º valor:\033[m "))
            except:
                print("\033[0;31m< ERRO > valores inseridos inválidados < ERRO >\033[m")
                continue
            else:
                if valor % 2 == 0:
                    lista[0].append(valor)
                else:
                    lista[1].append(valor)
                break
    print(f"\033[0;32mOs valores pares digitados foram:\033[m {sorted(lista[0])}")
    print(f"\033[0;32mOs valores impares digitados foram:\033[m {sorted(lista[1])}")

# Programa Principal
lista = [[], []]
while True:
    exibição()
    c = continuar()
    if c == True:
        continue
    else:
        break