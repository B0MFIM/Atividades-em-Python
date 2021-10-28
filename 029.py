# Definindo Funções
def lerVelocidade():
    while True:
        try:
            l = float(input("\033[0;32mQual a velocidade atual do carro?\033[m "))
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            print("\033[0;32mTente novamente...\033[m")
            continue
        else:
            break
    return l 

def exibir():
    if v > 80:
        print("\033[0;31m< MULTADO > velocidade permitida ultrapassada < MULTADO >\033[m")
        multa = (v - 80) * 7
        print(f"\033[0;32mRECEBERA UMA MULTA DE\033[m R${multa:.2f}")
    else:
        print("\033[0;32mTenha um bom dia, dirija com segurança.\033[m")


# Programa Principal
v = lerVelocidade()
exibir()