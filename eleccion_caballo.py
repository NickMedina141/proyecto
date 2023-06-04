from os import system
system("cls")
import lista_caballos
import random

caballos = []
caballos_apuesta = []
def eleccion(caballos_apuesta):
    print("Bienvenidos a la sala de apuestas del Patridonomo")
    print("__Lista de caballos a participiar para la carrera__\n")
    cont = 0
    while True:
        caballo = random.choice(lista_caballos.names_caballos)
        if caballo in caballos:
            continue
        else:
            caballos.append(caballo)  
        if len(caballos) >= 10:
            break
    for i in caballos:
        caballos_apuesta.append([cont+1,i])
        print(f"{cont+1} {caballos_apuesta[cont][1]}")
        cont += 1
    return caballos_apuesta