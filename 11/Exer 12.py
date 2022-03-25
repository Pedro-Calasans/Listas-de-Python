vha,na,imposto=float(input("Valor da hora:")), float(input("Numero de Aulas:")), float(input("Valor do imposto:"))
salario=vha*na
salariofinal=salario-(salario*(imposto/100))
print(f'O salario liquido é de: {salariofinal}')
