print('10 TERMOS DE UMA PA \n')
p = int(input('Digite o valor do PRIMEIRO TERMO da PA: '))
r = int(input('Digite o valor da RAZÃO da PA: '))
d = p + (11 - 1) * r
for c in range(p, d + r, r):
    print('{} '.format(c), end='-> ')
print('ACABOU')
