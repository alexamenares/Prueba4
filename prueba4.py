import datetime
NORMAL = 1
VIP = 2
PALABRA_CLAVE = "EstoyEnListaDeReserva"
STOCK_MAXIMO = 20
reservas = []

def mostrar_menu():
    print("\nTOTEM AUTOATENCIÓN RESERVA STRIKE")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas")
    print("3.- Ver stock de reservas")
    print("4.- Salir")

def reservar_zapatillas():
    global reservas

    if len(reservas) >= STOCK_MAXIMO:
        print("No hay stock disponible.")
        return
    nombre = input("Ingrese nombre del comprador: ").strip().title()

    for r in reservas:
        if r["nombre"] == nombre:
            print("Este comprador ya tiene una reserva registrada.")
            return
    frase = input("Ingrese la frase secreta: ").strip()
    if frase != PALABRA_CLAVE:
        print("Frase secreta incorrecta. No se pudo realizar la reserva.")
        return
    reservas.append({"nombre": nombre, "pares": 1})
    print(f"Reserva exitosa para {nombre} (1 par de zapatillas).")

def buscar_reserva():
    global reservas
    nombre = input("Ingrese el nombre del comprador a buscar: ").strip().title()
    for r in reservas:
        if r["nombre"] == nombre:
            print(f"Reserva encontrada para {nombre}. Tiene {r['pares']} par(es) reservado(s).")
            if r["pares"] == 2:
                print("Este usuario ya tiene una reserva VIP (2 pares).")
                return
            opcion = input("¿Desea pagar adicional para hacer reserva VIP (2 pares)? (s/n): ").lower()
            if opcion == "s":
                if total_pares_reservados() < STOCK_MAXIMO:
                    r["pares"] = 2
                    print("Reserva VIP realizada exitosamente.")
                else:
                    print("No hay stock suficiente para reserva VIP.")
            else:
                print("No se realizó cambio a VIP.")
            return
    print("No se encontró ninguna reserva con ese nombre.")

def ver_stock():
    total_reservadas = total_pares_reservados()
    print(f"\nTotal de pares reservados: {total_reservadas}")
    print(f"Pares disponibles para reservar: {STOCK_MAXIMO - total_reservadas}")

def total_pares_reservados():
    return sum(r["pares"] for r in reservas)

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                reservar_zapatillas()
            elif opcion == 2:
                buscar_reserva()
            elif opcion == 3:
                ver_stock()
            elif opcion == 4:
                fecha = datetime.datetime.now().strftime("%d/%m/%Y")
                print(f"\nPrograma terminado... Fecha: {fecha}")
                break
            else:
                print("Debe ingresar una opción válida!!")
        except ValueError:
            print("Debe ingresar un número válido!!")

main()
