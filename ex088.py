from random import randint
num_listas = int(input('Quantos jogos você quer sortear?  '))
num_sorteios = []
for jogos in range(0, num_listas):
    aleatorio = [0, 0, 0, 0, 0, 0]
    for pos, numero in enumerate(aleatorio):
        aleatorio[pos] = randint(1, 60)
    num_sorteios.append(aleatorio)
for jogos in range(0, num_listas):
    print(f'jogo {jogos + 1}: {num_sorteios[jogos]}')
