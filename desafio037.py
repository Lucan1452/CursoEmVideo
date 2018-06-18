# Bases de conversão
import math
##
n = int(input('Digite um valor: '))
n1 = int(input('''
Você que ver esse valor {}, convertido em:
[1] para Binário
[2] para Octal
[3] para Hexadecimal
Resposta: '''.format(n)))
##
if n1 == 1:
    print('Você escolheu ver {} em Binário --> {}'.format(n, bin(n)[2:]))
elif n1 == 2:
    print('Você escolheu ver {} em Octal --> {}'.format(n, oct(n)[2:]))
elif n1 == 3:
    print('Você escolheu ver {} em Hexadecimal --> {}'.format(n, hex(n)[2:]))
else:
    print('Por favor, escolha [1], [2] ou [3] ...')