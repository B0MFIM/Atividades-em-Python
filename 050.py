# Definindo Valores
def somandoPares():
    soma = 0
    for c in range(1, 6+1):
        while True:
            try:
                n = int(input(f"\033[0;32mDigite o {c}º valor:\033[m "))
            except:
                print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
                continue
            else:
                break
        if n % 2 == 0:
            soma = soma + n
    print(f"\033[0;34mA soma de todos os valores é de:\033[m {soma}")


# Programa Principal
somandoPares()