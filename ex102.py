def fatorial(fator, show=False):
    result = 1
    conta = f'{fator}! = '
    for num in range(fator, 0, -1):
        result *= num
        if show:
            conta += f'{num} x '
        if not show and num == 1:
            conta = f'{fator} = '
    conta += str(result)
    return conta if show else result
        
print(fatorial(15)) # mostra apenas o resultado
print(fatorial(15, show=True)) # mostra toda a conta e seu resultado ao fim

