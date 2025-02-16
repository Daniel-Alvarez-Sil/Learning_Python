# Closure con una Función Lambda

def operacion(a, b):
    return lambda: a - b

funcionClosure = operacion(5,9)
print(f'Resultado de la Función Closure: {funcionClosure()}')
print(f'Resultado de la Función Closure al Vuelo: {operacion(9, 5)()}')