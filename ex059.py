from time import sleep
r = 0
m = 0
print('Digite dois valores para abrir o menu.')
print('-=' * 20)
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
while not r == 5:
    print('-=' * 20)
    r = int(input('[1] Somar \n'
                  '[2] Multiplicar \n'
                  '[3] Maior \n'
                  '[4] Novos números \n'
                  '[5] Sair do programa \n'
                  'Resposta: '))
    print('-=' * 20)
    if r == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif r == 2:
        print('{} * {} = {}'.format(n1, n2, n1 * n2))
    elif r == 3:
        if n1 > n2:
            m = n1
        else:
            m = n2
        print('Entre {} e {} o maior número é {}'.format(n1, n2, m))
    elif r == 4:
        print('Ok apagando anotações...')
        print('Digite novos números...')
        sleep(2)
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    elif r == 5:
        print('Saindo...')
        sleep(2)
        print('Até mais.')
        exit()
    else:
        print('Opção inválida. tente novamente.')
