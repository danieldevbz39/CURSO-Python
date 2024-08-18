listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 240,
            'Compasso', 9.99,
            'Mochila', 120.33,
            'Canetas', 22.30,
            'Livros', 34.50)
print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*50)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:7.2f}')
print('-'*50)