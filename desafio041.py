# Categorizar faixa etária
from datetime import date
##
ano = int(input('Ano de nascimento do atleta: '))
idade = date.today().year - ano
##
if idade < 9:
    print('O atleta tem {} anos'.format(idade))
    print('MIRIM')
elif idade > 9 and idade < 14:
    print('O atleta tem {} anos'.format(idade))
    print('INFANTIL')
elif idade > 14 and idade < 19:
    print('O atleta tem {} anos'.format(idade))
    print('JUNIOR')
elif idade == 20:
    print('O atleta tem {} anos'.format(idade))
    print('SÊNIOR')
else:
    print('O atleta tem {} anos'.format(idade))
    print('MASTER')