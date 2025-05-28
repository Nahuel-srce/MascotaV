# Ejercicio 1: Gestión de una lista de compras Crea una lista vacía llamada lista_compras
# Luego:
# 1-Agregá 3 productos usando .append() 
# 2- Mostrá cuántos productos hay con len()
# 3- Eliminá el último producto con .pop()
# 4- Mostrá la lista actualizada
# El objetivo es aprender .append(), .pop() y .len()
# lista_compras = []

lista_compras.append("Leche")
lista_compras.append("Pan")
lista_compras.append("Huevos")


print("Cantidad de productos:", len(lista_compras))

producto_eliminado = lista_compras.pop(0)
print("Producto eliminado:", producto_eliminado)

print("Lista actualizada:", lista_compras)