# Encontrar letra "A" numa frase /1º) Quantas vezes o "A" aparece
#/2º)Posição da primeira vez que "A" aparece/3º) Posição da última vez
frase = input('Digite uma frase qualquer: ').upper().strip()
#1º)
countA = frase.count('A')
print('A letras "A" aparece {} vezes'.format(countA))
print('='*48)
#2º)
firstA = frase.find('A')+1
print('A letra "A" aparece pela primeira vez na posição {}'.format(firstA))
print('='*48)
#3º
lastA = frase.rfind('A')+1 # rfind() começa a contar do lado direito
print('A letra "A" aparece pela última vez na posição {}'.format(lastA))
print('='*48)