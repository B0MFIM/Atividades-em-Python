from time import sleep

# Definindo Funções
def progressão():
    for t in range(10, -1, -1):
        print(f"\033[0;34m{t}! \033[m")
        sleep(1)
    print("\033[0;35mGOOOOO!!\033[m")


# Programa Principal
progressão()