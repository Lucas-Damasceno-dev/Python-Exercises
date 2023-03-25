saldo = 0
extrato = []
limite_diario = 3
limite_valor_saque = 500

print("Bem-vindo ao Banco XYZ!")
while True:
    opcao = input('\nDigite a operação desejada (D para depósito, S para saque, E para extrato, ou Q para sair): ').upper()
    
    if opcao == 'D':
        valor = float(input('Digite o valor a ser depositado: '))
        if valor > 0:
            saldo += valor
            extrato.append(('Depósito', valor))
            print(f'\nDepósito de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {saldo:.2f}')
        else:
            print('\nValor inválido para depósito.')
    
    elif opcao == 'S':
        if len([op for op in extrato if op[0] == 'Saque']) >= limite_diario:
            print('\nLimite diário de saques atingido.')
            continue
        valor = float(input('Digite o valor a ser sacado: '))
        if valor <= 0 or valor > limite_valor_saque:
            print(f'\nValor inválido para saque. O valor máximo permitido é R$ {limite_valor_saque:.2f}.')
        elif valor > saldo:
            print('\nSaldo insuficiente.')
        else:
            saldo -= valor
            extrato.append(('Saque', valor))
            print(f'\nSaque de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {saldo:.2f}')
    
    elif opcao == 'E':
        print('\nExtrato:')
        print('------------------------------------------')
        print(f'{"Operação":<15}{"Valor":>15}')
        print('------------------------------------------')
        for operacao, valor in extrato:
            if operacao == 'Depósito':
                print(f'{operacao:<15} R$ {valor:>14.2f}')
            else:
                print(f'{operacao:<15} R$ {valor:>14.2f}')
        print('------------------------------------------')
        print(f'Saldo atual: R$ {saldo:.2f}')
        print('------------------------------------------')
    
    elif opcao == 'Q':
        print('\nObrigado por utilizar o Banco XYZ!')
        break
    
    else:
        print('\nOpção inválida.')
