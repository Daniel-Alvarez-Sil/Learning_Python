# La función ZIP toma cualquier elemento de un SET, ya que los elementos de un SET no tienen orden
# Ejemplo de lo establecido previamente:

lista = [2,3,4,5,6]
tupla = (3,4,5,6,7)
set = {5,3,4,2,1}

mezcla = list(zip(lista, tupla, set))

print(f'Mezcla de Iterables: {mezcla}')