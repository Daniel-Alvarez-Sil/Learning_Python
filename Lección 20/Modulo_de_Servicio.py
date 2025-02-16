from Modulo_de_Pelicula import Pelicula
from Modulo_de_Resource_Manager import ResourceManager
import os

class Servicio:
    cRutaArchivo = "C:\Programación\Python\Lección 20\Peliculas.txt"

    #Método para agregar una pelicula al listado de peliculas
    @classmethod
    def agregarPelicula(cls, oPelicula):
        with ResourceManager(cls.cRutaArchivo, "a") as docArchivo:
            docArchivo.write(oPelicula.cNombre + "\n")

    #Método para listar todas las peliculas
    @classmethod
    def imprimirPeliculas(cls):
        with ResourceManager(cls.cRutaArchivo, "r") as docArchivo:
            if docArchivo == -1:
                print("No hay ningula pelicula para imprimir. Por favor ingresa una pelicula")
            else:
                print(f'Impresion de Peliculas: ')
                for linea in docArchivo:
                    print(f'Pelicula: {linea}')

    #Método para eliminar el listado (documento .txt) de peliculas
    @classmethod
    def eliminarDocumentoPeliculas(cls):
        os.remove(cls.cRutaArchivo)

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con exito')
