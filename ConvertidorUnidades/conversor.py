# Convertidor de unidades (KM - MILLAS).

print("Bienvenido al conversor de unidades! Este programa permite convertir de KM a Millas")

while True:
    # Introducimos el numero de km que deseamos convertir a millas
    numero_km = input("Ingrese el numero de kilometros: ")

    # Mediante el metodo .replace() hacemos que se substituya la ',' por '.' en caso de ser introducida.
    numero_km = float(numero_km.replace(",", "."))
    # Realizamos el calculo para pasar de km a millas.
    millas = numero_km * 0.621371

    print("\nMillas", millas)

    opcion = input("Desea realizar otra conversion? PULSE->(y/n): ")

    # Hacemos uso del metodo .lower(), para controlar las mayusculas introducidas. Repetiremos (o no) la operacion.
    if opcion.lower() != "y" and opcion.lower() != "yes":

        print("\n***Cerrando aplicacion - Gracias por usar nuestro conversor de unidades!***")

        break