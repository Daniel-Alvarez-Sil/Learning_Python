class Orden(object):
    iContador = 0

    @classmethod
    def nextOrden(cls):
        cls.iContador = cls.iContador + 1
        return cls.iContador

    def __init__(self, listParamProductos):
        self._iID = self.nextOrden()
        self._listProductos = list(listParamProductos)

    #Método GET
    @property
    def listProductos(self):
        return self._listProductos
    #Método SET
    @listProductos.setter
    def listProductos(self, listParamProductos):
        self._listProductos = listParamProductos

    def agregarProducto(self, elementProducto):
        self._listProductos.append(elementProducto)

    def calcularImporteTotal(self):
        fTotal = 0.00
        for elementProducto in self._listProductos:
            fTotal = fTotal + elementProducto.fPrecio
        return fTotal

    def __str__(self):
        cInformacionOrden = f'Orden {self._iID} --> Total {self.calcularImporteTotal()}: \n'
        for elementProducto in self._listProductos:
            cInformacionOrden = cInformacionOrden + elementProducto.__str__() + " | "
        return cInformacionOrden

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con exito')