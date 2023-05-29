from os import system
system("cls")
import lista_caballos;import random
import apuestas
from datetime import date, time, datetime
import time

dataApuesta = []
dataTime = []
caballos_apuesta = []

def eleccion(caballos_apuesta,dataTime):
    print("Bienvenidos a la sala de apuestas del Patridonomo")
    print("__Lista de caballos a participiar para la carrera__\n")
    cont = 0
    while True:
        caballo = random.choice(lista_caballos.names_caballos)
        if caballo in caballos_apuesta:
            continue
        else:
            caballos_apuesta.append([cont+1,caballo])
        print(f"{cont+1} {caballos_apuesta[cont][1]}")
        cont += 1    
        if len(caballos_apuesta) >= 10:
            break
    return caballos_apuesta