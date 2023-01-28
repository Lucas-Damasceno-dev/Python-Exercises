s = 0
v = 0
for c in range(3, 501, 3):
    if c % 3 == 0 and c % 2 != 0:
        s = s + c
        v = v + 1
print('O valor da soma de todos os {} números ímpares de 1 a 500 é: {}'.format(v, s))
