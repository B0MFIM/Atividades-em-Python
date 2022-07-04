# Definindo Funções
def exibição():
    aluno["nome"] = str(input("\033[0;32mNome:\033[m "))
    while True:
        try:
            aluno["média"] = float(input("\033[0;32mMédia:\033[m "))
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            continue
        else:
            break

    if aluno["média"] >= 7:
        aluno["situação"] = "Aprovado"
    elif 5 <= aluno["média"] < 7:
        aluno["situação"] = "Recuperação"
    else:
        aluno["situação"] = "Reprovado"

    print("-=-" * 10)

    for chave, valor in aluno.items():
        print(f"\033[0;33m  - {chave} é igual a\033[m {valor}")


# Programa Principal
aluno = dict()
exibição()