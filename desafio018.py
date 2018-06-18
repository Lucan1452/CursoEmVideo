# Mostrar sen,cos e tg de x
import math
x = math.radians(float(input('Digite um ângulo em graus º')))
senx = math.sin(x)
cosx = math.cos(x)
tgx = math.tan(x)
print('O ângulo {:.2f}, possui SEN:{:.2f}, COS:{:.2f} e TG:{:.2f}'.format(x, senx, cosx, tgx))
