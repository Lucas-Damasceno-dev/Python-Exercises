from random import randint
print('VAMOS JOGAR ÍMPAR OU PAR')
jogador = 'vencer'
contador = 0
escolha = 'P'
while jogador == 'vencer':
    computador = randint(0, 10)
    numero = int(input('Digite um valor: '))
    escolha = str(input('Par ou ímpar? [P/I] ')).strip().upper()
    soma = computador + numero
    print(f'Você jogou {numero} e o computador {computador}. Total de {soma}!')
    if escolha == 'P' and soma % 2 == 0:
        contador += 1
        print('Você GANHOU!')
        print('Vamos jogar novamente...')
    elif escolha == 'P' and soma % 2 != 0:
        print('Você PERDEU!')
        jogador = 'perder'
    elif escolha == 'I' and soma % 2 != 0:
        contador += 1
        print('Você GANHOU!')
        print('Vamos jogar novamente...')
    elif escolha == 'I' and soma % 2 == 0:
        print('Você PERDEU!')
        jogador = 'perder'
print(f'GAME OVER! Você venceu {contador} vezes.')
