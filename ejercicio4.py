energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
intentos_forzar = 0

nombre = input("Ingrese el nombre del agente: ")
while not nombre.isalpha():
    nombre = input("Ingrese solo letras: ")
print(f"\nBienvenido, agente {nombre}.\n")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:


    print("\n--- ESTADO ACTUAL ---")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {'ON' if alarma else 'OFF'}")
    print(f"Código parcial: {codigo_parcial}")

    print("\n1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")

    opcion = input("Seleccione una opción: ")

    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        opcion = input(" Seleccione 1, 2 o 3: ")

    opcion = int(opcion)

    if opcion !=1: 
        intentos_forzar = 0

    if opcion == 1:
        intentos_forzar += 1

        energia -= 20
        tiempo -= 2

        if intentos_forzar == 3:
            alarma = True
            print("Forzaste 3 veces seguidas.se activó la alarma.")
            continue

        if energia < 40:
            riesgo = input("Elegí un número del 1 al 3: ")

            while not riesgo.isdigit() or int(riesgo) not in [1, 2, 3]:
                riesgo = input("Elegí 1, 2 o 3: ")

            if int(riesgo) == 3:
                alarma = True
                print("Se activó la alarma")

        if not alarma:
            cerraduras_abiertas += 1
            print("Abriste una cerradura.")
        
    elif opcion == 2:
        energia -= 10
        tiempo -= 3

        print("Iniciando hackeo.")
        for i in range(4):
            print(f"Paso {i+1}/4")
            codigo_parcial += "A"  

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Se abrió una cerradura.")   

    
    elif opcion == 3: 

        energia += 15
        tiempo -= 1

        if energia > 100:
            energia = 100  

        if alarma:
            energia -= 10  

        print("Descansaste y recuperaste energía.")


    if cerraduras_abiertas == 3:
        print("\n¡VICTORIA!")
        break
    elif energia <= 0:
        print("\nDERROTA")
        break
    elif tiempo <= 0:
        print("\nDERROTA")
        break
    elif alarma :
        print("\nDERROTA. bloqueo")
        break