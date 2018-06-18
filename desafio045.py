#Jokenpô
from time import sleep
from random import randint
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'vermelho':'\033[1;31m',
         'roxo':'\033[1;36m'}
##
jogo = 'Jokenpô !'
print('\033[1;33m==\033[m'*15)
print('{}{:^30}{}'.format(cores['azul'], jogo, cores['limpa']))
print('\033[1;33m==\033[m'*15)
##
jogador = int(input('''{}Escolha:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Resposta:{} '''.format(cores['roxo'], cores['limpa'])))
PC = randint(0,2)
##
print('{}JO'.format(cores['vermelho']))
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ !{}'.format(cores['limpa']))
sleep(0.5)
## PEDRA
if jogador == 0 and PC == 2:
    print('\033[1;33==\033[m' * 15)
    print('''Jogador : PEDRA
PC : TESOURA''')
    print('{}Jogador Venceu !{}'.format(cores['vermelho'], cores['limpa']))
    print('\033[1;33m==\033[m' * 15)
elif jogador == 0 and PC == 1:
    print('\033[1;33m==\033[m' * 15)
    print('''Jogador : PEDRA
PC : PAPEL''')
    print('\033[1;35mPC venceu !\033[m')
    print('\033[1;33m==\033[m' * 15)
elif jogador == 0 and PC == 0:
    print('\033[1;33m==\033[m' * 15)
    print('''Jogador : PEDRA
PC : PEDRA''')
    print('\033[1;34mEMPATE !\033[m')
    print('\033[1;33m==\033[m' * 15)
## PAPEL
elif jogador == 1 and PC == 0:
    print('\033[1;33m==\033[m' * 15)
    print('''Jogador : PAPEL
PC : PEDRA''')
    print('{}Jogador Venceu !{}'.format(cores['vermelho'], cores['limpa']))
    print('\033[1;33m==\033[m' * 15)

elif jogador == 1 and PC == 2:
    print('\033[1;33m==\033[m' * 15)
    print('''Jogador : PAPEL
PC : TESOURA''')
    print('\033[1;35mPC venceu !\033[m')
    print('\033[1;33m==\033[m' * 15)
elif jogador == 1 and PC == 1:
    print('\033[1;33m==\033[m' * 15)
    print('''Jogador : PAPEL
PC : PAPEL ''')
    print('\033[1;34mEMPATE !\033[m')
    print('\033[1;33m==\033[m' * 15)
## TESOURA
elif jogador == 2 and PC == 1:
    print('\033[1;33m==\033[m' * 15)
    print('''Jogador : TESOURA
PC : PAPEL''')
    print('{}Jogador Venceu !{}'.format(cores['vermelho'], cores['limpa']))
    print('\033[1;33m==\033[m' * 15)
elif jogador == 2 and PC == 0:
    print('\033[1;33m==\033[m' * 15)
    print('''Jogador : TESOURA
PC : PEDRA''')
    print('\033[1;35mPC venceu !\033[m')
    print('\033[1;33m==\033[m' * 15)
elif jogador == 2 and PC == 2:
    print('\033[1;33m==\033[m' * 15)
    print('''Jogador : TESOURA
PC : TESOURA'''.format(jogador, PC))
    print('\033[1;34mEMPATE !\033[m')
    print('\033[1;33m==\033[m' * 15)
##
print('\033[34mBom JOGO !')