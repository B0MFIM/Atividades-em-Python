from datetime import date

# Definindo Funções
def lerAno():
    while True:
        try:
            l = int(input("\033[0;33mQual ano você quer analisar? digite 0 se quiser analisar o ano atual:\033[m "))
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            print("\033[0;32mTente novamente...\033[m")
            continue
        else:
            break
    return l 

def exibirAno():
    if a == 0:
        e = date.today().year
        if e % 4 == 0 and e % 100 != 0 or e % 400 == 0:
            print(f"\033[0;32mO ano de\033[m {e} \033[0;34mé Bissexto!\033[m")
        else:
            print(f"\033[0;32mO ano de\033[m {e} \033[0;31mnão é bissexto!\033[m")
    else:
        if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
            print(f"\033[0;32mO ano de\033[m {a} \033[0;34mé Bissexto!\033[m")
        else:
            print(f"\033[0;32mO ano de\033[m {a} \033[0;31mnão é bissexto!\033[m")


# Programa Principal
a = lerAno()
exibirAno()