from time import sleep

# Definindo Funções
def lerNumero():
    while True:
        try:
            while True:
                l = int(input("\033[0;32mDigite um número de 0 a 9999:\033[m "))
                if l > 9999:
                    print("\033[0;31m< ERRO > Valor Inserido Inválido < ERRO >\033[m")
                    sleep(0.5)
                    print("\033[0;32mTente novamente...\033[m")
                    continue
                else:
                    break
        except:
            print("\033[0;31m< ERRO > Valor Inserido Inválido < ERRO >\033[m")
            sleep(0.5)
            print("\033[0;32mTente novamente...\033[m")
            continue
        else:
            break
    return l

def unidade(n):
    return n//1 % 10

def dezena(n):
    return n//10 % 10

def centena (n):
    return n//100 % 10

def milhar(n):
    return n//1000 % 10

def exibir():
    print("\033[0;32m=\033[m" * 30)
    print(f"\033[0;32mA Unidade:\033[m {unidade(numero)}")
    print(f"\033[0;32mA Dezena:\033[m  {dezena(numero)}")
    print(f"\033[0;32mA Centena:\033[m {centena(numero)}")
    print(f"\033[0;32mO Milhar:\033[m  {milhar(numero)}")
    print("\033[0;32m=\033[m" * 30)


# Programa Principal
numero = lerNumero()
exibir()