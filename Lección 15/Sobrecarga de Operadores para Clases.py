# La Sobrecarga de Operadores se refiere al distinto uso que le podemos dar a los operadores de Python.
# Este distinto uso depende del tipo de variables con las que estemos trabajando

print("Sobrecarga de la Suma". center(30, '-'))

# Suma de Enteros
a = 1
b = 2
print(f'Suma de Enteros: {a + b}')

# Suma (Concatenacion) de Caracteres
a = "Grifith"
b = "!!!"
print(f'Suma de Caracteres: {a + b}')

# Suma de Listas
a = [1,2,3,4,5]
b = [6,7,8,9,10]
print(f'Suma de Listas: {a + b}')

# Para sumar clases, es necesario sobreescribir la funcion correspondiente
class Objeto:
    def __init__(self, iParamNumero):
        self.iNumero = iParamNumero

    #Sobreescritura de la funcion de Suma
    # claseA + claseB = claseA.__add__(claseB)
    def __add__(self, other):
        return self.iNumero + other.iNumero

a = Objeto(10)
b = Objeto(11)

print(f'Suma de Clases: {a.__add__(b)}')