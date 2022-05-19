usuarios= {
    "iperuana":{
        "nombre":"Iñaki",
        "apellido":"Peruena",
        "Password":"654321"
    },
    "fmuguruza":{
        "nombre":"Fermin",
        "apellido":"Murguruza",
        "password":"654321",
    },
    "aolaizola":{
        "nombre":"Aimar",
        "apellido":"Olaizola",
        "password":"123456",
    }
}
for i in usuarios:
    n=str(input("usuario:"))
    contra=int(input("contraseña:"))
    if(n==i):
        for j in usuarios[i]["password"]:
            if (contra==j):
                print("bien")
                break
            