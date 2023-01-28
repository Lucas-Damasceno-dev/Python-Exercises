print('-=' * 37)
print('Vamos calcular o valor real do produto com base na condição de pagamento!')
print('-=' * 37)
v = float(input('Qual o valor do produto?'))
print('-=' * 37)
dc = int(input('Digite de 1 a 4 e escolha uma forma de pagamento: \n'

               'À vista com DINHEIRO ou CHEQUE: 10% de desconto = 1 \n'
               'À vista com CARTÃO: 5% de desconto = 2 \n'
               'Em até 2x NO CARTÃO: Preço normal = 3 \n'
               'Em 3x ou mais NO CARTÃO: 20% de juros = 4 \n'))
print('-=' * 37)
f1 = v * 0.9
f2 = v * 0.95
f4 = v * 1.2
if dc == 1:
    print('O valor final do produto é R${:.2f}'.format(f1))
elif dc == 2:
    print('O valor final do produto é R${:.2f}'.format(f2))
elif dc == 3:
    print('O valor final do produto é R${:.2f}'.format(v))
else:
    print('O valor final do produto é R${:.2f}'.format(f4))
print('-=' * 37)
