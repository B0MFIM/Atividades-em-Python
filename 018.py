from math import radians, sin, cos, tan

# Definindo Funções
def lerAngulo():
    while True:
        try:
            l = float(input("\033[0;32mDigite o ângulo desejado:\033[m "))
        except:
            print("\033[0;31m< ERRO > Valor inserido inválido < ERRO >\033[m")
            print("\033[0;32mTente novamente...\033[m")
            continue
        else:
            break
    return l

def exibir():
    print(f"\033[0;32mO ângulo de\033[m {a}° \033[0;32mpossui:\033[m ")
    print("=" * 30)
    print(f"\033[0;32mSEN de\033[m {sin(radians(a)):.2f}°")
    print(f"\033[0;32mCOS de\033[m {cos(radians(a)):.2f}°")
    print(f"\033[0;32mTAN de\033[m {tan(radians(a)):.2f}°")
    print("=" * 30)


# Programa Principal
a = lerAngulo()
exibir()