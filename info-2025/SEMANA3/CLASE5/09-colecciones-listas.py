# Se definen con [] y pueden contener cualquier tipo de elementos, incluso otras listas
# Son ordenadas (sus elementos tienen indice) y son mutables (podemos agregar, eliminar o modificar)
       #   0  1  2  3  4
numeros = [1, 3, 6, 2, 5, 4]

# primer elemento
print(numeros[0])

# ultimo elemento
print(numeros[-1])

# sublista (slicing)
print(f"Primeros 3 elementos: {numeros[:3]}")
print(f"Ultimos 2 elementos: {numeros[-2:]}")
print(f"Elementos del medio: {numeros[1:-1]}")

print(f"Longitud de la lista: {len(numeros)}")


print(f"### METODOS ###")


print(f"Cuantas veces aparece el elemento con valor 3: {numeros.count(3)}")

print(f"Cual es el indice con valor 3: {numeros.index(3)}")

numeros.append(6,)
print(f"Lista luego del append: {numeros}")

numeros.insert(0, 8)
print(f"Lista luego del insert: {numeros}")

numeros.pop()
print(f"Lista luego del pop: {numeros}")

numeros.remove(1)
print(f"Lista luego del remove: {numeros}")

numeros.sort()
print(f"Lista luego del sort: {numeros}")

