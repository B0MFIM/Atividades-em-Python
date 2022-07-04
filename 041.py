from datetime import date
from Biblioteca import continuar

# Definindo Funções
def lerNome():
    l = str(input("\033[0;33mQual o nome do atleta?\033[m "))
    return l
        
def lerAno():
    while True:
        try:
            l = int(input("\033[0;33mAno de Nascimento do Atleta:\033[m "))
        except:
            print("\033[0;31m< ERRO >valor inserido inválido < ERRO >\033[m")
            continue
        else:
            break
    return l

def idade():
    i = date.today().year - a
    return i

def exibição():
    print(f"\033[0;32mO atleta tem\033[m {idade()} \033[0;32manos.\033[m")
    if idade() <= 9:
        print(f"\033[0;32mO atleta {n} é\033[m MIRIM!")
    elif 9 < idade() <= 14:
        print(f"\033[0;32mO atleta {n} é\033[m INFANTIL")
    elif 14 < idade() <= 19:
        print(f"\033[0;32mO atleta {n} é\033[m JUNIOR")
    elif idade() == 20:
        print(f"\033[0;32mO atleta {n} é\033[m SÊNIOR")
    elif idade() > 20:
        print(f"\033[0;32mO atleta {n} é\033[m MASTER")


# Programa Principal
while True:
    n = lerNome()
    a = lerAno()
    exibição()
    c = continuar.continuar()
    if c == True:
        continue
    else:
        print("\033[0;32mAté...\033[m")
        break