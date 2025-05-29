# def saludo(nombre):
#     print(f"Hola {nombre}")
    
# saludo("Nahuel")
# saludo("José")
# saludo("Juan")

notas = [10, 5, 7, 8]
suma = 0

for nota in notas:
    suma += nota
    
promedio = suma / len(notas)
    
print(f"Suma: {suma}")
print(f"Cantidad de notas: {len(notas)}")
print(f"Promedio: {promedio}")

def promedio(notas):
    return sum(notas) / len(notas)

promedio_nahuel = promedio([6, 7, 8, 9])
promedio_juan = promedio([10, 5, 4, 9])

print(f"Promedio de Nahuel: {promedio_nahuel}")
print(F"Promedio de Juan: {promedio_juan}")


