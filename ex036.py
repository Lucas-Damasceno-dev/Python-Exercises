vc = float(input('Qual o valor da casa a ser financiada?'))
s = float(input('Qual o valor do seu salário?'))
t = float(input('Em quantos anos será a restituição do empréstimo?'))

pm = vc / (t * 12)
tt = vc / pm
if pm < (s * 0.3):
    print('O financiamento foi aprovado e o valor da parcela será {:.2f} por {} meses'.format(pm, tt))
else:
    print('O empréstimo foi negado. Sintimos muito.')
