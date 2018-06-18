# Mostrar cada caractére individualmente
num = int(input('Digite um número de 0 a 9999: '))
uni = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10
print('''\tO número é {}
\tPossui {} unidade(s)
\tPossui {} dezena(s)
\tPossui {} centena(s)
\tPossui {} milhare(s)'''. format(num, uni, dez, cent, mil))