class Persona:
    def __init__(self, cParamNombre, iParamEdad):
        self._cNombre = cParamNombre
        self._iEdad = iParamEdad

    #Método GET
    @property
    def cNombre(self):
        return self._cNombre

    #Método SET
    @cNombre.setter
    def cNombre(self, cParamNombre):
        self._cNombre = cParamNombre

    #Método SET
    @property
    def iEdad(self):
        return self._iEdad

    #Método SET
    @iEdad.setter
    def iEdad(self, iParamEdad):
        self._iEdad = iParamEdad

    #Procedimiento para imprimir atributos
    def imprimirDetalle(self):
        print(f'Persona: {self._cNombre}, {self._iEdad}')

    #Procedimiento a ejecutar cuando se elimine una instancia de esta clase
    def __del__(self):
        print(f'La persona, {self._cNombre}, ha sido eliminada con éxito')

    if __name__ != '__main__':
        print(f'{__name__} ha sido importado correctamente')