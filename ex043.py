p = float(input('Qual o seu peso?'))
h = float(input('Qual a sua altura?'))

imc = p / (h * h)

if imc < 18.5:
    print('IMC = {}: Abaixo do peso!'.format(imc))
elif 18.5 <= imc < 25:
    print('IMC = {}: Peso ideal!'.format(imc))
elif 25 <= imc < 30:
    print('IMC = {}: Sobrepeso!'.format(imc))
elif 30 < imc <= 40:
    print('IMC = {}: Obesidade!'.format(imc))
else:
    print('IMC = {}: Obesidade mórbida!'.format(imc))
