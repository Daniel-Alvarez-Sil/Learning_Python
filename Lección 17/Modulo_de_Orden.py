class Orden:
    iContador = 0

    #Método para incrementar el ID de las ordenes
    @classmethod
    def nextOrden(cls):
        cls.iContador = cls.iContador + 1
        return cls.iContador

    def __init__(self, listParamComputadoras):
        self._iID = self.nextOrden()
        self._listComputadoras = list(listParamComputadoras)

    #Método GET
    @property
    def iID(self):
        return self._iID

    #Método GET
    @property
    def listComputadoras(self):
        return self._listComputadoras
    #Método SET
    @listComputadoras.setter
    def listComputadoras(self, listParamComputadoras):
        self._listComputadoras = listParamComputadoras

    #Método para agregar otra computadora
    def agregarComputadora(self, elementComputadora):
        self._listComputadoras.append(elementComputadora)

    #Método para imprimir los atributos de la clase
    def __str__(self):
        cOrden = f'Orden: {self._iID}, computadoras: \n'
        for computadora in self._listComputadoras:
            cOrden = cOrden + computadora.__str__()
        return cOrden

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con exito')