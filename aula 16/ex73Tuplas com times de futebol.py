times = ('FORTALEZA', 'BOTAFOGO', 'FLAMENTO', 'PALMEIRAS',
         'SÃO PAULO', 'BAHIA', 'CRUZEIRO', 'ATLÉTICO MINEIRO',
         'ATHETICO-PR', 'VASCO DA GAMA', 'BRAGANTINO',
         'INTERNACIONAL', 'JUVENTUDE', 'GRÊMIO', 'CRICIÚMA',
         'CORINTIANS', 'EC VITÓRIA', 'FLUMINENSE',
         'CUIABÁ', 'ATLETICO-GO',)
print('-=' *55)
print(f'Lista de times: {times}')
print('-=' *55)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*55)
print(f'Os últimos 4 colocados: {times[-4:]}')
print('-='*55)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*55)
print(f'O Cruzeiro esta na {times.index("CRUZEIRO")+1}ª posição')
print('-='*55)
