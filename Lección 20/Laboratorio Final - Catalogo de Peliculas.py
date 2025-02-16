from Modulo_de_Servicio import Servicio
from Modulo_de_Pelicula import Pelicula

iOpcion = 0

while iOpcion != 4:
    iOpcion = 0
    print("Menu de Opciones". center(20, '-'))
    print(f'1) Agregar Pelicula\n2)Listar Peliculas\n3)Eliminar Archivo de Peliculas\n4)Salir')
    while not(1 <= iOpcion <= 4):
        try:
            iOpcion = int(input("\tIngresa tu opción: "))
            if not(1 <= iOpcion <= 4):
                raise ValueError
        except BaseException as e:
            print(f'ERROR: La has opcion que has escogido no es válida. Por favor escoge otra vez')
            iOpcion = 0
        else:
            if iOpcion == 1:
                pelicula1 = Pelicula(input("Ingresa el nombre de la pelicula: "))
                Servicio.agregarPelicula(pelicula1)
                print(f'La pelicula, {pelicula1.cNombre}, ha sido agregada a lista con exito')
            elif iOpcion == 2:
                Servicio.imprimirPeliculas()
            elif iOpcion == 3:
                Servicio.eliminarDocumentoPeliculas()

print("Gracias por usar el sistema. ¡Hasta Pronto!")