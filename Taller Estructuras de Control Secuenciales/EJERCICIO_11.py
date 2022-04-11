#entradas
nombre=str(input("Ingrese el nombre del trabajador: "))
numero_de_horas_trabajadas=int(input("ingrese el numero de horas trabajadas: "))
pago_hora=float(input("ingrese el valor por hora: "))
numero_horas_extras=int(input("Ingrese numero de horas extras: "))
numero_hijos=int(input("cuantos hijos tiene: "))
#caja negra
sueldo_base=(numero_de_horas_trabajadas*pago_hora)
pago_horae=numero_horas_extras*(pago_hora*1.25)
forzosos=(numero_de_horas_trabajadas*pago_hora)*0.05
politica_habitacional=(numero_de_horas_trabajadas*pago_hora)*0.02
caja_ahorros=(numero_de_horas_trabajadas*pago_hora)*0.07
extras=(250000+173000*numero_hijos+180000)

sueldo_neto=(extras+pago_horae+sueldo_base-forzosos-politica_habitacional-caja_ahorros)
asignaciones=pago_horae+extras
deducciones=forzosos+caja_ahorros+politica_habitacional
#salida
print("El trabajador gana un sueldo neto de:",sueldo_neto)
print("El trabajador tiene unas asignaciones de:",asignaciones)
print("Al trabajador se le descuentan unos deducibles de:",deducciones)
