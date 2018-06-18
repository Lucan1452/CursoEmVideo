# Números primos
n = int(input('Número: '))
tot = 0
## Laço
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end='')
## Fora do laço
print('\n\033[mO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('É um número PRIMO')
else:
    print('Não é um número PRIMO')
