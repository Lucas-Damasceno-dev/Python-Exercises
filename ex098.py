def contador(inicio, fim, passo):
    if passo == 0:
        print("Erro: o passo não pode ser zero.")
    elif inicio < fim:
        for i in range(inicio, fim+1, passo):
            print(i, end=' ')
        print("Fim!")
    else:
        for i in range(inicio, fim-1, -passo):
            print(i, end=' ')
        print("Fim!")


# Contagem de 1 a 10, de 1 em 1
contador(1, 10, 1)
print('~'*30)

# Contagem de 10 a 0, de 2 em 2
contador(10, 0, 2)
print('~'*30)

# Contagem personalizada
inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))
passo = int(input("Digite o valor do passo: "))
contador(inicio, fim, passo)
