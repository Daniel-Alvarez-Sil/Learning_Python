# Podemos acceder a la información de un componente entry mediante una variable
# Ejemplo:

# Importamos los módulos necesarios para la creación de una ventana y de sus widgets
import tkinter
from tkinter import ttk

# Creación de la ventana y asignación de sus atributos
ventana = tkinter.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Variables y Componentes Entry')
ventana.iconbitmap('icono.ico')

# Creación de los componentes de la ventana
    # Entry
        # Creación de una variable que será usada para acceder al componente
entrada1Var = tkinter.StringVar(value = 'Ingresa un valor')
        # Asignamos dicha variable dentro de los argumentos de la clase Entry
entrada1 = ttk.Entry(ventana, width = 30, justify = 'center', textvariable = entrada1Var)

    # Botón
        # Triggers del Botón
def eventoBoton1():
        # NOTA: Usamos la variable de acceso al objeto para modificar dicho objeto
    boton1.config(text = entrada1Var.get())
    entrada1Var.set('Cambio...')
boton1 = ttk.Button(ventana, text = 'Botón 1', command = eventoBoton1)


# Desplegamos la ventana y sus componentes (widgets)
boton1.grid(row = 0, column = 1)
entrada1.grid(row = 0, column = 0)
ventana.mainloop()