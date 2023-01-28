soma = barato = caros = cont = 0
pbarato = ' '
print('-' * 35)
print('LOJA SUPER BARATÃO')
print('-' * 35)
continuar = ' '
while continuar not in 'Nn':
    produto = str(input('Nome do produto: '))
    preco = int(input('Preço: R$'))
    soma += preco
    barato = preco
    continuar = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if preco >= 1000:
        caros += 1
    if preco <= barato or cont == 1:
        pbarato = produto
        barato = preco
print('{:-^40}'.format(' FIM DO PRIGRAMA '))
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {caros} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {pbarato} que custa R${barato}')
