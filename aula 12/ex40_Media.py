nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
média = (nota1 + nota2+ nota3) / 2
print('Tirando {:.1f}, {:.1f} {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, nota3, média))
if 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno esta REPROVADO.')
elif média >= 7:
    print('O aluno esta APROVADO.')