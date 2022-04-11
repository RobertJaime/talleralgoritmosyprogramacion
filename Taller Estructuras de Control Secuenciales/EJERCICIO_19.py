#entrada
naranjas=int(input("Ingrese el numero de naranjas:"))
valor=float(input("Ingrese el valor por docena de naranjas:"))
venta=float(input("Ingrese cuando se gano con la venta de todas las naranjas:"))
#caja negra
ganancia=(venta-naranjas/valor)*100
#salida
print("el porcentaje de ganancia es de:",ganancia)
