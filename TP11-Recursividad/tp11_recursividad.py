# EJERCICIO 1: Factorial recursivo

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingresá un número entero positivo: "))
for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}")


# EJERCICIO 2: Serie de Fibonacci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("\nIngresá la posición hasta donde mostrar Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")


# EJERCICIO 3: Potencia recursiva

def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m - 1)

base = int(input("\nIngresá la base: "))
exponente = int(input("Ingresá el exponente: "))
print(f"{base} elevado a {exponente} = {potencia(base, exponente)}")


# EJERCICIO 4: Decimal a binario

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero_decimal = int(input("\nIngresá un número entero positivo para convertir a binario: "))
resultado = decimal_a_binario(numero_decimal)
if resultado == "":
    resultado = "0"
print(f"{numero_decimal} en binario es: {resultado}")


# EJERCICIO 5: Palíndromo recursivo

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = input("\nIngresá una palabra (sin espacios ni tildes): ").lower()
if es_palindromo(palabra):
    print(f'"{palabra}" ES un palíndromo.')
else:
    print(f'"{palabra}" NO es un palíndromo.')


# EJERCICIO 6: Suma de dígitos

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("\nIngresá un número entero positivo para sumar sus dígitos: "))
print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")


# EJERCICIO 7: Contar bloques de pirámide

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

nivel = int(input("\nIngresá el número de bloques del nivel más bajo de la pirámide: "))
print(f"Total de bloques necesarios: {contar_bloques(nivel)}")


# EJERCICIO 8: Contar apariciones de un dígito

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        coincide = 1 if (numero % 10) == digito else 0
        return coincide + contar_digito(numero // 10, digito)

numero = int(input("\nIngresá un número entero positivo: "))
digito = int(input("Ingresá el dígito a buscar (0-9): "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} vez/veces en {numero}.")
