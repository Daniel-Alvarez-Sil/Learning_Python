class Lenguaje(object):

# Contexto Dinámico de la Clase (se tiene acceso a este contexto cuando se crea una instancia de la clase)
    def __init__(self, cParamNombre):
        self.cNombre = cParamNombre

    # Método de Instancia
    # Este tipo de método tiene acceso a las variables de instancia (cNombre) y es parte del contexto dinámico de la clase
    # Debido a esto, desde este método, tenemos acceso al todo el contexto dinámico y estático de la clase
    # En python, el contexto dinámico puede acceder al contexto estático, pero no vice versa
    def imprimirDetalleDinamico(self):
        self.imprimirDetalle()
        print(f'Lenguaje: {self.cNombre}')

# Fin del Contexto Dinámico

# Contexto Estático de la Clase (se tiene acceso a este contexto usando la clase como referencia)
    cTipo = 'Lenguaje de Programacion'

    # Método Estático
    # Este tipo de métodos no recibe la informacion de la clase como parametro
    # Debido a esto, debemos usar el nombre de la clase para hacer referencia a sus atributos de CLASE
    @staticmethod
    def imprimirDetalle():
        print(f'Tipo de Lenguaje: {Lenguaje.cTipo}')

    # Método de Clase
    # Este tipo de métodos recibe la informacion de la clase como parametro
    # Debido a esto, podemos usar un puntero (cls) para hacer referencia a los atributos de la CLASE
    @classmethod
    def imprimirDetalleConParametros(cls):
        print(f'Tipo de Lenguaje: {cls.cTipo}')

# Fin del Contexto Estatico


print(f'Impresion de los Metodos de la Clase (Contexto Estatico)'. center(70, '-'))
Lenguaje.imprimirDetalle()
Lenguaje.imprimirDetalleConParametros()

print(f'Impresion de la Instancia de la Clase (Contexto Dinámico)'. center(70, '-'))
lenguaje1 = Lenguaje("Python")
lenguaje1.imprimirDetalleDinamico()
