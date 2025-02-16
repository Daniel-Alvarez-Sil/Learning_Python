from Modulo_de_Persona import Persona

print("Creación de Objeto". center(50, '+'))
persona1 = Persona(input("Ingresa tu nombre: "), int(input("Ingresa tu edad: ")))
persona1.imprimirDetalle()

print("Eliminación de Objeto". center(50, '-'))
del persona1