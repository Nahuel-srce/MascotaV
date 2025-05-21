numero = int(input("Ingrese un número: \n"))

print(f"--- Tabla de Multiplicar del número {numero} --- \n")
      
for i in range (1, 11):
    calculo = numero * i
    print(f"{numero} x {i} = {calculo}")