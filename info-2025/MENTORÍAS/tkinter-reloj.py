import tkinter as tk
import time

ventana = tk.Tk()
ventana.geometry("600x200")
ventana.minsize(200, 100)
ventana.maxsize(600, 200)
ventana.configure(bg="purple")
ventana.title("Reloj")

reloj = tk.Label(ventana, font=("Arial", 60), bg="black", fg="purple")


def hora():
    tiempo_actual = time.strftime("%H:%M:%S")
    reloj.config(text=tiempo_actual)
    
    ventana.after(1000, hora)

reloj.pack()
hora()
ventana.mainloop()