from Modulo_de_DispositivoEntrada import DispositivoEntrada
from Modulo_de_Raton import Raton
from Modulo_de_Teclado import Teclado
from Modulo_de_Monitor import Monitor
from Modulo_de_Computadora import Computadora
from Modulo_de_Orden import Orden

print('\n')

#Aditamentos de de las Computadoras
raton1 = Raton("HP", "Bluetooth")
raton2 = Raton("Apple", "USB")
raton3 = Raton("Gamer", "USB-C")
teclado1 = Teclado("Logitech", "Bluetooth")
teclado2 = Teclado("Dell", "USB")
teclado3 = Teclado("Gamer", "USB-C")
monitor1 = Monitor("Samsung", 23)
monitor2 = Monitor("LG", 36)
monitor3 = Monitor("Gamer", 28)

#Computadoras
computadora1 = Computadora("DAS", monitor1, teclado1, raton1)
computadora2 = Computadora("AAS", monitor2, teclado2, raton2)
computadora3 = Computadora("Gamer", monitor3, teclado3, raton3)
computadoras1 = [computadora1, computadora2]
computadoras2 = [computadora2, computadora1]

#Ordenes de Computadoras
orden1 = Orden(computadoras1)
orden2 = Orden(computadoras2)
print(orden1)
print(orden2)
orden1.agregarComputadora(computadora3)
print(orden1)
#Pruebas
"""print(raton1)
print(teclado1)
print(monitor1)
print(computadora1)"""

