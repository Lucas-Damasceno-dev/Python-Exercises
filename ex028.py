from random import randint
from time import sleep
n = int(randint(0, 5))
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adinvinhar.')
print('-=-' * 20)
t = int(input('Qual número o PC escolheu de 0 a 5?'))
print('PROCESSANDO...')
sleep(3)
if t == n:
    print('Isso {} você acertou!!! pensas como mua?'.format(n))
else:
    print('Sinto muito {} está errado!!! A resposta é {} Talvez exista humanidade em você...'.format(t, n))
