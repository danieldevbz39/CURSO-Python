def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


# Programa Principal
título(' Curso de Python')
título(' Aprendendo Python')
título('Aprendendo def')


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print('-' * 30)


# Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)


def contador(*núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')
    print('-' * 70)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def contador(*núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')
    print('-' * 70)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
print('-' * 30)


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
print('-' * 50)