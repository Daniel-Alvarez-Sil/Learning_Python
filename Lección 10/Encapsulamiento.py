class Persona:
    def __init__(self, cParamNombre, iParamEdad):
        self._cNombre = cParamNombre # <--- Este encapsulamiento sirve para informar al desarrollador que el atributo solo puede modificarse/accederse junto con la clase
        self.__iEdad = iParamEdad # <--- Este encapsulamiento sirve para evitar que el atributo sea modificado individualmente (sin el resto de la clase)

    def imprimirDetalle(self):
        print(f'Persona: {self._cNombre}, {self.__iEdad}')

persona1 = Persona(input("Ingresa tu nombre completo: "), int(input("Ingresa tu edad: ")))
persona1.imprimirDetalle()

persona1._cNombre = "Modificacion de Nombre"
persona1.__iEdad = 19
print(f'{persona1.__iEdad}')

persona1.imprimirDetalle()
