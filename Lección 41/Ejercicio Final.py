# Este ejercicio consistió en aplicar la P00 a los widgets creados en sus tabuladores correspondientes
# El código correspondiente a este ejercicio se encuentra en el paquete 'Ejercicio_Final_Módulos'

# Importamos los módulos necesarios para el funcionamiento de las interfaces gráficas
import tkinter
from Ejercicio_Final_Módulos.Módulo_de_Tabuladores_de_Widgets import TabuladoresWidgets

# Creamos la ventana y asignamos sus atributos
ventana = tkinter.Tk()
ventana.geometry('600x300')
ventana.title('Ejercicio Final')
ventana.iconbitmap('icono.ico')
ventana.resizable(False, False)

# Creamos las ventanas
tabuladores = TabuladoresWidgets(ventana)

# Desplegamos la ventana y sus widgets
tabuladores.pack(fill = 'both')
ventana.mainloop()