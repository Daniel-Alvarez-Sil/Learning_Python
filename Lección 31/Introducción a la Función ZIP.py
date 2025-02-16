# La función ZIP sirve para juntar dos colecciones
# La función ZIP crea x (x = el numero de elementos de la colección más pequeña) tuplas en las cuales el elemento[0] de
# la primera colección comparte una tupla con el elemento[0] de la segunda colección y así sucesivamente hasta los
# elementos[x]

# Ejemplo:

lista = [1,2,3,4,5,6,7,8,9,10]
nombre = '12345678910'

# NOTA la función ZIP regresa un objeto ZIP, por lo que hay que convertir el objeto ZIP a algún tipo de dato iterable
print(f'Mezcla de 2 colecciones, mediante la función ZIP: {list(zip(lista,nombre))}')