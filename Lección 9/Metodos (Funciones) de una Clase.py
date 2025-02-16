class Persona:
    def __init__(self, cParamNombre, cParamApellido, iParamEdad):
        self.cNombre = cParamNombre
        self.cApellido = cParamApellido
        self.iEdad = iParamEdad

    def mostrarDetalle(self):
        print(f'Persona: {self.cNombre} {self.cApellido}, {self.iEdad}')

persona1 = Persona(input("Ingresa un nombre: "), input("Ingresa un apellido: "), int(input("Ingresa una edad: ")))
persona1.mostrarDetalle()