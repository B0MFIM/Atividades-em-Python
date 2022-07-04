from Biblioteca import continuar, leitura

# Definindo Funções
def exibição():
    quantidade = 0
    while True:
        numero = leitura.lerNúmInteiro()
        lista.append(numero)
        quantidade += 1
        c = continuar.continuar()
        if c == True:
            continue
        else:
            break
    print(f"\033[0;32mA quantidade de números digitados foram:\033[m {quantidade} \033[0;32melemento(s).\033[m")
    lista.sort(reverse=True)
    print("\033[0;32mA lista em ordem decrescente:\033[m", end=" ")
    for numero in lista:
        print(numero, end=" ")
    if 5 not in lista:
        print("\n\033[0;31mO valor 5 não foi digitado na lista!\033[m")
    else:
        print("\n\033[0;33mO valor 5 faz parte da lista.\033[m")


# Prgrama Principal
lista = list()
exibição()