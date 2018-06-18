# Somatório de valores pares
s = 0
count = 0
print('<>'*9)
print('Somatório de PARES')
print('<>'*9)
for c in range(1, 7):
    n = int(input('Digite um valor:'))
    if n % 2 == 0:
        s += n
        count += 1
print('<>'*9)
print('O somatório dos {} números\nPARES digitados é:'.format(count))
print(s)