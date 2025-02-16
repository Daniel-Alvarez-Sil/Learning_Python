def recursividad(numero):
    if numero == 1:
        return 1
    else:
        return numero * recursividad(numero - 1)

numero = int(input("Ingresa un valor: "))
print(f'El factorial de {numero} es {recursividad(numero)}')
