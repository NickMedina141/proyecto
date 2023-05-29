import datetime,time
import eleccion_caballo
from datetime import datetime
import Finalizando
import time
import random
dataApuesta = [{1:[1,5000]}]
personas = [{
            'cedula': 1234,
            'nombre': "nicolas",
            'edad': 19,
            'sexo': "masculino"}]
def Solicitar_datos_personales():
    while True:
        try:
            num_persona = int(input("Ingrese el número de personas que desean participar: "))
            break
        except:
            print("Solo se leen numeros")

    for i in range(num_persona):
        print("\nIngrese los datos de la persona", i+1)
        print(num_persona)
        while True:
            try:
                Cedula = int(input("Ingrese la cedula: "))
                break
            except:
                print("ERROR solo numeros")
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
                    print("Lo siento no tienes la edad suficiente apara hacer la apuesta")
                    continue
                elif Edad >= 18:
                    print("Puede hacer la apuesta")
                    break
            except:
                print("ERROR solo numeros")
                
        while True: # es necesario?
            try:
                
                print("+---------------------------------+")
                print("|---------ELIJA SU SEXO-----------|")
                print("|---------------------------------|")
                print("|---------(1).MASCULINO-----------|")
                print("|---------(2).FEMENINO------------|")
                print("+---------------------------------+\n")
                
                Sexo = int(input("Ingrese su sexo: "))
                
                if Sexo == 1: # corregir eso
                    print("Masculino")
                    break
                elif Sexo == 2:
                    print("Femenino")
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
    eleccion_caballo.eleccion(eleccion_caballo.caballos_apuesta,eleccion_caballo.dataTime)
    proceso(eleccion_caballo.dataApuesta,eleccion_caballo.dataTime,num_persona)
    return personas,num_persona

def proceso(dataApuesta,dataTime,num_persona):
    print(eleccion_caballo.caballos_apuesta)
    apuestas = {}
    for i in range(num_persona): # toca hacer una excepcion para cada caballo
        caballoF = int(input(f"Participante {i+1} eliga al caballo que desea apostar: "))
        n_apuesta = int(input(f"¿Participante {i+1} Cuanto desea apostar?: "))
        apuestas[i+1] = [caballoF,n_apuesta]
        nows = datetime.now()
        dataTime.append(nows)
    for j in range(1):
        ganador = random.choice(eleccion_caballo.caballos_apuesta)
        print(f"¡¡¡El ganador de la carrera es el caballo  #{ganador[0]} {ganador[1]}!!!")
        time.sleep(1)
    for l in range(num_persona):
        if  apuestas[l+1][0] == ganador:
            print(f"¡¡¡Felicidades Participante {l+1} ha ganado!!!");print(f"Su recompensa fue de: {apuestas[l+1][1]*2}")
        elif apuestas[l+1][0] != ganador:
            print(f"Uy Parcitipante{l+1} parece que haz perdido");print(f"Tu perdida fue: -{apuestas[l+1][1]} ")
            apuestas[l+1][1] - apuestas[l+1][1]
    dataApuesta.append(apuestas)
    Finalizando.menu_principal()
            
if __name__ == "__main__":
    Solicitar_datos_personales()