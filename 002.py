# Definindo Métodos
def soma(a=0, b=0):
    s = a + b
    return s

def leiaInt():
    while True:
        try: 
            l = int(input("\033[0;32mDigite um número: \033[m"))
        except:
            print("\033[0;31m< ERRO > Falha na leitura dos dados < ERRO >\033[m")
            continue
        else:
            break
    return l

def linha():
    print("\033[0;33m~\033[m"*20)

def exibir():
    print(f"\033[0;33mA Soma de {n1} + {n2} é {soma(n1, n2)}\033[m")

# Programa Principal
n1 = leiaInt()
n2 = leiaInt()
linha()
exibir()
linha()