#entrada
pagado=float(input("Ingrese el valor pagado por el producto:"))
valor=float(input("Ingrese el precio de venta al publico:"))
#caja negra
diferencia=valor-pagado
descuento=(diferencia/valor)*100
#salida
print(f"El descuento efectuado al producto es de: {descuento} %")