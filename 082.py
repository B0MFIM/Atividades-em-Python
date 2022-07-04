from Biblioteca import leitura, continuar

# Definindo Funções
def exibição():
    while True:
        numero = leitura.lerNúmInteiro()
        listaNúm.append(numero)
        c = continuar.continuar()
        if numero % 2 == 0:
            listaPares.append(numero)
        else:
            listaImpares.append(numero)
        if c == True:
            continue
        else:
            break
    print(f"\033[0;32mOs valores digitados são:\033[m ", end="")
    for numero in listaNúm:
        print(numero, end=" ")
    print(f"\n\033[0;33mOs valores pares:\033[m ", end="")
    for numero in listaPares:
        print(numero, end=" ")
    print(f"\n\033[0;33mOs valores impares:\033[m ", end="")
    for numero in listaImpares:
        print(numero, end=" ")


# Programa Principal
listaNúm = list()
listaPares = list()
listaImpares = list()
exibição()