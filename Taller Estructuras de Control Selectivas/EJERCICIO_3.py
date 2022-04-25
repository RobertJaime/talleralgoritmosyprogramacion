"""
ENTRADAS
A-->int-->a
B-->int-->b
C-->int-->c
D-->int-->d
resultado-->int-->r
"""
#ENTRADA
a=int(input("Ingrese el valor de A:"))
b=int(input("Ingrese el valor de B:"))
c=int(input("Ingrese el valor de C:"))
d=int(input("Ingrese el valor de D:"))
#caja negra

if(d==0):
    r=((a-c)**2 )
else:
    r=((a-b)**3)/d
#salida
print(f"la solucion es {r}")
