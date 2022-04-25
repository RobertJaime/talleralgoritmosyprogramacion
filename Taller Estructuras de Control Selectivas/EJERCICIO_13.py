from datetime import datetime
from re import I
#Saca fecha del sistema
ahora= datetime.now()
año_actual = ahora.year
mes_actual = ahora.month
dia_actual = ahora.day
#Año de nacimento con forma AÑO/MES/DIA
fecha_de_nacimiento=input("Digite fecha de nacimiento:")
año,mes,dia=fecha_de_nacimiento.split("/")
año_de_nacimiento=int(año)
mes_nacimiento=int(mes)
dia_nacimiento=int(dia)
año_de_nacimiento=int(año)
mes_nacimiento=int(mes)
dia_nacimiento=int(dia)
#Calcular edad
zodiaco=""
if((mes_nacimiento==5 and dia_nacimiento>=14) or(mes_nacimiento==6 and dia_nacimiento<=19)):
    zodiaco="Tauro"
elif((mes_nacimiento==6 and dia_nacimiento>=20) or(mes_nacimiento==7 and dia_nacimiento<=20)):
    zodiaco="Geminis"


#Salidas
print(f"su signo es:{zodiaco}")