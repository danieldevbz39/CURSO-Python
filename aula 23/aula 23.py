try: # [{try}Tente ]
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError): #['except' excessão]
    print('Tivemos um problema com os típos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.___cause___}')
else:
    print(f'O resultado é {r:.1f}')
    print('Volte sempre! Muito obrigado!')
