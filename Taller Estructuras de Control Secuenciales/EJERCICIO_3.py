#Entrada
sueldo=float(input("Ingrese sueldo base: "))
venta1=float(input("Ingrese valor de la venta:"))
venta2=float(input("Ingrese valor de la venta:"))
venta3=float(input("Ingrese valor de la venta:"))
#caja negra
ventas=(venta1+venta2+venta3)/3
sueldo_total=sueldo+(ventas*0.1)
#salidas
print("El valor de sus comisiones del mes es:",ventas)
print("su sueldo de comisiones mas sus sueldo base es:",sueldo_total)