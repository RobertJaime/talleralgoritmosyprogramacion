#Entrada
nota1=float(input("Ingrese calificacion 1:"))
nota2=float(input("Ingrese calificacion 2:"))
nota3=float(input("Ingrese calificacion 3:"))
examen=float(input("Ingrese calificacion de examen:"))
trabajof=float(input("Ingrese claificacion de trabajo final:"))
#caja negra
promedio_calificacion_parcial=(nota1+nota2+nota3)/3
promed=promedio_calificacion_parcial*0.55
calificacion_examen=examen*0.30
calificacion_tabajof=trabajof*0.15
notafinal=promed+calificacion_examen+calificacion_tabajof
#salidas
print("su nota final es:",notafinal)
