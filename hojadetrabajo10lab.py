#Fabritzio Lopez
# #Ejercicio 1
class Animal:
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre
        self.edad=edad
        self.peso=peso
    def mostrar_datos(self):
        return f"Nombre : {self.nombre}, Edad: {self.edad}, peso: {self.peso}"
    def calcular_dosis(self):
        return "Dosis aún no definida por especie"
    def ficha_medica(self):
        ficha= self.mostrar_datos()
        ficha+= f"\nDosis recomendada:{self.calcular_dosis()}"
        return ficha
            

class Perro(Animal):
    def __init__(self,nombre,edad,peso,raza):
        super().__init__(nombre,edad,peso)
        self.raza = raza
    def calcular_dosis(self):
        return f"{round(self.peso*2.5,2)}mg"
    def ficha_medica(self):
        ficha = super().ficha_medica()
        ficha += f"\nRaza: {self.raza}"
        return ficha
    
        
class Gato(Animal):
    def __init__(self,nombre,edad,peso,color):
        super().__init__(nombre,edad,peso)
        self.color=color
    def calcular_dosis(self):
        return f"{round(self.peso*1.8,2)}mg"
    def ficha_medica(self):
        ficha = super().ficha_medica()
        ficha += f"\nColor: {self.color}"
        return ficha

class Ave(Animal):
    def __init__(self,nombre,edad,peso,plumaje):
        super().__init__(nombre,edad,peso)
        self.plumaje = plumaje
    def calcular_dosis(self):
        return f"{round(self.peso*0.6,2)}mg"
    def ficha_medica(self):
        ficha = super().ficha_medica()
        ficha += f"\nColor de plumaje: {self.plumaje}"
        return ficha
class Reptil(Animal):
    def __init__(self,nombre,edad,peso,tipo):
        super().__init__(nombre,edad,peso)
        self.tipo = tipo
    def calcular_dosis(self):
        return f"{round(self.peso*1.1,2)}mg"
    def ficha_medica(self):
        ficha = super().ficha_medica()
        ficha += f"\nTipo de reptil: {self.tipo}"
        return ficha
perro= Perro("Max",6,15,"Dalmata")
gato= Gato("Miau",2,5,"Negro")
ave = Ave("Paquita",1,2,"Verde")
reptil = Reptil("Donatello",7,1,"Iguana")
print("La ficha medica de los animales son:")
print(perro.ficha_medica())
print()
print(gato.ficha_medica())
print()
print(ave.ficha_medica())
print()
print(reptil.ficha_medica())
#Ejercicio 2 
class Persona:
    def __init__(self,nombre,edad,DNI):
        self.nombre=nombre
        self.edad=edad
        self.DNI=DNI
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.DNI}"

class Estudiante(Persona):
    def __init__(self, nombre, edad, DNI,carrera,semestre):
        super().__init__(nombre, edad, DNI)
        self.carrera=carrera
        self.semestre=semestre
    def mostrar_info(self):
        info= super().mostrar_info()
        info+=f" Carrera: {self.carrera}, Semestre: {self.semestre}"
        return info
class Profesor(Persona):
    def __init__(self, nombre, edad, DNI,curso,seccion):
        super().__init__(nombre, edad, DNI)
        self.curso=curso
        self.seccion=seccion
    def mostrar_info(self):
        info= super().mostrar_info()
        info+=f" Curso: {self.curso}, Seccion: {self.seccion}"
        return info
class Administrativo(Persona):
    def __init__(self, nombre, edad, DNI,area,turno):
        super().__init__(nombre, edad, DNI)
        self.area=area
        self.turno=turno
    def mostrar_info(self):
        info= super().mostrar_info()
        info+=f" Area: {self.area}, Turno: {self.turno}"
        return info
estudiante = Estudiante("Carlos",20,150520,"Ingenieria en sistemas","Segundo")
profesor= Profesor("Maria",45,10010,"Calculo",2)
administrativo= Administrativo("Jose",32,5225101,"Facultad de salud","Matutino")
personas = [estudiante, profesor, administrativo]
for persona in personas:
    tipo = persona.__class__.__name__ 
    print(f"Este es un {tipo}:")
    print(persona.mostrar_info())
    print("-" * 40)
