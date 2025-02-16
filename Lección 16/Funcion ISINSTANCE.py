from Modulo_de_Empleado import Empleado
from Modulo_de_Gerente import Gerente

def imprimeClaseDeInstancia(objeto):
    # La funcion "isinstance" retorna TRUE si el objeto es una instancia del 2do parametro ingresado
    if isinstance(objeto, Gerente):
        print(f'El objeto es de tipo GERENTE')
    elif isinstance(objeto, Empleado):
        print(f'El objeto es de tipo EMPLEADO')

empleado1 = Empleado("Rene", 6000)
empleado2 = Empleado("Jose", 6500)
gerente1 = Gerente("Ramon", 8000, "Sistemas")
gerente2 = Gerente("Manuel", 9000, "Infraestructura")

imprimeClaseDeInstancia(empleado1)
imprimeClaseDeInstancia(gerente1)

