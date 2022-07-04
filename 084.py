from Biblioteca.continuar import continuar

# Definindo Funções
def análise():
    while True:
        while True:
            try:
                dados.append(str(input("Nome: ")))
                dados.append(int(input("Idade: ")))
            except:
                dados.clear()
                print("< ERRO > valores inseridos inválidos < ERRO >")
                continue
            else:
                break
        nomes.append(dados[:])
        idades.append(dados[1])
        c = continuar()
        if c == True:
            dados.clear()
            continue
        else:
            break
    
    print()
    print(f"Foram cadastrado(s) {len(nomes)} pessoa(s).")
    print(f"A maior idade foi de {max(idades)} anos. Idade de ", end="")
    for nome in nomes:
        if nome[1] == max(idades):
            print(f"{nome[0]}", end="")
    print(f"\nA menor idade foi de {min(idades)} anos. Idade de ", end="")
    for nome in nomes:
        if nome[1] == min(idades):
            print(f"{nome[0]}", end="")


# Programa Principal
nomes = list()
idades = list()
dados = list()
análise()