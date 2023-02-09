pessoas = []
pesos = []
continuar = 's'
peso_max = peso_min = 0
pessoas_max = []
pessoas_min = []
while continuar == 's':
    nome_pessoa = str(input('Nome:  '))
    peso_pessoa = float(input('Peso:  '))
    pessoas.append(nome_pessoa)
    pesos.append(peso_pessoa)
    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()
    if continuar not in 'sn':
        while continuar not in 'sn':
            print('Resposta inválida. Tente novamente...')
            continuar = str(input('Quer continuar? [S/N] ')).strip().lower()
    if continuar == 'n':
        for pos, peso in enumerate(pesos):
            if peso == max(pesos):
                pessoas_max.append(pessoas[pos])
            if peso == min(pesos):
                pessoas_min.append(pessoas[pos])
print('-='*25)
print(f'Ao todo, você cadastrou {len(pessoas)}.')
print(f'O MAIOR peso foi de {max(pesos)}Kg. Peso de {pessoas_max}')
print(f'O MENOR peso foi de {min(pesos)}Kg. Peso de {pessoas_min}')
