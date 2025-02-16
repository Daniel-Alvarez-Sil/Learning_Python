# Este Módulo se encarga de manejar los cursores y sus conexiones del POOL correspondientes

from Modulo_de_Log      import log
from Modulo_de_Conexion import Conexion

class Cursor:
    def __init__(self):
        self.conexion = None
        self.cursor = None

    def __enter__(self):
        self.conexion = Conexion.obtenerConexion()
        log.debug(f'Inicio de intento de adquisición de cursor para ejecutar sentencias sobre la base de datos. ')
        self.cursor = self.conexion.cursor()
        log.debug(f'Se ha conseguido exitosamente el cursor. ')
        return self.cursor

    def __exit__(self, tipoError, valorError, traceback):
        if valorError:
            self.conexion.rollback()
            log.error(f'Se ha presentado un error durante la transaccion: {traceback}. Deshaciendo la transcacción...')
        else:
            self.conexion.commit()
            log.debug(f'Se han guardado los cambios correctamente. ')
        log.debug(f'Incio de cierre de cursor. ')
        self.cursor.close()
        log.debug(f'Se ha cerrado correctamente el cursor. ')
        Conexion.liberarConexion(self.conexion)

if __name__ != '__main__':
    log.info(f'{__name__} ha sido importado con éxito. ')
else:
    with Cursor() as cursor:
        pass