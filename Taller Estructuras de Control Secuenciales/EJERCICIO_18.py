#entradas
capital=float(input("Ingrese la cantidad prestada:"))
pagado=float(input("Ingrese la cantidad pagada:"))
tiempo=int(input("Ingrese el tiempo en años:"))
#caja negra
interes=(pagado-capital)/capital
razon=(interes*100)/(capital*tiempo)
porcentaje_Interes=(capital*tiempo*razon)/100
#salida
print("el porcentaje de interes pagado en un año es de:",porcentaje_Interes)