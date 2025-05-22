#Ejercicio 2: Contar apariciones
#Dada la lista:
#Colores = ["rojo"]
#1- Mostrá cuantas veces aparece "rojo" usando .coun()
#Remplazá el primer verde por amarillo
#Mostrá la lista final

colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo", "rojo"]

cantidad_rojo = colores.count("rojo")

print("La cantidad de veces que se repite rojo es: ", cantidad_rojo)

indice_primer_verde = colores.index("verde")
colores[indice_primer_verde] = "Amarillo"

print("Colores finales: ", colores)