print("--- BIENVENIDO A LA ARENA ---")
nombre = ""

while not nombre.isalpha():
    nombre = input("Nombre del Gladiador: ")

    if not nombre.isalpha():
        print("Error: Solo se permiten letras.")

print(f"\n=== INICIO DEL COMBATE ===")


vida_jugador = 100      
vida_enemigo = 100      
pociones = 3            
danio_jugador = 15      
danio_enemigo = 12      

juego_activo = True

while juego_activo and vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("  1. Ataque Pesado")
    print("  2. Ráfaga Veloz")
    print("  3. Curar")

    opcion = ""

    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        opcion = input("Elige una opción: ")

        if not opcion.isdigit():
            print(" Ingrese un número válido.")
        
        elif opcion not in ["1", "2", "3"]:
            print(" Ingrese una opción entre 1 y 3.")

opcion = int(opcion)

if opcion == 1:
    if vida_enemigo < 20:
        danio_final = danio_jugador * 1.5
        print(f"¡GOLPE CRÍTICO! Daño multiplicado x1.5")
    else:
        danio_final = danio_jugador

    vida_enemigo = vida_enemigo - int(danio_final)
    print(f"¡Atacaste al enemigo por {int(danio_final)} puntos de daño!")

elif opcion == 2:

    print(">> ¡Inicias una ráfaga de golpes!")
    for golpe in range(3):
        vida_enemigo = vida_enemigo - 5
        print(" > Golpe conectado por 5 de daño")

elif opcion == 3:
        
    if pociones > 0:
        vida_jugador= vida_jugador + 30   # Sumamos 30 HP
        pociones = pociones - 1            # Gastamos 1 poción
        print(f"¡Te curaste! +30 HP. Pociones restantes: {pociones}")
    else:
        print("¡No quedan pociones!")

if vida_enemigo > 0:
        vida_jugador = vida_jugador - danio_enemigo
        print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")

print("=== NUEVO TURNO ===")

if vida_jugador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print(f"\nDERROTA. Has caído en combate.")