# Ejercicio 3: Diccionario de estudiante
# Dado este diccionario:
# estudiante = {
#     "nombre": "Ana",
#     "edad": 20,
#     "materias": ["Matemática", "Historia"]
# }
# 1- Mostrá el nombre y la edad
# 2-Agregá una materia nueva a la lista materias
# 3- Mostrá cuántas materias cursa con len()
# 4- Usá .get() para obtener la clave “promedio” con valor por defecto 0 


estudiantes = {
    "nombre": "Ana",
    "edad": "20",
    "materias": ["Matemática", "Historia"]
}

print("Nombre:", estudiantes["nombre"])
print("Edad:", estudiantes["edad"])

estudiantes["materias"].append("Plástica")
print("Tu diccionario ahora quedó así:", estudiantes)

cantidad_materias = len(estudiantes["materias"])
print("La cantidad de materias es:", cantidad_materias)