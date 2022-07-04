from Biblioteca import continuar

# Definindo Funções
def exibição():
    expressão = str(input("\033[0;32mDigite aqui a expressão matemática:\033[m "))
    for simbolo in expressão:
        if simbolo == "(":
            pilha.append("(")
        elif simbolo == ")":
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(")")
    if len(pilha) == 0:
        print("\033[0;34mSua expressão está válida!\033[m")
    else:
        print("\033[0;33mSua expressão está inválida!\033[m")


# Programa Principal
pilha = list()
while True:
    exibição()
    c = continuar.continuar()
    if c == True:
        pilha.clear()
        continue
    else:
        print("\033[0;32mAté...\033[m")
        break