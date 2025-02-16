class Empleado(object):
    def __init__(self, cParamNombre, fParamSueldo):
        self._cNombre = cParamNombre
        self._fSueldo = fParamSueldo

    #Método GET
    @property
    def cNombre(self):
        return self._cNombre
    #Método SET
    @cNombre.setter
    def cNombre(self, cParamNombre):
        self._cNombre = cParamNombre

    #Método GET
    @property
    def fSueldo(self):
        return self._fSueldo
    #Método SET
    @fSueldo.setter
    def fSueldo(self, fParamSueldo):
        self._fSueldo = fParamSueldo

    #Método para imprimir los atributos
    def __str__(self):
        return f'Empleado [Nombre: {self._cNombre}, Sueldo: {self._fSueldo}]'

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con exito')
