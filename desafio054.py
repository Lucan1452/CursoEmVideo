# Contador, idades
from datetime import date
maior = 0
menor = 0
##
for c in range(1, 8):
    n = int(input('\033[34mEm que ano a {}ª pessoa nasceu? \033[m'.format(c)))
    idade = date.today().year - n
    if idade >= 21:
        print('\033[33m', end='')
        maior += 1
    else:
        print('\033[31m', end='')
        menor += 1
print('\033[31mDos {} anos de nascimento inseridos\n\033[33m{} são maiores de idade\ne {} são menores.'.format(c, maior, menor))
