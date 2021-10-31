# Definindo Funções

def ler():
    """
    -> Fazer leitura de qualquer valor
    return: l
    """
    l = input("\033[0;32mDigite Aqui: \033[m")
    return l

def lerNúmInteiro():
    """
    -> Fazer leitura de um número inteiro
    return: l
    """
    while True:
        try:
            l = int(input("\033[0;32mDigite um número:\033[m "))
        except:
            print("\033[0;31m< ERRO > indique um valor inteiro válido < ERRO >\033[m")
            continue
        else:
            break
    return l

def lerNúmReal():
    """
    -> Fazer leitura de um número real
    return: l
    """
    while True:
        try:
            l = float(input("\033[0;32mDigite um número:\033[m "))
        except:
            print("\033[0;31m< ERRO > indique um valor real válido < ERRO >\033[m")
            continue
        else:
            break
    return l

def lerNome():
    """
    -> Fazer leitura de um nome
    return: a
    """
    a = str(input("\033[0;32mDigite o seu nome: \033[m")).strip().upper()
    return a