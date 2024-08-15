print('~'*20)
print('Cadastro de Clientes')
print('~'*20)
print('Ola, seja bem vindo!')
print('-='*20)

branco = '\033[0;37;40m'
vermelho = '\033[1;30;43m'
verde = '\033[1;30;42m'
amarelo = '\033[1;31;43m'
azul = '\033[1;37;44m'
roxo = '\033[1;30;45m'
azulc = '\033[1;37;46m'
cinza: str = '\033[1;30;47m'

nome = str(input(f'{branco}Digite o nome do cliente: '))
empresa = str(input(f'{vermelho}Digite o nome da empresa: '))
produto = str(input(f'{verde}Digite o produto: '))
tamanho = str(input(f'{amarelo}Digite o tamanho: '))
cores = str(input(f'{azul}Serviço 4x0, 4x1, 4x4: '))
quant = int(input(f'{roxo}Digite a Quantidade: '))

print('-='*20)
print(f'{branco}Nome: {nome}, Empresa: {empresa}')
print('-='*20)
print(f'{vermelho}Produto: {produto}, Tamanho: {tamanho}, Cores: {cores}, Quantidade: {quant}.')
print('-='*20)
print(f'{cinza}CADASTRO REALIZADO COM SUCESSO')