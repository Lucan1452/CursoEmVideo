# Cálculo de IMC
from time import sleep
##
print('\033[;34m~~~\033[m'*15)
print('\033[1;36mOlá ! Será que você está acima do peso ?')
print('\033[1;36mHoje vamos calcular seu IMC!\033[m')
print('\033[;34m~~~\033[m'*15)
##
peso = float(input('\033[4;33mQual o seu peso: '))
altura = float(input('Qual a sua altura em m: \033[m'))
IMC = float(peso/altura **2)
##
print('\033[:34m---\033[m'*15)
print('\033[1;34;40mVamos calcular ...\033[m')
print('\033[;34m---\033[m'*15)
##
sleep(1.5)
##
if IMC < 18.5:
    print('\033[1;36mIMC: {:.2f} Você está ABAIXO do peso !'.format(IMC))
elif IMC > 18.5 and IMC < 25:
    print('IMC: {:.2f} Você está no PESO IDEAL !'.format(IMC))
elif IMC > 25 and IMC < 30:
    print('IMC: {:.2f} É bom começar a se exercitar, está um pouco ACIMA DO PESO'.format(IMC))
elif IMC > 30 and IMC <40:
    print('IMC: {:.2f} Está na hora de fazer um bela dieta, você está OBESO !\033[m'.format(IMC))
else:
    print('\033[1;31;4mIMC: {:.2f} ALERTA! Você está com OBESIDADE MÓRBIDA !!!\033[m'.format(IMC))
print('\033[1;33mCuide sempre da sua saúde, FAÇA EXERCÍCIOS !!!\033[m')