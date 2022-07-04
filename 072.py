from Biblioteca import leitura, continuar

# Definindo Funções
def tuplaPosição():
    if n > 20 or n < 0:
        print("\033[0;32mTente Novamente!\033[m")
    elif 0 <= n <= 20:
        print(f"\033[0;33mVocê digitou o número {tupla[n]}\033[m")


# Programa Principal
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = leitura.lerNúmInteiro()
    tuplaPosição()
    c = continuar.continuar()
    if c == True:
        continue
    else:
        print("\033[0;32mAté a próxima!!\033[m")
        break