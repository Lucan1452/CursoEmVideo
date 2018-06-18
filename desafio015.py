dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))
total = 60 * dias + (0.15) * km
print('O carro foi alugado por {} dias, e foram percorridos {}km, logo, o valor a ser pago será de R${:.2f}'.format(dias, km, total))
