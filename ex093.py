dados = dict()
total_gols = []
jogador = str(input('Nome do jogador:  ')).strip().capitalize()
jogos = int(input('Quantos partidas jogou?  '))
dados['Nome'] = jogador
for partida in range(0, jogos):
    num_gols = int(input(f'Quantos gols na partida {partida+1}?  '))
    total_gols.append(num_gols)
    dados['Gols'] = total_gols
    total = 0
    for gol in total_gols:
        total += gol
        dados['Total'] = total
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados["Nome"]} jogou {jogos}')
cont = 1
for gol in total_gols:
    print(f'  => Na partida {cont}, fez {gol}.')
    cont += 1
print(f'Foi um total de {dados["Total"]} gols.')
