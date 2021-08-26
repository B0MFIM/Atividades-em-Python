# Definindo Funções
def lerNota():
    for c in range(1, 2+1):
        while True:
            try:
                n = float(input(f"\033[0;32mDigite sua {c}º nota: \033[m"))
            except:
                print("\033[0;31m< ERRO > Indique um valor válido < ERRO >\033[m")
                continue
            else:
                notas.append(n)
                break

def media(a, b):
    m = (a + b) / 2
    return m

def exibirMedia():
    print(f"\033[0;32mA média das notas é de:\033[m \033[0;33m{media(notas[0], notas[1])}\033[m")


# Programa Principal
notas = list()
nota = lerNota()
exibirMedia()