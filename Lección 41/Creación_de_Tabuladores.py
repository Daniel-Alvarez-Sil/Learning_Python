# Este módulo se encarga de crear ventanas(tabuladores) que se implementarán en un notebook de Python

# Importamos los módulos necesarios para el manejo de interfaces gráficas
import tkinter
from tkinter import ttk

# Esta clase crea instancias de tipo tabulador
def Tabulador(cParamPadreDeTabuladores, cParamTituloDeTabulador):
    # Parámetros:
        # cParamPadreDeTabuladores = Objeto Notebook en el que el Tabulador será insertado
        # cParamTituloDeTabulador = Nombre del Tabulador que se está creando

    # Creamos el tabulador (el tabulador es un frame)
    tab = ttk.Frame(cParamPadreDeTabuladores)
    # Insertamos el frame en el notebook
    cParamPadreDeTabuladores.add(tab, text = cParamTituloDeTabulador)
    return tab

if __name__ != '__main__':
    # Impresión de mensaje de exportación correcta del módulo
    print(f'El módulo, {__name__}, ha sido importado con éxito. ')
else:
    # Realización de pruebas del módulo
    ventana = tkinter.Tk()
    ventana.geometry('600x600')
    ventanas = ttk.Notebook(ventana)
    tab1 = Tabulador(ventanas, 'Tab 1')
    tab2 = Tabulador(ventanas, 'Tab 2')
    ventanas.pack(fill = 'both')
    ventana.mainloop()