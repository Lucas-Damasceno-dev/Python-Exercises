from datetime import date
aa = date.today().year
tma = 0
tme = 0
for c in range(1, 8):
    an = int(input('Digite o ano de nascimento da {}° pessoa:'.format(c)))
    i = aa - an
    if i < 21:
        tme += 1
    else:
        tma += 1
print('O número de pessoas MAIORES de idade (21 anos) é: {}'.format(tma))
print('O total de pessoas MENORES de idade (21 anos) é: {}'.format(tme))
