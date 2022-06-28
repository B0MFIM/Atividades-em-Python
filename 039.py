from datetime import date
from Biblioteca import continuar

# Definindo Funções
def exibirOpções():
    print("\033[0;33mEscolha uma das opções abaixo:\033[m")
    print("\033[0;34m[ 1 ] - para Homem\033[m")
    print("\033[0;34m[ 2 ] - para Mulher\033[m")
    print("\033[0;34m[ 3 ] - para Outro\033[m")

def lerOpção():
    while True:
        try:
            while True:
                l = int(input("\033[0;32mSua Opção:\033[m "))
                if l == 1 or l == 2 or l == 3:
                    break
                else:
                    print("\033[0;31m< ERRO > Opção inválida < ERRO >\033[m")
                    continue
        except:
            print("\033[0;31m< ERRO > Opção inválida < ERRO >\033[m")
            continue
        else:
            break
    return l

def lerAno():
    while True:
        try:
            l = int(input("\033[0;32mQual seu ano de nascimento:\033[m "))
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            continue
        else:
            break
    return l

def Idade():
    i = date.today().year - a
    return i

def exibição():
    print(f"Quem nasceu em {a} tem {Idade()} anos em {date.today().year}")
    if o == 2 or o == 3:
        print("Somente Homens podem se alistar!")
    elif Idade() < 18 and o == 1:
        saldo = 18 - Idade()
        print(f"Ainda faltam {saldo} anos para o seu alistamento!")
        ano = date.today().year + saldo
        print(f"Seu alistamento será em {ano}.")
    elif Idade() == 18 and o == 1:
        print("Você tem que se alistar imediatamente!")
    elif Idade() > 18 and o == 1:
        saldo = Idade() - 18
        print(f"Você ja deveria ter se alistado há {saldo} ano(s)!")
        ano = date.today().year - saldo
        print(f"Seu alistamento foi em {ano}.")

# Programa Principal
while True:
    exibirOpções()
    o = lerOpção()
    a = lerAno()
    exibição()
    c = continuar.continuar()
    if c == True:
        continue
    else:
        break