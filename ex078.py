maior_numero = menor_numero = 0
posmax = []
posmin = []
numeros = []

for pos in range(5):
    novo_numero = int(input('Digite um número:  '))
    numeros.append(novo_numero)
    if pos == 0:
        posmax = [pos]
        posmin = [pos]
        maior_numero = menor_numero = novo_numero
    else:
        if novo_numero > maior_numero:
            maior_numero = novo_numero
            posmax = [pos]
        elif novo_numero == maior_numero:
            posmax.append(pos)
        elif novo_numero < menor_numero:
            menor_numero = novo_numero
            posmin = [pos]
        elif novo_numero == menor_numero:
            posmin.append(pos)

print('-='*30)
print(f'Você digitou os valores {numeros}')
print(f'O MAIOR número digitado foi {maior_numero} nas posições: {posmax}')
print(f'O MENOR número digitado foi {menor_numero} nas posições {posmin}')
