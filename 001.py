from Biblioteca import leitura

# Definindo Métodos
def linha():
    print("\033[0;33m~\033[m"*40)

def boasvindas(txt):
    linha()
    print(f"\033[0;33mBOAS VINDAS AO SISTEMA {txt}\033[m".center(50))
    linha()

# Programa Principal
nome = leitura.lerNome()
boasvindas(nome)