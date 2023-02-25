from datetime import datetime


def voto():
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos. NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


ano_nascimento = int(input('Qual seu ano de nascimento?  '))
voto()
