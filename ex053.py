f = str(input('Digite aqui uma frase para verificarmos se ela é um palíndromo: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = ""
for c in range(len(j) - 1, -1, -1):
    i += j[c]
print('O inverso de {} é {}.'.format(j, i))
if i == j:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')
