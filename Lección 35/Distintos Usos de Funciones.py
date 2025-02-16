# Las funciones en Python son FIRST CLASS CITIZENS
# Esto significa que las funciones pueden ser implementadas en cualquier parte de nuestro código

# Distintos tipos de Usos:

def sumar(a, b):
    return a + b

# 1.- Asignar una función(como referencia) a una variable
funcionDeSuma = sumar
print(f'La suma de 5 y 6 es {funcionDeSuma(5,6)}')

# 2.- Función como argumento de otra función
def operacion(a, b, sumarParam):
    print(f'Resultado de sumar {a} y {b}: {sumarParam(a, b)}')

operacion(1, 100, sumar)

# 3.- Retornar una función desde una función
def retornarFuncion():
    # Retornamos una función
    return sumar

print(f'La suma de 6 y 7 es {retornarFuncion()(6, 7)}')

