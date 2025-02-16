from Modulo_de_Persona import Persona
from Ejemplo_de_Herencia import Empleado

persona1 = Persona("", 1)
empleado1 = Empleado("Daniel", 19, 5000)

print(f'Uso Estandar de la funcion dunder str: {persona1}')
print(f'Uso de la funcion dunder str sobreescrita: {empleado1}')