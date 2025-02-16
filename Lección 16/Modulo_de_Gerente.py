from Modulo_de_Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, cParamNombre, fParamSueldo, cParamArea):
        Empleado.__init__(self, cParamNombre, fParamSueldo)
        self._cArea = cParamArea

    #Método GET
    @property
    def cArea(self):
        return self._cArea
    #Método SET
    @cArea.setter
    def cArea(self, cParamArea):
        self._cArea = cParamArea

    #Método para imprimir los atributos
    def __str__(self):
        return f'Gerente [{self._cArea}], {Empleado.__str__(self)}'

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con exito')
