# Las etiquetas en tkinter son un componente individual, por lo que no son parte de un botón o de una entrada como sí
# lo son en Progress
# Las etiquetas se crean y se trabajan de la siguiente manera:

# Importamos los módulos necesarios para la creación de una ventana y sus componentes
import tkinter
from tkinter import ttk

# Creamos la ventana y asignamos sus atributos
ventana = tkinter.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Etiquetas')
ventana.iconbitmap('icono.ico')
ventana.rowconfigure(0, weight = 50)
ventana.rowconfigure(1, weight = 20)
ventana.columnconfigure(0, weight = 50)
ventana.columnconfigure(1, weight = 50)

# Creamos los widgets de la ventana
    # Botónes
boton1 = ttk.Button(ventana, text = 'Botón 1')
boton2 = ttk.Button(ventana, text = 'Botón 2')
    # Etiqueta
label1 = ttk.Label(ventana, text = 'Despliegue los Botones 1 y 2')

# Desplegamos la ventana y sus widgets
boton1.grid(row = 0, column = 0, sticky = 'NSWE')
boton2.grid(row = 0, column = 1, sticky = 'NSWE')
label1.grid(row = 1, column = 0, columnspan = 2)
ventana.mainloop()


