# Definindo Funções
def lerDistância():
    while True:
        try:
           l = int(input("\033[0;33mQual a distância de sua viagem?\033[m "))  
        except:
            print("\033[0;31m< ERRO > Valor Inserido Inválido < ERRO >\033[m")
            print("\033[0;32mTente novamente...\033[m")
            continue
        else:
            break
    return l

def valores():
    if d <= 200:
        p = 0.5 * d
    else:
        p = 0.45 * d
    return p

def exibir():
    print(f"\033[0;32mVocê está prestes a começar uma viagem de\033[m {d}Km.")
    print(f"\033[0;32mE o preço de sua viagem é de\033[m R${valores():.2f}")

# Programa Principal
d = lerDistância()
exibir()
