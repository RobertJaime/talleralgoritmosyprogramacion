import math
"""
ENTRADA
A-->float-->a
B-->float-->b
C-->float-->c
SALIDAS
x1-->float-->x1
x2..>gloat.._x2
"""
#entrada
a=float(input("Digite A:"))
b=float(input("Digite B:"))
c=float(input("Digite C:"))
#caja negra
d=b**2-(4*a*c)
x1=0.0
x2=0.0
if(d>0):
    x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
elif(d==0):
    x1=x2=-b/(2*a)
else:
    x1="no tiene solución en los Reales"

#salida
print(f"el resultado es {x1}")