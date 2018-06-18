# Analise completa
idades = 0
menor20 = 0
homemvelho = []
velho = 0
##
for pess in range(1, 5):
    print('----- {}ª PESSOA -----'.format(pess))
    nome = str(input('NOME: '.format(pess))).strip().capitalize()
    idade = int(input('IDADE: '.format(pess)))
    sexo = input('SEXO [ M ] ou [ F ]: '.format(pess))
    idades += idade
    medid = float(idades / 4)
    if pess == 1 and sexo in 'Mm':
        velho = idade
        homemvelho = nome
    elif sexo in 'Mm' and idade > velho:
            velho = idade
            homemvelho = nome
    if idade < 20 and sexo in 'Ff':
        menor20 += 1
        novo = nome

print('\033[1;36mA média da idade deste grupo é \033[4;34m{} anos'.format(medid))
print('\033[1;36mO nome do homem mais velho é \033[4;34m{} com {} anos'.format(homemvelho, velho))
print('\033[4;34m{} \033[1;36mmulhere(s) tem menos de 20 anos'.format(menor20))
