cont = 0
while True:
    cpf = str(input('Digite seu CPF: '))

    if not cpf.isdigit():
        print('CPF INVALIDO, TENTE NOVAMENTE: ')
    else:
        for i in cpf:
            if i in cpf:
                cont = cont + 1
        if cont == 11:
            print(f'CPF VALIDO: {cpf}')
            break
        else:
            print('CPF INVALIDO, TENTE NOVAMENTE: ')
