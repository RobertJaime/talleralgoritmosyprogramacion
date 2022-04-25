"""
entrada
temperatura en grados fahrenheit---> float--->t
salidas
deporte--->str--->d
"""
#entrada
t=float(input("digite temperatura:"))
#caja negra
d=""
if(t>85 and t<=120):
    d="natación"
elif(t>70 and t<=85):
    d="tenis"
elif(t>32 and t<=70):
    d="golf"
elif(t>10 and t<=32):
    d="esqui"
elif(t>=0 and t<=10):
    d="marcha"
else:
    d="La temperatura no pertenece a ningun deporte"
#salida
print-(f"el deporte que prectica es: {d}")
