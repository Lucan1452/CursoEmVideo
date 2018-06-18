# Advinhação
from random import randint
import time
print('-=-'*20)
print('Olá, vamos jogar o JOGO da adivinhação ?')
print('-=-'*20)
print('Irei pensar em um número entre 0 e 5, tente adivinhar!!')
print('-=-'*20)
x = int(input('Digite um número entre 0 e 5: '))
y = randint(0, 5)
print('PROCESSANDO ...')
time.sleep(2)
if x == y:
    print('Uau ! Você acertou !! Pensamos no número {}, que incrível !'.format(x))
else:
    print('PERDEU eu pensei no número {} não no {} !'.format(y, x))