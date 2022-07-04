from random import randint
from time import sleep

# Definindo Funções
def lin():
    print("-=-" * 11)

def exibição():
    lin()
    titulo = "JOGAR NA MEGA SENA"
    print(f"{titulo: ^33}")
    lin()

    while True:
        try:
            quantidade = int(input("Quantos jogos para sorteiar? "))
        except:
            print("< ERRO > valor inserido inválido < ERRO >")
            continue
        else:
            break

    total = 1
    while total <= quantidade:
        contador = 0
        while True:
            numero = randint(1, 60)
            if numero not in dados:
                dados.append(numero)
                contador += 1
            if contador >= 6:
                break
        dados.sort()
        jogos.append(dados[:])
        dados.clear()
        total += 1

    print(f"=--=--= SORTEANDO {quantidade} JOGOS =--=--=")

    for indice, dado in enumerate(jogos):
        print(f"Jogo {indice + 1}: {dado}")
        sleep(1)
    
    print("-=--=--=--= BOA SORTE =--=--=--=-")


# Programa Principal
jogos = list()
dados = list()
exibição()