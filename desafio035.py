# Condição para formar um triângulo
print('Vamos descobrir se é possível fazer um triângulo com as retas abaixo?')
a = len(str(input('Digite uma reta: ')).strip())
b = len(str(input('Digite outra reta: ')).strip())
c = len(str(input('Digite mais uma reta: ')).strip())
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Com as retas {}cm, {}cm e {}cm é possível formar um triângulo.'.format(a, b, c))
else:
    print('Com as retas {}cm, {}cm e {}cm não é possível formar um triângulo.'.format(a, b, c))
