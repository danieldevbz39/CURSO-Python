preço = float(input('Qual é o preço do produto? R$ '))
des = int(input('Descontos de: '))
novo = preço- (preço * des / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de {}%  vai custar R${:.2f}.'.format(preço, des, novo))