n = int(input('Digite um número inteiro qualquer: '))
c = int(input('Escolha uma das bases para conversão: \n'
              '[ 1 ] Conventer para BINÁRIO \n'
              '[ 2 ] Converter para OCTAL \n'
              '[ 3 ] Converter para HEXADECIMAL'))
if c == 1:
    print('{} covertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif c == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif c == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção invalida. Tente novamente.')
