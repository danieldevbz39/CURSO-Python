n = int(input('Digite um número: '))
mais = n + 1
menos = n - 1
dobro = n * 2
triplo = n * 3
raisquad = n ** (1/2)
print('{}<<, {}, >>{}'.format(menos, n, mais))
print('O dobro de {} é {}'.format(n, dobro))
print('O triplo de {} é {}'.format(n, triplo))
print('A rais quadrada de {} é {:.2f}'.format(n, raisquad))