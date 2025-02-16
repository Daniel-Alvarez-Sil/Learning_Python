class Persona:
    def __init__(self, cParamNombre, cParamApellido, iParamEdad): #Podemos utilizar "this" en lugar de "self"
        self.cNombre = cParamNombre
        self.cApellido = cParamApellido
        self.iEdad = iParamEdad

    def imprimirDetalle(this):
        print(f'Persona: {this.cNombre} {this.cApellido}, {this.iEdad}')

persona1 = Persona(input("Ingresa el nombre: "), input("Ingresa el apellido: "), int(input("Ingresa la edad: ")))

#Cualquiera de las 2 siguientes sintaxis es correcta
persona1.imprimirDetalle()
Persona.imprimirDetalle(persona1)

#Creacion de un atributo dinamico
#Este atributo dinamico es exclusivo del objeto al que se le aplica
#El atributo dinamico no estara disponible para otros objetos

persona1.cTelefono = "55-7839-5839"
print(f'Atributo Dinamico, telefono: {persona1.cTelefono}')


persona2 = Persona(input("Ingresa el nombre: "), input("Ingresa el apellido: "), int(input("Ingresa la edad: ")))
persona2.imprimirDetalle()
print(f'Atribute Dinamico (no disponible), telefono: {persona2.telefono}')