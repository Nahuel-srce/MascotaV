import tkinter as tk

# CREAR UNA VENTANA
ventana = tk.Tk()
ventana.title("Menú desplegable")
ventana.geometry("400x200")

# CREAR UN MENÚ
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_principal=tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Principal", menu=menu_principal)

submenu = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Opciones", menu=submenu)

def mostrar_mensaje():
    print("Hola desde la terminal")

button = tk.Button(ventana, text="Saludar", command=mostrar_mensaje)
button.pack()

# FUNCION PARA OPCIONES DEL MENÚ

# EJECUTAR ESA FUNCION
submenu.add_command(label="Salir", command=ventana.quit)
submenu.add_command(label="Saludar", command=mostrar_mensaje)


# MOSTRAR LA VENTANA
ventana.mainloop()