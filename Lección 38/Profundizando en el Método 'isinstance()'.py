from Ejercicio_de_Herencias import *

# La función isinstance() tiene la siguiente sintáxis:
# Sintáxis: isinstance(<objeto de una clase>, <clase>)
#           La función retorna True si es que el objeto es una instancia de la clase indicada o si la clase indicada se
#           encuentra dentro del mro de la clase de la cual el objeto es una instancia.
#           De no ser así, la función retorna False

# Ejemplos del uso de la función:
    # Ejemplos con Tipos de Datos:
print(f'¿10 es un objeto de la clase int?: {isinstance(10, int)}')
print(f'¿[1,2,3,4] es un objeto de la clase list?: {isinstance([1,2,3,4], list)}')
    # Ejemplos con Clases:
claseConHerenciaMultiple = Clase4()
print(f'¿El objeto, claseConHerenciaMultiple, es una instancia de la Clase 4?: {isinstance(claseConHerenciaMultiple, Clase4)}')
print(f'¿El objeto, claseConHerenciaMultiple, es una instancia de la Clase 2?: {isinstance(claseConHerenciaMultiple, Clase2)}')
print(f'¿El objeto, claseConHerenciaMultiple, es una instancia de la Clase 3?: {isinstance(claseConHerenciaMultiple, Clase3)}')
print(f'¿El objeto, claseConHerenciaMultiple, es una instancia de la Clase 1?: {isinstance(claseConHerenciaMultiple, Clase1)}')
    # Ejemplo con Múltiples Clases:
print(f'¿El objeto, claseConHerenciaMultiple, es una instancia de la Clase 1, de la Clase 2 y de la Clase 3?: {isinstance(claseConHerenciaMultiple, (Clase1, Clase2, Clase3))}')
