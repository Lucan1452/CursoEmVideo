# Use o comando .is para definir os tipos possível do algo escrito.

n = input('Digite algo: ')
print('O tipo primitivo é: ',type(n))
print('É um número? ',n.isnumeric())
print('São só letras? ',n.isalpha())
print('São espaços? ',n.isspace())
print('É printável? ',n.isprintable())
print('É decimal? ',n.isdecimal())
