from Biblioteca import leitura, continuar

# Definindo Funções
def exibição():
    while True:
        numero = leitura.lerNúmInteiro()
        if numero not in lista:
            lista.append(numero)
            print("\033[0;34mValor adicionado com sucesso!\033[0;32m")
        else:
            print("\033[0;33m< ALERT > Valor duplicado! Não adicionado! < ALERT >\033[m")
        c = continuar.continuar()
        if c == True:
            continue
        else:
            print(f"\033[0;32mOs valores digitados foram:\033[m {sorted(lista)}")
            print("\033[0;32mAté...\033[m")
            break

# Programa Principal
lista = list()
exibição()