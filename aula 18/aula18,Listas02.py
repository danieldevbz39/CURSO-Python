teste = list()
teste.append('Daniel')
teste.append(38)
galera = list()
galera.append(teste[:])  #[:] copia de teste
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])  #[:] copia de teste
print(galera)

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])  #copia de list
    dado.clear()

for p in galera: #('for' pra cada) ('p' pessoa) ('in' em) galera
    if p[1] >= 21: #('if' se) ('p[1]' pessoa idade)('>=' maior igual )
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')