valor=float(input("Valor"))
v50=valor % 50
valor=valor - v50 * 50
v10=valor % 10
valor=valor -v10 * 10
v1=valor %  1
valor=valor -v1 * 1
print(f"O numero de notas de 50 é {v50}\nO numero de notas de 10 é {v10}\nO numero de notas de 1 é {v1}")
