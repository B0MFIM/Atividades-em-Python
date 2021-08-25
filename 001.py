def linha():
    print("\033[0;33m~\033[m"*40)

def leiaSTR():
    a = str(input("\033[0;32mDigite o seu nome: \033[m"))
    return a

def boasvindas(txt):
    linha()
    print(f"\033[0;33m{'BOAS VINDAS AO SISTEMA'} {txt}\033[m".center(40).upper())
    linha()

nome = leiaSTR()
boasvindas(nome)