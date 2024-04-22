dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
carro = int(input('Digite o valor da diária do carro: '))
kmr = float(input('Digite o valor por km rodado: '))
pagos = (dias * carro) + (km * kmr)
print('O total a pagar é de R${:.2f}'.format(pagos))
div = pagos / carro
print('O valor de cada dia é R${:.2f}'.format(div))