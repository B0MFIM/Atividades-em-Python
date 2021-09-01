from time import sleep

# Definindo Funções
def lerDias():
    while True:
        try:
            l = int(input("\033[0;32mQuantos dias de aluguel?\033[m "))
        except:
            print("\033[0;31m< ERROR > Valor inserido inválido < ERRO >\033[m")
            sleep(0.8)
            print("\033[0;32mTente novamente...\033[m")
            continue
        else:
            break
    return l

def lerKm():
    while True:
        try:
            l = float(input("\033[0;32mQuantos Km rodados?\033[m "))
        except:
            print("\033[0;31m< ERROR > Valor inserido inválido < ERRO >\033[m")
            sleep(0.8)
            print("\033[0;32mTente novamente...\033[m")
            continue
        else:
            break
    return l

def pagar():
    p = (dias * 60) + (km * 0.15)
    return p

def exibir():
    print(f"\033[0;32mO total a ser pago é de:\033[m R${pagar():.2f}")

# Programa Principal
dias = lerDias()
km = lerKm()
exibir()