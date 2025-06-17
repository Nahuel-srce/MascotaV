class Vehiculo():
    def __init__(self, param_marca, param_modelo, param_estado):
        self.marca = param_marca           #PUBLICO
        self.modelo = param_modelo         #PUBLICO
        self._estado = param_estado        #PROTEGIDO
        self.__id_vehiculo = "VEH-1"       #PRIVADO
        
    def mostrar_info(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEstado: {self._estado}")
        
        def get_estado(self):
            return self._estado
        
        def set_estado(self, nuevo_estado):
            self._estado = nuevo_estado
   
        
        
v = Vehiculo("Nissan", "350Z", "Nuevo")
v.mostrar_info()
# print(v._Vehiculo__id_vehiculo)