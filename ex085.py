numeros = [[], []]
for c in range(0, 7):
    novo_numero = int(input(f'Digite o {c}ª valor:  '))
    if novo_numero % 2 == 0:
        numeros[0].append(novo_numero)
    elif novo_numero % 2 != 0:
        numeros[1].append(novo_numero)
numeros[0].sort()
numeros[1].sort()
print('-='*25)
print(f'Os valores PARES digitados foram: {numeros[0]}')
print(f'Os valores ÍMPARES digitados foram: {numeros[1]}')
