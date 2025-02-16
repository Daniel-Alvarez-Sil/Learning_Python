# Python Closure es el uso de una función anidada para
# usar una variable aunque ésta ya esté fuera del scope

def operacion(a, b):
    def sumar():
        return a + b

    return sumar # <-- OJO: No estamos regresando "sumar()" sino "sumar"

miFuncionClosure = operacion(10,20)
print(f'Resultado de la Función Closure: {miFuncionClosure()}')
print(f'Resultado de la Función Closure al Vuelo: {operacion(5,7)()}')