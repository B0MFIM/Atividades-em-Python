# Definindo Métodos
def exibição(v):
    linha()
    print(f"\033[0;32mO valor '{v}' é uma string?\033[m")
    if v.isalpha():
        print(f"\033[0;33mSim, '{v}' é um valor string!\033[m")
        linha()
    else:
        print(f"\033[0;31mNão, '{v}' não é um valor string!\033[m")
        linha()
    print(f"\033[0;32mO valor '{v}' é um número?\033[m")
    if v.isnumeric():
        print(f"\033[0;33mSim, '{v}' é um valor numérico!\033[m")
        linha()
    else:
        print(f"\033[0;31mNão, '{v}' não é um valor numérico!\033[m")
        linha() 
    print(f"\033[0;32mO valor '{v}' é alfanumérico?\033[m")
    if v.isalnum():
        print(f"\033[0;33mSim, '{v}' é um valor alfanumérico!\033[m")
        linha()
    else:
        print(f"\033[0;31mNão, '{v}' não é um valor alfanumérico!\033[m")
        linha()

def leitura():
    l = input("\033[0;32mDigite algo a ser analisado: \033[m")
    return l

def linha():
    print("="*40)

# Programa Principal
v = leitura()
exibição(v)