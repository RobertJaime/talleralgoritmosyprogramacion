#entradas
p=float(input("Ingrese el valor de la computadora:"))
t=float(input("Ingrese el valor de cada cuota:"))
#caja negra
total_cuota=t*12
diferencia=total_cuota-p
porcentaje=(diferencia/p)*100
#salida
print(f"El porcentaje de aumento si se paga a cuotas es de: {porcentaje}%")