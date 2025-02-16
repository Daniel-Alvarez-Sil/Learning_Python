# Este Menú nos permite ejecutar las operacions CRUD sobre la tabla de USUARIO de la base de datos

from Modulo_de_Log                          import log
from Modulo_de_Usuario_Data_Access_Object   import UsuarioDAO
from Modulo_de_Usuario                      import Usuario

iOpcion = 0
iRows = 0

class CrearUsuario:
    @classmethod
    def create(cls, iParamMode):
        usuario = Usuario()
        if (iParamMode == 1 or iParamMode == 3):
            log.info(f'Ingresa el ID del usuario: ')
            usuario.iID = input()
        if (iParamMode == 2 or iParamMode == 3):
            log.info(f'Ingresa el nombre del usuario: ')
            usuario.cUser = input()
            log.info(f'Ingresa la contraseña del usuario: ')
            usuario.cPassword = input()
        return usuario

while iOpcion != 5:
#    log.info(f'Menú de Opciones'. center(40, '-'))
    log.info(f'''
                Menú de Opciones:
    1) CREATE: Crear un Usuario
    2) READ:   Consulta de Todos los Usuarios 
    3) UPDATE: Actualizar un Usuario
    4) DELETE: Eliminar un Usuario
    
    5) EXIT:   Salir  
    ''')
    try:
        log.info("Ingresa tu opción (1-5): ")
        iOpcion = int(input())
        if 1 > iOpcion or iOpcion > 5:
            raise ValueError
    except Exception:
        log.info(f'Por favor ingresa un valor válido. ')
    else:
        # Create:
        if iOpcion == 1:
            UsuarioDAO.insert(CrearUsuario.create(2))

        # Read:
        elif iOpcion == 2:
            registros = UsuarioDAO.select()
            if len(registros) >= 1:
                for registro in registros:
                    log.info(f'{registro}')

        # Update:
        elif iOpcion == 3:
            UsuarioDAO.update(CrearUsuario.create(3))

        # Delete:
        elif iOpcion == 4:
            UsuarioDAO.delete(CrearUsuario.create(1))

log.info(f'Gracias por usar nuestro sistema. ¡Hasta luego!')