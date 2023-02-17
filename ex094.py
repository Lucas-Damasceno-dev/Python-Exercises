dados = list()
tot_pessoas = 0
tot_idade = 0
mulheres = list()
velhos = list()
sexo_velhos = list()
idade_velhos = list()
while True:
    tot_pessoas += 1
    pessoa = dict()
    nome = str(input('Nome:  ')).strip().capitalize()
    pessoa['Nome'] = nome
    sexo = str(input('Sexo: [M/F]  ')).strip().lower()
    if sexo not in 'mf':
        while sexo not in 'mf':
            print('ERRO! Responda apenas M ou F.')
            sexo = str(input('Sexo: [M/F]  ')).strip().lower()
    pessoa['Sexo'] = sexo
    if sexo == 'f':
        mulheres.append(nome)
    idade = int(input('Idade:  '))
    pessoa['Idade'] = idade
    tot_idade += idade
    media = tot_idade / tot_pessoas
    dados.append(pessoa)
    if idade >= media:
        velhos.append(nome)
        sexo_velhos.append(sexo)
        idade_velhos.append(idade)
    continuar = str(input('Quer continuar? [S/N]  ')).strip().lower()
    if continuar not in 'sn':
        while continuar not in 'sn':
            print('ERRO! Responda apenas S ou N.')
            continuar = str(input('Quer continuar? [S/N]  ')).strip().lower()
    if continuar == 'n':
        break
print('-='*30)
print(f'A) Ao todo temos {tot_pessoas} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}')
print(f'D) Listas das pessoas com idade acima da média:')
for ser in range(0, len(velhos)):
    print(f'Nome = {velhos[ser]}; sexo = {sexo_velhos[ser]}; idade = {idade_velhos[ser]}')
print()
print('<< ENCERRADO >>')
