# Definido Funções
def lerNomeCompleto():
    l = str(input("\033[0;32mDigite seu nome completo:\033[m ")).strip().upper()
    return l

def exibir():
    if "SILVA" in nome:
        print("\033[0;32mSeu nome possui um sobrenome bem\033[m \033[0;33mpopular\033[m \033[0;32mmano\033[m \033[0;33m:)\033[m")
    else:
        print("\033[0;32mSeu sobrenome\033[m \033[0;31mnão\033[m \033[0;32mé tão popular assim cara\033[m \033[0;31m:(\033[m")

# Programa Principal
nome = lerNomeCompleto()
exibir()