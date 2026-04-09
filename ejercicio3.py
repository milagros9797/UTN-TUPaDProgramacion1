lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

while True:
    operador = input("Ingrese el nombre del operador: ")
    if operador.isalpha():
        break
    else:
        print("Error: solo se permiten letras.")

while True:
    print("\n--- MENÚ ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Seleccione una opción del 1 al 5: ")

    if opcion == "1":
        while True:
            dia = input("ingrese el día :lunes o martes ").lower() 
            if dia == "lunes":
                dia_num = "1"
                break
            elif dia == "martes":
                dia_num = "2"
                break
            else:
                print("Ingrese 'lunes' o 'martes'.")

        while True:
            paciente = input("Ingrese nombre del paciente: ")
            if paciente.isalpha():
                break
            else:
                print("solo se permiten letras.")

        if dia_num == "1":  
            if (paciente.lower() == lunes1.lower() or
            paciente.lower() == lunes2.lower() or
            paciente.lower() == lunes3.lower() or
            paciente.lower() == lunes4.lower()):
                print(f"el paciente :{paciente }  ya tiene turno el dia lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print(f"Turno 1 reservado para {paciente} el dia lunes")
            elif lunes2 == "":
                lunes2 = paciente
                print(f"Turno 2 reservado para {paciente} el dia lunes ")
            elif lunes3 == "":
                lunes3 = paciente
                print(f"Turno 3 reservado para {paciente} el dia lunes")
            elif lunes4 == "":
                lunes4 = paciente
                print(f"Turno  4 reservado para {paciente} el dia lunes ")
            else:
                print("Agenda del lunes completa.")

        elif dia_num == "2":  
            if (paciente.lower() == martes1.lower() or
            paciente.lower() == martes2.lower() or
            paciente.lower() == martes3.lower()):
                print(f"El paciente {paciente} ya tiene turno el día martes.")
            elif martes1 == "":
                martes1 = paciente
                print(f"Turno 1 reservado para {paciente} el día martes")
            elif martes2 == "":
                martes2 = paciente
                print(f"Turno 2 reservado para {paciente} el día martes")
            elif martes3 == "":
                martes3 = paciente
                print(f"Turno 3 reservado para {paciente} el día martes")
            else:
                print("Agenda del martes completa.")

    elif opcion == "2":
        while True:
            dia = input("Ingrese el día para cancelar turno (lunes/martes): ").lower()
            if dia == "lunes":
                dia_num = "1"
                break
            elif dia == "martes":
                dia_num = "2"
                break
            else:
                print("Error: ingrese 'lunes' o 'martes'.")

        while True:
            paciente = input("Ingrese el nombre del paciente a cancelar: ")
            if paciente.isalpha():
                break
            else:
                print("ingrese el nombre, solo se permiten letras.")

        if dia_num == "1":  
            if paciente.lower() == lunes1.lower():
                lunes1 = ""
                print(f"Turno 1 el dia lunes de :{paciente} cancelado")
            elif paciente.lower() == lunes2.lower():
                lunes2 = ""
                print(f"Turno 2 el dia lunes de: {paciente} cancelado")
            elif paciente.lower() == lunes3.lower():
                lunes3 = ""
                print(f"Turno 3 el dia lunes de:{paciente} cancelado")
            elif paciente.lower() == lunes4.lower():
                lunes4 = ""
                print(f"Turno 4 el dia lunes de: {paciente} cancelado")
            else:
                print(f"No se encontró al paciente {paciente} en el dia Lunes.")

        elif dia_num == "2":
            if paciente.lower() == martes1.lower():
                martes1 = ""
                print(f"Turno de {paciente} cancelado en Martes, Turno 1")
            elif paciente.lower() == martes2.lower():
                martes2 = ""
                print(f"Turno de {paciente} cancelado en Martes, Turno 2")
            elif paciente.lower() == martes3.lower():
                martes3 = ""
                print(f"Turno de {paciente} cancelado en Martes, Turno 3")
            else:
                print(f"No se encontró al paciente {paciente} en el día martes.")

    elif opcion == "3":
        while True:
            dia = input("Ingrese el lunes o martes para ver la agenda.").lower()
            if dia == "lunes":
                dia_num = "1"
                break
            elif dia == "martes":
                dia_num = "2"
                break
            else:
                print("ingrese 'lunes' o 'martes'.")

        print(f"\n--- Agenda del día {dia} ---")
        if dia_num == "1":  
            if lunes1 != "":
                print(f"Turno 1: {lunes1}")
            else:
                print("Turno 1: (libre)")

            if lunes2 != "":
                print(f"Turno 2: {lunes2}")
            else:
                print("Turno 2: (libre)")

            if lunes3 != "":
                print(f"Turno 3: {lunes3}")
            else:
                print("Turno 3: (libre)")

            if lunes4 != "":
                print(f"Turno 4: {lunes4}")
            else:
                print("Turno 4: (libre)")

        elif dia_num == "2":  
            if martes1 != "":
                print(f"Turno 1: {martes1}")
            else:
                print("Turno 1: (libre)")

            if martes2 != "":
                print(f"Turno 2: {martes2}")
            else:
                print("Turno 2: (libre)")

            if martes3 != "":
                print(f"Turno 3: {martes3}")
            else:
                print("Turno 3: (libre)")


    elif opcion == "4":
        libres_lunes = 0
        if lunes1 == "": libres_lunes += 1
        if lunes2 == "": libres_lunes += 1
        if lunes3 == "": libres_lunes += 1
        if lunes4 == "": libres_lunes += 1
        ocupados_lunes = 4 - libres_lunes 

        libres_martes = 0
        if martes1 == "": libres_martes += 1
        if martes2 == "": libres_martes += 1
        if martes3 == "": libres_martes += 1
        ocupados_martes = 3 - libres_martes  

        if ocupados_lunes == 0 and ocupados_martes == 0:
            dia_mas_turnos = "no hay dia con turnos ocupados"
        elif ocupados_lunes > ocupados_martes:
            dia_mas_turnos = "Lunes"
        elif ocupados_martes > ocupados_lunes:
            dia_mas_turnos = "Martes"
        else:
            dia_mas_turnos = "Empate"
        print("\n--- Resumen General ---")
        print(f"Lunes: {ocupados_lunes} turnos ocupados, {libres_lunes} libres")
        print(f"Martes: {ocupados_martes} turnos ocupados, {libres_martes} libres")
        print(f"Día con más turnos ocupados: {dia_mas_turnos}")


    elif opcion == "5":
        print("Cerrando sistema...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")