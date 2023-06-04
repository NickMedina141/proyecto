from os import system
system("clear")
import apuestas
import factura
import csv
import informacion 

data_administrador = {}

def Iniciar__sesion(data_administrador):
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
            
    data_administrador["cedula"] = Cedula
    data_administrador["nombre"] = Nombre
    print("\nBIENVENIDO ADMINISTRADOR")
    ingreso(data_administrador);return data_administrador
    
def ingreso(data_administrador):
    with open("datos.txt","a",encoding= "UTF-8",newline="") as csv_writer:
        csv_write = csv.writer(csv_writer,quotechar='"')
        csv_write.writerow(data_administrador.values())
#El menu principal
def menu_principal():
    while True:
        print("+--------------------------+")
        print("|-------BIENVENIDOS -------|")
        print("|--------------------------|")
        print("|-------Menu principal-----|")
        print("|--------------------------|")   
        print("|---(1).Iniciar sesión-----|")
        print("|---(2).Datos personales---|")
        print("|---(3).Mostrar datos------|")
        print("|---(4).Apuestas-----------|")
        print("|---(5).Cerrar sesión------|")
        print("+--------------------------+\n")
        
        Opc = int(input("Ingrese una opción: "))
        if Opc == 1:
            Iniciar__sesion(data_administrador)
        elif Opc == 2:
            print(f"\nPersona: {data_administrador['cedula']}\nCedula: {data_administrador['nombre']}")
        elif Opc <= 3:
            informacion.menu2()
        elif Opc == 4:
            apuestas.Solicitar_datos_personales(apuestas.personas,apuestas.num_personas)
        elif Opc == 5:
            print("Has cerrado sesión")
            exit() 
        else:
            print("Error")
            continue
        
if __name__=="__main__":
    menu_principal()