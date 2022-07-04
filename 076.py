# Definindo funções
def exibição():
    print("=" * 40)
    titulo = "LISTAGEM DE PREÇOS"
    print(f"{titulo: ^40}")
    print("=" * 40)

    for posição in range(0, len(tuplaEscolar)):
        if posição % 2 == 0:
            print(f"{tuplaEscolar[posição]:.<30}", end="")
        else:
            print(f"R${tuplaEscolar[posição]: >7}")
    
    print("=" * 40)


# Programa Principal
tuplaEscolar = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
                "Compasso", 9.99,"Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
exibição()