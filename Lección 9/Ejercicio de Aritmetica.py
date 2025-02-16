class Aritmetica:
    def __init__(self, iParamOperandoA, iParamaOperandoB):
        self.iOperandoA = iParamOperandoA
        self.iOperandoB = iParamaOperandoB

    def sumar(self):
        return self.iOperandoA + self.iOperandoB

    def restar(self):
        return self.iOperandoA - self.iOperandoB

    def multiplicar(self):
        return self.iOperandoA * self.iOperandoB

    def dividir(self):
        return self.iOperandoA / self.iOperandoB

operacion1 = Aritmetica(int(input("Ingresa un numero: ")), int(input("Ingresa un numero: ")))
print(f'{operacion1.iOperandoA} + {operacion1.iOperandoB} = {operacion1.sumar()}')
print(f'{operacion1.iOperandoA} - {operacion1.iOperandoB} = {operacion1.restar()}')
print(f'{operacion1.iOperandoA} * {operacion1.iOperandoB} = {operacion1.multiplicar()}')
print(f'{operacion1.iOperandoA} / {operacion1.iOperandoB} = {operacion1.dividir():.2f}')