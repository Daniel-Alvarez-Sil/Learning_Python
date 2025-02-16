# NOTA: Las Listas son Mutables

lista1 = ['Daniel', 'Mariana', 'Alvaro']
lista2 = 'Armando Jesús Valeria Pablo'.split()

# Sumar Listas
print(f'Suma de Listas: {lista1 + lista2}')

# Extensión de una Lista con otra Lista
lista1.extend(lista2)
print(f'Lista 1 Modificada: {lista1}')