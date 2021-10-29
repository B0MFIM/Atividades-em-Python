# Definindo Funções
def lerSegmento():
    while True:
        try: 
            l = float(input(f"\033[0;33mQual o segmento:\033[m "))
        except:
            print("\033[0;31m< ERRO > valor inserido inválido < ERRO >\033[m")
            print("\033[0;32mTente novamente...\033[m")
            continue
        else:
            break
    return l

def triangulo():
    if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
        print("\033[0;34mSIM!!\033[m \033[0;32mPODEMOS FORMAR UM TRIANGULO COM SEUS SEGMENTOS!!\033[m")
    else:
        print("\033[0;31mNÃO!!\033[m \033[0;32mIMPOSSÍVEL FORMARMOS UM TRIANGULO COM SEUS SEGMENTOS!!\033[m")


# Programa Principal
s1 = lerSegmento()
s2 = lerSegmento()
s3 = lerSegmento()
triangulo()