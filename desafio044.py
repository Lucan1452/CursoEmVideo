# Calculando taxas
from time import sleep
##
print('\033[1;37m^^^\033[m'*15)
print('\033[1;33mOlá, sou seu assistente de caixa\033[m')
print('\033[1;37m^^^\033[m'*15)
##
preço_normal = float(input('\033[1;33mQual o valor do produto? R$ '))
pagamento = int(input('''Qual a forma de pagamento?
[1]-para à vista
[2]-para parcelado '''))
##
print('\033[4;30;41mCerto ...\033[m')
sleep(1)
##
if pagamento == 1:
    pay = int(input('''\033[1;36mEscolha:
[1]-À vista em dinheiro/cheque recebe 10% de desconto
[2]-À vista no cartão recebe 5% de desconto'''))
    if pay == 1:
        print('O produto custará R${:.2f}'.format(preço_normal - (preço_normal*0.1)))
    else:
        print('O produto custará R${:.2f}\033[m'.format(preço_normal - (preço_normal*0.05)))
elif pagamento == 2:
    pay2 = int(input('''\033[1;35mEm quantas parcelas? '''))
    if pay2 <= 2:
        print('O produto custará R${:.2f}'.format(preço_normal))
    else:
        print('O produto custará R${:.2f}\033[m'.format(preço_normal + (preço_normal*0.2)))
##
print('\033[1;37m^^^\033[m'*15)
print('\033[1;32mObrigado! Volte Sempre !\033[m')
print('\033[1;37m^^^\033[m'*15)
