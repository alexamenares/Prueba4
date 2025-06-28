PALABRA_CLAVE = "EstoyEnListaDeReserva"
STOCK_MAXIMO = 20
reservas = [] 

def mostrar_menu():
    print("TOTEM AUTOATENCIÓN RESERVA STRIKE")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas")
    print("3.- Ver stock de reservas")
    print("4.- Salir")

def total_pares_reservados():
    return sum(r["pares"] for r in reservas)

def reservar_zapatillas():
    print("Reservar Zapatillas")
    if total_pares_reservados() >= STOCK_MAXIMO:
        print("No hay stock disponible. No se puede hacer más reservas.")
        return
    nombre = input("Nombre del comprador: ").strip().title()

    for r in reservas:
        if r["nombre"] == nombre:
            print("Este comprador ya tiene una reserva registrada.")
            return

    frase = input("Digite la palabra secreta para confirmar la reserva: ").strip()

    if frase != PALABRA_CLAVE:
        print("Error: palabra clave incorrecta. Reserva no realizada.")
        return

    reservas.append({"nombre": nombre, "pares": 1})
    print(f"Reserva realizada exitosamente para {nombre}.")


def buscar_reserva():
    print(" Buscar Zapatillas Reservadas")
    nombre = input("Nombre del comprador a buscar: ").strip().title()

    for r in reservas:
        if r["nombre"] == nombre:
            tipo = "VIP" if r["pares"] == 2 else "estándar"
            print(f"Reserva encontrada: {nombre} - {r['pares']} par(es) ({tipo}).")
            if r["pares"] == 2:
                return

            decision = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").strip().lower()
            if decision in ["s", "si"]:
                if total_pares_reservados() < STOCK_MAXIMO:
                    r["pares"] = 2
                    print(f"Reserva actualizada a VIP. Ahora {nombre} tiene 2 pares reservados.")
                else:
                    print("No hay stock suficiente para actualizar a VIP.")
            else:
                print("Manteniendo reserva actual.")
            return

    print("No se encontró ninguna reserva con ese nombre.")

def ver_stock():
    print(" Ver Stock de Reservas")
    reservados = total_pares_reservados()
    disponibles = STOCK_MAXIMO - reservados
    print(f"Pares reservados: {reservados}")
    print(f"Pares disponibles: {disponibles}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if not opcion.isdigit():
            print("Debe ingresar una opción válida!!")
            continue

        opcion = int(opcion)

        if opcion == 1:
            reservar_zapatillas()
        elif opcion == 2:
            buscar_reserva()
        elif opcion == 3:
            ver_stock()
        elif opcion == 4:
            print("Programa terminado..")
            break
        else:
            print("Debe ingresar una opción válida!!")

main()
