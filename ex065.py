contador = 1
resposta = ''
soma = 0
numeros = int(input('Digite o número inteiro aqui: '))
soma += numeros
maior = numeros
menor = numeros
while resposta != 'N':
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta == 'S':
        numeros = int(input('Digite o número inteiro aqui: '))
        contador += 1
        soma += numeros
        if numeros >= maior:
            maior = numeros
        else:
            menor = numeros
    elif resposta == 'N':
        print('Ok. já finalizamos...')
    else:
        print('Resposta inválida... Tente de novo...')
print('Você digitou {} números e a média foi {}'.format(contador, soma / contador))
print(f'O maior valor foi {maior} e o menor é {menor}')
