a=int(input("ingrese valor de a:"))
b=int(input("a dividido en:"))
c=0
while (a>1):
    if(a!=0 or a!=1):
        a=a-b
        c=c+1
    elif(a==0 or a==1):
        break

print(f"cociente={c} y el resto {a}")