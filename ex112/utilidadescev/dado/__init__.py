def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.').strip() #['replace']substitui todas as vírgulas por ponto
        if entrada.isalpha() or entrada == '': #['strip' tira os espaços antes e depois]
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)