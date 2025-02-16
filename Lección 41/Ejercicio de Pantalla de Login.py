# Importamos los módulos necesarios para el manejo de ventanas y sus componentes
import tkinter
from tkinter import ttk, messagebox

# Creamos la ventana y sus atributos
ventanaLogIn = tkinter.Tk()
ventanaLogIn.geometry('300x100')
ventanaLogIn.title('Login')
ventanaLogIn.iconbitmap('icono.ico')
    # Evitamos que la ventana cambie de tamaño
ventanaLogIn.resizable(False, False) # <-- El primer parámetro corresponde a las modificaciones sobre el eje x y
                                     #     el segundo corresponde a las modificaciones sobre el eje y
    # Proporción de las filas y de las columnas
        # Filas
ventanaLogIn.rowconfigure(0, weight = 15)
ventanaLogIn.rowconfigure(1, weight = 15)
ventanaLogIn.rowconfigure(2, weight = 20)
        # Columnas
ventanaLogIn.columnconfigure(0, weight = 15)
ventanaLogIn.columnconfigure(1, weight = 40)

# Creamos los widgets de la ventana
    # Entradas
entradaUsuario = ttk.Entry(ventanaLogIn, width = 30, justify = 'left')
entradaPassword = ttk.Entry(ventanaLogIn, width = 30, justify = 'left', show = '*')

    # Etiquetas
labelUsuario = ttk.Label(ventanaLogIn, text = 'Usuario: ')
labelPassword = ttk.Label(ventanaLogIn, text = 'Contraseña: ')

    # Botones
def eventoLogin():
    messagebox.showinfo(title = 'Datos del Usuario', message = f'Usuario: {entradaUsuario.get()}\nContraseña: {entradaPassword.get()}')
botonLogin = ttk.Button(ventanaLogIn, text = 'Login', command = eventoLogin)

# Desplegamos la ventana
botonLogin.grid(row = 2, column = 0, columnspan = 2)
labelPassword.grid(row = 1, column = 0, sticky = 'E')
labelUsuario.grid(row = 0, column = 0, sticky = 'E')
entradaPassword.grid(row = 1, column = 1)
entradaUsuario.grid(row = 0, column = 1)
ventanaLogIn.mainloop()