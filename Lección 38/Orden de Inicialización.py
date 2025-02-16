class Padre:
    def __init__(self):
        print(f'Método inicializador de la clase padre.')

    def metodo(self):
        print(f'Método de la clase padre.')

# NOTA: En una clase Hija, si no se han sobreescrito los métodos existentes en la clase Padre, el IDE usa los métodos
#       de la clase Padre
class Hijo(Padre):
    def __init__(self):
        print(f'Método inicializador de la clase hija. ')

    def metodo(self):
        # NOTA: Con la ayuda de la función 'super()', podemos hacer uso de los métodos de la clase Padre
        super().metodo()
        print(f'Método de la clase hija. ')

padre1 = Padre()
hijo1 = Hijo()
hijo1.metodo()