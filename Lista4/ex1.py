st1 = input('Digite a primeira string: ')
st2 = input('Digite a segunda string: ')

letras1=0
letras2=0

for i in st1:
    if i in st1:
        letras1 = letras1 + 1

for i in st2:
    if i in st2:
        letras2 = letras2 + 1

if st1 == st2:
    print('As strings são iguais.')
else:
    print('As strings sao diferentes.')

print(f'String 1 = {st1}')
print(f'String 2 = {st2}')
print(f'Tamanho da string 1: {letras1}')
print(f'Tamanho da string 2: {letras2}')