# Usando find() ou in
cidade = input('Onde você mora? ').strip().upper()
city = cidade.split()
print('O nome desta cidade começa com "Santo"?', end = ' ')
print('SANTO' in city[0])