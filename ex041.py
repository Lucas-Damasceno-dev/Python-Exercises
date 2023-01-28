from datetime import date

an = int(input('Qual o ano de nascimento do(a) atleta?'))
at = date.today().year
i = at - an

if i <= 9:
    print('Você tem {} anos. Sua classificação é MIRIM!'.format(i))
elif 9 < i <= 14:
    print('Você tem {} anos. Sua classificação é INFANTIL!'.format(i))
elif 14 < i <= 19:
    print('Você tem {} anos. Sua classificação é JUNIOR!'.format(i))
elif 19 < i <= 20:
    print('Você tem {} anos. Sua classificação é SÊNIOR!'.format(i))
else:
    print('Você tem {} anos. Sua classificação é MASTER!'.format(i))
