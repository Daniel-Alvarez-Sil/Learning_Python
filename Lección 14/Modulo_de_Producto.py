class Producto(object):
    iContador = 0

    @classmethod
    def nextProducto(cls):
        cls.iContador = cls.iContador + 1
        return cls.iContador

    def __init__(self, cParamNombre, fParamPrecio):
        self._iID = self.nextProducto()
        self._cNombre = cParamNombre
        self._fPrecio = fParamPrecio

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
    def fPrecio(self):
        return self._fPrecio
    #Método SET
    @fPrecio.setter
    def fPrecio(self, fParamPrecio):
        self._fPrecio = fParamPrecio

    def __str__(self):
        return f'{self._iID}.- Producto: {self._cNombre} --> {self._fPrecio}'

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con exito')

