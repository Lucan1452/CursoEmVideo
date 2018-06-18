# Somatoria de múltiplos de 3
s = 0
count = 0
print('A somatória dos valores múltiplos de 3 entre 1 e 500 é:')
for c in range(1, 501, 2):
    if c % 3 == 0:
     s += c
     count += 1
print('A soma de todos os {} números multiplos de três entre 1 e 500 é {}'.format(count, s))
