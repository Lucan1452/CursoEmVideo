# Leia 3 números e indique o maior e o menor
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))
menor = n1
maior = n3
print('Você digitou os valores {} , {} , {}'.format(n1, n2, n3))
# Para o menor valor
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
# Para o maior valor
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
print('O menor valor é: {}'.format(menor))
print('O maior valor é: {}'.format(maior))