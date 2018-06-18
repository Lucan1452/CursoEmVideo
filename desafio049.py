# Refazer desafio 009, com conhecimentos de for
print('~~'*14)
print('Vamos estudar a TABUADA !')
print('~~'*14)
n = int(input('Digite um número inteiro: '))
print('~~'*14)
r = n
for c in range(1,11):
    r = n * c
    print('{} x {} = {}'.format(n, c, r))
print('~~'*14)
print('FIM!')