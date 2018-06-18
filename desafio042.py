# Desafio do triângulos masi elaborado
r1 = int(input('Primeiro lado: '))
r2 = int(input('Segundo lado: '))
r3 = int(input('Terceiro lado: '))
# Tipos de triângulo
equi = (r1 == r2 == r3)
iso = (r1 == r2) or (r1 == r3) or (r2 == r3)

if r1 < r2 + r3 and r2 < r2 + r3 and r3 < r1 + r2:
    print('Sim, é possível formar um triângulo')
    if equi:
        print('É um triângulo EQUILÁTERO')
    elif iso:
        print('É um triângulo ISÓCELES')
    else:
        print('É um triângulo ESCALENO')
else:
    print('Não é possível formar um triângulo')
print('Obrigado!')