primeiro = 1
segundo = 1
proximos = 0
contador = 0
print('-' * 50)
print('Sequência de Fibonacci')
print('-' * 50)
termos = int(input('Qual o número de termos que você quer da sequencia se Fibonacci? '))
print('{} - {} - '.format(primeiro, segundo), end='')
while contador != termos:
    proximos = primeiro + segundo
    primeiro = segundo
    segundo = proximos
    contador += 1
    print('{} '.format(proximos), end='- ')
print('FIM...', end='')
