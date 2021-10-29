# Definindo Funções
def lerCasa():
    while True:
        try:
            l = float(input("\033[0;32mQual o valor da casa a ser comprada?\033[m R$"))
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            print("\033[0;32mTente novamente...\033[m")
            continue
        else:
            break
    return l


def lerSalário():
    while True:
        try:
            l = float(input("\033[0;32mQual o salário do comprador?\033[m R$"))
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            print("\033[0;32mTente novamente...\033[m")
            continue
        else:
            break
    return l

def lerAno():
    while True:
        try:
            l = int(input("\033[0;32mEm quantos anos a casa será paga?\033[m "))
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            print("\033[0;32mTente novamente...\033[m")
            continue
        else:
            break
    return l

def prestação():
    p = c / (a * 12)
    return p

def mínimo():
    m = s * 30 / 100
    return m

def exibir():
    print(f"\033[0;32mPara pagar a casa de\033[m R${c:.2f} \033[0;32mem\033[m {a} ano(s)\033[0;32m, a prestação será de\033[m R${prestação():.2f}")
    if prestação() <= mínimo():
        print("\033[0;33m< Empréstimo Concedido >\033[m")
    else:
        print("\033[0;31m< Empréstimo Negado >\033[m")


# Programa Principal
c = lerCasa()
s = lerSalário()
a = lerAno()
exibir()