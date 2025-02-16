class DispositivoEntrada(object):
    def __init__(self, cParamMarca, cParamTipoEntrada):
        self._cMarca = cParamMarca
        self._cTipoEntrada = cParamTipoEntrada

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
    def cTipoEntrada(self):
        return self._cTipoEntrada
    #Método SET
    @cTipoEntrada.setter
    def cTipoEntrada(self, cParamTipoEntrada):
        self._cTipoEntrada = cParamTipoEntrada

    #Método para imprimir los atributos
    def __str__(self):
        return f'Marca: {self._cMarca}, Tipo de Entrada: {self._cTipoEntrada}'

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con exito')