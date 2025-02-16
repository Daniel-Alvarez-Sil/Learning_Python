class Persona():
    #Atributos de Instancia (Objeto)
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona("Daniel", "Alvarez", 18)
print(f'Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona("Juan", "Perez", "20")
print(f'Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')


