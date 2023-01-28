d = float(input('Qual a distância da viagem em Km?'))
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print('O valor de uma passagem será de R${:.2f}'.format(p))
