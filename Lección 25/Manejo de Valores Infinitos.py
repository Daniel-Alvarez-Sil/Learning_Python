import math
from decimal import Decimal

# Asignación de infinitos usando el constructor FLOAT
    # Establecimiento del infinito positivo a una variable
fPositiveInfinite = float('inf')
print(f'Variable ({type(fPositiveInfinite)}) con un infinito positivo: {fPositiveInfinite}. ')
print(f'¿La variable es igual a algún infinito?: {math.isinf(fPositiveInfinite)}. ')

    # Establecimiento del infinito negativo a una variable
fNegativeInfinite = float('-inf')
print(f'Variable ({type(fNegativeInfinite)}) con un infinito negativo: {fNegativeInfinite}. ')
print(f'¿La variable es igual a algún infinito?: {math.isinf(fPositiveInfinite)}. ')

print('\n')

# Asignación de infinitos usando el Módulo MATH
    # Establecimiento del infinitivo positivo a una variable
fPositiveInfinite = math.inf
print(f'Variable ({type(fPositiveInfinite)}) con un infinitivo positivo: {fPositiveInfinite}. ')
print(f'¿La variable es igual a algún infinito?: {math.isinf(fPositiveInfinite)}. ')

    #Establecimiento del infinito negativo a un variable
fNegativeInfinite = -math.inf
print(f'Variable ({type(fNegativeInfinite)}) con un infinitivo negativo: {fNegativeInfinite}. ')
print(f'¿La variable es igual a algún infinito?: {math.isinf(fPositiveInfinite)}. ')

print('\n')

# Asignación de infinitos usando el Módulo DECIMAL
    #Establecimiento del infinito positivo a una variable
fPositiveInfinite = Decimal("Infinity")
print(f'Variable ({type(fPositiveInfinite)}) con un infinito positivo: {fPositiveInfinite}. ')
print(f'¿La variable es igual a algún infinito?: {math.isinf(fPositiveInfinite)}. ')

    #Establecimiento del infinito negativo a una variable
fNegativeInfinite = Decimal("-Infinity")
print(f'Variable ({type(fNegativeInfinite)}) con un infinite negativo: {fNegativeInfinite}. ')
print(f'¿La variable es igual a algún infinito?: {math.isinf(fNegativeInfinite)}')
