# Unpacking de Tuplas
a, b = 'Hola', 'Adiós'
print(f'Valor de a: {a}, Valor de b: {b}')

# Swap de Variables
a, b = b, a
print(f'Valor de a: {a}, Valor de b: {b}')

# Regresa multiples variables de una función
def minMax(elementos):
    return min(elementos), max(elementos) # <-- Esto es una tupla
lista = [1,2,3,5,9,4,10,11,100]
menor, mayor = minMax(lista)
print(f'Entre los numeros, {lista}, el numero mayor es {mayor} y el numero menor {menor}')

# Prueba de tuplas
#def miFuncion1(args):
#    for arg in args:
#        print(arg)
#
#tupla = (1,2,3,4,5)
#miFuncion1(tupla)

# Calcular la Suma de una Tupla (aplica para cualquier colección)
def calcularSuma(variosArgumentos):
    return sum(variosArgumentos)
print(f'La suma de 1,2,3 y 54 es {calcularSuma((1,2,3,54))}')