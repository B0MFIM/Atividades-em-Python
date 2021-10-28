# Definindo Funções
def lerNome():
    l = str(input("\033[0;32mDigite o seu nome:\033[m ")).strip()
    return l

def upperName():
    return n.upper()

def lowerName():
    return n.lower()

def exibir():
    print("\033[0;32m=\033[m" * 40)
    print(f"\033[0;32mO seu nome em maiúsculas é:\033[m {upperName()}")
    print(f"\033[0;32mO seu nome em minúsculas é:\033[m {lowerName()}")
    print("\033[0;32m=\033[m" * 40)

# Programa Principal

n = lerNome()
exibir()