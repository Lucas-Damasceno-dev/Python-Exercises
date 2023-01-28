from random import randint
maior = 0
menor = 10
escolha = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: {escolha}')
print(f'O maior valor sorteado foi {max(escolha)}')
print(f'O menor valor sorteado foi {min(escolha)}')