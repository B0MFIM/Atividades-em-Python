# Iniciando nivelamento em python - Antero

# listas guardam variaveis
lista = ["Antero", "Aline", "Luana", "Maoly", "Bomfim"] # 0, 1, 2, 3, 4
print(lista[0]) # mostra o valor "Antero"
listaDict = [{"nome": "Bomfim", "endereço": "Rua tal"},
             {"nome": "Fulano", "endereço": "Rua ow"}]

# dicionarios organizam dados através de chaves e valores
corPredileta = {"cor": "Amarelo"} # dicionario simples
dicionarioList = {"cores": ["Azul", "Verde", "Amarelo"]}
print(dicionarioList["cores"])
tempo = {"dados": {"cidade": "Porto Velho", "Temperatura": "31", "Escala": "Celsius"}}



for item in listaDict:
    print(f"item: {item['nome']}")

for itemLista in lista:
    print(f"item lista: {itemLista}")

for cor in dicionarioList["cores"]:
    print(f"cor: {cor}")