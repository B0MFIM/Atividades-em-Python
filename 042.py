from Biblioteca import continuar

# Definindo Funções
def lerSegmento():
    while True:
        try:
            for c in range(1, 3+1):
                l = float(input(f"\033[0;33mQual o {c}º segmento?\033m "))
                lista.append(l)
        except:
            continue
        else:
            break
                
def exibição():
    if lista[0] < lista[1] + lista[2] and lista[1] < lista[0] + lista[2] and lista[2] < lista[0] + lista[1]:
        print("\033[0;34mSIM!! PODEMOS FORMAR UM TRIANGULO COM SEUS SEGMENTOS!!\033[m")
        if lista[0] == lista[1] == lista[2]:
            print("\033[0;32mE ESTE É UM TRIANGULO\033[m EQUILÁTERO!!")
        elif lista[0] != lista[1] != lista[2] != lista[0]:
            print("\033[0;32mE ESTE É UM TRIANGULO\033[m ISÓCELES!!")
        else:
            print("\033[0;32mE ESTE É UM TRIANGULO\033[m ESCALENO!!")
    else:
        print("\033[0;31mNÃO!! IMPOSSÍVEL FORMARMOS UM TRIANGULO COM SEUS SEGMENTOS!!\033[m")


# Programa Principal
while True:
    lista = list()
    s = lerSegmento()
    exibição()
    c = continuar.continuar()
    if c == True:
        continue
    else:
        print("\033[0;32mAté...\033[m")
        break