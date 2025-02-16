setA = {0,1,2,3,4,5,6,7,8,9}
setB = {1,2,3}
setC = {10,11,12,13}
print(f'Impresión de SETs'.center(len('Impresión de SETs') + 20, '+'))
print(f'Set A: {setA}\nSet B: {setB}\nSet C: {setC}')

# Subset
# Esta función valida si un SET está contenido dentro de otro SET
print(f'¿El set B es un subset del set A?: {setB.issubset(setA)}')
print(f'¿El set A es un subset del set B?: {setA.issubset(setB)}')

# Superset
# Esta función valida si un SET contiene la totalidad de otro SET
print(f'¿El set A es un superset del set B?: {setA.issuperset(setB)}')
print(f'¿El set B es un superset del set A?: {setB.issuperset(setA)}')

# Disjoint
# Esta función valida que dos SETs no intercedan en ningún elemento
print(f'¿El set A y el set B son sets disjuntos?: {setA.isdisjoint(setB)}')
print(f'¿El set A y el set C son sets disjuntos?: {setA.isdisjoint(setC)}')