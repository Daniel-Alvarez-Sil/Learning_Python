# NOTA: En Python, no existe la sobrecarga de constructores.
#       Sin embargo, podemos simular esta sobre carga, de la siguiente manera:

class Persona:
    def __str__(self):
        return f'Nombre - {self.cNombre}, Apellido - {self.cApellido}'

    # Constructor de la Clase
    def __init__(self, cParamNombre, cParamApellido):
        self.cNombre = cParamNombre
        self.cApellido = cParamApellido

    # Sobrecarga de Constructores
    @classmethod
    def crearPersonaVacia(cls):
        return cls(None, None) # <-- Esta sintáxis regresa una objeto de Persona con sus atributos establecidos a None

    @classmethod
    def crearPersona(cls, cParamNombre, cParamApellido):
        return cls(cParamNombre, cParamApellido)

persona1 = Persona.crearPersonaVacia()
persona2 = Persona.crearPersona('Daniel', 'Alvarez')

print(f'Persona con Datos Nulos: {persona1}')
print(f'Persona con Datos: {persona2}')