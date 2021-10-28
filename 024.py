# Definindo Funções
def lerNomeCidade():
    l = str(input("\033[0;32mDigite o nome da sua cidade:\033[m ")).strip().upper()
    return l

def exibir():
    if cidade[:5] == "PORTO":
        print(f"\033[0;32mA cidade\033[m {cidade} \033[0;32mtem inicial 'PORTO'!\033[m")
    else:
        print(f"\033[0;32mA cidade\033[m {cidade} \033[0;31mNÃO\033[m \033[0;32mtem inicial 'PORTO'!\033[m")


# Programa Principal
cidade = lerNomeCidade()
exibir()