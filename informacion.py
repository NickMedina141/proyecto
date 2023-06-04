import csv
def menu2():
    pregunta = int(input("\n1. Buscar informacion\n2. Filtrar informacion\n\nEliga una opcion: "))
    if pregunta == 1:
        buscar()
    elif pregunta == 2:
        filtro()
    else:
        print("Error")
        menu2()
def buscar():
    print("Informacion de las personas\n")
    with open("datos_personas.txt","r",encoding= "UTF-8") as f:
        leer = csv.DictReader(f)
        for row in leer:
            print(f"Cedula: {row['cedula']}\nNombre: {row['nombre']}\nEdad: {row['edad']}\nGenero: {row['genero']}\n"
                f"Numero: {row['numero_caballo']}\nCaballo: {row['caballo']}\nDinero: {row['dinero']}\n")
    menu2()
            
def filtro():
    pregunta = int(input("\n1. Masculino\n2. Femenino\n\nEliga una opcion: "))
    if pregunta == 1:
        print("Genero masculino")
        with open("datos_personas.txt","r",encoding= "UTF-8") as k:
            leer = csv.DictReader(k)
            for row in leer:
                if row["genero"] == "masculino":
                    print(f"{row['nombre']}")
        menu2()
    elif pregunta == 2:
        print("Genero femenino")
        with open("datos_personas.txt","r",encoding= "UTF-8") as k:
            leer = csv.DictReader(k)
            for row in leer:
                if row["genero"] == "femenino":
                    print(f"{row['nombre']}")
        menu2()