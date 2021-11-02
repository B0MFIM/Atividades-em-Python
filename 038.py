from Biblioteca import continuar

# Definindo Funções
def lerNúmero():
    while True:
        try:
            for c in range(1, 2+1):
                l = int(input(f"Digite o {c}º número: "))
                lista.append(l)
        except:
            print("< ERRO > valor inserido inválido < ERRO >")
            lista.clear()
            continue
        else:
            break

def valorMaior():
    if lista[0] > lista[1]:
        print("O 1º valor digitado é o maior!")
    elif lista[0] == lista[1]:
        print("Não há valor maior, os dois são iguais!")
    else:
        print("O 2º valor digitado é o maior!")


# Programa Principal
lista = list()
while True:
    n = lerNúmero()
    valorMaior()
    c = continuar.continuar()
    if c == True:
        lista.clear()
        continue
    else:
        break