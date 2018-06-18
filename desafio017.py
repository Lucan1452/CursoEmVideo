# Calculando hipotenusa de um triângulo retângulo
from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjascente: '))
hip = hypot(co, ca)
print('O cateto oposto é {} e o cateto adjascente é {}, logo a hipotenusa é {:.2f}'.format(co, ca, hip))