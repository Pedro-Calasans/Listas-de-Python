qw,sl=float(input("Quilowatts:")),float(input("Salario:"))
vqw=sl/7
valortotal=vqw*qw
imposto=valortotal*0.1
desconto=valortotal-imposto
print(f"O valor da conta é de {valortotal:.2f}")
print(f"O valor com desconto é de {desconto:.2f}")
