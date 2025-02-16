class convertidorTemperatura:
    # NOTA: Una variable constante se caracteriza por ser definida con mayúsculas
    MIN_CELSIUS = -273.15
    MIN_FAHRENHEIT = -459.67

    @classmethod
    def cToF(cls, fC):
        if fC < cls.MIN_CELSIUS:
            raise ValueError(f'La temperatura, {fC} C, es menor que el límite teórico')
        else:
            return fC * 9 / 5 + 32

    @classmethod
    def fToC(cls, fF):
        if fF < cls.MIN_FAHRENHEIT:
            raise ValueError(f'La temperatura, {fF} F, es menor que el límite teórico')
        else:
            return (fF - 32) * 5 / 9


if __name__ != '__main__':
    print(f'El módulo, {__name__}, ha sido importado con éxito. ')
else:
    print(f'La temperatura, {1:0.2f} C, es equivalente a {convertidorTemperatura.cToF(1):0.2f} F. ')
    print(f'La temperatura, {50:0.2f} F, es equivalente a {convertidorTemperatura.fToC(50):0.2f} C. ')

