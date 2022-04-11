#Entradas
chelines_austriacos=float(input("Ingrese cantidad de chelines austriacos:"))
dracmas_griegos=float(input("Ingrese cantidad de dracmas griegos:"))
pesetas=float(input("Ingrese cantidad de pesetas:"))
#caja negra
pesetas1=chelines_austriacos*9.56871
pesetas2=dracmas_griegos*0.88607
fancos_frances=pesetas2/20.110 
dolares=pesetas/122.499
libras_italaiana=pesetas/0.09289
#salida
print("El cambio de Chelines Austriacos a Pesetas es de:",pesetas1)
print("El cambio de Dracmas Griegos a Francos franceses se de:",fancos_frances)
print("El cambio de Pesetas a Dolares es de:",dolares)
print("El cambio de Pesetas a Libras Italianas es de:",libras_italaiana)