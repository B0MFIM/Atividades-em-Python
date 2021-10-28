# Definindo Funções
def lerNúmero():
    while True:
        try:
            l = int(input("\033[0;33mDigite um número:\033[m "))
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            print("\033[0;32mTente novamente...\033[m")
            continue
        else:
            break
    return l

def exibir():
    r = n % 2
    if r == 0:
        print(f"\033[0;32mO número\033[m {n} \033[0;32mé PAR!\033[m")
    else:
        print(f"\033[0;32mO número\033[m {n} \033[0;32mé IMPAR!\033[m")


# Programa Principal
n = lerNúmero()
exibir()