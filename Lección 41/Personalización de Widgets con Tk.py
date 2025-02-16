# Personalización de un Botón usando directamente el módulo Tk no el módulo ttk
# Con este método, tenemos más control sobre la personalización de un widget

# Importamos el módulo necesario para implementar una ventana y sus widgets correspondientes
import tkinter

# Creamos y Establecemos los atributos de la ventana
ventana = tkinter.Tk()
ventana.geometry('600x400')
ventana.title('Personalización de los Botones')
ventana.iconbitmap('icono.ico')
ventana.rowconfigure(0, weight = 50)
ventana.rowconfigure(1, weight = 50)
ventana.columnconfigure(0, weight = 50)
ventana.columnconfigure(1, weight = 50)

# Creación del Botón Personalizable
def metodoPersonalizador():
    boton1.config(text = 'Botón Presionado', fg = 'blue', relief = tkinter.GROOVE, bg = 'yellow')
boton1 = tkinter.Button(ventana, text = 'Botón 1', command = metodoPersonalizador)
boton1.grid(row = 1, column = 1, sticky = 'NSWE')

# Desplegamos la ventana
ventana.mainloop()