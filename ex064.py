print('-=' * 50)
print('Calculadora de soma com números inteiros (Digite "999" para parar):')
print('-=' * 50)
numero = 0
soma = 0
contador = 0
while numero != 999:
    numero = int(input('Digite um inteiro:'))
    soma += numero
    contador += 1
print('Foram digitados {} números e o valor da soma deles é: {}'.format(contador, soma))
