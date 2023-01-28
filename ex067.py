while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if numero < 0:
        break
    for c in range(1, 11):
        print(f'{numero} * {c} = {numero * c}')
    print('-' * 30)
print(' PROGRAMA TABUADA ENCERRADA. VOLTE SEMPRE.')
