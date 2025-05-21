print("### STRINGS ###")

nombre = "Nahuel"
edad = 19
saludo = "Hola me llamo {} y tengo {}".format(nombre, edad)

print(saludo)

#///////////////////////////////////////////////

saludo = f"Hola me llamo {nombre} y tengo {edad}"

print(saludo)

a = 10
b = 9
mensaje = f"Hola me llamo {nombre} y tengo {a + b}"

print(mensaje)

#/////////////////////////////////////////////

print("### OPERACIONES CON STRINGS ###")

cadena1 = "Hola"
cadena2 = "Info"

cadena_concatenada = cadena1 + " " + cadena2
print(cadena_concatenada)

cadena = "Hola Mundo"
longitud = len(cadena)
print(longitud)

#/////////////////////////////////////////////

cadena_mayuscula = cadena.upper()
print(cadena_mayuscula)

cadena_minuscula = cadena.lower()
print(cadena_minuscula)
