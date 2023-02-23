def maior(* numeros):
    print('-='*30)
    print('Analisando os valores passados...')
    if numeros == ():
        print('Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0.')
    if numeros != ():
        tot_num = 0
        for numero in numeros:
            tot_num += 1
        print(f'{numeros} Foram informados {tot_num} valores ao todo.')
        print(f'O maior valor informado foi {max(numeros)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
