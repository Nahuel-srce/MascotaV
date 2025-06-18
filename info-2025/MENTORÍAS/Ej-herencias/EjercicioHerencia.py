class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def nombre_completo(self):
        return f"Su nombre completo es: {self.nombre} {self.apellido}"
    
    
class Estudiante(Persona):
    def __init__(self, nombre, apellido, carrera):
        super().__init__(nombre, apellido)
        self.carrera = carrera
            
    def getCarrera(self):
        return f"Está estudiando: {self.carrera}"
    
    
# persona1 = Persona("Nahuel", "Storace")
Estudiante1 = Estudiante("Nahuel", "Storace", "Desarrollo Web")
print(Estudiante1.nombre_completo())
print(Estudiante1.getCarrera())