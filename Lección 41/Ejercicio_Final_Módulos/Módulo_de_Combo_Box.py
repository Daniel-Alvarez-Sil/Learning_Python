# Este módulo crea una clase para generar instancia de tipo Frame con un Widget de ComboBox

# Importamos los módulos necesarios para manejar interfaces gráficas
import tkinter
from tkinter import ttk, messagebox

# Clase de Tipo Frame con Widget de Combo Box
class TabuladorComboBox(ttk.Frame):
    def __init__(self, cParamTabuladorPadre):
    # Utilizamos el inicializador de la clase Frame
        super().__init__(cParamTabuladorPadre)

        # Asignamos los atributos del Frame
        self.rowconfigure(0, weight = 50)
        self.rowconfigure(1, weight = 20)
        self.columnconfigure(0, weight = 10)
        self.columnconfigure(1, weight = 10)

        # Asignamos los widgtes del Frame
            # Etiquetas
        ttk.Label(self, text = 'Selecciona un número:').grid(row = 0, column = 0, sticky = 'E')
            # Combo-Box
        self._comboBox = ttk.Combobox(self, values = [x + 1 for x in range(10)], state = 'readonly')
        self._comboBox.current(0)
        self._comboBox.grid(row = 0, column = 1)
            # Botones
        ttk.Button(self, text = 'Seleccionar', command = self.eventoBoton).grid(row = 1, column = 0, columnspan = 2)

    def eventoBoton(self):
        messagebox.showinfo(title = 'Selección', message = f'Has seleccionado el número {self._comboBox.get()}. ')

if __name__ != '__main__':
    # Impresión con relación a la exportación correcta del módulo
    print(f'El módulo, {__name__}, ha sido importado con éxito. ')
else:
    # Realización de Pruebas
    ventana = tkinter.Tk()
    ventana.geometry('300x300')
    ventana.title('Prueba')

    tabuladores = ttk.Notebook(ventana)
    tabuladores.add(TabuladorComboBox(tabuladores), text = 'Combo Box')

    tabuladores.pack(fill = 'both')
    ventana.mainloop()