class Color(object):
    def __init__(self, cParamColor):
        self._cColor = cParamColor

    #Método GET
    @property
    def cColor(self):
        return self._cColor
    #Método SET
    @cColor.setter
    def cColor(self, cParamColor):
        self._cColor = cParamColor

    #Método de impresion de atributos
    def __str__(self):
        return f'Color: {self._cColor}. '

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con exito')