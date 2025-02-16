# Una Representación de un Objeto es la Impresión de sus Atributos en un String
# Formas de Representar un Objeto Mediante una Cadena String
# Métodos Dunder para realizar esto: __str__, __repr__, __format__

class Persona:
    def __init__(self, cParamNombre, cParamApellido):
        self.cNombre = cParamNombre
        self.cApellido = cParamApellido

    # Método __repr__
    # Este método esta dirigido a desarrolladores
    # NOTA: Este método es utilizado por el método __str__, ya que, si no se ha sobreescrito el método __str__, __str__
    #       usa la cadena definida en el método __repr__
    def __repr__(self):
        return f'{self.__class__.__name__}(cNombre: {self.cNombre}, cApellido: {self.cApellido})'

    # Método __str__
    # Este método está dirigido para el uso de usuarios
    # La implementación de este método por default llama al método __repr__
    def __str__(self):
        return f'{self.__class__.__name__}: {self.cNombre} {self.cApellido}'

    # Método __format__
    # La implementación de este método por defaulta llama al método __str__
    def __format__(self, formatSpecifications):
        return f'{self.__class__.__name__} con nombre {self.cNombre} y apellido {self.cApellido}'

# Método __repr__
# Este método es llamado automáticamente por 'print()' siempre y cuando no se ha sobreescrito el método __str__
persona1 = Persona('Daniel', 'Alvarez')
print(f'Representación de la clase, mediante el método __repr__: {persona1!r}')

# Método __str__
# Este método es llamado automáticamente por 'print()'
print(f'Representación de la clase, mediante el método __str__: {persona1!s}')

# Método __format__
# Este método se llama cuando el desarrollador usa un f string para representar el objeto
print(f'Representación de la clase, mediante el método __format__: {persona1}')
