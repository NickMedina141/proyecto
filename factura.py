import eleccion_caballo
import csv
import principal 

def imprimir_factura(dataApuesta,personas,num_personas):
    datos = {}
    for l in range(num_personas[0]):
        print(f"\nParticipante {l+1}:\nCedula: {personas[l]['cedula']}\nNombre:  {personas[l]['nombre']}\n"
            f"Edad: {personas[l]['edad']}\nGenero: {personas[l]['sexo']}")
    for l in range(num_personas[0]):
        print("\nInformacion de las apuestas de los participantes")
        print(f"caballo #{eleccion_caballo.caballos_apuesta[dataApuesta[0][l+1][0]-1][0]}: {eleccion_caballo.caballos_apuesta[dataApuesta[0][l+1][0]-1][1]}\nDinero apostado: {dataApuesta[0][l+1][1]}")
        datos[l+1] = {"cedula":personas[l]["cedula"],"nombre":personas[l]["nombre"], "edad":personas[l]["edad"], "genero":personas[l]['sexo'],
                    "numero_caballo": eleccion_caballo.caballos_apuesta[dataApuesta[0][l+1][0]][0],
                    "caballo":eleccion_caballo.caballos_apuesta[dataApuesta[0][l+1][0]][1],"dinero": dataApuesta[0][l+1][1]}
    informacion(datos,num_personas)
    return datos

def informacion(datos,num_personas):
    for i in range(num_personas[0]):
        with open("datos_personas.txt","a",encoding= "UTF-8",newline="") as csv_ingreso:
            csv_datos = csv.writer(csv_ingreso,quotechar='"')
            csv_datos.writerow(datos[i+1].values())
    principal.menu_principal()