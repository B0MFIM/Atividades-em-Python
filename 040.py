from time import sleep
from Biblioteca import continuar

# Definindo Funções
def lerNotas():
    while True:
        try:
            for c in range(1, 2+1):
                l = float(input(f"\033[0;32mDigite a sua {c}º nota:\033[m"))
                lista.append(l)
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            lista.clear()
            continue
        else:
            break

def média():
    m = (lista[0] + lista[1]) / 2
    return m

def exibir():
    if média() < 5.0:
        print(f"Sua média foi de: {média()}")
        sleep(1)
        print("\033[0;31m< REPROVADO >\033[m")
    elif 5.0 <= média() < 7.0:
        print(f"Sua média foi de: {média()}")
        sleep(1)
        print("\033[0;33m< RECUPERAÇÃO >\033[m")
    elif média() >= 7.0:
        print(f"Sua média foi de: {média()}")
        sleep(1)
        print("\033[0;35m< APROVADO >\033[m")


# Programa Principal
while True:
    lista = list()
    n = lerNotas()
    exibir()
    c = continuar.continuar()
    if c == True:
        continue
    else:
        break