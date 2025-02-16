from Modulo_de_Persona_Data_Access_Object import PersonaDAO
from Modulo_de_Persona import Persona

iOpcion = 0
iRows = 0

while iOpcion != 5:
    print('\n')
    print("Menú de Opciones: CRUD". center(40, '-'))
    print(f'''          
            1) Create
            2) Read
            3) Update
            4) Delete
            
            5) Exit    
    ''')
    try:
        iOpcion = int(input("Ingresa tu opción: "))
        if 1 > iOpcion or iOpcion > 5:
            raise TypeError
    except Exception as e:
        print(f'Por favor ingresa un valor válido. ')
    else:
        #Create:
        if iOpcion == 1:
            print(f'Creación de una Persona: ')
            iRows = PersonaDAO.insert(Persona(cParamNombre = input("\tIngresa el nombre de la persona: "), cParamApellido = input("\tIngresa el apellido de la persona: "), cParamMail = input("\tIngresa el correo de la persona: ")))
            if iRows >= 1:
                print(f'¡Listo, la persona se ha creado con éxito!')
            else:
                print(f'ERROR: La transcacción no pudo ser finalizada. Por favor valida tu información e intenta nuevamente')
        #Read:
        elif iOpcion == 2:
            print(f'Lectura de los Registros de la Base de Datos:')
            print(f'\tImpresión: ')
            consulta = PersonaDAO.select()
            if len(consulta) >= 1:
                for fila in consulta:
                    print(f'\t\t {fila}')
            else:
                print(f'ERROR: No existe ningún registro en la base de datos. Por favor añade un registro e intente nuevamente')
        #Update:
        elif iOpcion == 3:
            print(f'Actualización de una Registro de la Base de Datos: ')
            iRows = PersonaDAO.update(Persona(iParamID = input("\tIngresa el ID de la persona a modificar: "), cParamNombre = input("\t\tIngresa el nuevo nombre: "), cParamApellido = input("\t\tIngresa el nuevo apellido: "), cParamMail = input("\t\tIngresa el nuevo correo: ")))
            if iRows >= 1:
                print(f'¡Listo, la persona se ha actualizado con éxito!')
            else:
                print(f'ERROR: La transcacción no pudo ser finalizada. Por favor valida tu información e intenta nuevamente')
        #Delete:
        elif iOpcion == 4:
            print(f'Eliminación de un Registro de la Base de Datos: ')
            iRows = PersonaDAO.delete(Persona(iParamID = input("\tIngresa el ID de la persona a eliminar: ")))
            if iRows >= 1:
                print(f'¡Listo, la persona se ha eliminado con éxito!')
            else:
                print(f'ERROR: La transcacción no pudo ser finalizada. Por favor valida tu información e intenta nuevamente')

print(f'Gracias por usar nuestro sistema. ¡Hasta Pronto!')