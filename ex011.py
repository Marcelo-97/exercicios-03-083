larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = alt * larg
tinta = area / 2
print('sua parede tem a dimensão de {}x{} e sua área é de {}m².\n'
      'Para pintar essa parede, você precisa de {}L de tinta'.format(larg,alt,area,tinta))
