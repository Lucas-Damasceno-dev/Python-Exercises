a = float(input('Digite o valor da 1° reta:'))
b = float(input('Digite o valor da 2° reta:'))
c = float(input('Digite o valor da 3° reta:'))
if a < b + c or b < a + c or c < b + a:
    print('Os segmentos PODEM FORMAR um triângulo!!!')
else:
    print('Os segmentos NÃO PODEM formar um triângulo!!!')
