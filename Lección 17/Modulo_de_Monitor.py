class Monitor(object):
    iContador = 0

    #Método para incrementar el ID de los monitores
    @classmethod
    def nextMonitor(cls):
        cls.iContador = cls.iContador + 1
        return cls.iContador

    def __init__(self, cParamMarca, fParamTamaño):
        self._iID = self.nextMonitor()
        self._cMarca = cParamMarca
        self._fTamaño = fParamTamaño

    #Método GET
    @property
    def iID(self):
        return self._iID

    #Método GET
    @property
    def cMarca(self):
        return self._cMarca
    #Método SET
    @cMarca.setter
    def cMarca(self, cParamMarca):
        self._cMarca = cParamMarca

    #Método GET
    @property
    def fTamaño(self):
        return self._fTamaño
    #Método SET
    @fTamaño.setter
    def fTamaño(self, fParamTamaño):
        self._fTamaño = fParamTamaño

    #Método para imprimir los atributos de la instancia
    def __str__(self):
        return f'Monitor --> ID: {self._iID}, Marca: {self._cMarca}, Tamaño: {self._fTamaño} pulgadas'

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con exito')