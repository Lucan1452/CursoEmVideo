# Cáculo de média de alunos
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
med = float((n1+n2)/2)
if med < 5:
    print('Você está REPROVADO! Média {} ...'.format(med))
elif med >= 5 and med <= 6.9:
    print('Você está de RECUPERAÇÃO! Média {}.'.format(med))
else:
    print('Parabéns, você foi APROVADO! Média {} !!!'.format(med))