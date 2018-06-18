# Analisar string nome/ 1º) todas maiúsculas/ 2ª) minusculas
# /3º) comprimento sem espaços/4º) comprimento 1º nome
nome = input('Qual o seu nome completo? ').strip()
# 1º)
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('='*48)
# 2º)
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('='*48)
# 3º)
print('O seu nome tem {} letras'.format(len(nome.replace(' ',''))))
# Ou
print('O seu nome tem {} letras'.format((len(nome) - nome.count(' '))))
print('='*24)
# 4º)
nome1 = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(nome1[0],(len(nome1[0]))))
print('='*48)