from time import sleep
from math import hypot

# Definindo Funções
def lerOposto():
    while True:
        try: 
            l = float(input("\033[0;32mQual o valor do Cateto Oposto?\033[m "))
        except:
            print("\033[0;31m< ERRO > Valor Inválido < ERRO >\033[0;31m")
            sleep(0.8)
            print("\033[0;32mTente Novamente...\033[m")
            continue
        else:
            break
    return l
            
def lerAdjacente():
    while True:
        try:
            l = float(input("\033[0;32mQual o valor do Cateto Adjacente?\033[m "))
        except:
            print("\033[0;31m< ERRO > Valor Inválido < ERRO >\033[m") 
            sleep(0.8)
            print("\033[0;32mTente Novamente...\033[m")
            continue
        else:
            break
    return l     

def hipotenusa(o, a):
    h = hypot(o, a)
    return h

def exibir():
    print(f"\033[0;32mO comprimento da hipotenusa é de:\033[m {hipotenusa(co, ca):.2f}")


# Programa Principal
co = lerOposto()
ca = lerAdjacente()
exibir()