def notas(*notas, situacao=False):
    """
    -> Função que recebe várias notas de alunos e retorna um dicionário com as seguintes informações:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional)
    :param notas: uma ou mais notas dos alunos
    :param situacao: valor opcional que indica se a situação dos alunos deve ser incluída no dicionário
    :return: um dicionário com as informações solicitadas
    """
    resultado = {}
    resultado['Quantidade de notas'] = len(notas)
    resultado['Maior nota'] = max(notas)
    resultado['Menor nota'] = min(notas)
    resultado['Média da turma'] = sum(notas) / len(notas)
    if situacao:
        if resultado['Média da turma'] >= 7:
            resultado['Situação'] = 'BOA'
        elif resultado['Média da turma'] >= 5:
            resultado['Situação'] = 'RAZOÁVEL'
        else:
            resultado['Situação'] = 'RUIM'
    return resultado
