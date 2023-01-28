maior = 0
menor = 0
for c in range(1, 6):
    p = float(input('Digite o peso da {}ª pessoa : '.format(c)))
    if p == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O MAIOR peso lido foi de {}Kg'.format(maior))
print('O MENOR peso lido foi de {}Kg'.format(menor))
