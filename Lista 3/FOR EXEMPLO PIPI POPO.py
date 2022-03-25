nomes = ['A','By','Casa','vrau']
for nome in nomes[:]:
    print(nome, len(nome))
    if len(nome) > 3:
        nomes.insert(0,nome)
print(nomes)
