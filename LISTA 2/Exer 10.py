idade=int(input("Digite a idade:"))
if idade <=7:
   categoria="Infantil A"
elif idade >7 and idade<=10:
    categoria="Infantil B"
elif idade >11 and idade<=13:
    categoria="Juvenil A"
elif idade>=14 and idade<=17:
    categoria="Juvenil B"
elif idade>17:
    categoria="Senior"

print(f"A idade  é de {idade}\nE a categoria é de:{categoria}")
