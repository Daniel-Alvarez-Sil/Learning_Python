# El componente Entry se usa para leer y para mostrar información del y al usuario

# Importamos los módulos necesarios para crear una ventana y sus componentes
import tkinter
from tkinter import ttk

# Creamos la ventana y le asignamos atributos personalizados
ventana = tkinter.Tk()
ventana.geometry('300x200')
ventana.title('Manejo del Componente Entry')
ventana.iconbitmap('icono.ico')

# Creación de los widgets de la ventana
    # Entry
        # Creación del componente de entrada
entrada1 = ttk.Entry(ventana, width = 30, state = 'normal', justify = 'center')
        # Añadimos texto al componente (OUTPUT)
entrada1.insert(0, 'Ingresa un texto')
        # Añadimos texto al final del componente
entrada1.insert(tkinter.END, '.')
        # Modificamos el estado del widget (Si este paso se ejecuta antes, la adición de texto no será completada)
# entrada1.config(state = 'readonly')
        # Despliegue del componente
entrada1.grid(row = 0, column = 0)

def accionesConLaEntrada():
        # Leer la información de la entrada (INPUT)
    print(entrada1.get())
        # Eliminar el contenido
    # entrada1.delete(0, tkinter.END)
        # Seleccionar el texto de la entrada
    entrada1.select_range(0, tkinter.END)
    entrada1.focus()

    # Botón
boton1 = ttk.Button(ventana, text = 'Botón 1', command = accionesConLaEntrada)
boton1.grid(row = 0, column = 1)

# Desplegamos la ventana
ventana.mainloop()