# Este módulo crea una clase de la cual se pueden generar instancias de tipo Frame

# Importamos los módulos necesarios para el manejo de interfaces gráficas
import tkinter
from tkinter import ttk, messagebox

# Clase de Tipo Frame
class TabuladorNormal(ttk.Frame):
    def __init__(self, cParamTabuladorPadre):
        # Inicializamos las instancias de esta clase con el inicializador de Frames
        super().__init__(cParamTabuladorPadre)
        # Asignamos los atributos del Frame
        self.rowconfigure(0, weight = 30)
        self.rowconfigure(1, weight = 40)
        self.columnconfigure(0, weight = 25)
        self.columnconfigure(1, weight = 40)
        # Creamos los widgets del Frame
            # Etiquetas
        ttk.Label(self, text = 'Mensaje: ').grid(row = 0, column = 0, sticky = 'E')
            # Entradas
        self._entryMessage = ttk.Entry(self, width = 30, justify = 'left')
        self._entryMessage.grid(row = 0, column = 1)
            # Botones
        ttk.Button(self, text = 'Enviar', command = self._eventoBoton).grid(row = 1, column = 0, columnspan = 2)

    def _eventoBoton(self):
        messagebox.showinfo(title = 'Éxito', message = f'El mensaje, {self._entryMessage.get()}, ha sido enviado exitosamente. ')

if __name__ != '__main__':
    # Impresión de exportación correcta del módulo
    print(f'El módulo, {__name__}, ha sido importado con éxito. ')
else:
    # Realización de pruebas con el módulo
    ventana = tkinter.Tk()
    ventana.geometry('300x200')
    ventana.title('Pruebas')

    tabuladores = ttk.Notebook(ventana)
    tabuladores.add(TabuladorNormal(tabuladores), text = 'Envió de Mensaje')

    tabuladores.pack(fill = 'both')
    ventana.mainloop()

