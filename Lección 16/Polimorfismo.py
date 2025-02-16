# El poliformismo en Python concierne la funcionalidad de Python de guardar distintos tipos de objetos en la misma variable (no simulltaneamente)
# Ejemplo:

from Modulo_de_Empleado import Empleado
from Modulo_de_Gerente import Gerente

print("\n")

def imprimeClase(objeto):
    print(objeto)

print(f'Impresión de Empleado'. center(75, '-'))
empleado1 = Empleado("Daniel", 5000)
imprimeClase(empleado1)

print(f'Impresion de Gerente'. center(75, '-'))
gerente1 = Gerente("Brenda", 5000, "Recursos Humanos")
imprimeClase(gerente1)