import random

# Definindo Funções
def lerAlunos():
    for a in range(1, 4+1):
        aluno = str(input(f"\033[0;32mDigite o nome do {a}º aluno:\033[m "))
        lista.append(aluno)

def escolhido():
    e = random.choice(lista)
    return e

def exibir():
    print("~" * 30)
    print(f"\033[0;32mO aluno escolhido foi:\033[m {escolhido()}")
    print("~" * 30)


# Programa Principal
lista = list()
al = lerAlunos()
exibir()