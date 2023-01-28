from random import randint
numero = int(randint(0, 10))
contador = 0
acertou = False
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adinvinhar.')
print('-=-' * 20)
while not acertou:
    jogador = int(input('Tente acertar: '))
    contador += 1
    if jogador == numero:
        acertou = True
    else:
        if jogador > numero:
            print('O número que pensei é um tanto MENOR. Tente novamente...')
        else:
            print('O número que pensei é um tanto MAIOR. Tente novamente...')
print('Você acertou com {} tentativas!!!'.format(contador))
