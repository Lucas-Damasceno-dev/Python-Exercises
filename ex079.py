resposta = 's'
numeros = []
while resposta == 's':
    novo_numero = int(input('Digite um valor:   '))
    if novo_numero not in numeros:
        numeros.append(novo_numero)
        print('Valor adicionado com sucesso..')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resposta = str(input('Quer continuar? [S/N]  ')).strip().lower()
    while resposta not in 'sn':
        print('Desculpe resposta inválida... Tente novamente.')
        resposta = str(input('Quer continuar? [S/N]  ')).strip().lower()
print('-='*25)
numeros.sort()
print(f'Você digitou os valores {numeros}')
