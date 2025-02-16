# Creación de una Ventana por Medio de Tkinter

# GUI - Graphical User Interface

# Importamos el módulo Tkinter
import tkinter

# Importamos el módulo Ttkinter, el cual contiene los widgets que podemos implementar en nuestra ventana
from tkinter import ttk

# Creamos una instancia de la clase Tk
ventana = tkinter.Tk()

# Modificamos el tamaño de la ventana
ventana.geometry('600x400')

# Cambiamos el nombre de la ventana
ventana.title('Creación de la Primer Ventana')

# Cambiamos el icono de la ventana
ventana.iconbitmap('icono.ico')

def eventClick():
    print(f'Botón 1 seleccionado. ')
    boton1.config(text = 'Botón seleccionado')

# Creamos un widget, un botón, cuyo padre es la ventana y le asignamos un comando asociado a su evento, el click
boton1 = tkinter.ttk.Button(ventana, text = 'Botón 1', command = eventClick)

# Mostramos el botón dentro de la ventana
boton1.pack()

# Iniciamos la ventana
# Esta línea de código debe ir al final de todas las modificaciones a la ventana
# De no ser así, las modificaciones no tendrán cabida en la ventana
ventana.mainloop()