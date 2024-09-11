from random import randint
from time import sleep
lista = list()
jogos = list ()
print('-' * 50)
print('           JOGAR NA MEGA SENA           ')
print('-' * 50)
quant = int(input("Quantos jogos você quer que eu sorteie? "))
tot = 1
while tot <= quant:
    cont = 0
    while True: #enquanto
        num = randint (1, 60)
        if num not in lista: #('if' se) o num ['not' não] ['in' esta] na lista:
            lista.append(num)
            cont += 1
        if cont >= 6: #['if' se] ['cont' contador ['>=6:'maior igual a 6]
            break #parar
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos): #['for' pra cada] ['i, l' lista] ['in' esta] ['enumerate' numerado]
    print(f'jogo {i+1}: {l}') #jogo ['i' índice] ['l' lista]
    sleep(0.5)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)