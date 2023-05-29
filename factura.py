import apuestas
import eleccion_caballo
#caballos_apuesta = [[1,"pegaso"]]
def imprimir_factura(): # esta bien pero revisar para hacerlo mejor 
    print("Resultados de las apuestas")
    print("Informacion de los participantes")
    print(f"Participante {1}:\nCedula: {apuestas.personas[0]['cedula']}\nNombre:  {apuestas.personas[0]['nombre']}\n"
        f"Edad: {apuestas.personas[0]['edad']}\nGenero: {apuestas.personas[0]['sexo']}")
    print(eleccion_caballo.caballos_apuesta)
    print("\nInformacion de las apuestas de los participantes")
    print(f"caballo #{eleccion_caballo.caballos_apuesta[0][0]}: {eleccion_caballo.caballos_apuesta[0][1]}\nDinero apostado: {apuestas.dataApuesta[0][1][1]}")
    

'''def crear_factura():
    factura = {}

    #Información de la factura al usuario
    factura["numero"] = input("Ingrese el número de factura: ")
    factura["fecha"] = input("Ingrese la fecha de la factura: ")
    factura["cliente"] = input("Ingrese el nombre del cliente: ")
    factura["direccion"] = input("Ingrese la localidad del cliente: ")

    #Información de los caballos
    factura["caballos"] = []
    while True:
        caballos = {}

        caballos["nombre"] = input("Ingrese el número del caballo que apostó (o 'fin' para terminar): ")
        if caballos["nombre"] == "fin":
            break

        caballos["precio"] = float(input("Ingrese el valor apostado: "))
        caballos["cantidad"] = int(input("Ingrese la cantidad de veces que apostó: "))

        factura["caballos"].append(caballos)

    return factura


def imprimir_factura(factura):
    print("Factura #: ", factura["numero"])
    print("Fecha: ", factura["fecha"])
    print("Cliente: ", factura["cliente"])
    print("Dirección: ", factura["direccion"])
    print("-----------------------------")
    print("-----------------------------")
    print("Número de caballo\t\tPrecio\tCantidad\tTotal")
    print("-----------------------------")

    total_factura = 0

    for caballos in factura["caballos"]:
        total_ca = caballos["precio"] * caballos["cantidad"]
        total_factura += total_ca

        print("{}\t\t{}\t{}\t\t{}".format(caballos["nombre"], caballos["precio"], caballos["cantidad"], total_ca))

    print("-----------------------------")
    print("Total factura: ", total_factura)

factura = crear_factura()
imprimir_factura(factura)
'''

if __name__ == "__main__":
    imprimir_factura()