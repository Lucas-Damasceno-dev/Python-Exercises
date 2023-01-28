cont1 = cont10 = cont20 = cont50 = 0
print('=' * 50)
print(' ' * 18, 'BANCO CEV')
print('=' * 50)
saque = int(input('Que valor você quer sacar? R$'))
while True:
    while saque != 0:
        if saque >= 50:
            saque -= 50
            cont50 += 1
            if saque < 50:
                print(f'Total de {cont50} células de R$50')
        elif 20 <= saque < 50:
            saque -= 20
            cont20 += 1
            if saque < 20:
                print(f'Total de {cont20} células de R$20')
        elif 10 <= saque < 20:
            saque -= 10
            cont10 += 1
            if saque < 10:
                print(f'Total de {cont10} células de R$10')
        elif 1 <= saque < 10:
            saque -= 1
            cont1 += 1
            if saque < 1:
                print(f'Total de {cont1} células de R$1')
        if saque == 0:
            print('=' * 50)
            print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
            break
