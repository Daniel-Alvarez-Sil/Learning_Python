setA = {1,2,3,4,5}
setB = {6,7,8,9,10}
setC = {4,5,6,7}

# Unión (Operación Conmutativa)
print(f'La unión de los conjuntos A y B es: {setA.union(setB)}')

# Intersección (Operación Conmutativa)
print(f'La intersección de los conjuntos A y C es: {setA.intersection(setC)}')

# Diferencia (Operación no Conmutativa)
print(f'Los elementos del conjunto A que no interceden en el conjunto C son: {setA.difference(setC)}')

# Diferencia Simétrica (Operación Conmutativa)
print(f'Los elementos del conjunto B y del conjunto C que no interceden en el conjunto opuesto es: {setC.symmetric_difference(setB)}')
