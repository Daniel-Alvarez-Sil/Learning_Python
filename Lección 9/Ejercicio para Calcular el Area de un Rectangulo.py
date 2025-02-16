class Rectangulo:
    def __init__(self, fParamBase, fParamAltura):
        self.fBase = fParamBase
        self.fAltura = fParamAltura

    def calcularArea(self):
        return self.fBase * self.fAltura

rectangulo1 = Rectangulo(float(input("Ingresa el ancho del rectangulo: ")), float(input("Ingresa la altura del rectangulo: ")))
print(f'El area del rectangulo ingresado es: {rectangulo1.calcularArea():.2f}')
