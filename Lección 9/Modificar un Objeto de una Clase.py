class Persona:
    def __init__(self, cNombre, cApellido, iEdad):
        self.nombre = cNombre
        self.apellido = cApellido
        self.edad = iEdad

persona1 = Persona("Daniel", "Alvarez", 19)
print(f'Persona 1: {persona1.nombre} {persona1.apellido}, {persona1.edad}')

persona1.nombre = input("Ingresa un nombre: ")
persona1.apellido = input("Ingresa un apellido: ")
persona1.edad = int(input("Ingresa una edad: "))

print("Despues de modificar: ")
print(f'Persona 1: {persona1.nombre} {persona1.apellido}, {persona1.edad}')