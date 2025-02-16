cNom = input("Ingresa el nombre del libro:")
iD = int(input("Ingresa el código del libro: "))
lEnvio = bool(int(input("¿El libro incluye envío gratis? (1 = SI, 0 = NO): ")))
fCost = float(input("Ingresa el precio del libro: "))

print(f'Libro: {cNom} \n'
      f'Código: {iD} \n'
      f'Envío Gratis: {lEnvio} \n'
      f'Precio: {fCost} \n')