from os import system
system("clear")
import apuestas
import factura
persona = []

'''def Mostrar_datos():
    
    print("\nDatos personales ingresados:")
    for i, persona in enumerate(personas):
        print("\nPersona", i+1)
        print("|Cedula:|",persona['cedula'])
        print("|Nombre:|", persona['nombre'])
        print("|Edad:|", persona['edad'])
        print("|Sexo:|",persona['sexo'])
'''
#Iniciar sesión
def Iniciar__sesion(persona):
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
            
    persona.append([Cedula,Nombre])
    print(persona)# quitar
    print("\nBIENVENIDO ADMINISTRADOR")
    menu_principal() 
    return persona
    

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
            Iniciar__sesion(persona)
        elif Opc == 2: # revisar, cuando voy al archivo de apuesta y vuelvo aqui la informacion se borra
            if len(persona) > 0:
                print(f"Persona: {persona[0][1]}\nCedula: {persona[0][0]}")
            else:
                print("No te has regirtrado")
                Desea = input("¿Deseas registrarte?  si/no: ")
                if Desea == "si":
                    Iniciar__sesion(persona)

                elif Desea == "no":
                    print("NO podra realizarse la apuesta")
                    exit()
            
        elif Opc <= 3:
            if len(persona) > 0:
                factura.imprimir_factura()
            else:
                print("No hay personas registradas")
                menu_principal()
            
        elif Opc == 4:
            apuestas.Solicitar_datos_personales()
        elif Opc >= 5:
            print("Has cerrado sesión")
            exit() 
        
if __name__=="__main__":
    menu_principal()
