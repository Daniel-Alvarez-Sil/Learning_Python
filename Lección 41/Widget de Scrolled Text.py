# Cómo implementar y usar un widget de scrolled text

# Importamos los módulos necesarios para manejar interfaces gráficas
from Creación_de_Tabuladores import Tabulador
import tkinter
from tkinter import ttk, scrolledtext

# Creamos la ventana y asignamos sus atributos correspondientes
ventana = tkinter.Tk()
ventana.geometry('600x500')
ventana.title('Widget de Scrolled Text')
ventana.iconbitmap('icono.ico')

# Creamos los widgets de la Ventana
    # Notebook
tabuladores = ttk.Notebook(ventana)
        # Tabuladores del Notebook
tab1 = Tabulador(tabuladores, 'Tabulador para Revisar el Widget Scrolled Text')
tab2 = Tabulador(tabuladores, 'Tabulador de Pruebas')
    # Scrolled Text
scroll = scrolledtext.ScrolledText(tab1, width = 50, height = 10, wrap = tkinter.WORD) # <-- El argumento, 'wrap' = tkinter.WORD, especifica que queremos que las palabras no se corten en los bordes del widget
        # Ingresamos text dentro del widget
scroll.insert(1.0, 'Ingresa tu información')
scroll.grid(row = 0, column = 0)

# Desplegamos la ventana y sus componentes
tabuladores.pack(fill = 'both')
ventana.mainloop()