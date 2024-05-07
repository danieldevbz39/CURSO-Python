número = int(input('Digite um número: '))
result = número %2
if result == 0:
    print('O número {} é PAR'. format(número))
else:
    print('O número {} ÍMPAR'.format(número))