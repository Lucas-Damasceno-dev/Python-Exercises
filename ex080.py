numeros = []
for c in range(0, 5):
    novo_numero = int(input('Digite um valor:  '))
    if c == 0 or novo_numero > numeros[-1]:
        numeros.append(novo_numero)
        print('Adicionado ao FINAL da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if novo_numero < numeros[pos]:
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*25)
print(f'Os valores digitados em ordem foram {numeros}')
