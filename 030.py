from Biblioteca import leitura

# Definindo Funções
def exibir():
    r = n % 2
    if r == 0:
        print(f"\033[0;32mO número\033[m {n} \033[0;32mé PAR!\033[m")
    else:
        print(f"\033[0;32mO número\033[m {n} \033[0;32mé IMPAR!\033[m")


# Programa Principal
n = leitura.lerNúmInteiro()
exibir()