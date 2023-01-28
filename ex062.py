print('10 TERMOS DE UMA PA \n')
primeiro = int(input('Digite o valor do PRIMEIRO TERMO da PA: '))
razao = int(input('Digite o valor da RAZÃO da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pause')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('Progresso finalizado com {} termos apresentados'.format(total))
print('FIM')
