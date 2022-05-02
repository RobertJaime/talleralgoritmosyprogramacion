n=int(input("Ingrese valor de N"))
k=int(input("Ingrese valor de k que sea menor a N"))
c=0
while(n>0 and k>0):
    if(k<n):
        n=n-1
        c=c+1
    else:
        break
print(c)
