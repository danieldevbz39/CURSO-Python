a = input('Digite algo: ')
print('O tipo primitivo deste valor é ', type(a))
print('Existe apenas espaço? ', a.isspace())
print('É um número? ', a.isnumeric())
print('Está em ordem alfabética? ', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em maiúscula?', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Isso está em maiúscula? ', a.istitle())