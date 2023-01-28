numero = int(input('Digite um número para \n'
                   'Calcular seu fatorial: '))
fatorial = 1
soma = 1
contador = numero
print('Calculando {}! = '.format(numero), end='')
while numero > fatorial:
    fatorial += 1
    contador -= 1
    soma *= fatorial
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
print('{}'.format(soma))
