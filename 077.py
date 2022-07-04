# Definindo Funções
def análise():
    for palavra in tuplaPalavras:
        print(f"\n\033[0;32mNa palavra\033[m {palavra.upper()} \033[0;32mtemos:\033[m ", end="")
        for letra in palavra:
            if letra.lower() in "aeiou":
                print(letra, end=" ")


# Programa Principal
tuplaPalavras = ("aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar", "trabalhar",
            "mercado", "programador", "futuro")
análise()