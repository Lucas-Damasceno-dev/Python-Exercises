from datetime import date
an = int(input('Qual o ano de seu nascimento?'))
aa = date.today().year
i = aa - an
if i > 18:
    print('Já passou do momento de você se alistar!!! Exatos {} anos!!!'.format(i - 18))
elif i < 18:
    print('Não chegou ainda seu momento de se alistar!!! Faltam exatos {} anos!!!'.format(18 - i))
else:
    print('Este é o ano de seu alistamento {}!!! Ih caramba é o atual!!! Corre negão!!!'.format(aa))
