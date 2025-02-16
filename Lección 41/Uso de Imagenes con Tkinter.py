# Uso de Imagenes

# Importamos los módulos necesarios para el manejo de interfaces gráficas
import tkinter
from tkinter import ttk, messagebox

# Creamos la ventana  y asignamos sus atributos
ventana = tkinter.Tk()
ventana.geometry('600x500')
ventana.title('Uso de Imagenes')
ventana.iconbitmap('icono.ico')

# Creamos un botón con una imagen de fondo
imagen = tkinter.PhotoImage(file = 'python-logo.png')
def eventoBoton():
    messagebox.showinfo(title = 'Mensaje Informativo', message = 'Has seleccionado la imagen. ')
boton1 = ttk.Button(ventana, image = imagen, command = eventoBoton)

# Desplegamos la ventana y sus atributos
boton1.grid(row = 0, column = 0)
ventana.mainloop()