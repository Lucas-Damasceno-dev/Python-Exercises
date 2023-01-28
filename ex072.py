numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze \n'
          'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
escolha = 21
while not 0 <= escolha <= 20:
    escolha = int(input('Digite um número entre 0 e 20: '))
    if escolha in range(21):
        print(numero[escolha])
    else:
        print('Número digitado não está entre 0 e 20.')    
