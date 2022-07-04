# Definindo Funções
def progressãoA():
    print("-=-" * 10)
    print("\033[0;33m10 TERMOS DE UMA PA\033[m".center(42))
    print("-=-" * 10)
    while True:
        try:
            pt = int(input("\033[0;32mDigite o Primeiro Termo:\033[m "))
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            continue
        else:
            while True:
                try:
                    razão = int(input("\033[0;32mDigite a Razão:\033[m "))
                except:
                    print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
                    continue
                else:
                    break
            break
    pa = pt + (10 - 1) * razão
    for c in range(pt, pa + razão, razão):
        print(f"{c}", end=" -> ")
    print("Fim!")


# Programa Principal
progressãoA()