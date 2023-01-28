n1 = int(input('Digite o 1° valor:'))
n2 = int(input('Digite o 2° valor:'))
n3 = int(input('Digite o 3° valor:'))

m = n1
if n2 < n1 and n2 < n3:
    m = n2
if n3 < n1 and n3 < n2:
    m = n3

M = n1
if n2 > n1 and n2 > n3:
    M = n2
if n3 > n1 and n3 > n2:
    M = n3

print('O maior valor é: {}'. format(M))
print('O menor valor é: {}'.format(m))
