num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(3)
print(num)
print(f'Essa lista tem {num} elementos.')

print('H' * 45)
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição  {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

print('I-' * 20)
valores = list()
for cont in range(0, 2):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a  #cria uma ligação entre a lista
b = a[:] #cria uma cópia da primeira lista
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

