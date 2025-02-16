# Atributos de Clases y de Objetos (Instancias de Clase)

class Persona:
    # Atributos de Clase
    iContador = 0
    def __init__(self, cParamNombre, cParamApellido):
        # Atributos de Objetos
        self.cNombre = cParamNombre
        self.cApellido = cParamApellido

# Como visualizar los atributos de objeto de una instancia
persona1 = Persona('Daniel', 'Alvarez')
print(f'Atributos de \'persona1\': {persona1.__dict__}')

print()
print("Impresión del Atributo, \'iContador\', ya sea de Clase o de Objeto". center(100, '+'))

# Cualquier objeto tiene acceso de lectura a los atributos de su clase correspondiente
print(f'Atributo de la clase correspondiente de \'persona1\': {persona1.iContador}')

# Sin embargo, sólo podemos modificar los atributos de clase llamando directamente a la clase
Persona.iContador = 1
print(f'Atributo de la clase correspondiente de \'persona1\': {persona1.iContador}')

# No obstante, si intentamos modificar los atributos de clase mediante el llamamiento de una instancia, el atributo de
# clase no será modificado sino que se creara dinámicamente un atributo de instancia para el objeto que se usó para la llamada
persona1.iContador = 2
print(f'Atributo de instancia del objeto, \'persona1\', el cual oculta (shadows) el atributo de clase correspondiente de la instancia: {persona1.iContador}')
print(f'Atributo de la clase, \'Persona\': {Persona.iContador}')

# Creación de Atributos al Vuelo
# Para crear atributos al vuelo de clase e instancias, debemos seguir la siguiente sintáxis:
# Sintáxis: <clase u objeto>.<nuevo atributo> = <valor a asignar>
print()
print(f'Creación de Atributos al Vuelo'.center(100, '-'))
persona1.iEdad = 19
print(f'Nuevo Atributo, \'iEdad\', del Objeto, \'persona1\': {persona1.iEdad}')

Persona.cPais = 'México'
print(f'Nuevo Atributo, \'cPais\', de la Clase, \'Persona\': {persona1.cPais}')
# NOTA: Todos los atributos, ya sean creados al vuelo o no, de una clase son accesibles desde cualquier instancia de la clase




