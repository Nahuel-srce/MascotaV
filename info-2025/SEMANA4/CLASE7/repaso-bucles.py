# while True:
#     contador += 1
#     print(f"Hola, hace frio, {contador} veces")


# flag = True
# while flag:
#     print("Hola info, tenfo frio")
#     respuesta = input("Desea continuar? s/n: ")
    
#     if respuesta == "n":
#         flag = False


# while True:
#     print("Hola info, tenfo frio")
#     respuesta = input("Desea continuar? s/n: ")
    
#     if respuesta == "n":
#         break 
        
        
while True:
    print("Hola info, tengo frio")
    respuesta = input("Desea continuar? s/n: ")
    
    if not (respuesta == "s" or respuesta == "n"):
        print("Introduce una respuesta valida")
        continue
        
    if respuesta == "n":
        break
        

        