# Este Módulo maneja las conexiones del POOL a la base de datos

from Modulo_de_Log  import log
from psycopg2       import pool
import sys


class Conexion:
    # Atributos estáticos (o de clase) de la clase
    iMINCON = 1
    iMAXCON = 5
    cUSER = 'postgres'
    cPASSWORD = 'admin'
    cHOST = 'localhost'
    cPORT = '5432'
    cDATABASE = 'test_db'
    POOL = None

# Métodos de clase (pertenecen al contexto estático)
    @classmethod
    def obtenerPool(cls):
        log.debug(f'Iniciando adquisición de POOL de conexiones para la base de datos.')
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
            except Exception as e:
                log.critical(f'No se pudo concretar la creación del POOL de conexiones. Detalle del error: {e}. Terminando proceso...')
                sys.exit()
            log.debug(f'Se ha creado exitosamente el POOL de conexiones: {cls.POOL}.')
        else:
            log.debug(f'Se ha conseguido exitosamente el POOL existente: {cls.POOL}.')
        return cls.POOL

    @classmethod
    def obtenerConexion(cls):
        log.debug(f'Inicio de Solicitud de una conexion del POOL.')
        try:
            conexion = cls.obtenerPool().getconn()
        except Exception:
            log.error(f'No hay conexiones disponibles en el POOL. Terminando proceso...')
            sys.exit()
        log.debug(f'Hemos obtenido exitosamente la conexion, {conexion}, del POOL')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        log.debug(f'Iniciando proceso de liberacion de conexion: {conexion}.')
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Se ha liberado exitosamente la conexion: {conexion}.')

    @classmethod
    def cerrarConexiones(cls):
        log.debug(f'Iniciando proceso de liberacion de todas las conexiones del POOL: {cls.POOL}')
        cls.obtenerPool().closeall()
        log.debug(f'Se han cerrado exitosamente todas las conexiones a la base de datos. ')

if __name__ != '__main__':
    log.info(f'{__name__} ha sido importado con éxito. ')
else:
    pass