def pyhelp(comando):
    """
    -> Função que mostra a documentação de um comando ou função do Python.
    :param comando: o comando ou função do Python para o qual se deseja obter a documentação
    :return: sem retorno
    """
    help(comando)


while True:
    comando = input('\033[1;30mDigite um comando ou função do Python (ou "FIM" para sair): \033[m')
    if comando.upper() == 'FIM':
        print('\033[1;32mSaindo... \033[m')
        break
    else:
        pyhelp(comando)
