# Definindo Funções
def lerFrase():
    l = str(input("\033[0;32mDigite a sua frase:\033[m ")).strip().upper()
    return l

def exibir():
    print(f"\033[0;32mSão encontradas\033[m {frase.count('A')} A's \033[0;32mem sua frase!\033[m")
    print(f"\033[0;32mA primeira ocorrência da letra 'A' apareceu na\033[m {frase.find('A') + 1}\033[0;32mº posição!\033[m")
    print(f"\033[0;32mA ultima ocorrência da letra 'A' apareceu na\033[m {frase.rfind('A') + 1}\033[0;32mº posição!\033[m")


# Programa Principal
frase = lerFrase()
exibir()