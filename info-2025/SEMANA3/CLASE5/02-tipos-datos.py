print("### TPOS DE DATOS ###")

edad = int(19) #int
print(f"Edad: {edad}, tipo: {type(edad)}")

altura = 1.74 #float
print(f"Altura: {altura}, tipo: {type(altura)}")

z = 2+5j #complex
print(f"Complejo: {z}, Tipo: {type(z)}")

cadena = "Juan" #str
print(f"Nombre: {cadena}, Tipo{type(cadena)}")

verdadero = True #bool
print(f"Bool: {verdadero}, Tipo: {type(verdadero)}")

valor = None #NoneType
print(f"None: {valor}, Tipo: {type(valor)}")

empty_string = "" #str
print(f"None: {empty_string}, Tipo: {type(empty_string)}")

infinito = float("inf") #float
print(f"Infinito: {infinito} Tipo: {type(infinito)}")

lista = ["algo", 19, 22, 45, 0.5, ["otra lista, 02"]] #list (arrays)
print(f"Lista: {lista} Tipo: {type(lista)}")

 #tuple -> Coleccion de elementos ordenados,
 # inmutables y que tiene una longitud fija (no se pueden agregar ni eliminar)
tupla = (10.5, 48.5)
print(f"tupla: {tupla} Tipo: {type(tupla)}")

#Conjunto -> colección de elementos unicos (no se pueden repetir), y no tienen un orden definido, sin embargo si son mutables.
colores = {"azul, rojo, verde"} #set
print(f"Colores: {colores} Tipo: {type(colores)}")


#diccionarios -> es una coleccion de elementos que tienen partes clave-valor (key-value)

estudiante = {
    
        "nombre": "Nahuel",
        "edad": 19,
        "curso": {
            "nombre": "Programacion Web",
            "Iniciales": ["PW", "WP"] 
        }
    }
print(estudiante)