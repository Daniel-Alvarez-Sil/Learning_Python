# Este código implementa las clases definidas en el diagrama que se encuentra en el archivo 'Ejercicio de Herencias.png'

class Clase1(object):
    def __init__(self):
        print(f'Método Inicializador de la Clase 1. ')

    def metodo(self):
        print(f'Método de la Clase 1. ')

class Clase2(Clase1):
    def __init__(self):
        print(f'Método Inicializador de la Clase 2. ')
        super().__init__()

    def metodo(self):
        print(f'Método de la Clase 2. ')
        super().metodo()

class Clase3(Clase1):
    def __init__(self):
        print(f'Método Inicializador de la Clase 3. ')
        super().__init__()

    def metodo(self):
        print(f'Método de la Clase 3. ')
        super().metodo()

class Clase4(Clase2, Clase3):
    def __init__(self):
        print(f'Método Inicializador de la Clase 4. ')
        super().__init__()

    def metodo(self):
        print(f'Método de la Clase 4. ')
        super().metodo()

# NOTA: En una clase que posee cualquier tipo de herencia, para conocer la jerarquía de los métodos que se utlizarán,
#       se manda a llamar el método dunder mro

if __name__ != '__main__':
    print(f'Los módulos de herencia múltiple han sido importados correctamente. ')
else:
    print(f'MRO (Method Resolution Order) de la Clase 4: {Clase4.__mro__}')
    claseMasJoven = Clase4()
    claseMasJoven.metodo()