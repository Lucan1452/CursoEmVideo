# Palindromo
frase = str(input('Digite uma frase: ')).strip().replace(' ', '').upper()
inverso = ''
## Fatiamento

inverso1 = frase[::-1]

##
'''for letra in range (len(frase) -1, -1, -1):
    inverso += frase[letra]'''
##
print('O inverso da frase {} é {}'.format(frase, inverso1))
if inverso1 == frase:
    print('Por isso temos um palíndromo!')
else:
    print('Por isso não temos um palíndromo!')
