class Vehiculos:
    def __init__(self, param_marca, param_modelo, param_estado, param_color):
        self.marca = param_marca
        self.modelo = param_modelo
        self.estado = param_estado
        self.color = param_color

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Estado: {self.estado}, Color: {self.color}")
        
        
class Auto(Vehiculos):
    def __init__(self, param_marca, param_modelo, param_estado, param_color, param_numero_puertas):
        super().__init__(param_marca, param_modelo, param_estado, param_color)
        self.numero_puertas = param_numero_puertas

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, de {self.numero_puertas}, Estado: {self.estado}, Color: {self.color}")
    
    
moto = Vehiculos("Yamaha", "Fz16", "excelente", "Azul") 
auto = Auto("Nissan", "350Z", "nuevo", "Naranja", "5 puertas")
camion = Vehiculos("Mercedez", "1114", "se defiende", "Blanco")


moto.mostrar_info()
auto.mostrar_info()
camion.mostrar_info()