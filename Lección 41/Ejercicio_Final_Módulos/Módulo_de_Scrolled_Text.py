# Este módulo crea una clase para crear objetos de un tabulador con un scrolled text implementado

# Importamos los módulos necesarios para el manejo de interfaces gráficas
import tkinter
from tkinter import ttk, scrolledtext

# Clase de Tipo Frame con Widget Scrolled Text:
class TabuladorScrolledText(ttk.Frame):
    # Utilizamos el método inicializador de la clase Frame
    def __init__(self, cParamTabuladorPadre):
        super().__init__(cParamTabuladorPadre)
        scrolledtext.ScrolledText(self, width = 50, height = 20, wrap = tkinter.WORD).grid(row = 0, column = 0)


if __name__ != '__main__':
    # Impresión de exportación correcta del módulo
    print(f'El módulo, {__name__}, ha sido importado con éxito. ')
else:
    ventana = tkinter.Tk()
    ventana.geometry('200x100')
    ventana.title('Prueba')

    tabuladores = ttk.Notebook(ventana)
    tabuladores.add(TabuladorScrolledText(tabuladores), text = 'Scrolled Text')

    tabuladores.pack(fill = 'both')
    ventana.mainloop()