while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*40)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*40)
print(f'\033[1;30;43mPROGRAMA TABUADA ENCERRADO. Volte sempre!')