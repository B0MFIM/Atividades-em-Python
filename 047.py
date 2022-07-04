# Definindo Funções
def progressão():
    for n in range(2, 50+1, 2):
        if n % 2 == 0:
            print(f"\033[0;33m{n}\033[m", end=" ")
    print("\033[0;34mFim!\033[m")


# Programa Principal
progressão()