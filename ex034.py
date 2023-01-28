s = float(input('Digite o valor do seu salário:'))
if s > 1250:
    ns = s * 1.1
    print('O novo valor do seu salário com o aumento de 10% é: R%{:.2f}'.format(ns))
else:
    ns = s * 1.15
    print('O novo valor do seu salário com o aumento de 15% é: R%{:.2f}'.format(ns))
