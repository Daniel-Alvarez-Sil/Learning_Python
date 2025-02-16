class Computadora:
    iContador = 0

    #Método para incrementar el ID de las computadoras
    @classmethod
    def nextComputadora(cls):
        cls.iContador = cls.iContador + 1
        return cls.iContador

    def __init__(self, cParamNombre, oParamMonitor, oParamTeclado, oParamRaton):
        self._iID = self.nextComputadora()
        self._cNombre = cParamNombre
        self._oMonitor = oParamMonitor
        self._oTeclado = oParamTeclado
        self._oRaton = oParamRaton

    #Método GET
    @property
    def iID(self):
        return self._iID

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
    def oMonitor(self):
        return self._oMonitor
    #Método SET
    @oMonitor.setter
    def oMonitor(self, oParamMonitor):
        self._oMonitor = oParamMonitor

    #Método GET
    @property
    def oTeclado(self):
        return self._oTeclado
    #Método SET
    @oTeclado.setter
    def oTeclado(self, oParamTeclado):
        self._oTeclado = oParamTeclado

    #Método GET
    @property
    def oRaton(self):
        return self._oRaton
    #Método SET
    @oRaton.setter
    def oRaton(self, oParamRaton):
        self._oRaton = oParamRaton

    #Método para imprimir los atributos de la clase
    def __str__(self):
        return f'\n\t{self._cNombre}: {self._iID} \n\t\t{self._oMonitor}\n\t\t{self._oTeclado}\n\t\t{self._oRaton}'

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con exito')