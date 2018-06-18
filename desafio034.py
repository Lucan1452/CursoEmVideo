# Aumento de salário
sal = float(input('Digite o salário do funcionário: '))
if sal > 1250 :
    print('O salário é {}, logo o aumento será de 10%, dessa forma o novo salário é {}'.format(sal, sal+(sal*0.10)))
elif sal <= 1250:
    print('O salário é {}, logo o aumento será de 15%, dessa forma o novo salário é {}'.format(sal, sal+(sal*0.15)))
