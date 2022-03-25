n = int(input("Numero positivo:"))
f = 1
while n > 0:
    f *= n
    n -= 1
print(f"Fatorial: {f}")
