f = str(input('Digite uma frase:')).strip().lower()
print('Existem {} letras "a" na frase'.format(f.count('a')))
print('e sua primeira aparição é na posição {}'.format(f.find('a') + 1))
print('já sua ultima aparição é na posição {}.'.format(f.rfind('a') + 1))
