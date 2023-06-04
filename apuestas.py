import eleccion_caballo
import principal
import factura
import time
import random
dataApuesta = []
personas = []
num_personas = []

def Solicitar_datos_personales(personas,num_personas):
    while True:
        try:
            num_persona = int(input("Ingrese el número de personas que desean participar: "))
            break
        except:
            print("Solo se leen numeros")

    for i in range(num_persona):
        print("\nIngrese los datos de la persona", i+1)
        while True:
            try:
                Cedula = int(input("Ingrese la cedula: "))
                break
            except:
                print("Error solo numeros")
        while True:
            Nombre = input("Ingrese su nombre: ")
            if Nombre.isalpha()==True:
                break
            else:
                print("Solo ingresar letras")
                continue
        while True:
            try:
                Edad = int(input("Ingrese su edad: "))
                if Edad <= 17:
                    print("\nLo siento no tienes la edad suficiente apara hacer la apuesta")
                    Solicitar_datos_personales(personas)
                elif Edad >= 18:
                    print("Puede hacer la apuesta")
                    break
            except:
                print("Error solo numeros")
                
        while True:
            try:
                print("+---------------------------------+")
                print("|---------ELIJA SU SEXO-----------|")
                print("|---------------------------------|")
                print("|---------(1).MASCULINO-----------|")
                print("|---------(2).FEMENINO------------|")
                print("+---------------------------------+\n")
                
                Sexo = int(input("Ingrese su sexo: "))
                
                if Sexo == 1:
                    Sexo = "masculino"
                    break
                elif Sexo == 2:
                    Sexo = "femenino"
                    break
                elif Sexo >= 3:
                    print("ERROR")
                    print("Elija los sexos preestablecidos")
            except:
                print("ERROR solo numeros")
        persona = {
            'cedula': Cedula,
            'nombre': Nombre,
            'edad': Edad,
            'sexo': Sexo}
        personas.append(persona)
        num_personas.append(num_persona)
    eleccion_caballo.eleccion(eleccion_caballo.caballos_apuesta)
    proceso(num_persona)
    return personas,num_persona,num_personas 

def proceso(num_persona):
    apuestas = {}
    for i in range(num_persona): 
        while True:
            try:
                caballoF = int(input(f"Participante {personas[i]['nombre']} eliga al caballo que desea apostar: "))
            except ValueError:
                print("Error")
                continue
            if caballoF <= 0 or caballoF >10:
                print(f"Error, eleccion fuera del rango establecido, por favor intentelo de nuevo")
                continue
            else:
                break
        while True:
            try:
                n_apuesta = int(input(f"¿Participante {personas[i]['nombre']} Cuanto desea apostar?: "))
            except ValueError:
                print("Error")
                continue
            if n_apuesta <= 0:
                print(f"Error")
                continue
            else:
                break
            
        apuestas[i+1] = [caballoF,n_apuesta] 
    for j in range(1):
        ganador = random.choice(eleccion_caballo.caballos_apuesta)
        print(f"\n¡¡¡El ganador de la carrera es el caballo  #{ganador[0]} {ganador[1]}!!!")
        time.sleep(1)
    for l in range(num_persona):
        if  apuestas[l+1][0] == ganador[0]:
            print(f"\n¡¡¡Felicidades Participante {personas[l]['nombre']} ha ganado!!!");print(f"Su recompensa fue de: {apuestas[l+1][1]*2}")
        elif apuestas[l+1][0] != ganador[0]:
            print(f"\nUy Parcitipante {personas[l]['nombre']} parece que haz perdido");print(f"Tu perdida fue: -{apuestas[l+1][1]} ")
            apuestas[l+1][1] - apuestas[l+1][1]
    dataApuesta.append(apuestas)
    factura.imprimir_factura(dataApuesta,personas,num_personas)
    return dataApuesta

if __name__ == "__main__":
    Solicitar_datos_personales(personas,num_personas)