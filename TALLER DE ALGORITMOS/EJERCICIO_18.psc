Algoritmo Iniciales_nombre
	Escribir "escriba Nombre sin apellidos: "
	leer nombre
	Escribir "escribir primer apellido: "
	leer ap1
	escribir"esciribir segundo apellido: "
	leer ap2
	Escribir "nombre completo: " nombre ap1 ap2 
	
	Inicial_nombre<-SubCadena(nombre,1,1)
	Inicial_apellido1<-SubCadena(ap1,1,1)
	Inicial_apellido2<-SubCadena(ap2,1,1)
	Escribir Mayusculas(Inicial_nombre) Mayusculas(Inicial_apellido1) Mayusculas(Inicial_apellido2)
	
	
FinAlgoritmo
