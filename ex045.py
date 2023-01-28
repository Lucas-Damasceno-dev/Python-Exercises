from random import choice
print('-=' * 37)
print('Vamos jogar um pouco...?')
w = input('Que tal uma partidinha de JOKENPÔ??? \n'
          '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

q = input('REGRAS: \n'
          '1°: JOGAR NO "POOO!!!" \n'
          '2°: SÓ PODE JOGAR UM (PEDRA/PAPEL/TESOURA \n'
          '3°: PEDRA VENCE TESOURA E PERDE PARA PAPEL. \n'
          '4°: PAPEL VENCE PEDRA E PERDE PARA TESOURA. \n'
          '5°: TESOURA VENCE PAPEL E PERDE PARA PEDRA. \n'
          '6°: NÃO VALE ROUBAR!!! TÔ DE OLHO... \n'
          '7°: JÁ ESCOLHI O MEU AGORA É SUA VEZ \n'
          '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

m = 1
o = 2
k = 3
lista = [m, k, o]
x = choice(lista)

n = input('VAMOS LÀ!!!')
f = input('JO...')
a = input('KEN...')
v = input('POOO!!! ...')
print('-=' * 37)

v1 = int(input('Qual você escolheu? \n'
               'PEDRA = 1 \n'
               'PAPEL = 2 \n'
               'tesoura = 3 \n'
               '       '))
if v1 == x:
    print('Hmm... Empatamos... VAMOS DE NOVO!!!')
elif x == m and v1 == o or x == o and v1 == k or x == k and v1 == m:
    print('Droga perdi!!! VAMOS DE NOVO!!!')
elif x == m and v1 == k or x == o and v1 == m or x == k and v1 == o:
    print('HÁ HÁ HÁ!!! VENCI!!! QUER TENTAR NOVAMENTE?')
