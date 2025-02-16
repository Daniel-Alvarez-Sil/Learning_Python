from Modulo_de_DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    iContador = 0

    #Método para incrementar el ID de los teclados
    @classmethod
    def nextTeclado(cls):
        cls.iContador = cls.iContador + 1
        return cls.iContador

    def __init__(self, cParamMarca, cParamTipoEntrada):
        DispositivoEntrada.__init__(self, cParamMarca, cParamTipoEntrada)
        self._iID = self.nextTeclado()

    #Método GET
    @property
    def iID(self):
        return self._iID

    #Método para imprimir los atributos
    def __str__(self):
        return f'Teclado --> ID: {self._iID}, {DispositivoEntrada.__str__(self)}'

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con exito')
