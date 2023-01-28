from math import cos, sin, tan, radians
a = float(input('Digite o valor do ângulo desejado em graus "º":'))
c = cos(radians(a))
s = sin(radians(a))
t = tan(radians(a))
print('Os respectivos valores de seu cosseno, seno e tangente são: {}, {} e{}'.format(c, s, t))

