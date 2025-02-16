# Global es una función que nos permite usar la variable que se ha definido en el nivel más alto posible

contador = 0

def imprimirContador():
    print(f'Contador Información: {contador}')

def modificarContador(iNuevoValor):
    global contador # <-- Sin esta línea de código, el contador global no se modificaría con la línea 10
    contador = iNuevoValor

imprimirContador()
modificarContador(1)
imprimirContador()