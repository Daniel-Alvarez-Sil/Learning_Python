#Para importar todas las clases de un modulo, usa la siguiente sintaxis:
# ---> from <modulo> import *

from Modulo_de_Persona import Persona

persona1 = Persona(input("Ingresa tu nombre: "), int(input("Ingresa tu edad: ")))

persona1.imprimirDetalle()