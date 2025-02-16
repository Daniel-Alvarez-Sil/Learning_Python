class Cubo:
    def __init__(self, fParamAltura, fParamAncho, fParamProfundo):
        self.fAltura = fParamAltura
        self.fAncho = fParamAncho
        self.fProfundo = fParamProfundo

    def calcularVolumen(self):
        return self.fAltura * self.fAncho * self.fProfundo

cubo1 = Cubo(float(input("Ingresa la altura del cubo: ")), float(input("Ingresa el ancho del cubo: ")), float(input("Ingresa la profundidad del cubo: ")))
print(f'El volumen del cubo ingresado es: {cubo1.calcularVolumen():.2f}')