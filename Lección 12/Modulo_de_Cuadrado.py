from Modulo_de_FiguraGeometrica import FiguraGeometrica
from Modulo_de_Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, fParamLado, cParamColor):
        FiguraGeometrica.__init__(self, fParamLado, fParamLado)
        Color.__init__(self, cParamColor)

    #Método GET para el area del cuadrado
    @property
    def fArea(self):
        return self._fAlto * self._fAncho

    #Método de impresion de atributos
    def __str__(self):
        return f'Cuadrado con {self._fAlto} unidades de lado y un color {self._cColor}. '

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con exito')