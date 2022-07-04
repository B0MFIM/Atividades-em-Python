# Definindo Funções
def tabuada():
    while True:
        try:
            n = int(input("\033[0;32mDigite um número:\033[m "))
        except:
            print("< ERRO > valor inserido inválido < ERRO >")
            continue
        else:
            for v in range(1, 10+1):
                print(f"\033[0;33m{n} x {v:2} =\033[m {n * v}")
            c = str(input("\033[0;32mQuer tentar novamente? [S/N]\033[m ")).strip().upper()
            if c == "S":
                continue
            else:
                print("\033[0;32mAté...\033[m")
                break


# Programa Principal
tabuada()