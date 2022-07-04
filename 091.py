from random import randint
from time import sleep
from operator import itemgetter

# Definindo Funções
def exibição():
    print("\033[0;32mValores Sorteados:\033[m ")
    for chave, valor in jogo.items():
        print(f"\033[0;33m{chave}\033[m \033[0;32mtirou\033[m {valor} \033[0;32mno dado.\033[m")
        sleep(1)
    ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
    print("-=-" * 10)
    for item, valor in enumerate(ranking):
        print(f"\033[0;32m{item + 1}º Lugar:\033[m {valor[0]} com {valor[1]}")


# Programa Principal
ranking = list()
jogo = {"Jogador-1": randint(1, 6),
        "Jogador-2": randint(1, 6),
        "Jogador-3": randint(1, 6),
        "Jogador-4": randint(1, 6)}
exibição()