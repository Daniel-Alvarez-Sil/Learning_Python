def suma(a:int = 0, b:int = 0) -> int:
    return a + b

print(f'Valor inicial de la suma: {suma()}')
x = int(input("Ingresa el primer valor: "))
y = int(input("Ingresa el segundo valor: "))
print(f'Suma de los valores ingresados: {suma(x, y)}')