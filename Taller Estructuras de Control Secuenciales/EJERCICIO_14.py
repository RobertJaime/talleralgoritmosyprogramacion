#entrad
lectura1=float(input("Ingrese el valor de la lectura anterior:"))
lectura2=float(input("Ingrese el valor de la entrada actual:"))
vkvatio=float(input("Ingrese el costo por Kilovatio:"))
#caja negra
lectura=lectura2-lectura1
costo=lectura*vkvatio
#salida
print("el monto a pagar por un mes es de:",costo)