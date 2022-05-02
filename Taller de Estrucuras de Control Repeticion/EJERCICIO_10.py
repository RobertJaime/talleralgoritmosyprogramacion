#entrada
cantidad=int(input("Digite cantidad de estudiantes:"))
altura_mayor=0
for i in range (1,cantidad+1):
    #entrada
    altura=float(input("Digite altura:"))
    #caja negra
    if(altura_mayor<=altura):
        altura_mayor=altura
print(altura_mayor)
