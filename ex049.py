n = int(input('Digite um número para acessar sua tabuada: \n'))
print('A tabuada no número {} é:'.format(n))
for c in range(0, 11):
    print('{} * {} = {}'.format(n, c, n * c))
