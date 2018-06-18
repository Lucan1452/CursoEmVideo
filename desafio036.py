# Calculando financiamento
from time import sleep
print('\033[1;37m-=-'*22)
print('\033[1;33mOlá! Vamos simular seu financiamento de compra de uma casa ?')
print('\033[1;37m-=-'*22)
##
house_price = int(input('\033[4;35mQual o valor da casa desejada? R$'))
salário = int(input('\033[4;35mQual o seu salário mensal? R$'))
time_for_pay = int(input('\033[4;35mEm quantos anos pretende quitar a divida? '))
valor_mensal = (house_price) / (time_for_pay*12)
print('\033[1;34;40mUm momento, estou fazendo meus cálculos ...\033[m')
sleep(1.5)
print('Para quitar uma casa de R${} durante {} anos\nA prestação será de R${:.2f}'.format(house_price, time_for_pay, valor_mensal))
##
if valor_mensal < (salário*0.3):
    print('\033[1;32mMuito bem, você irá pagar R${:.2f} por mês durante {} anos!'.format(valor_mensal, time_for_pay))
elif valor_mensal == (salário*0.3):
    print('\033[1;32mVai ser apertado, mas é possível quitar a dívida em {} anos'.format(time_for_pay))
else:
    print('\033[1;32mNEGADO você não tem condições de comprar essa casa agora!')
##
print('\033[1;37m-=-'*22)
print('\033[1;33mEspero ter ajudado!')
print('\033[1;37m-=-'*22)
