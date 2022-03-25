x,y=int(input("N1:")), int(input("N2:"))
c,cont,b=0,0,0
while x<=y:
    if  x % 2==0:
        print(f"num{x}")
        b=+1
        c=c+1
    x=x+1
print(f"numero:{c} top {b}")

