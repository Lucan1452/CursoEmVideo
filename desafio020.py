# Ordem de quem vai lavar a louça
import random
nome1 = input('Primeiro nome: ')
nome2 = input('Segundo nome: ')
nome3 = input('Terceiro nome: ')
nome4 = input('Quarto nome: ')
nomes = [nome1, nome2, nome3, nome4]
random.shuffle(nomes)
print('A ordem de quem vai lavar a louça é')
print(nomes)