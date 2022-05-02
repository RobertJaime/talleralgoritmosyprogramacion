while True:
    datos=input()
    x,m=datos.split(" ")
    x=int(x)
    m=int(m)
    #Condicion de cierre
    if(x==0 and m==0):
        break
    #caja negra
    r=x*m
    #salida
    print(r)
