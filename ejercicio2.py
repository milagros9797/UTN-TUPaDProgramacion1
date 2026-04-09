usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
max_intentos = 3

while intentos < max_intentos:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido\n")
        break  
    else:
        intentos += 1
        print(f"Credenciales inválidas. Intento {intentos} de {max_intentos}.\n")
if intentos == max_intentos:
    print("Cuenta bloqueada")
else:
    while True:
        print("\n--- MENÚ ---")
        print("1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mostrar mensaje motivacional")
        print("4. Salir")

    
        while True:
            opcion = input("Seleccione una opción del 1 al 4: ")

            if not opcion.isdigit() or not (1 <= int(opcion) <= 4):  
                print("Debe ingresar un número del 1 al 4.Opcion fuera de rango")
                continue  

            opcion = int(opcion)
            break  
            

        if opcion == 1:
            print("Estado de inscripción: Inscripto")
        elif opcion == 2:
            while True:  
                nueva_clave = input("Ingrese la nueva clave (mínimo 6 caracteres): ")
                if len(nueva_clave) < 6:
                    print("La clave debe tener al menos 6 caracteres.")
                    continue 
                confirmacion = input("Confirme la nueva clave: ")
                if nueva_clave != confirmacion:
                    print("Las claves no coinciden, intente nuevamente.")
                    continue  
                clave_correcta = nueva_clave  
                print(f"Clave cambiada exitosamente.Tu nueva clave es :{clave_correcta}")
                break 

        elif opcion == 3:
            print("¡Sigue adelante!")
        elif opcion == 4:
            print("Saliendo del sistema. ¡Hasta luego!")
            break 