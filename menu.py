from reserva import reserva
from equipo import equipo
modulo = "0"
reservas={}
codigo_reserva=0
while modulo != "4":
    print("1. Facturacion")
    print("2. Reservas")
    print("3. Equipo")
    print("4. Salir")

    opcion = input("Indique el modulo:")

    if opcion == "1":
        print("facturacion")
        print(reservas)
    elif opcion == "2":
        reservas[codigo_reserva]=reserva()
        print(f"reserva exitosa! #  de reserva:{codigo_reserva}")
        codigo_reserva+=1
    elif opcion == "3":
        ticket= int(input("Cual es su # de reserva?"))
        if  ticket not in reservas:
            print("No existe su reserva!")
            continue 
        equipo(reservas[ticket])
    elif opcion == "4":
        print("Saliendo del programa...")

        
        
    

    