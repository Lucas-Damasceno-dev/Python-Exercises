matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
coluna3 = 0
linha2 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição {l}, {c}:  '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            coluna3 += matriz[l][c]
        if l == 1:
            linha2 += matriz[l][c]

print('-='*25)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {coluna3}')
print(f'A soma dos valores da segunda linha é {linha2}')
