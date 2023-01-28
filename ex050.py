s = 0
v = 0
for c in range(0, 6):
    n = int(input('Digite um número inteiro:'))
    if n % 2 == 0:
        s += n
        v += n
print('A soma de {} números pares escolhidos é igual a: {}'.format(v, s))
