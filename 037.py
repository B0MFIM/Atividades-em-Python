from Biblioteca import continuar

# Definindo Funções
def lerNúmero():
    while True:
        try:
            l = int(input("\033[0;32mDigite um número qualquer:\033[m "))
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            print("\033[0;32mTente novamente...\033[m")
            continue
        else:
            break
    return l

def exibirOpções():
    print("\033[0;32mEscolha uma das bases de conversão:\033[m")
    print("\033[0;33m[ 1 ] - BINÁRIO\033[m")
    print("\033[0;33m[ 2 ] - OCTAL\033[m")
    print("\033[0;33m[ 3 ] - HEXADECIMAL\033[m")

def opção():
    while True:
        try:
            while True:
                o = int(input("\033[0;32mSua Opção:\033[m "))
                if o == 1:
                    print(f"\033[0;32mO Nº\033[m {n} \033[0;32mconvertido para Binário é igual a:\033[m {binário()}")
                    break
                elif o == 2:
                    print(f"\033[0;32mO Nº\033[m {n} \033[0;32mconvertido para Octal é igual a:\033[m {octal()}")
                    break
                elif o == 3:
                    print(f"\033[0;32mO Nº\033[m {n} \033[0;32mconvertido para Hexadecimal é igual a:\033[m {hexadecimal()}")
                    break
                else:
                    print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
                    print("\033[0;32mTente novamente...\033[m")
                    continue
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            print("\033[0;32mTente novamente...\033[m")
            continue
        else:
            break
    return o

def binário():
    return bin(n)[2:]

def octal():
    return oct(n)[2:]

def hexadecimal():
    return hex(n)[2:]


# Programa Principal
while True:
    n = lerNúmero()
    exibirOpções()
    opção()
    c = continuar.continuar()
    if c == True:
        continue
    else:
        print("\033[0;32mAté...\033[m")
        break