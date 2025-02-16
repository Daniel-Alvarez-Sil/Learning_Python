import math
from decimal import Decimal

# NaN = Not a Number
# En python, "nan" no es case-sensitive
# NaN es un tipo de dato numérico indefinido

# Asignación de NaN mediante el constructor FLOAT
fA = float("NaN")
print(f'fA({type(fA)}) = {fA}')
print(f'¿Es "fA" un tipo de dato NaN?: {math.isnan(fA)}')

# Assignación de NaN mediante el módulo DECIMAL
fA = Decimal("NaN")
print(f'fA({type(fA)}) = {fA}')
print(f'¿Es "fA" un tipo de dato NaN?: {math.isnan(fA)}')