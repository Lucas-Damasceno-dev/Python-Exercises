numeros = []
pares = []
impares = []
resposta = 's'
while resposta == 's':
    novo_numero = int(input('Digite um número:  '))
    if novo_numero in numeros:
        print("Esse número já foi inserido anteriormente.")
        continue
    numeros.append(novo_numero)
    if novo_numero % 2 == 0:
        if novo_numero in pares:
            continue
        pares.append(novo_numero)
    elif novo_numero % 2 != 0:
        if novo_numero in impares:
            continue
        impares.append(novo_numero)
    resposta = str(input('Quer continuar?  [S/N] ')).lower().strip()
    while resposta not in 'sn':
        print('Resposta inválida... Tente novamente.')
        resposta = str(input('Quer continuar?  [S/N] ')).lower().strip()
print('-='*30)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
