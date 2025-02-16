# Creación de un Decorador para Clases
# Dicho decorador tiene como propósito crear dinámicamente una función __repr__ en la clase que decora
# NOTA: Los decoradores permiten cambiar drásticamente nuestras clases

# Función Decoradora
# Esta función recibe como parámetro una clase
def decoradorRepr(classParam):
    print(f'Llamando a la función decoradora... para la clase {classParam.__name__}')

    # Validamos que la función __init__ esté sobreescrita en la clase que se va a decorar. De no ser así, se produce un
    # error
    if '__init__' not in vars(classParam):
        raise TypeError(f'La función, \'__init__\', no se ha sobreescrito en la clase {classParam.__name__}. ')

    # Recolectamos los Atributos Legibles de la Clase
    atributos = [llave for llave, valor in vars(classParam).items() if isinstance(valor, property)]

    # Definimos la función __repr__ que será injertada dinámicamente en la clase a decorar
    def __repr__(self):
        return f'{self.__class__.__name__}({", ".join(list(f"{atributo} = {getattr(self, atributo)!r}" for atributo in atributos))})'

    # Injertamos dinámicamente la función __repr__ en la clase a decorar
    setattr(classParam, '__repr__', __repr__)

    # Retornamos la clase que recibimos como parámetro
    return classParam


@decoradorRepr
class Persona(object):
    # pass
    def __init__(self, cParamNombre, cParamApellido, iParamEdad):
        self._cNombre = cParamNombre
        self._cApellido = cParamApellido
        self._iEdad = iParamEdad

    # Métodos GET
    @property
    def cNombre(self):
        return self._cNombre
    @property
    def cApellido(self):
        return self._cApellido
    @property
    def iEdad(self):
        return self._iEdad

@decoradorRepr
class Libro(object):
    def __init__(self, iParamISBN, cParamTitulo, cParamAutor):
        self._iISBN = iParamISBN
        self._cTitulo = cParamTitulo
        self._cAutor = cParamAutor

    # Métodos GET
    @property
    def iISBN(self):
        return self._iISBN
    @property
    def cTitulo(self):
        return self._cTitulo
    @property
    def cAutor(self):
        return self._cAutor


persona1 = Persona('Daniel', 'Alvarez', 19)
print(persona1)
libro1 = Libro(12345678910, 'Monster', 'Naoki Urasawa')
print(libro1)