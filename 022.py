from Biblioteca import leitura

# Definindo Funções
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

n = leitura.lerNome()
exibir()