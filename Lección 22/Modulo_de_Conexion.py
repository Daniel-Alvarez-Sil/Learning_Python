from Modulo_de_Log import log
import psycopg2
import sys

class Conexion:
    # Atributos de la clase (estáticos)
    cDatabase = 'test_db'
    cUsername = 'postgres'
    cPassword = 'admin'
    cHost = 'localhost'
    cPort = '5432'
    conexion = None
    cursor = None

    #Métodos de la clase (estáticos)
    @classmethod
    def obtenerConexion(cls):
        if cls.conexion == None:
            try:
                cls.conexion = psycopg2.connect(user = cls.cUsername, password = cls.cPassword, host = cls.cHost, port = cls.cPort, database = cls.cDatabase)
                log.debug(f'La conexion a la base de datos ha sido exitosa\nConexion: {cls.conexion}')
            except Exception as e:
                log.error(f'No se pudo concretar la conexion a la base de datos\nDetalle del error: {e}')
                sys.exit()
            else:
                pass
        return cls.conexion
    @classmethod
    def obtenerCursor(cls):
        if cls.cursor == None or cls.cursor.closed == True:
            try:
                cls.cursor = cls.obtenerConexion().cursor()
                log.debug(f'La adquisición del cursor para la base de datos fue exitosa\nCursor: {cls.cursor}')
            except Exception as e:
                log.error(f'No se pudo obtener un cursor para la base de datos\nDetalle del error: {e}')
                sys.exit()
            else:
                pass
        return cls.cursor

    @classmethod
    def cerrarConexion(cls):
        if cls.cursor != None:
            cls.cursor.close()
        if cls.conexion != None:
            cls.conexion.close()

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con éxito')
else:
    #Conexion.obtenerConexion()
    Conexion.obtenerCursor()
