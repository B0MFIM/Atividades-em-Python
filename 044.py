from Biblioteca import continuar

# Definindo Funções
def linha():
    print("\033[0;35m-=-\033[m" * 15)

def lerPreço():
    while True:
        try:
            l = float(input("\033[0;33mQual o preço de suas compras?\033[m R$"))
        except:
            print("\033[0;31m< ERRO > valor digitado inválido < ERRO >\033[m")
            continue
        else:
            break
    linha()
    return l

def exibirOpções():
    print("FORMAS DE PAGAMENTO".center(45))
    linha()
    print("\033[0;34m[ 1 ] - Á Vista em Dinheiro/Cheque\033[m")
    print("\033[0;34m[ 2 ] - Á Vista no Cartão\033[m")
    print("\033[0;34m[ 3 ] - Em 2x no Cartão\033[m")
    print("\033[0;34m[ 4 ] - Em 3x ou mais no Cartão\033[m")
    linha()

def lerOpções():
    while True:
        try:
            while True:
                l = int(input("\033[0;33mSua Opção:\033[m "))
                if l == 1 or l == 2 or l == 3 or l == 4:
                    break
                else:
                    print("\033[0;31m< ERRO > valor digitado inválido < ERRO >\033[m")
                    continue
        except:
            print("\033[0;31m< ERRO > valor digitado inválido < ERRO >\033[m")
            continue
        else:
            break
    linha()
    return l

def exibição():
    if o == 1:
        desconto = p - (p * 10 / 100)
        print(f"\033[0;32mSua compra de\033[m R${p:.2f} \033[0;32mvai custar\033[m R${desconto:.2f} \033[0;32mno final.\033[m")
        linha()
    elif o == 2:
        desconto = p - (p * 5 / 100)
        print(f"\033[0;32mSua compra de\033[m R${p:.2f} \033[0;32mvai custar\033[m R${desconto:.2f} \033[0;32mno final.\033[m")
        linha()
    elif o == 3:
        parcela = p / 2
        print(f"\033[0;32mSua compra foi parcelada em\033[m 2x \033[0;32mde\033[m R${parcela:.2f}\033[0;32m, sem juros.\033[m")
        print(f"\033[0;32mSua compra de\033[m R${p:.2f} \033[0;32mvai custar\033[m R${p:.2f} \033[0;32mno final.\033[m")
        linha()
    elif o == 4:
        while True:
            try:
                qualParcela = int(input("\033[0;33mQuantas Parcelas vão ser?\033[m "))
            except:
                print("\033[0;31m< ERRO > valor digitado inválido < ERRO >\033[m")
                continue
            else:
                break
        juros = (p * 20 / 100) + p
        parcela = juros / qualParcela
        print(f"\033[0;32mSua compra foi parcelada em\033[m {qualParcela}x \033[0;32mde\033[m R${parcela:.2f}\033[0;32m, com juros.\033[m")
        print(f"\033[0;32mSua compra de\033[m R${p:.2f} \033[0;32mvai custar\033[m R${juros:.2f} \033[0;32mno final.\033[m")
        linha()


# Programa Principal
while True:
    p = lerPreço()
    exibirOpções()
    o = lerOpções()
    exibição()
    c = continuar.continuar()
    if c == True:
        continue
    else:
        print("\033[0;32mAté...\033[m")
        break