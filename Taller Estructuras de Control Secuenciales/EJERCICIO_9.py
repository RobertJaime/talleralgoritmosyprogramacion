#entrada
horas=int(input("Ingrese numero de horas:"))
valor_hora=float(input("Ingrese el valor por hora:"))
sueldob=float(input("Ingrese sueldo base:"))
#caja negra
descuento=sueldob*0.20
salario_neto=horas*valor_hora-descuento
#salida
print("el salario neto es igual a:",salario_neto)