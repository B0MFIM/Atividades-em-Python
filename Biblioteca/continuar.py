# Definindo Funções

def continuar():
    """
    -> Faz uma codagem para continuar um programa qualquer desejavel
    c: é uma variavel float com input
    return: c
    """
    while True:
        c = str(input("\033[0;32mDeseja continuar? [S/N]\033[m ")).upper().strip()
        if c == "S":
            c = True
            break
        elif c == "N":
            c == False
            break
        else:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            print("\033[0;32mTente novamente...\033[m")
            continue
    return c