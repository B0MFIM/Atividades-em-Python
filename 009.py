# Definindo Funções
def carteira():
    while True:
        try:
            c = float(input("\033[0;32mQuantos reais há em sua carteira?\033[m R$"))
        except:
            print("\033[0;31m< ERRO > Indique um valor válido < ERRO >\033[m")
            continue
        else:
            break
    return c

def dolar(v):
    d = v/5.25
    return d

def euro(v):
    e = v/6.18
    return e

def iene(v):
    i = v/0.048
    return i

def exibir():
    linha()
    print(f"\033[0;32mCom R${c:.2f} você pode obter:\033[m")
    print(f"\033[0;34mUS$\033[m\033[0;33m{dolar(c):.2f}\033[m")
    print(f"\033[0;34mEU$\033[m\033[0;33m{euro(c):.2f}\033[m")
    print(f"\033[0;34mien$\033[m\033[0;33m{iene(c):.2f}\033[m")
    linha()

def linha():
    print("\033[0;32m~\033[m"*30)


# Programa Principal
c = carteira()
exibir()