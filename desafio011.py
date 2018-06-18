# Calcular área e quantidade de tinta necessário para pintar esta área
alt = float(input('Altura em metros da parede: '))
larg = float(input('Largura em metros da parede: '))
área = alt*larg
print('Sua parede possui a dimensão de {} x {}, sua área é de {} '. format(alt,larg,área,))
tinta = área/2
print("Você vai precisar de {}l de tinta".format(tinta))