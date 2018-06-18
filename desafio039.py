# Calcular tempo de alistamento
from datetime import date
##
print('\033[1;34mOlá! Vamos ver se você está em dia com o exército?')
##
ano = int(input('Em qual ano você nasceu? '))
sexo = input('''Sexo:
[M] Masculino
[F] Feminino ''')
idade = int((date.today().year) - ano)
##
if sexo == 'M' or sexo == 'm':
    print('Para você o alistamento é obrigatório')
    if idade == 18:
        print('Você tem {} anos, este é o ano em que você deve se alistar !'.format(idade))
        print('Alistamento em {}'.format(date.today().year))

    elif idade > 18:
        saldo = int(idade - 18)
        print('Você tem {} anos, seu alistamento foi a {} ano(s), espero que esteja em dia !'.format(idade, saldo))
        print('Alistamento foi em {}'.format((date.today().year) - saldo))

    elif idade < 18:
        saldo = int(18- idade)
        print('Você tem {} anos, faltam {} ano(s) para seu alistamento'.format(idade, saldo))
        print('Seu alistamento será em {}'.format(date.today().year + saldo))

else:
    print('Você não precisa se alistar !')