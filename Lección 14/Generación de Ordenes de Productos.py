from Modulo_de_Producto import Producto
from Modulo_de_Orden import Orden

producto1 = Producto("Manga One Piece", 99.00)
producto2 = Producto("Manga Chainsaw Man", 139.00)
producto3 = Producto("Manga One Punch Man", 129.00)
producto4 = Producto("Manga Berserk", 119.00)

print(f'\nImpresion de Ordenes\n'. center(100, '-'))
listOfProducts = [producto1, producto2]
orden1 = Orden(listOfProducts)
orden1.agregarProducto(producto4)
listOfProducts = [producto3, producto4]
orden2 = Orden(listOfProducts)
print(orden1)
print(orden2)