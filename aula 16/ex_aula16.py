lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print('-'*40)

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print('-'*40)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

print('-'*40)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na {pos}')

print('Comi pra caramba!')
print('-'*40)