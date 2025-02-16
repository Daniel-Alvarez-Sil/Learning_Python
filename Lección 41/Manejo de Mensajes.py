# Dentro de una ventana, podemos mandar mensajes usando el módulo, messagebox

# Importamos los modulos necesarios para la creación de la ventana y de sus componentes
import tkinter
from tkinter import ttk

# Importamos el módulo de messagebox
from tkinter import messagebox

# Uso del módulo messagebox
def messageInfo():
    messagebox.showinfo(title = 'Información', message = 'Despliegue de Mensaje de Información')

def messageError():
    messagebox.showerror(title = 'Error', message = 'Despliegue de Mensaje de Error')

def messageAlert():
    messagebox.showwarning(title = 'Advertencia', message = 'Despliegue de Mensaje de Advertencia')

# Creamos la ventana y asignamos sus atributos
ventana = tkinter.Tk()
ventana.geometry('200x600')
ventana.title('Manejo de Mensajes')
ventana.iconbitmap('icono.ico')
ventana.rowconfigure(0, weight = 30)
ventana.rowconfigure(1, weight = 30)
ventana.rowconfigure(2, weight = 30)
ventana.columnconfigure(0, weight = 30)

# Creamos los botones
boton1 = ttk.Button(ventana, text = 'Mensaje de Información', command = messageInfo)
boton2 = ttk.Button(ventana, text = 'Mensaje de Error', command = messageError)
boton3 = ttk.Button(ventana, text = 'Mensaje de Alerta', command = messageAlert)


# Desplegamos la ventana y sus objetos
boton3.grid(row = 2, column = 0, sticky = 'NSWE')
boton2.grid(row = 1, column = 0, sticky = 'NSWE')
boton1.grid(row = 0, column = 0, sticky = 'NSWE')
ventana.mainloop()

