# Iniciando nivelamento em python - Antero

tempo = {"dados": [
            {"cidade": "Porto Velho", "Temperatura": 31, "Escala": "Celsius"},
            {"cidade": "São Paulo", "Temperatura": 44, "Escala": "Celsius"}
            ],
        "tamanho": 2
        }

# loop na chave que é uma lista de dicionarios
for dados in tempo["dados"]:
    print(f"Bom dia, a temperatura em {dados['cidade']} é de {dados['Temperatura']} {dados['Escala']}")

# print em uma chave de dicionario
print(tempo["tamanho"])

# loop nas chaves do dicionario
for item in tempo:
    print(item)

print(tempo["dados"][0]["cidade"])