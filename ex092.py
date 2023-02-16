import datetime
pessoa = {}
nome = str(input('Nome:  ')).strip().capitalize()
nascimento = int(input('Ano de nascimento:  '))
idade = datetime.datetime.now().year - nascimento
ctps = int(input('Carteira de Trabalho (0 Não tem):  '))
pessoa['nome'] = nome
pessoa['idade'] = idade
pessoa['ctps'] = ctps
if ctps != 0:
    salario = float(input('Salário:  '))
    contratacao = int(input('Ano de contratação:  '))
    pessoa['Salário'] = salario
    pessoa['Contratação'] = contratacao
    pessoa['Aposentadoria'] = idade + contratacao + 35 - datetime.datetime.now().year
print('-='*30)
for k, v in pessoa.items():
    print(f'- {k} tem valor {v}')
