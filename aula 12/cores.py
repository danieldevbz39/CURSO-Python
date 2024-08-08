from random import randint
from time import sleep
itens = ('Azul', 'Vermelho', 'Empate')
computador = randint (0, 2)
print('''Escolha...
\033[34m [ 0 ] Azul\033[m 
\033[31m [ 1 ] Vermelho\033[m
\033[33m [ 2 ] Empate\033[m''')
jogador = int(input('Qual é a sua jogada? '))
print('5')
sleep(0.5)
print('4')
sleep(0.5)
print('3')
sleep(0.5)
print('2')
sleep(0.5)
print('1')
sleep(0.5)
print('0')
sleep(0.5)
print('-='*15)
print('Computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-='*15)
if computador == 0: #computador jogou AZUL
    if jogador == 0:
        print('\033[1;33;41mGANHOU\033[m')
    elif jogador == 1:
        print('\033[1;31;43mJOGADOR PERDEU\033[m')
    elif jogador == 2:
        print('\033[1;31;43mJOGADOR PERDEU\033[m')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #computador jogou Vermelho
    if jogador == 0:
        print('JOGADOR PERDEU')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('JOGADOR PERDEU')
    else:
        print('JOGADA INVÁLIDA!')