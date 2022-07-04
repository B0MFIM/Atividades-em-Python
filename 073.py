# Definindo Funções
def lin():
    print("\033[0;35m-=-\033[m" * 12)

def exibição():
    lin()
    print("\033[0;33mOs Cinco primeiros colocados são:\033[m ")
    lin()
    for contador in range(1, 5+1):
        print(f"O {tabela[contador]} está em {contador}º posição")
    
    lin()
    print("\033[0;33mOs ultimos quatro colocados são:\033[;33m ")
    lin()
    for contador in range(16, 20):
        print(f"O {tabela[contador]} está em {contador + 1}º posição")
    
    lin()
    print("\033[0;33mVinte colocados em ordem alfabética:\033[m ")
    lin()
    alfa = sorted(tabela)
    for contador in range(0, 20):
        print(f"{alfa[contador]}")
    lin()


# Programa Principal
tabela = ("Atlético-MG", "Palmeiras", "Fortaleza", "Bragantino", "Flamengo", "Atlético-PR", "Ceará SC", "Santos",
          "Atlético-GO", "Bahia", "Internacional", "Corinthians", "Fluminense", "Juventude", "Sport Recife",
          "São Paulo", "América-MG", "Cuiabá", "Grêmio", "Chapecoense")
exibição()