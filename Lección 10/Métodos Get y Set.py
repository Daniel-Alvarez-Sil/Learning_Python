class Persona:
    def __init__(self, cParamNombre, iParamEdad):
        self._cNombre = cParamNombre #Encapsulamiento
        self.iEdad = iParamEdad

    #Método Get
    @property #Decorador del metodo
    def cNombre(self):
        print("Llamando al Metodo GET")
        return self._cNombre

    #Método Set
    #Si queremes que el atributo 'cNombre' sea READ-ONLY, debemos comentar el método SET
    @cNombre.setter
    def cNombre(self, cParamNombre):
        print("Llamando al Metodo SET")
        self._cNombre = cParamNombre

    def imprimirDetalle(self):
        print(f'Persona: {self._cNombre}, {self.iEdad}')

persona1 = Persona(input("Ingresa tu nombre completo: "), int(input("Ingresa tu edad: ")))
persona1.imprimirDetalle()

persona1.cNombre = "Daniel"
print(f'{persona1.cNombre}')