numeros = [10,111,32,3,4,34,3,99,3,3]
num=int(input("numero:"))
c=0
for x in numeros:
    if x == num:
        c +=1

print(f"{c}")
