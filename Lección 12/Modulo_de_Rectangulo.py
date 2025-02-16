from Modulo_de_FiguraGeometrica import FiguraGeometrica
from Modulo_de_Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, fParamAlto, fParamAncho, cParamColor):
        FiguraGeometrica.__init__(self, fParamAlto, fParamAncho)
        Color.__init__(self, cParamColor)

    #Método GET para el area del rectangulo
    @property
    def fArea(self):
        return self._fAlto * self._fAncho

    #Método para imprimir los atributos
    def __str__(self):
        return f'Rectangulo con {self._fAlto} unidades de alto, {self._fAncho} unidades de ancho y un color {self._cColor}. '

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con exito ')