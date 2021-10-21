import random

# Definindo Funções
def lerAlunos():
    for a in range(1, 4+1):
        aluno = str(input(f"Digite o nome do {a}º aluno: "))
        lista.append(aluno)

def exibir():
    print("A ordem de apresentação sera: ")
    print(lista)


# Programa Principal
lista = list()
alunos = lerAlunos()
random.shuffle(lista)
exibir()