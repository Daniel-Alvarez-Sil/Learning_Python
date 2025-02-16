class Pelicula:
    def __init__(self, cParamNombre):
        self._cNombre = cParamNombre

    #Método GET
    @property
    def cNombre(self):
        return self._cNombre
    #Método SET
    @cNombre.setter
    def cNombre(self, cParamNombre):
        self._cNombre = cParamNombre

    def __str__(self):
        return f'Pelicula: {self._cNombre}'

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con exito')
else:
    pelicula1 = Pelicula("Batman")
    print(pelicula1)