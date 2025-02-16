from Modulo_de_Persona import Persona

class Empleado(Persona):
    def __init__(self, cParamNombre, iParamEdad, fParamSueldo):
        super().__init__(cParamNombre, iParamEdad)
        self._fSueldo = fParamSueldo

    #Método GET
    @property
    def fSueldo(self):
        return self._fSueldo

    #Método SET
    @fSueldo.setter
    def fSueldo(self, fParamSueldo):
        self._fSueldo = fParamSueldo

    #Método para imprimir los atributos de la instancia
    def imprimirDetalle(self):
        print(f'Empleado: {self._cNombre}, Sueldo: {self._fSueldo:.2f}')

    #Método a ejecutar cuando se elimina una instancia de esta clase
    def __del__(self):
        print(f'El empleado, {self._cNombre}, ha sido eliminado con exito')

    #Sobreescritura del metodo dunder str
    def __str__(self):
        return f'Empleado: [Nombre: {self._cNombre}] [Edad: {self._iEdad}] [Sueldo: {self._fSueldo}]'

if __name__ == '__main__':
    empleado1 = Empleado(input("Ingresa tu nombre: "), int(input("Ingresa tu edad: ")), float(input("Ingresa tu sueldo: ")))
    empleado1.imprimirDetalle()
else:
    print(f'{__name__} ha sido importado con exito')