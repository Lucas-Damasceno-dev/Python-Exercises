v = float(input('Qual a velocidade do carro em Km/h:'))
m = float(v - 80)
mu = m * 7
if v > 80.0:
    print('Você está acima da velocidade permitida. A sua multa será de: R${}!!!.'.format(mu))
else:
    print('Tenha um bom dia. Dirija com segurança!')
