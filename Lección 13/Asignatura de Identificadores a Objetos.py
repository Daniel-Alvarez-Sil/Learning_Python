class Persona(object):
    identificador = 0

    @classmethod
    def nextId(cls):
        cls.identificador = cls.identificador + 1
        return cls.identificador

    def __init__(self, cParamNombre, iParamEdad):
        self.iID = self.nextId()
        self.cNombre = cParamNombre
        self.iEdad = iParamEdad

    def __str__(self):
        return f'{self.iID}.- Persona: {self.cNombre}, Edad = {self.iEdad}'


persona1 = Persona(input("Ingresa tu nombre: "), int(input("Ingresa tu edad: ")))
print(persona1)

persona2 = Persona(input("Ingresa tu nombre: "), int(input("Ingresa tu edad: ")))
print(persona2)