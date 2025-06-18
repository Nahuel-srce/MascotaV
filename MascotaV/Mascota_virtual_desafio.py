import random
from mascota import imagen


class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = random.randint(30, 60)
        self.felicidad = 0
        self.salud = 100
        self.viva = True

        self.imagen = imagen.inicio
        self.imagen_triste = imagen.triste
        self.imagen_muerto = imagen.muerto
        self.imagen_disgustado = imagen.disgustado
        self.imagen_feliz = imagen.feliz
        self.durmiendo = imagen.durmiendo

    def verificar_estado(self):
        if self.salud <= 0:
            self.salud = 0
            self.viva = False
            print(self.imagen_muerto)
            print(f"💀 {self.nombre} ha muerto por falta de cuidado...")

    def alimentar(self):
        if not self.viva:
            print("⚰️ No puedes alimentar a una mascota que ha fallecido.")
            return

        if self.hambre >= 95:
            print(self.imagen_disgustado)
            print(f"{self.nombre} está lleno, no puede comer más...")
        else:
            aumento = random.randint(10, 15)
            self.hambre += aumento
            if self.hambre > 100:
                self.hambre = 100

            mejora = random.randint(5, 10)
            self.salud += mejora
            if self.salud > 100:
                self.salud = 100

            print(self.imagen_feliz)
            print(f"{self.nombre} ha sido alimentado (+{aumento} de comida)!")
            print(f"🍽️ Salud +{mejora} → Salud actual: {self.salud}")
            print(f"🥗 Hambre actual: {self.hambre}")

        self.verificar_estado()

    def jugar(self):
        if not self.viva:
            print("💔 No puedes jugar con una mascota muerta...")
            return

        print("\n🎮 Vamos a jugar a 'Adivina el Número'!")
        secreto = random.randint(1, 5)
        try:
            intento = int(input("Adivina un número del 1 al 5: "))
            if intento == secreto:
                self.felicidad += 10
                if self.felicidad > 100:
                    self.felicidad = 100
                print(self.imagen_feliz)
                print(f"🎉 Acertaste! Felicidad +10 (Actual: {self.felicidad})")
            else:
                self.salud -= 5
                if self.salud < 0:
                    self.salud = 0
                print(self.imagen_triste)
                print(f"Fallaste... era {secreto}. Salud -5 (Actual: {self.salud})")
        except ValueError:
            print("⚠ï¸ Ingresá un número válido!")

        self.verificar_estado()

    def sanar(self):
        if not self.viva:
            print("💀 No puedes sanar a una mascota muerta...")
            return

        if self.salud >= 100:
            print(f"{self.nombre} ya está completamente sano.")
        else:
            recuperacion = random.randint(10, 20)
            self.salud += recuperacion
            if self.salud > 100:
                self.salud = 100
            print(f"💊 {self.nombre} ha sido curado. Salud actual: {self.salud}")

    def estado_animo(self):
        if not self.viva:
            print(self.imagen_muerto)
            print(f"{self.nombre} ha fallecido. 😔")
            return

        if self.hambre >= 90:
            estado_hambre = "lleno"
        elif self.hambre <= 30:
            estado_hambre = "hambriento"
        else:
            estado_hambre = "normal"

        print(f"🧰 Estado de {self.nombre}:")
        print(f"🥗 Hambre: {self.hambre} ({estado_hambre})")
        print(f"🎉 Felicidad: {self.felicidad}")
        print(f"❤️ Salud: {self.salud}")

    def prender_luz(self):
        if not self.viva:
            print("⚰️ Tu mascota no puede despertar… ha fallecido.")
            return

        print(f"{self.nombre} despertó! ¿Cómo estará?")
        self.felicidad = random.randint(0, 10)
        self.hambre = random.randint(0, 10)

        if self.hambre <= 5:
            print(self.imagen_disgustado)
            print(f"{self.nombre} tiene hambre!")
        elif self.hambre >= 8:
            print(self.imagen_feliz)
            print(f"{self.nombre} está satisfecho!")
        else:
            print(self.imagen)
            print(f"{self.nombre} quisiera comer algo")

    def apagar_luz(self):
        if not self.viva:
            print("⚰️ Ya está descansando en paz...")
            return

        print(self.durmiendo)
        while True:
            self.felicidad = 5
            self.hambre = 5
            print(f"{self.nombre} está durmiendo... 🛌")
            respuesta = input("¿Desea volver al menú? (s/n): ")
            if respuesta.lower() == 's':
                break
            else:
                print("El carpincho sigue durmiendo...")

    def presentacion(self):
        print(
            f"\n╔══════════════════════════════════════╗\n║ Te presento a tu mascota!          ║\n╚══════════════════════════════════════╝\n{self.imagen}\tSu nombre es {self.nombre}"
        )

    def despedida(self):
        print(
            f"\n╔══════════════════════════════════════╗\n║ Nos vemos!                         ║\n╚══════════════════════════════════════╝\n{self.imagen}\n╔══════════════════════════════════════╗\n║ Juguemos otro día!                 ║\n╚══════════════════════════════════════╝\n"
        )


# Interfaces visuales
interfaz_inicio = "\n╔══════════════════════════════════════╗\n║       Bienvenido a tu primera      ║\n║          mascota virtual!          ║\n╚══════════════════════════════════════╝\n"

interfaz_juego = """
╔══════════════════════════════════════╗
║       Opciones disponibles:          ║
║                                      ║
║ 1 - Alimentar                        ║
║ 2 - Jugar                            ║
║ 3 - Sanar                            ║
║ 4 - Mostrar información              ║
║ 5 - Apagar luz (dormir)              ║
║ 6 - Prender luz (despertar)          ║
║ 7 - Salir                            ║
║                                      ║
╚══════════════════════════════════════╝
"""

# Inicio del juego
print(interfaz_inicio)
nombre = input("Elije un nombre para tu mascota: ")
mascota = MascotaVirtual(nombre)
mascota.presentacion()

while True:
    if not mascota.viva:
        print("Fin del juego. Tu mascota ha muerto. 🙏")
        break

    print(interfaz_juego)
    try:
        opcion = int(input("Elija una opción: "))
        if opcion == 1:
            mascota.alimentar()
        elif opcion == 2:
            mascota.jugar()
        elif opcion == 3:
            mascota.sanar()
        elif opcion == 4:
            mascota.estado_animo()
        elif opcion == 5:
            mascota.apagar_luz()
        elif opcion == 6:
            mascota.prender_luz()
        elif opcion == 7:
            mascota.despedida()
            break
        else:
            print("❌ Opción no válida.")
    except ValueError:
        print("❗ Por favor ingrese un número válido.")
