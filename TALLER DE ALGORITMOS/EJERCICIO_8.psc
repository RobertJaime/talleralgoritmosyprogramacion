Algoritmo minutos_a_horas
	Escribir "Ingrese cantidad de minutos: "
	Leer minutos 
	Hora<-minutos/60
	Horas=trunc(Hora)
	minutos<-(Hora-Horas)*60
	Escribir "la cantidad de horas es: " Horas " hora(s)" 
	Escribir minutos " minutos"
FinAlgoritmo
