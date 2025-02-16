# El concepto de grid se refiera a la división de la ventana en una composición de filas y columnas

# Importamos los módulos necesarios para el manejo de una ventana
import tkinter
from tkinter import ttk

# Creamos la ventana
ventana = tkinter.Tk()
ventana.geometry('600x400')
ventana.title('Manejo del Grid')
ventana.iconbitmap('icono.ico')

# Creamos los botones de la ventana
    # Triggers del Click de los Botones:
def eventoBoton1():
    boton1.config(text = 'Botón 1 Seleccionado')
def eventoBoton2():
    boton2.config(text = 'Botón 2 Seleccionado')
    # Creación de los Botones
boton1 = ttk.Button(ventana, text = 'Botón 1', command = eventoBoton1)
boton2 = ttk.Button(ventana, text = 'Botón 2', command = eventoBoton2)
    # Despliegue de los botones
boton1.grid(row = 0, column = 0, sticky = 'W') # <-- El argumento sticky determina la posición del botón con respecto
                                               #     al centro de la cordenada
boton2.grid(row = 1, column = 0, sticky = 'E')


ventana.mainloop()