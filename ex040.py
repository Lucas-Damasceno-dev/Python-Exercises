n1 = float(input('Qual tua primeira nota?'))
n2 = float(input('Qual a tua segunda nota?'))

m = (n1 + n2) / 2
print('Sua média é {}!!!'.format(m))

if m < 5.0:
    print('REPROVADO!!!')
elif 5 <= m <= 6.9:
    print('RECUPERAÇÃO!!!')
else:
    print('APROVADO!!!')
