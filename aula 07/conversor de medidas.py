l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
ar = l * a
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l,a,ar))
t = ar / 2
print('Para pintar essa parede, você precisará de {}L de tinta'.format(t))