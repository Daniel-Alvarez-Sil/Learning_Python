from Modulo_de_Log  import log
from psycopg2       import pool
import sys

class Conexion:
    cUSER = 'postgres'
    cPASSWORD = 'admin'
    cHOST = 'localhost'
    cPORT = '5432'
    cDATABASE = 'test_db'
    iMINCON = 1
    iMAXCON = 5
    POOL = None

    # Método para Crear un POOL de Conexiones
    @classmethod
    def obtenerPool(cls):
        if cls.POOL == None:
            try:
                cls.POOL = pool.SimpleConnectionPool(
                    cls.iMINCON,
                    cls.iMAXCON,
                    user = cls.cUSER,
                    password = cls.cPASSWORD,
                    host = cls.cHOST,
                    port = cls.cPORT,
                    database = cls.cDATABASE
                )
                log.debug(f'Se ha establecido la conexion al pool de manera exitosa.\nPOOL: {cls.POOL}')
                #return cls.POOL
            except Exception as e:
                log.error(f'No se ha podido establecer el POOL de conexiones a la base de datos\nDetalle del error: {e}')
                sys.exit()
        return cls.POOL

    # Creación de Conexiones Mediante el POOL
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Se ha obtenida una conexion a la base de datos: {conexion}')
        return conexion

    # Liberacion de una Conexion a la Base de Datos
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Conexión liberada: {conexion}')

    # Liberacion de Todas las Conexiones del POOL
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        log.debug(f'Hemos cerrado todas las conexiones a la base de datos')

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con éxito')
else:
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    Conexion.cerrarConexiones()
    #conexion4 = Conexion.obtenerConexion()


