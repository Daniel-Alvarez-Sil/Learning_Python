# Importamos los módulos necesarios para implementar una ventana
import tkinter
from tkinter import ttk

# Asignación de los Atributos de la Ventana
ventana = tkinter.Tk()
ventana.geometry('600x400')
ventana.title('Arte de Botones')
ventana.iconbitmap('icono.ico')
    # Asignación de la proporción de las columnas y de las filas existentes
ventana.rowconfigure(0, weight = 5)
ventana.rowconfigure(1, weight = 5)
ventana.columnconfigure(0, weight = 5)
ventana.columnconfigure(1, weight = 5)

# Creación de Botones
boton1 = ttk.Button(ventana, text = 'Botón 1')
boton1.grid(row = 0, column = 0, sticky = 'NSWE') # <-- Con el argumento de sticky establecido a 'NSWE' indicamos que el
                                                  #     botón se expandirá para ocupar todo el espacio disponible de su celda
boton2 = ttk.Button(ventana, text = 'Botón 2')
boton2.grid(row = 1, column = 0, sticky = 'NSWE')
boton3 = ttk.Button(ventana, text = 'Botón 3')
boton3.grid(row = 0, column = 1, sticky = 'NSWE')
boton4 = ttk.Button(ventana, text = 'Botón 4')
boton4.grid(row = 1, column = 1, sticky = 'NSWE')
boton5 = ttk.Button(ventana, text = 'Botón 5')
boton5.grid(row = 3, column = 3)

# Desplegamos la Ventana
ventana.mainloop()

