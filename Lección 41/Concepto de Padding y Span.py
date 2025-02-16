# Padding es el concepto mediante el cual insertamos un margen dentro o fuera de un widget
# Span es el concepto de expandir una columna o una fila
# Aplicación de ambos conceptos:


# Importamos los módulos para la creación de una ventana y sus widgets correspondientes
import tkinter
from tkinter import ttk

# Creación de la ventana y asignación de sus atributos
ventana = tkinter.Tk()
ventana.geometry('600x400')
ventana.title('Concepto de Padding y Span')
ventana.iconbitmap('icono.ico')
ventana.rowconfigure(0, weight = 30)
ventana.rowconfigure(1, weight = 50)
ventana.columnconfigure(0, weight = 50)
ventana.columnconfigure(1, weight = 50)

# Creación de los Botones
boton1 = ttk.Button(ventana, text = 'Botón 1')
boton2 = ttk.Button(ventana, text = 'Botón 2')
boton2.grid(row = 1, column = 0, sticky = 'NSWE')
boton3 = ttk.Button(ventana, text = 'Botón 3')
boton3.grid(row = 1, column = 1, sticky = 'NSWE')

# Aplicación de los conceptos:
    # Padding y Span
boton1.grid(row = 0, column = 0, sticky = 'NSWE', columnspan = 2, padx = 20, pady = 20)

# Desplegamos la ventana
ventana.mainloop()