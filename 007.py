# Definindo Funções
def lerValor():
    while True:
        try: 
            l = int(input("\033[0;32mDigite um número: \033[m"))
        except:
            print("\033[0;31m< ERRO > Indique um número inteiro válido < ERRO >\033[m")
            continue
        else:
            break
    return l

def converter(v):
    print(f"\033[0;33m{v/1000}\033[m km")
    print(f"\033[0;33m{v/100}\033[m hm")
    print(f"\033[0;33m{v/10}\033[m dam")
    print(f"\033[0;33m{v*10:.0f}\033[m dm")
    print(f"\033[0;33m{v*100:.0f}\033[m cm")
    print(f"\033[0;33m{v*1000:.0f}\033[m mm")

def exibir():
    print(f"\033[0;32mA medida de {n}m corresponde a:\033[m")
    converter(n)


# Programa Principal
n = lerValor()
exibir()