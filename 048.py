# Definindo Funções
def somandoValores():
    soma = 0
    cont = 0
    for n in range(1, 500+1, 2):
        if n % 3 == 0:
            cont = cont + 1
            soma = soma + n
    print(f"\033[0;32mA soma entre todos os\033[m {cont} \033[0;32mvalores solicitados é de:\033[m {soma}")


# Programa Principal
somandoValores()