# Comparando valores
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('O primeiro valor:{} é o MAIOR'.format(n1))
elif n2 > n1:
    print('O segundo valor:{} é o MAIOR'.format(n2))
else:
    print('Não existe valor maior, ambos são iguais')
