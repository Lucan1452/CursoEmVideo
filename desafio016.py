# Mostrar um número inteiro e sua parte real
from math import floor,ceil,trunc
num = float(input('Digite um número qualquer: '))
int = floor(num)
int1 = ceil(num)
inteiro = trunc(num)
print('O número é {} e sua porção inteira arredondado para cima é {}'.format(num, int))
print('o número é {} e sua porção inteira arredondado para baixo é {}'.format(num, int1))
print('o número é {} e sua porção inteira é {}'.format(num, inteiro))