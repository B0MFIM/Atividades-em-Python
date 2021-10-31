from Funções import matematica

# Iniciando nivelamento em python - Antero

numero1 = input("Insira o 1º número: ")           # Valor input Formatado para Float
numero2 = input("Insira o 2º número: ")           # Valor não formatado
matematica.somar(numero1, numero2)                # Valor Formatado para Float

print(f"A soma desse valores é de: {matematica.somar(numero1, numero2):.0f}")        