somaidade = 0
maioridadehomem = 0
totmulher = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip()
    somaidade += i
    if p == 1 and s in 'Mn':
        maioridadehomem = i
        nomevelho = n
    if s in 'Mm' and i > maioridadehomem:
        maioridadehomem = i
        nomevelho = n
    if s in 'Ff' and i < 20:
        totmulher += 1
media = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anios'.format(totmulher))
