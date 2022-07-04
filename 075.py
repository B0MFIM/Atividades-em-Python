from Biblioteca import leitura, continuar

# Definindo Funções
def codagem():
    tuplaNúm = (leitura.lerNúmInteiro(), leitura.lerNúmInteiro(), leitura.lerNúmInteiro(), leitura.lerNúmInteiro())
    
    print(f"\033[0;32mVocê digitou os valores:\033[m", end=" ")
    for numero in range(0, 3+1):
        print(f"{tuplaNúm[numero]}", end=" ")

    print(f"\n\033[0;32mO número 9 apareceu\033[m {tuplaNúm.count(9)} \033[0;32mvez(es) na tupla.\033[m")
    if 3 in tuplaNúm:
        print(f"\033[0;32mO primeiro valor 3 foi digitado na\033[m {tuplaNúm.index(3) + 1}º \033[0;32mposição.\033[m")
    else:
        print("\033[0;31mO valor 3 não foi digitado.\033[m")

    print("\033[0;32mOs valores pares digitados foram:\033[m", end=" ")
    for numero in range(0, 3+1):
        if tuplaNúm[numero] % 2 == 0:
            print(tuplaNúm[numero], end=" ")
    print("\n")


# Programa Principal
while True:
    codagem()
    c = continuar.continuar()
    if c == True:
        continue
    else:
        print("Até...")
        break