# Definindo Métodos
def linha():
    print("\033[0;33m~\033[m"*40)

def leiaSTR():
    while True:
        try: 
            a = str(input("\033[0;32mDigite o seu nome: \033[m")).strip().upper()
        except:
            print("\033[0;31m< ERRO > Falha na leitura dos dados < ERRO >\033[m")
            continue
        else:
            break
    return a

def boasvindas(txt):
    linha()
    print(f"\033[0;33mBOAS VINDAS AO SISTEMA {txt}\033[m".center(50))
    linha()

# Programa Principal
nome = leiaSTR()
boasvindas(nome)