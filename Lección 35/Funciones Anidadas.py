def calculadora(a, b):
    def suma(a, b):
        return a+b
    def resta(a, b):
        return a-b
    return suma(a, b), resta(a, b)

valor1 = int(input("Ingresa un valor entero: "))
valor2 = int(input("Ingresa un valor entero: "))
print(f'La suma de los numeros ingresados es {calculadora(valor1, valor2)[0]} y la diferencia es {calculadora(valor1, valor2)[1]}')