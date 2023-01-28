contador = 0
soma = 0
while True:
    numero = int(input('Digite um número inteiro: [digite 999 para parar] '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'A soma dos {contador} valores foi {soma}!')
