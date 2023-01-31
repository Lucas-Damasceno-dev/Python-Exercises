palavras = ('arroz', 'feijão', 'carne', 'suiça')
for palavra in palavras:
    print(f'\n Na palavra "{palavra}" temos as vogais', end=' ')
    for letra in palavra:
        if letra in 'aáãâeéêiíoôóuú':
            print( letra, end=' ')
