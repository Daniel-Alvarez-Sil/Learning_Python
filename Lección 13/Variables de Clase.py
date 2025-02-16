class Humano(object):
    # Definimos una variable de clase (esta variable será la misma para todas las instancias de esta clase)
    cNacionalidad = 'Mexicano'

    # Definimos las variables de instancia
    def __init__(self, cParamNombre):
        self._cNombre = cParamNombre

    #Método GET
    @property
    def cNombre(self):
        return self._cNombre
    #Método SET
    @cNombre.setter
    def cNombre(self, cParamNombre):
        self._cNombre = cParamNombre

# Las variables de clase pueden ser impresas sin necesidad de crear un objeto
print(f'Nacionalidad de los humanos de la clase: {Humano.cNacionalidad}')

# Para imprimir las variables de instancia, debemos crear un objeto
# Las variables de clase se pueden imprimir directamente desde la clase o desde cualquier objeto
humano1 = Humano(input("Ingresa tu nombre: "))
print(f'Persona: {humano1.cNombre}, Nacionalidad: {humano1.cNacionalidad}')

# Podemos crear variables de clase de manera dinamica
Humano.cEspecie = 'Humano'
print(f'Persona: {humano1.cNombre}, Nacionalidad: {humano1.cNacionalidad}, Especie: {humano1.cEspecie}')