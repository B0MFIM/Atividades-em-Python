from Biblioteca import continuar

# Definindo Funções
def lerPeso():
    while True:
        try:
            l = float(input("\033[0;33mQual o peso(Kg)?\033[m "))
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            continue
        else:
            break
    return l

def lerAltura():
    while True:
        try:
            l = float(input("\033[0;33mQual a altura(m)?\033[m "))
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            continue
        else:
            break
    return l

def imc():
    i = p / (a ** 2)
    return i

def exibição():
    if imc() < 18.5:
        print("\033[0;32mEssa pessoa está abaixo do peso!\033[m")
    elif 18.5 <= imc() < 25:
        print("\033[0;32mEssa pessoa está no peso ideal!\033[m")
    elif 25 <= imc() < 30:
        print("\033[0;32mEssa pessoa está com sobrepeso!\033[m")
    elif 30 <= imc() < 40:
        print("\033[0;32mEssa pessoa está com obesidade!\033[m")
    elif imc() >= 40:
        print("\033[0;32mEssa pessoa está com obesidade mórbida!\033[m")


# Programa Principal
while True:
    p = lerPeso()
    a = lerAltura()
    exibição()
    c = continuar.continuar()
    if c == True:
        continue
    else:
        print("\033[0;32mAté...\033[m")
        break