print('10 TERMOS DE UMA PA \n')
primeiro = int(input('Digite o valor do PRIMEIRO TERMO da PA: '))
razao = int(input('Digite o valor da RAZÃO da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
