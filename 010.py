# Definindo Funções
def largura():
    while True:
        try:
            l = float(input("\033[0;32mIndique a Largura: \033[m"))
        except:
            print("\033[0;31m< ERRO > Indique um valor válido < ERRO >\033[m")
            continue
        else:
            break
    return l

def altura():
    while True:
        try:
            a = float(input("\033[0;32mIndique a Altura: \033[m"))
        except:
            print("\033[0;31m< ERRO > Indique um valor válido < ERRO >\033[m")
            continue
        else:
            break
    return a

def area(x=0, y=0):
    a = x * y
    return a

def pintar(x=0, y=0):
    p = (x * y) / 2
    return p


# Programa Principal
L = largura()
A = altura()
print(f"\033[0;32mSua parede tem a dimensão de\033[m \033[0;33m{L}x{A}\033[m \033[0;32me sua área é de\033[m \033[0;33m{area(L, A)}\033[m\033[0;32mm².\033[m")
print(f"\033[0;32mPara pintar sua parede é necessário de\033[m \033[0;33m{pintar(L, A)}\033[m\033[0;32ml de tinta.\033[m")