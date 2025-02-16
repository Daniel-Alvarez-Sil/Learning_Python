# Los DocStrings pueden ser usados para imprimir documentacíon de la siguiente manera

from Modulo_de_Prueba import MiPrueba

# Manera 1:
help(MiPrueba)

# Manera 2:
print(MiPrueba.__doc__)
print(MiPrueba.__init__.__doc__)
print(MiPrueba.metodo.__doc__)