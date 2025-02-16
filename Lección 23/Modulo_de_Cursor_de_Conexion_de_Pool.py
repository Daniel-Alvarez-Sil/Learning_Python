from Modulo_de_Log import log
from Modulo_de_Conexion import Conexion

# Esta clase es un Resource Manager para manejar las conexiones y cursores provinientes de un POOl
class Cursor:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'Entramos al ciclo __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        log.debug(f'Hemos conseguido un cursor para conectarnos a la base de datos')
        return self._cursor

    def __exit__(self, tipoExcepcion, valorExcepcion, traceback):
        log.debug(f'Entramos al ciclo __exit__')
        if valorExcepcion:
            self._conexion.rollback()
            log.error(f'Se ha producido un error: {traceback}\nDeshaciendo cambios hechos a la base de datos...')
        else:
            self._conexion.commit()
            log.debug(f'Se han guardado los cambios a la base de datos')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ != '__main__':
    print(f'{__name__} ha sido importado con éxito')
else:
    with Cursor() as cursor:
        log.debug(f'Entramos al bloque de WITH')
        cursor.execute('SELECT * FROM persona')
        log.debug(f'Realización de una consulta de prueba:\n{cursor.fetchall()}')