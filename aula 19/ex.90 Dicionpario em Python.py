aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Recuperação'
print('-=' *30)
for k, v in aluno.items():#['for' pra cada, ['k'] chave, ['v'] valor, ['in']esta em]
    print(f' - {k} é igual a {v}')