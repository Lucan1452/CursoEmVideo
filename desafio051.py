# P.A
x = int(input('Primeiro termo da P.A: '))
z = int(input('Razão da P.A: '))
f= x + (10 * z)
for c in range(x, f, z):
    print(c, end='')
    print(' -> ', end='')
print('FIM !')