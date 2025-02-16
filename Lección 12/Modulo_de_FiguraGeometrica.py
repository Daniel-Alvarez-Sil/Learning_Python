# Convertiremos FiguraGeometrica en una Clase Abstracta
#   No se pueden crear objetos de una Clase Abstracta
#   Una Clase Abstracta Contiene Metodos Abstractos (metodos que obligatoriamente deben existir en las clases hija)
#   Una Clase Abstraca hereda de la clase abc
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, fParamAlto, fParamAncho):
        self._fAlto = fParamAlto
        self._fAncho = fParamAncho

    #Método GET
    @property
    def fAlto(self):
        return self._fAlto
    #Método SET
    @fAlto.setter
    def fAlto(self, fParamAlto):
        self._fAlto = fParamAlto

    #Método GET
    @property
    def fAncho(self):
        return self._fAncho
    #Método SET
    @fAncho.setter
    def fAncho(self, cParamAncho):
        self._fAncho = cParamAncho

    #Método Abstracto que deben incluir (obligatoriamente) las clases hija
    @property
    @abstractmethod
    def fArea(self):
        return self._fAlto * self._fAncho

    #Método de impresion de atributos
    def __str__(self):
        return f'Figura Geometrica con {self._fAlto} unidades de alto y {self._fAncho} unidades de ancho. '

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con exito')