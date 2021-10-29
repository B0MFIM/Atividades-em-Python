# Definindo Funções
def lerSalario():
    while True:
        try:
            l = float(input("\033[0;33mDigite o salário do funcionário:\033[m R$"))
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            print("\033[0;32mTente novamente...\033[m")
            continue
        else:
            break
    return l

def calcularSalário():
    if s >= 1250.00:
        a = (s * 10 / 100) + s
    else:
        a = (s * 15 / 100) + s
    return a

def exibir():
    print(f"\033[0;32mQuem ganhava\033[m R${s:.2f} \033[0;32mpassa a receber\033[m R${calcularSalário():.2f}")


# Programa Principal
s = lerSalario()
exibir()