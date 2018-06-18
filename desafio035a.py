# Condição para formar um triângulo
print('Vamos descobrir se é possível fazer um triângulo com as retas abaixo?')
a = float(input('Digite uma reta: '))
b = float(input('Digite outra reta: '))
c = float(input('Digite mais uma reta: '))
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Com as retas {}cm, {}cm e {}cm é possível formar um triângulo.'.format(a, b, c))
else:
    print('Com as retas {}cm, {}cm e {}cm não é possível formar um triângulo.'.format(a, b, c))
