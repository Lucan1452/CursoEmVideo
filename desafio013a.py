# Porcentagens
salario = float(input('\tDigite o salário do funcionário:\t'))
percent = float(input('\tDigite a % do aumento:\t'))
valor_aumentado = float((salario*percent)/100)
salario_com_aumento = float(salario + valor_aumentado)
print('\tO salário é {}'.format(salario))
print('\tO aumento é de {}%'.format(percent))
print('\tSerá aumentado {} reais'.format(valor_aumentado))
print('\tO valor do salário será {}'.format(salario_com_aumento))