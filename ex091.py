from random import randint
from time import sleep
from operator import itemgetter
print('Valores sorteados:')
jogo = {'1º jogador': randint(1, 6),
        '2º jogador': randint(1, 6),
        '3º jogador': randint(1, 6),
        '4º jogador': randint(1, 6)}
ranking = dict()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('    == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
