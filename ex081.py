numeros = []
resposta = 's'
while resposta == 's':
    novo_numero = int(input('Digite um valor:  '))
    resposta = str(input('Quer continuar? [S/N]  ')).strip().lower()
    numeros.append(novo_numero)
    while resposta not in 'sn':
        print('Resposta inválida... Tente novamente.')
        resposta = str(input('Quer continuar? [S/N]  ')).strip().lower()
numeros.sort(reverse=True)
print('-='*25)
print(f'Você digitou {len(numeros)} elementos')
print(f'Os valores em ordem decresente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
if 5 not in numeros:
    print('O valor 5 não faz parte da lista!')
