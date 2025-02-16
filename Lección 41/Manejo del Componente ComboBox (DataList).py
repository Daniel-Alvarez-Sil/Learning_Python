# Manejo del Widget de ComboBox

# Importamos los módulos necesarios para el manejo de interfaces gráficas
import tkinter
from tkinter import ttk, messagebox
from Creación_de_Tabuladores import Tabulador

# Creamos la ventana y asignamos sus atributos
ventana = tkinter.Tk()
ventana.geometry('600x400')
ventana.title('Manejo del Componente ComboBox')
ventana.iconbitmap('icono.ico')

# Creamos los widgets de la ventana
    # Notebook
tabuladores = ttk.Notebook(ventana)
        # Tabuladores del Notebook
tab1 = Tabulador(tabuladores, 'Tabulador de Manejo de ComboBox')
tab2 = Tabulador(tabuladores, 'Tabulador de Relleno')
    # Etiquetas
labelCombobox = ttk.Label(tab1, text = 'Elige un número:')
    # ComboBox
combobox = ttk.Combobox(tab1, width = 5, values = [str(x + 1) for x in range(10)], state = 'readonly')
        # Establecemos un valor inicial al comboBox
combobox.current(0)
    # Botón
def printEleccion():
    messagebox.showinfo(title = 'Elección', message = f'Tu elección es: {combobox.get()}')
boton1 = ttk.Button(tab1, text = 'Presioname', command = printEleccion)

# Desplegamos la ventana y sus componentes
boton1.grid(row = 0, column = 2)
combobox.grid(row = 0, column = 1)
labelCombobox.grid(row = 0, column = 0, sticky = 'W')
tabuladores.pack(fill = 'both')
ventana.mainloop()