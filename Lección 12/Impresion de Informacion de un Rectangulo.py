from Modulo_de_FiguraGeometrica import FiguraGeometrica
from Modulo_de_Color import Color
from Modulo_de_Rectangulo import Rectangulo

rectangulo1 = Rectangulo(float(input("Ingresa el alto del rectangulo: ")), float(input("Ingresa el ancho del rectangulo: ")), input("Ingresa el color del rectangulo: "))
print(rectangulo1)
print(f'El area del rectangulo {rectangulo1.cColor} es {rectangulo1.fArea} ')