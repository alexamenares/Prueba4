import datetime
NORMAL = 1
VIP = 2
Palabra_clave = "EstoyEnLaListaDeReserva"
zapatillas = 20
stock_zapatillas = []
compradores = []

for numero in range(1, 21): 
        zapallitas = {
            "codigo": f"{VIP or NORMAL}",
            "disponible": True,
            "nombre": "",
            "rut": "",
        }
        stock_zapatillas.append (zapatillas)

#menu
while True:
        try:
            def menu():
                print(" Bienvenido a Totem autoatención reserva strike ")
                print("1. Reservar zapatillas")
                print("2. Buscar zapatillas reservadas")
                print("3. Ver stock de reservas")
                print("4. Salir")
                opcion = int(input("Ingrese su opción"))
                
#stock de zapatillas
            def stock_d_zapatillas():
                print("\n zapatillas disponibles:")
                contador = 0
                for zapatillas in stock_zapatillas:
                 estado = "X" if not zapatillas["disponible"] else tipo["codigo"]
                print(f"{estado:<8}", end=" ")
                contador += 1
                if contador % 4 == 0:
                    print()   
                    
#reserva zapatillas
            def reserva_zapatillas():
                stock_d_zapatillas()
                codigo = input("\nIngrese cuantas zapatillas desea:(Vip = 2 o NORMAL=1) ").upper()
            for zapatillas in stock_zapatillas:
                if zapatillas == VIP or NORMAL:
                  if not zapatillas["disponible"]:
                    print(" no disponible.")
                nombre = input("Ingrese nombre: ").strip().title()
                rut = input("Ingrese RUT (sin puntos ni guion): ").strip()
                palabra_clave = str(input("ingrese la palabra_clave"))
                if palabra_clave == palabra_clave:
                    confirmar = input(f"Confirma la reserva por {zapatillas}? (s/n): ").lower()
                    if confirmar == "s":
                        zapatillas["disponible"] = False
                        zapatillas["nombre"] = nombre
                        zapatillas["rut"] = rut
                    print(" ¡Reserva realizada con éxito!")
                else:
                    print("Reserva cancelada.")
                
#lista_d_reservas_totales
            def reservas_totales():   
                print("\n Compradores agendados (ordenados por RUT):")
                compradores = [(a["rut"], a["nombre"], a["codigo"]) for a in stock_d_zapatillas if not a["disponible"]]
                if not compradores:
                     print("No hay compradores registrados.")
                return
                for rut, nombre, codigo in sorted(compradores):
                         print(f"RUT: {rut} | Nombre: {nombre} | cantidad de zapatillas reservadas: {codigo}")

#consecuencias de opciones
            def main():
                while True:
                    menu()
                    try:
                        opcion = int(input("Seleccione una opción: "))
                        if opcion == 1:
                            reserva_zapatillas()
                        elif opcion == 2:
                            reservas_totales()
                        elif opcion == 3:
                            stock_d_zapatillas()
                        elif opcion == 4:
                            fecha = datetime.datetime.now().strftime("%d/%m/%Y")
                            print(f"\nSistema cerrado por Alexa Menares. Fecha: {fecha}")
                        else:
                            print(" Opción inválida. Intente nuevamente.")
                    except ValueError:
                        print(" Debes ingresar un número válido.")
                        
        except ValueError:
            print("Ingrese nuevamente su opción")


main()



IA = 300
cuposIA = []
ROBOT = 300
cuposROBOT = []

def validar_codigo_ia(codigo):
    return (
        len(codigo) >= 6 and
        any(c.isdigit() for c in codigo) and
        any(c.islower() for c in codigo) and
        ' ' not in codigo
    )

def validar_codigo_robot(codigo):
    return (
        len(codigo) >= 5 and
        sum(1 for c in codigo if c.isupper()) >= 2 and
        any(not c.isalnum() for c in codigo) and
        ' ' not in codigo
    )

def inscribir_ia():
    global IA
    if IA <= 0:
        print("No hay más cupos para 'IA para todos'.")
        return

    nombre = input("Ingrese su nombre: ")
    if nombre in cuposIA:
        print("Error: El nombre ya está inscrito.")
        return

    tipo = input("Escriba 'EST' si es estudiante o 'PROF' si es profesional: ").upper()
    if tipo not in ['EST', 'PROF']:
        print("Tipo de inscripción no válido.")
        return

    codigo = input("Ingrese su código de acceso: ")
    if not validar_codigo_ia(codigo):
        print("Código inválido: mínimo 6 caracteres, 1 número, 1 minúscula y sin espacios.")
        return

    cuposIA.append(nombre)
    IA -= 1
    print("¡Inscripción exitosa a charla 'IA para todos'!")

def inscribir_robot():
    global ROBOT
    if ROBOT <= 0:
        print("No hay más cupos para 'Robots en la vida diaria'.")
        return

    nombre = input("Ingrese su nombre: ")
    if nombre in cuposROBOT:
        print("Error: El nombre ya está inscrito.")
        return

    tipo = input("Escriba 'INV' si es investigador o 'ENT' si es empresario: ").upper()
    if tipo not in ['INV', 'ENT']:
        print("Tipo de inscripción no válido.")
        return

    codigo = input("Ingrese su código de acceso: ")
    if not validar_codigo_robot(codigo):
        print("Código inválido: mínimo 5 caracteres, 2 mayúsculas, 1 símbolo y sin espacios.")
        return

    cuposROBOT.append(nombre)
    ROBOT -= 1
    print("¡Inscripción exitosa a charla 'Robots en la vida diaria'!")

def ver_cupos():
    print(f"Cupos disponibles para 'IA para todos': {IA}")
    print(f"Cupos disponibles para 'Robots en la vida diaria': {ROBOT}")

def main():
    while True:
        print("\nBIENVENIDO A LA FERIA TECNOLÓGICA FUTURETEC 2025")
        print("1.- Inscribirse a charla 'IA para todos'.")
        print("2.- Inscribirse a charla 'Robots en la vida diaria'.")
        print("3.- Ver cupos disponibles para ambas charlas.")
        print("4.- Salir.")

        try:
            opcion = int(input("Elija una opción: "))
            if opcion == 1:
                inscribir_ia()
            elif opcion == 2:
                inscribir_robot()
            elif opcion == 3:
                ver_cupos()
            elif opcion == 4:
                print("Sistema cerrado. ¡Gracias por participar en FUTURETEC!")
                break
            else:
                print("Debe seleccionar una opción válida!")
        except ValueError:
            print("Debe ingresar un número válido.")

main()