# Multa por limite de velocidade
import colorsys
vel = int(input('Qual a velocidade do carro: '))
multa = (vel - 80)*7
if vel > 80:
    print('Você foi MULTADO !')
    print('Você excedeu o limite de velocidade, deverá pagar uma multa de {} reais'.format(multa))
else:
    print('Tudo OK, você é um motorista consciente !')
