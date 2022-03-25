salario=float(input("Salario:"))
if salario <=600:
   imposto=float(0.07)
elif salario>600 and  salario<=800:
    imposto=float(0.08)
elif salario>800 and salario<=1200:
    imposto=float(0.09)
elif salario>1200:
    imposto=float(0.11)
salario=salario-(salario*imposto)
print(f"O salario é de {salario}")
