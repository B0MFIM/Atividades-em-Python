from random import randint

# Definindo Funções
def exibição():
    print(f"Os valores sorteados foram:", end=" ")
    for numero in range(0, 4+1):
        print(f"{tuplaRandom[numero]}", end=" ")
    print(f"\nO Maior valor sorteado foi: {max(tuplaRandom)}")
    print(f"O Menor número sorteado foi: {min(tuplaRandom)}")


# Programa Principal
tuplaRandom = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
exibição()