h = float(input('Qual a altura da parede em metros?'))
k = float(input('Qual a largura da parede em metros?'))
s = float(h * k)
q = float(s / 2)
print('Você precisa de {} litros de tinta para pintar {} m² de parede.'.format(q, s))
