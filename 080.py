from Biblioteca import leitura, continuar

# Definindo Funções
def exibição():
    for contador in range(0, 5):
        numero = leitura.lerNúmInteiro()
        if contador == 0 or numero > lista[-1]:
            lista.append(numero)
        else: 
            posição = 0
            while posição < len(lista):
                if numero <= lista[posição]:
                    lista.insert(posição, numero)
                    break
                posição += 1
    print(f"\033[0;32mOs valores digitados, em ordem, foram:\033[m", end=" ")
    for numero in lista:
        print(numero, end=" ")
    print("\n")


# Programa Principal
lista = list()
while True:
    exibição()
    c = continuar.continuar()
    if c == True:
        lista.clear()
        continue
    else:
        print("\033[0;32mAté...\033[m")
        break