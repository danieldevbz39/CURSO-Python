s = float(input("Qual é o salário do Funcionário? R$ "))
d = int(input('Digite o valor do acrecimo: '))
au = s + (s * d / 100)
print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}'.format(s,d,au))