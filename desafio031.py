# Calculando valor de viagens
dist = float(input('Digite a distancia a ser percorrida em km: '))
if dist <= 200:
    print('O valor a ser pago pela passagem é {} reais'.format(dist*0.5))
else:
    print('O valor a ser pago é {} reais'.format(dist*0.45))