from time import sleep
from Biblioteca.continuar import continuar

# Definindo Funções
def exibição():
    while True:
        nome = str(input("Nome: "))
        while True:
            try:
                nota1 = int(input("Nota 1: "))
                nota2 = int(input("Nota 2: "))
            except:
                print("< ERRO > valor inserido inválido < ERRO >")
                continue
            else:
                media = (nota1 + nota2) / 2
                break
        fichas.append([nome, [nota1, nota2], media])
        c = continuar()
        if c == True:
            continue
        else:
            break

    print("-=" * 20)
    print(f"{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}")
    print("-=" * 20)

    for indice, aluno in enumerate(fichas):
        print(f"{indice:<4}{aluno[0]:<10}{aluno[2]:>8}")

    while True:
        print("-=" * 20)
        opção = int(input("Ver notas de qual aluno? [999 parar] "))
        if opção == 999:
            print("FINALIZANDO...")
            sleep(1)
            break
        if opção <= len(fichas) - 1:
            print(f"Notas de {fichas[opção][0]} são {fichas[opção][1]}")
            
    print("<<< VOLTE SEMPRE >>>".center(40))


# Programa Principal
fichas = list()
exibição()