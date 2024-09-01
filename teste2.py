altura = float(input('Digite o tamanho da grade "ALTURA" em cm: '))
comprimento: float = float(input('Digite o tamanho da grade "COMPRIMENTO" em cm: '))
comp = int(input('Dividir comprimento: '))
alt = int(input('Dividir altura: '))

soma = comprimento / comp
soma2 = altura / alt

print(f'total é {soma}m de comprimento ')
print(f'Total é {soma2}m de altura')
tot = soma, soma2

umquartolar = 10
umquartoalt = 15
totquarto = umquartoalt,umquartolar

if tot > totquarto:

print(f'{tot}')