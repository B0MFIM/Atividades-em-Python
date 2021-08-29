# Definindo Funções
from time import sleep
def lerCelcius():
    while True:
        try:
            l = float(input("\033[0;32mDigite a temperatura em °C:\033[m "))
        except:
            print("\033[0;31m< ERROR > Falha ao ler a temperatura < ERRO >\033[m")
            sleep(0.5)
            print("\033[0;32mTente Novamente...\033[m")
            continue
        else:
            break
    return l

def fahrenheit():
    f = ((9 * c)/ 5) + 32
    return f

def exibir():
    linha()
    print(f"\033[0;32mA temperatura de\033[m {c}°C \033[0;32mconvertida para Fahrenheit é de:\033[m {fahrenheit()}°F")
    linha()

def linha():
    print("\033[0;32m~\033[m"*65)


# Programa Principal
c = lerCelcius()
exibir()