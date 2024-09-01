print('-'*20)
print(' ORÇAMENTO GRADE ')
print('-'*20)
print("""ESCOLHA!!!
[ 1 ] Cartões
[ 2 ] Panfletos
[ 3 ] Santinhos
[ 4 ] Cartaz""")

opção = int(input('Qual é a opção? '))
if opção == 1:
    print('''Quantas cores?
    [ 1 ] 4x0
    [ 2 ] 4x1
    [ 3 ] 4x4''')
    if opção == 1:
        print('4x0')
    else:
        total = soma

if opção == 2:
    print('''Escolha uma das opções: 
    [ 1 ] 7x10
    [ 2 ] 10x14
    [ 3 ] 14x20
    [ 4 ] 20x28
    [ 5 ] 28x40''')
    tpanfletos = int(input('Digite o tamanho deles: '))
    if tpanfletos == 1:
        uquartoa = 10
        uquartol = 70
    else:
        total = soma


    print(f'{total}')
else:
    opção = tpanfletos
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')