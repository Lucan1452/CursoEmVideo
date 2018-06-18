#Conversor de medidas
medida = float(input('Digite uma medida em metro: '))
km = medida/1000
hm = medida/100
dam = medida/10
dm = medida*10
cm = medida*100
mm = medida*1000

print('''Conversos de medidas
\t {}
\t {}
\t {}
\t {}
\t {}
\t {}
\t {}'''.format(km, hm, dam, medida, dm, cm, mm))
