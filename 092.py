from datetime import datetime

# Definindo Funções
def exibição():
    dados["Nome"] = str(input("\033[0;32mNome:\033[m "))
    while True:
        try:
            anoNasc = int(input("\033[0;32mAno de Nascimento:\033[m "))
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            continue
        else:
            dados["Idade"] = datetime.now().year - anoNasc
            while True:
                try:
                    dados["CTPS"] = int(input("\033[0;32mCarteira de Trabalho: [0 - Não]\033[m "))
                except:
                    print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
                    continue
                else:
                    if dados["CTPS"] != 0:
                        while True:
                            try:
                                dados["Contratação"] = int(input("\033[0;32mAno de Contratação:\033[m "))
                                dados["Salário"] = float(input("\033[0;32mSalário: R$\033[m"))
                            except:
                                print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
                                continue
                            else:
                                dados["Aposentadoria"] = dados["Idade"] + ((dados["Contratação"] + 35) - datetime.now().year)
                                break
                    break
            break

    print("-=-" * 15)

    for chave, valor in dados.items():
        print(f"\033[0;33m  - {chave} tem o valor:\033[m {valor}")


# Programa Principal
dados = dict()
exibição()