nombre = input("Ingrese nombre del cliente: ")
while nombre == "" or nombre.isalpha() == False:
    nombre = input("Error. Ingrese solo letras: ")

cantidad = input("Ingrese cantidad de productos: ")
while cantidad == "" or cantidad.isdigit() == False or int(cantidad) == 0:
    cantidad = input("ingrese un número entero mayor a 0: ")

cantidad = int(cantidad)

total_sin_desc = 0
total_con_desc = 0

for i in range(1, cantidad + 1):
    precio = input(f"Ingrese el precio del producto {i}: ")
    while precio == "" or precio.isdigit() == False:
        precio = input("Error. Ingrese un precio válido: ")

    precio = int(precio)

    descuento = input("¿Tiene descuento? (S/N): ").lower()
    while descuento not in ["s", "n"]:
        descuento = input("Error. Ingrese S o N: ").lower()

    total_sin_desc = total_sin_desc + precio
    if descuento == "s":
        precio_con_desc = precio * 0.9  
    else:
        precio_con_desc = precio

    total_con_desc = total_con_desc + precio_con_desc 

ahorro = total_sin_desc - total_con_desc
promedio = total_con_desc / cantidad

print(f"Total sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")