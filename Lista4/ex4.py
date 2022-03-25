esp=a=e=i=o=u = 0

frase = input('Digite uma Frase: ')
frase = frase.lower()

for caracter in frase:
    if caracter in 'a':
        a = a + 1

for caracter in frase:
    if caracter in 'e':
        e = e + 1

for caracter in frase:
    if caracter in 'i':
        i = i + 1

for caracter in frase:
    if caracter in 'o':
        o = o + 1

for caracter in frase:
    if caracter in 'u':
        u = u + 1

for caracter in frase:
    if caracter in ' ':
        esp = esp + 1

print(f'o A aparece {a} vezes na frase.')
print(f'o E aparece {e} vezes na frase.')
print(f'o I aparece {i} vezes na frase.')
print(f'o O aparece {o} vezes na frase.')
print(f'o U aparece {u} vezes na frase.')
print(f'A Frase possui {esp} espaços.')