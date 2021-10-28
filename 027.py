# Definindo Funções
def lerNome():
    l = str(input("\033[0;32mDigite o seu nome:\033[m ")).strip().split()
    return l

def exibir():
    print(f"\033[0;32mPrazer em conhecer você {nome[0]}\033[m")
    print(f"\033[0;32mSeu primeiro nome é\033[m {nome[0]}")
    print(f"\033[0;32mSeu ultimo nome é\033[m {nome[len(nome)-1]}")


# Programa Principal
nome = lerNome()
exibir()