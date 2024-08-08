from random import randint
from time import sleep
itens = ('CARA', 'COROA')
computador = randint( 0, 2)
print('''ESCOLHA UMA DAS OPÇÕES
[ 1 ] CARA
[ 2 ] COROA''')
jogador = int(input('FAÇA SUA ESCOHA:'))
print('.')
sleep(0.3)
print('..')
sleep(0.4)
print('...')
sleep(0.5)
print('....')
sleep(0.5)
print('.....')
sleep(0.5)
print('......')
sleep(0.5)
print('-='*15)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*15)
if computador == 1: #computador jogou CARA
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('JOGADA INVÁLIDA!')
